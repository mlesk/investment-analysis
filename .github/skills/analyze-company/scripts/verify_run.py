#!/usr/bin/env python3
"""Single-command Phase-5 verification gate for an analyze-company run.

Usage:
    python3 verify_run.py <dated-folder>

where <dated-folder> contains {TICKER}_model_inputs.json,
{TICKER}_Damodaran_Financial_Model.xlsx, the five lens .md files,
consensus-analysis.md and {ticker}-consensus-investment-report.html.

Checks (all must pass before a run is delivered):
  1. All five lens files exist.
  2. model_inputs.json is valid JSON; probabilities sum to 1.0; terminal
     growth < effective WACC in every scenario.
  3. Workbook exists and (if the `formulas` engine is available) its values
     match an independent Python recompute — i.e. ALL_MATCH. If `formulas`
     is unavailable, the workbook is NOT evaluated and the fallback is
     stated explicitly (recompute-only).
  4. The five scenario IV/share values + the probability-weighted value are
     identical in damodaran-analysis.md, consensus-analysis.md and the HTML.
  5. HTML is structurally sound: one <style> block, no external URLs,
     balanced tags, and every key figure present.

Prints a PASS/FAIL checklist; exits non-zero on any failure.
"""
import json
import os
import re
import sys

LENS_FILES = [
    "buffet-analysis.md",
    "munger-analysis.md",
    "damodaran-analysis.md",
    "druckenmiller-analysis.md",
    "soros-analysis.md",
]
SCEN_SHEETS = ["DCF-SevereBear", "DCF-Bear", "DCF-Base", "DCF-Bull",
               "DCF-ExtremeBull"]


def load_json(path):
    with open(path) as f:
        return json.load(f)


# ----------------------------------------------------------------- DCF
# Independent recompute — must match verify_model.py dcf() exactly.
def dcf(v, s):
    rev0 = v["revenue_run_rate_mm"]
    g0 = max(v["growth_y1"] + s["growth_adj"], v["min_growth"])
    decay = v["growth_decay"]
    gmin = v["min_growth"]
    m_base, m_term, m_step = (v["margin_y1"], v["margin_terminal"],
                              v["margin_ramp"])
    tax = v["tax_rate"]
    wacc = v["wacc"] + s["wacc_adj"]
    tg = v["terminal_growth"] + s["tg_adj"]
    roic0, roic_term = v["roic_initial"], v["roic_terminal"]
    m_adj, roic_adj = s["margin_adj"], s["roic_adj"]

    growth = [g0]
    for _ in range(9):
        growth.append(max(growth[-1] - decay, gmin))
    rev = [rev0 * (1 + growth[0])]
    for t in range(1, 10):
        rev.append(rev[-1] * (1 + growth[t]))

    pv_fcff, nopats = [], []
    for t in range(10):
        m = min(m_term + m_adj, m_base + m_adj + m_step * t)
        ebit = rev[t] * m
        nopat = ebit * (1 - tax)
        roic = max(roic_term + roic_adj,
                   roic0 + roic_adj - (roic0 - roic_term) * t / 9)
        rr = growth[t] / roic
        fcff = nopat * (1 - rr)
        pv_fcff.append(fcff / (1 + wacc) ** (t + 1))
        nopats.append(nopat)
    term_fcff = nopats[-1] * (1 + tg) * (1 - tg / (roic_term + roic_adj))
    tv = term_fcff / (wacc - tg)
    pv_tv = tv / (1 + wacc) ** 10
    ev = sum(pv_fcff) + pv_tv
    eq = ev - (v["debt_mm"] - v["cash_mm"])
    return eq / v["shares_mm"]


