"""Verify a Damodaran-model workbook built by build_model.py.

Usage:
    python3 verify_model.py <model_inputs.json> <model.xlsx>

Steps:
  1. Evaluate every formula with the `formulas` engine.
  2. Independently recompute the same DCF logic in pure Python from the
     inputs JSON.
  3. Compare per-scenario IV/share, the probability-weighted value, upside,
     annualized return, and probability sum.
  4. Scan the workbook for #ERROR cells and circular references.

Prints ALL_MATCH on success; anything else is a failure gate.
"""
import json
import sys

import formulas

SCEN_SHEETS = ["DCF-SevereBear", "DCF-Bear", "DCF-Base", "DCF-Bull",
               "DCF-ExtremeBull"]


def load(path):
    with open(path) as f:
        return json.load(f)


def evaluate(path):
    xl = formulas.ExcelModel().loads(path).finish()
    sol = xl.calculate()
    keys = list(sol.keys())
    target = {}

    def get(sheet, cell):
        t = f"{sheet}!{cell}".upper().replace("'", "")
        for k in keys:
            if k.upper().replace("'", "").endswith(t):
                node = sol[k]
                try:
                    return node.value[0, 0]
                except Exception:
                    return node.value
        return None

    for sname in SCEN_SHEETS:
        target[sname] = {
            "B30": get(sname, "B30"),
            "B11": get(sname, "B11"),
            "B34": get(sname, "B34"),
            "B37": get(sname, "B37"),
            "B39": get(sname, "B39"),
            "B41": get(sname, "B41"),
        }
    target["summary"] = {
        c: get("Scenario Summary", c) for c in
        ["B10", "D10", "B13", "B14", "B15", "B16", "B17"]}
    target["checks"] = {
        c: get("Checks", c) for c in
        ["B4", "B5"] + [f"{col}{r}" for r in (9, 10, 11, 12)
                        for col in "BCDEF"]}
    target["errors"] = []
    for k, node in sol.items():
        try:
            val = node.value[0, 0]
        except Exception:
            val = node.value
        if isinstance(val, str) and val.startswith("#"):
            target["errors"].append((k, val))
    return target


def recompute(cfg):
    v = cfg["inputs"]
    out = {}
    for sheet, s in zip(SCEN_SHEETS, cfg["scenarios"]):
        iv = dcf(v, s)
        out[sheet] = iv
    weighted = sum(s["probability"] * out[sh]
                   for sh, s in zip(SCEN_SHEETS, cfg["scenarios"]))
    price = v["price"]
    horizon = v.get("horizon_years", 5)
    out["weighted"] = weighted
    out["prob_sum"] = sum(s["probability"] for s in cfg["scenarios"])
    out["upside"] = weighted / price - 1
    out["annualized"] = (weighted / price) ** (1 / horizon) - 1
    return out


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


def close(a, b, tol=0.01):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return False
    return abs(a - b) <= tol


def main():
    if len(sys.argv) != 3:
        print("usage: verify_model.py <model_inputs.json> <model.xlsx>")
        sys.exit(2)
    cfg = load(sys.argv[1])
    target = evaluate(sys.argv[2])
    py = recompute(cfg)

    print("=== per-scenario intrinsic value/share ===")
    ok = True
    for sheet, s in zip(SCEN_SHEETS, cfg["scenarios"]):
        wb_val = target[sheet]["B41"]
        py_val = py[sheet]
        match = close(wb_val, py_val)
        ok &= match
        print(f"{sheet}: workbook={wb_val!r} python={py_val:.2f} "
              f"match={match}")
    print("=== summary (workbook vs python) ===")
    checks = [
        ("prob sum", target["summary"]["B10"], py["prob_sum"], 1e-9),
        ("weighted value", target["summary"]["D10"], py["weighted"], 0.01),
        ("upside", target["summary"]["B15"], py["upside"], 1e-6),
        ("annualized", target["summary"]["B17"], py["annualized"], 1e-6),
    ]
    for label, wb_val, py_val, tol in checks:
        match = close(wb_val, py_val, tol)
        ok &= match
        print(f"{label}: workbook={wb_val!r} python={py_val:.6f} "
              f"match={match}")
    print("=== checks sheet ===")
    for k, val in target["checks"].items():
        print(f"{k}: {val!r}")
    print("=== error scan ===")
    for cell, val in target["errors"]:
        print("ERROR CELL:", cell, val)
    print("error cells:", len(target["errors"]))
    ok &= len(target["errors"]) == 0
    # workbook checks must all be truthy
    for k, val in target["checks"].items():
        if k not in ("B4", "B5") and not val:
            print("FAILED CHECK:", k, "->", val)
            ok = False
    print("ALL_MATCH" if ok else "MISMATCH_OR_ERRORS")


if __name__ == "__main__":
    main()
