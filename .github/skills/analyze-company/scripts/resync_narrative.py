"""Re-sync the Damodaran lens narrative (damodaran-analysis.md) to the workbook.

The workbook is the source of truth. This script recomputes every intrinsic
value / share (per scenario), the probability-weighted value, and the implied
upside / annualized return from the *verified* workbook (via verify_model.evaluate)
or, if the workbook is unavailable, from verify_run.recompute (pure Python DCF),
then rewrites the numbers embedded in the narrative so the story always matches
the model.

Usage:
    python3 resync_narrative.py <folder> [--dry-run]

where <folder> is an analysis output dir such as Analysis/BRK/2026-08-16
containing  {TICKER}_model_inputs.json,
             {TICKER}_Damodaran_Financial_Model.xlsx,
             damodaran-analysis.md.

It rewrites five spots in damodaran-analysis.md:
  1. Exec-summary rows:  Base / Bear / Bull / Severe Bear / Extreme Bull /
                         Probability-weighted / Implied upside
  2. §13 scenario table (cells[-3] = IV/share, cells[-2] = vs price)
  3. §20 value table     (cells[3] = Value/share, cells[4] = Return at price)
  4. §20 weighted bullet ("Probability-weighted intrinsic value: ≈$X")
  5. §20 expected-return bullet (optional; only if present)

Prints a unified diff. Exit 0 if all required patterns were found and applied
(or were already correct); exit 1 if any required pattern is missing.
"""
import difflib
import glob
import json
import os
import re
import sys

# Keep everything self-contained in this scripts dir.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SCEN_ORDER = ["Severe Bear", "Bear", "Base", "Bull", "Extreme Bull"]


# ---------------------------------------------------------------- formatting
def fmt_price(x):
    return f"${x:.2f}"


def pct_str(x, nd=0):
    """Format a fraction (e.g. -0.49) as +19% / −49% using U+2212 minus."""
    pct = x * 100
    sign = "+" if pct >= 0 else "\u2212"
    return f"{sign}{abs(pct):.{nd}f}%"


def load_values(folder):
    """Return dict with ivs (per SCEN_ORDER), weighted, price, horizon."""
    inputs_path = glob.glob(os.path.join(folder, "*_model_inputs.json"))
    if not inputs_path:
        raise SystemExit(f"ERROR: no *_model_inputs.json in {folder}")
    with open(inputs_path[0]) as f:
        cfg = json.load(f)
    price = float(cfg["inputs"]["price"])
    horizon = float(cfg["inputs"].get("horizon_years", 5))

    # Prefer the verified workbook; fall back to the pure-Python recompute.
    ivs, weighted = None, None
    wb = glob.glob(os.path.join(folder, "*_Damodaran_Financial_Model.xlsx"))
    if wb:
        try:
            import verify_model
            target = verify_model.evaluate(wb[0])
            ivs = [float(target[s]["B41"]) for s in verify_model.SCEN_SHEETS]
            weighted = float(target["summary"]["D10"])
        except Exception as e:  # noqa: BLE001
            print(f"  ! workbook evaluate failed ({e}); using recompute fallback")
            ivs, weighted = None, None
    if ivs is None:
        import verify_run
        out = verify_run.recompute(cfg)
        ivs = [float(out[s]) for s in
               ["DCF-SevereBear", "DCF-Bear", "DCF-Base",
                "DCF-Bull", "DCF-ExtremeBull"]]
        weighted = float(out["weighted"])

    return {
        "ivs": ivs,
        "weighted": weighted,
        "price": price,
        "horizon": horizon,
        "upside": weighted / price - 1,
        "annualized": (weighted / price) ** (1 / horizon) - 1,
    }


# ---------------------------------------------------------------- edit specs
def split_cells(line):
    return line.split("|")


def join_cells(cells):
    return "|".join(cells)


# Token regexes: match only the numeric token, leaving bold `**`, `≈`, and
# column-padding whitespace untouched so alignment is preserved.
IV_TOKEN = re.compile(r"(\$[\d,]+\.\d{2})")
PCT_TOKEN = re.compile(r"([+\u2212-][\d.]+%)")


def replace_token(cell, pattern, repl):
    """Replace the FIRST token matched by `pattern` in `cell` with `repl`,
    preserving every surrounding character (spaces, **, ≈)."""
    return pattern.sub(lambda m: repl, cell, count=1)


def edit_exec_summary(lines, v):
    """1. Exec-summary rows keyed by label prefix. Preserve column padding."""
    mid_for = {
        "Base intrinsic value / share":
            lambda: f"≈ {fmt_price(v['ivs'][2])}",
        "Bear / Bull value / share":
            lambda: (f"≈ {fmt_price(v['ivs'][1])} / "
                     f"≈ {fmt_price(v['ivs'][3])}"),
        "Severe Bear / Extreme Bull value / share":
            lambda: (f"≈ {fmt_price(v['ivs'][0])} / "
                     f"≈ {fmt_price(v['ivs'][4])}"),
        "Probability-weighted value / share":
            lambda: f"≈ {fmt_price(v['weighted'])}",
        "Implied upside at":
            lambda: (f"≈ **{pct_str(v['upside'])}** "
                     f"(annualized ≈ {pct_str(v['annualized'], 1)})"),
    }
    matched = {k: False for k in mid_for}
    for i, line in enumerate(lines):
        cells = split_cells(line)
        if len(cells) < 4:
            continue
        label = cells[1].strip()
        for prefix, make in mid_for.items():
            if not matched[prefix] and label.startswith(prefix):
                m = re.match(r"^(\s*)(.*?)(\s*)$", cells[2], re.S)
                lead, _mid, trail = m.groups()
                cells[2] = f"{lead}{make()}{trail}"
                lines[i] = join_cells(cells)
                matched[prefix] = True
                break
    return [k for k, m in matched.items() if not m]