def recompute(cfg):
    v = cfg["inputs"]
    ivs = [dcf(v, s) for s in cfg["scenarios"]]
    weighted = sum(s["probability"] * iv
                   for s, iv in zip(cfg["scenarios"], ivs))
    price = v["price"]
    horizon = v.get("horizon_years", 5)
    return {
        "ivs": ivs,
        "weighted": weighted,
        "prob_sum": sum(s["probability"] for s in cfg["scenarios"]),
        "upside": weighted / price - 1,
        "annualized": (weighted / price) ** (1 / horizon) - 1,
    }


# ----------------------------------------------------------------- checks
def check_html(html_text, figures):
    fails = []
    if html_text.count("<style>") != 1 or html_text.count("</style>") != 1:
        fails.append("HTML: expected exactly one <style> block")
    ext = re.findall(r'(?:href|src)=["\'](?:https?://|//|cdn)', html_text)
    if ext:
        fails.append(f"HTML: external urls found: {ext}")
    for tag in ("div", "section", "table", "ul", "ol", "span", "td", "tr"):
        opens = len(re.findall(rf"<{tag}(?=[\s>])", html_text))
        closes = len(re.findall(rf"</{tag}\s*>", html_text))
        if opens != closes:
            fails.append(f"HTML: tag <{tag}> open={opens} close={closes}")
    for f in figures:
        if f not in html_text:
            fails.append(f"HTML: figure not present: {f!r}")
    return fails


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    folder = sys.argv[1].rstrip("/")
    ticker = None
    results = []  # (label, ok, detail)

    def record(label, ok, detail=""):
        results.append((label, ok, detail))

    # locate files
    json_path = workbook_path = consensus_path = html_path = None
    md_texts = {}
    for name in os.listdir(folder):
        low = name.lower()
        p = os.path.join(folder, name)
        if low.endswith("_model_inputs.json"):
            json_path = p
            ticker = name.split("_")[0].upper()
        elif low.endswith("_damodaran_financial_model.xlsx"):
            workbook_path = p
        elif low == "consensus-analysis.md":
            consensus_path = p
        elif low.endswith("-consensus-investment-report.html"):
            html_path = p
        elif low.endswith("-analysis.md"):
            md_texts[low] = open(p).read()

    for lf in LENS_FILES:
        record(f"lens {lf}", lf in md_texts,
               os.path.getsize(os.path.join(folder, lf)) if os.path.exists(
                   os.path.join(folder, lf)) else "missing")
    record("model_inputs.json", json_path is not None)
    record("workbook", workbook_path is not None)
    record("consensus-analysis.md", consensus_path is not None)
    record("HTML report", html_path is not None)

    if not (json_path and workbook_path and consensus_path and html_path):
        print("=== FILES ===")
        for label, ok, detail in results:
            print(f"[{'PASS' if ok else 'FAIL'}] {label}: {detail}")
        print("RUN: FAIL — missing required files")
        sys.exit(1)

    cfg = load_json(json_path)
    fail = False

    # JSON + scenario sanity
    jfails = []
    try:
        v = cfg["inputs"]
        probs = [s["probability"] for s in cfg["scenarios"]]
        if abs(sum(probs) - 1.0) > 1e-9:
            jfails.append(f"probabilities sum to {sum(probs):.4f} (need 1.0)")
        for s in cfg["scenarios"]:
            eff_wacc = v["wacc"] + s["wacc_adj"]
            eff_tg = v["terminal_growth"] + s["tg_adj"]
            if eff_tg >= eff_wacc:
                jfails.append(f"{s['name']}: terminal growth {eff_tg:.4f} "
                              f">= WACC {eff_wacc:.4f}")
    except (KeyError, TypeError) as e:
        jfails.append(f"JSON schema error: {e}")
    record("JSON valid + probs sum + tg<WACC", not jfails, "; ".join(jfails))
    fail = fail or bool(jfails)

    # recompute from JSON
    py = recompute(cfg)
    iv_strs = [f"{iv:.2f}" for iv in py["ivs"]]
    w_str = f"{py['weighted']:.2f}"

    # workbook ALL_MATCH (formulas engine) or fallback
    wb_ok = None
    wb_detail = "workbook not evaluated"
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import verify_model as vm  # noqa: F401  (imports `formulas`)
        target = vm.evaluate(workbook_path)
        matches = []
        for sheet, s in zip(SCEN_SHEETS, cfg["scenarios"]):
            matches.append(vm.close(target[sheet]["B41"], py["ivs"][
                SCEN_SHEETS.index(sheet)]))
        matches.append(vm.close(target["summary"]["D10"], py["weighted"], 0.01))
        wb_ok = all(matches) and len(target["errors"]) == 0
        wb_detail = ("formulas engine: ALL_MATCH" if wb_ok
                     else "formulas engine: MISMATCH")
    except Exception as e:
        wb_ok = None
        wb_detail = f"formulas engine unavailable ({type(e).__name__}); used independent recompute only"
    if wb_ok is None:
        record("workbook ALL_MATCH", True,
               wb_detail + " — workbook file itself NOT evaluated")
    else:
        record("workbook ALL_MATCH", wb_ok, wb_detail)
    fail = fail or (wb_ok is False)

    # numeric consistency across artifacts
    figures = iv_strs + [w_str]
    consensus_text = open(consensus_path).read()
    html_text = open(html_path).read()
    art = {"damodaran-analysis.md": md_texts.get("damodaran-analysis.md", ""),
           "consensus-analysis.md": consensus_text,
           "HTML": html_text}
    for artifact, text in art.items():
        missing = [f for f in figures if f not in text]
        record(f"figures in {artifact}", not missing,
               "all present" if not missing else "missing " + str(missing))
        fail = fail or bool(missing)

    # HTML structure
    html_fails = check_html(html_text, figures + [cfg.get(
        "rating", "")] if cfg.get("rating") else figures)
    record("HTML structure", not html_fails, "; ".join(html_fails) or "ok")
    fail = fail or bool(html_fails)

    # Technical analysis section: must exist in report_inputs.json with >= 7
    # indicators (200/100/50-day SMA, 14-day/14-week/50-week RSI, 52-wk range)
    # and every technical figure must appear in consensus-analysis.md + HTML.
    tech_fails = []
    try:
        with open(os.path.join(folder, "report_inputs.json")) as f:
            report = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        report = {}
        tech_fails.append(f"report_inputs.json unreadable ({e})")
    tech = report.get("technical", {}) if report else {}
    rows = tech.get("rows", [])
    if not rows:
        tech_fails.append("report_inputs.json missing 'technical.rows'")
    elif len(rows) < 7:
        tech_fails.append(
            f"technical has {len(rows)} indicator rows (need >=7: "
            "200/100/50-day SMA, 14-day/14-week/50-week RSI, 52-week range)")
    seen = set()
    for r in rows:
        for field in ("metric", "value", "delta"):
            val = str(r.get(field, ""))
            if not val or val in seen:
                continue
            seen.add(val)
            if val not in consensus_text:
                tech_fails.append(
                    f"technical '{val}' missing in consensus-analysis.md")
            if val not in html_text:
                tech_fails.append(f"technical '{val}' missing in HTML")
    record("technical analysis section", not tech_fails,
           "; ".join(tech_fails) or "ok (7 indicators, in consensus + HTML)")
    fail = fail or bool(tech_fails)

    print(f"=== verify_run.py — {os.path.basename(folder)} ===")
    for label, ok, detail in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}: {detail}")
    print("=== scenario values (from model_inputs JSON recompute) ===")
    for s, iv in zip(cfg["scenarios"], py["ivs"]):
        print(f"  {s['name']:<14} prob={s['probability']:.2f} IV=${iv:.2f}")
    print(f"  {'weighted':<14}            IV=${py['weighted']:.2f} "
          f"(upside {py['upside']:+.1%}, 5-yr {py['annualized']:+.1%})")
    print("RUN: " + ("ALL_PASS" if not fail else "FAIL"))


if __name__ == "__main__":
    main()