def edit_scenario13(lines, v):
    """2. §13 scenario table: cells[-3] = IV/share, cells[-2] = vs price.
    Token-only replacement preserves **bold** and column alignment."""
    missing = []
    row_iv = {
        "**Severe Bear**": v["ivs"][0], "**Bear**": v["ivs"][1],
        "**Base**": v["ivs"][2], "**Bull**": v["ivs"][3],
        "**Extreme Bull**": v["ivs"][4],
    }
    for i, line in enumerate(lines):
        cells = split_cells(line)
        if len(cells) < 4:
            continue
        name = cells[1].strip()
        if name in row_iv:
            iv = row_iv[name]
            cells[-3] = replace_token(cells[-3], IV_TOKEN, fmt_price(iv))
            cells[-2] = replace_token(
                cells[-2], PCT_TOKEN, pct_str(iv / v["price"] - 1))
            lines[i] = join_cells(cells)
        elif name == "**Weighted**":
            cells[-3] = replace_token(
                cells[-3], re.compile(r"(≈?\s*)\$[\d,]+\.\d{2}"),
                f"≈{fmt_price(v['weighted'])}")
            cells[-2] = replace_token(
                cells[-2], PCT_TOKEN, pct_str(v["upside"]))
            lines[i] = join_cells(cells)
    return missing


def edit_scenario20(lines, v):
    """3. §20 value table: cells[3] = Value/share, cells[4] = Return.
    Token-only replacement preserves column alignment."""
    missing = []
    row_iv = {
        "Severe Bear": v["ivs"][0], "Bear": v["ivs"][1], "Base": v["ivs"][2],
        "Bull": v["ivs"][3], "Extreme Bull": v["ivs"][4],
    }
    for i, line in enumerate(lines):
        cells = split_cells(line)
        if len(cells) < 6:
            continue
        name = cells[1].strip()
        if name in row_iv:
            iv = row_iv[name]
            cells[3] = replace_token(cells[3], IV_TOKEN, fmt_price(iv))
            cells[4] = replace_token(
                cells[4], PCT_TOKEN, pct_str(iv / v["price"] - 1))
            lines[i] = join_cells(cells)
    return missing


def edit_weighted_bullets(lines, v):
    """4+5. §20 bullets: weighted IV + optional expected-return bullet."""
    missing = []
    found_w = found_r = False
    pat_w = re.compile(
        r"(- \*\*Probability-weighted intrinsic value: )(≈?\s*\$[\d.,]+)")
    pat_r = re.compile(
        r"(- \*\*Expected one-time return:\*\* )(≈ [^()]+(\(annualized ≈ [^)]+\)))")
    for i, line in enumerate(lines):
        if pat_w.search(line):
            lines[i] = pat_w.sub(
                lambda m: m.group(1) + f"≈{fmt_price(v['weighted'])}", line)
            found_w = True
        if pat_r.search(line):
            lines[i] = pat_r.sub(
                lambda m: (m.group(1)
                           + f"≈ {pct_str(v['upside'])} "
                           + f"(annualized ≈ {pct_str(v['annualized'], 1)})"),
                line)
            found_r = True
    if not found_w:
        missing.append("§20 weighted bullet")
    # Expected-return bullet is optional: only report (not fail) when missing.
    if not found_r:
        print("  ! §20 expected-return bullet not found (optional; skipped)")
    return missing


# ---------------------------------------------------------------- main
def main():
    args = [a for a in sys.argv[1:]]
    dry_run = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]
    if len(args) != 1:
        print(__doc__)
        sys.exit(2)
    folder = args[0]
    md_path = os.path.join(folder, "damodaran-analysis.md")
    if not os.path.exists(md_path):
        print(f"ERROR: no {md_path}")
        sys.exit(1)

    v = load_values(folder)
    print(f"price={fmt_price(v['price'])}  "
          f"ivs={[fmt_price(x) for x in v['ivs']]}  "
          f"weighted={fmt_price(v['weighted'])}  "
          f"upside={pct_str(v['upside'])}  "
          f"annualized={pct_str(v['annualized'], 1)}")

    with open(md_path) as f:
        original = f.read()
    lines = original.splitlines(keepends=True)

    missing = []
    missing += edit_exec_summary(lines, v)
    missing += edit_scenario13(lines, v)
    missing += edit_scenario20(lines, v)
    missing += edit_weighted_bullets(lines, v)

    new_text = "".join(lines)
    if new_text != original:
        diff = difflib.unified_diff(
            original.splitlines(True), new_text.splitlines(True),
            fromfile=f"damodaran-analysis.md", tofile="damodaran-analysis.md")
        sys.stdout.writelines(diff)
        if not dry_run:
            with open(md_path, "w") as f:
                f.write(new_text)
            print(f"APPLIED -> {md_path}")
        else:
            print("DRY-RUN (no changes written)")
    else:
        print("No changes: narrative already matches workbook")

    if missing:
        print("MISSING PATTERNS (script could not re-sync these):")
        for m in missing:
            print("  -", m)
        sys.exit(1)
    print("RESYNC OK")


if __name__ == "__main__":
    main()
