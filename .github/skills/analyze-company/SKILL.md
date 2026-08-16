---
name: analyze-company
description: Runs a complete three-lens investment analysis of a company and produces a full report set: parallel Buffett, Munger, and Damodaran persona analyses built on web research (company site, SEC EDGAR, investor releases, market data), a Damodaran-style scenario-DCF financial model spreadsheet, a deliberative-debate consensus synthesis with an investment recommendation, and a polished single-file HTML report. Use when the user asks to "analyze a company/stock/ticker", names a company or ticker to evaluate, or invokes /analyze-company <name-or-ticker>.
---

# analyze-company

Analyze one company through three investment lenses, then reconcile them into a single investment recommendation. Input is a company name or ticker symbol. Output is a dated folder of durable artifacts in the current workspace.

## Output contract

For `{TICKER}` analyzed on `{YYYY-MM-DD}`, create in the workspace root:

```text
{TICKER}/{YYYY-MM-DD}/
├── buffet-analysis.md                 # Warren Buffett lens
├── munger-analysis.md                 # Charlie Munger lens
├── damodaran-analysis.md              # Aswath Damodaran lens
├── druckenmiller-analysis.md          # Stanley Druckenmiller lens
├── soros-analysis.md                  # George Soros lens
├── {TICKER}_Damodaran_Financial_Model.xlsx   # 5-scenario FCFF DCF workbook
├── consensus-analysis.md              # deliberative debate + consensus
└── {ticker}-consensus-investment-report.html # polished single-file report
```

The gold standard for every artifact is the IREN example run. Read it before starting:
`./reference/IREN/` in this skill folder. The bundled `reference/example-report.html` is the same report as a standalone file — reuse its CSS design system verbatim.

## Phase 0 — Parse the invocation

0. If no argument was provided, ask the user which company to analyze before doing anything else. If more than one company was provided, ask the user which single company to analyze first; this skill analyzes one company per run.
1. The argument is a company name or ticker (e.g. `iren` → IREN, `Walmart` → WMT).
2. If a ticker was given: uppercase it.
3. If a name was given: resolve the ticker with a web search ("{name} stock ticker"). Prefer the primary listing.
4. Confirm the identity against a web search before any analysis: "{Ticker} stock" must return the intended company. If the lookup is ambiguous, stop and ask the user to disambiguate.
5. Set `{TICKER}` (uppercase) and `{YYYY-MM-DD}` (today's date). Create the output folder, relative to workspace root under 'Analysis', so `{TICKER}/{YYYY-MM-DD}/` exists. If the folder already exists, stop and ask the user to confirm overwriting it.
6. Never reuse or overwrite an existing dated folder for the same ticker; create a new dated folder.

## Phase 1 — Research + parallel per persona analyses

Launch **three subagents in parallel**, one per lens. Each subagent:

- Reads its profile file **verbatim** before writing anything:
  - Buffett → `profiles/buffet.md`
  - Munger → `profiles/munger.md`
  - Damodaran → `profiles/damodaran.md`
  - Druckenmiller → `profiles/druckenmiller.md`
  - Soros → `profiles/soros.md`
- Researches the company with web tools. Minimum sources, all with URLs:
  - company investor-relations site (latest 10-K/10-Q, earnings releases, investor decks)
  - SEC EDGAR filings (full-text search; DEF 14A for compensation)
  - market data (current price, shares outstanding, market cap)
  - competitor and industry data where the profile requires it
- Writes its full analysis to its output file in the dated folder.
- **Returns** a structured summary to the orchestrator (do not end the turn without it): rating, intrinsic-value estimates, key metrics, buy/sell zones, main risks, and source URLs used.

Depth gate — applies to all three analyses, checked in Phase 5:

- **Source floor:** large caps ≥ 12 distinct fetched sources with URLs; small caps ≥ 8. Every material number must trace to a source or carry an explicit "estimate" label. Link references must resolve to pages actually consulted.
- **Coverage floor:** every numbered section of the profile must be addressed. A section may be declared "not applicable" only with a one-line reason.
- **Research budget:** at most 5 additional search rounds after the initial pass. If data is still missing, state the gap in the analysis rather than researching indefinitely.

Mandatory per-lens output requirements (checked in Phase 5):

All five analyses open with the **bottom line first**: the final rating and a one-paragraph verdict, then an executive summary table (scores per dimension / value estimates) before any detailed section. This mirrors the IREN example and makes the three analyses cross-comparable.

- **Buffett** (`buffet-analysis.md`): bottom-line rating first; executive summary score table across the profile's dimensions; moat rating; management assessment; owner-earnings analysis; DCF with conservative/neutral/optimistic scenarios; margin-of-safety verdict; final A/B/C/D rating. Cite sources as `[SEC][1]`-style link references.
- **Munger** (`munger-analysis.md`): circle-of-competence rating; 3–5 mental models applied; inversion section (how the investment fails); quality standards checklist; earnings-quality tests; conservative DCF (WACC+3% discount, terminal growth ≤2%); scenario table with probabilities and expected return; final A/B/C/D rating.
- **Damodaran** (`damodaran-analysis.md`): the full profile arc — fundamental story, historical fundamentals, competitive advantage, accounting normalization, growth, risk, WACC, FCFF DCF, terminal value, relative valuation, reverse DCF, five-scenario valuation, sensitivity, market-expectations comparison, probability-weighted case, A–E rating, five conclusions, Damodaran-style final judgment. **Additionally** the Damodaran subagent must return a `model_inputs` JSON block (schema below) populated with the company's numbers, so Phase 2 can build the workbook without re-deriving inputs.
- **Druckenmiller** (`druckenmiller-analysis.md`): macroeconomic context, interest-rate and inflation sensitivity, liquidity and credit risk, market sentiment, relative valuation, scenario analysis, expected return distribution, final A–E rating.
- **Soros** (`soros-analysis.md`): reflexivity analysis, feedback loops, market psychology, trend and momentum analysis, scenario analysis, expected return distribution, final A–E rating.

```json
{
  "company": "IREN",
  "ticker": "IREN",
  "date": "2026-08-16",
  "inputs": {
    "price": 45.0,
    "shares_mm": 380.0,
    "cash_mm": 2600.0,
    "debt_mm": 3800.0,
    "revenue_run_rate_mm": 3700.0,
    "growth_y1": 0.45,
    "growth_decay": 0.06,
    "margin_y1": 0.25,
    "margin_terminal": 0.42,
    "tax_rate": 0.18,
    "wacc": 0.115,
    "terminal_growth": 0.03,
    "roic_terminal": 0.15,
    "roic_initial": 0.22,
    "margin_ramp": 0.025,
    "min_growth": 0.05,
    "horizon_years": 5
  },
  "scenarios": [
    {
      "name": "Severe Bear",
      "probability": 0.1,
      "growth_adj": -0.25,
      "margin_adj": -0.15,
      "wacc_adj": 0.025,
      "tg_adj": -0.005,
      "roic_adj": -0.05,
      "description": "AI economics deteriorate; high financing risk"
    },
    {
      "name": "Bear",
      "probability": 0.2,
      "growth_adj": -0.15,
      "margin_adj": -0.08,
      "wacc_adj": 0.015,
      "tg_adj": -0.0025,
      "roic_adj": -0.03,
      "description": "Slower AI growth, weaker margins"
    },
    {
      "name": "Base",
      "probability": 0.35,
      "growth_adj": 0.0,
      "margin_adj": 0.0,
      "wacc_adj": 0.0,
      "tg_adj": 0.0,
      "roic_adj": 0.0,
      "description": "Strong execution but normalized returns"
    },
    {
      "name": "Bull",
      "probability": 0.25,
      "growth_adj": 0.1,
      "margin_adj": 0.05,
      "wacc_adj": -0.01,
      "tg_adj": 0.0025,
      "roic_adj": 0.03,
      "description": "Strong utilization/pricing and execution"
    },
    {
      "name": "Extreme Bull",
      "probability": 0.1,
      "growth_adj": 0.2,
      "margin_adj": 0.1,
      "wacc_adj": -0.015,
      "tg_adj": 0.005,
      "roic_adj": 0.05,
      "description": "Exceptional AI platform economics"
    }
  ]
}
```

Rules for the JSON:

- **The example values above are IREN's. Replace every value with the target company's numbers — never ship the example numbers.** Use `scripts/model_inputs.example.json` as a shape reference only.
- Scenario probabilities **must sum to 1.0** exactly. Adjust the Base probability to make it so.
- All adjustments are in decimal points (e.g. `growth_adj: -0.15` = −15 pts on the Y1 growth rate).
- `tg_adj` is applied to terminal growth; terminal growth must stay **below** the effective WACC in every scenario (checked by the workbook and verifier).
- Values come from the company's actual filings and market data, not placeholders.
- The example above is IREN's; the schema is also in `scripts/model_inputs.example.json`.

## Phase 2 — Damodaran financial model spreadsheet

1. Save the Damodaran subagent's `model_inputs` JSON to `{TICKER}/{YYYY-MM-DD}/{TICKER}_model_inputs.json`.
2. Build the workbook:

```bash
UV_CACHE_DIR="$PWD/.uv-cache" uv run --no-project --python 3.13 --with openpyxl -- \
  python3 /Users/Mark/.copilot/skills/analyze-company/scripts/build_model.py \
  "{TICKER}/{YYYY-MM-DD}/{TICKER}_model_inputs.json" \
  "{TICKER}/{YYYY-MM-DD}/{TICKER}_Damodaran_Financial_Model.xlsx"
```

3. Verify it (recomputes every formula with the `formulas` engine and independently recomputes the same DCF logic in pure Python):

```bash
UV_CACHE_DIR="$PWD/.uv-cache" uv run --no-project --python 3.13 --with openpyxl --with formulas -- \
  python3 /Users/Mark/.copilot/skills/analyze-company/scripts/verify_model.py \
  "{TICKER}/{YYYY-MM-DD}/{TICKER}_model_inputs.json" \
  "{TICKER}/{YYYY-MM-DD}/{TICKER}_Damodaran_Financial_Model.xlsx"
```

4. **Gate:** the verifier must print `ALL_MATCH`. If not, fix the JSON inputs or the builder, rebuild, and re-verify. Do not continue with a failing workbook.
   - `ALL_MATCH` but a Checks-sheet cell is FALSE (e.g. terminal growth ≥ WACC in a scenario): lower that scenario's `tg_adj`, raise its `wacc_adj`, or lower the base `terminal_growth`, then rebuild and re-verify.
   - Builder or verifier raises a traceback: fix the JSON first (wrong types, missing keys, probabilities not summing to 1), then the script. Verify with `python3 -m json.tool` that the JSON is valid before rebuilding.
5. Record the five scenario IV/share values and the probability-weighted value — the consensus debate will need them.
6. **Re-sync the narrative (mandatory):** the workbook is the source of truth for Damodaran's numbers. Edit `damodaran-analysis.md` so its executive-summary table, scenario table, and probability-weighted value use the **verified workbook values**. If the narrative's earlier scenario figures differ materially, keep the verified numbers and add one line noting the calibration. This rule exists because the IREN reference run itself drifted (workbook weighted value ≠ narrative weighted value) — do not reproduce that drift.

Workbook contents (built from scratch by `scripts/build_model.py`): README, Inputs, Scenarios, five complete 10-year FCFF DCF sheets (`DCF-SevereBear` … `DCF-ExtremeBull`), a circularity-free `Scenario Summary` (probability-weighted value, expected upside, annualized return), Reverse DCF, two sensitivity grids, and a Checks sheet. The summary never feeds back into any DCF.

Environment notes (from the IREN run): this Mac has no LibreOffice, so the `formulas` engine is the verification path. `uv` needs `--no-project` and a workspace-local `UV_CACHE_DIR` inside the sandbox. If the `formulas` package cannot be installed, verify sheet-by-sheet with openpyxl data_only reads plus the independent Python recomputation inside `verify_model.py` and state clearly which verification was used.

## Phase 3 — Deliberative debate & consensus synthesis

Launch **one subagent** to produce `consensus-analysis.md`. The subagent must:

1. Read all three lens analyses in the dated folder plus the verified model output (five scenario values, weighted value). Damodaran's column of the consensus valuation matrix **must use the verified workbook values**; if a narrative value contradicts the workbook, the workbook wins and the disagreement is a point of contention worth recording.
2. Run a **structured deliberative debate**, not a merge summary:
   - **Shared fact base** — a table of facts all three analyses agree on (price band, shares, revenue, key contracts/figures, cash/debt, compensation, share-count trajectory), each with its source.
   - **Opening statements** — each profile's position in its own voice.
   - **Points of agreement** — the uncontested consensus core.
   - **Points of contention** — **at least 5 contentions**, each with: each side's argument, cross-examination, an explicit named concession by at least one profile, and a recorded **resolution**. Contend at minimum on: reference price, base-case intrinsic value, right-tail credit, the price that compensates for uncertainty, and management quality. Fewer than 5 contentions means the debate was not actually run.
   - **Final rebuttals and concessions** — one paragraph each.
   - **Debate conclusion** — the unanimous rating and conditions.
3. Write **Part II — The Consensus Synthesis**: the business (what you own); the economics (the one valuation-critical variable, e.g. incremental ROIC vs WACC, with a monitoring hierarchy); management score; consensus valuation matrix (each scenario × each profile's value → consensus value + consensus probability); probability-weighted consensus value with confidence level; reverse-DCF check of what the market price assumes; pros and cons (for/against at the current price); **consensus investment recommendation** (rating A–E, do-not-initiate band, a **price ladder** table of bands → actions, what upgrades the rating, what downgrades it); the five consensus conclusions; and a final consensus judgment paragraph.
4. Rules: introduce **no new valuation math** — synthesize, challenge, and merge what the three profiles concluded. Flag any place the three disagree and why. End with a disclaimer that this is an estimate of estimates, not investment advice.

Output format must mirror the IREN `consensus-analysis.md` structure (method note → shared fact base → debate rounds → Part II synthesis).

## Phase 4 — Polished HTML report

Produce `{ticker}-consensus-investment-report.html` (lowercased ticker) — a single-file, self-contained HTML report of the consensus.

Requirements:

- Read `reference/html-design.md` and reuse the design system from `reference/example-report.html` (navy/gold palette, hero header, numbered sections, card grids, tags, chips, rating badge, styled tables). Do not import external CSS/fonts/JS; system font stack only.
- Content mirrors the consensus: hero with ticker + rating badge, executive summary cards, the three positions, points of agreement/contention summary, consensus valuation matrix table, probability-weighted value, pros/cons, price ladder table, upgrade/downgrade triggers, five conclusions, disclaimer.
- All numbers must match `consensus-analysis.md` and the verified workbook exactly.
- Open the file via `file://` in the browser to confirm it renders; fix any layout breakage. If no browser is available, verify structurally instead: check the file has a single `<style>` block, no external URLs (`http://`, `https://`, `cdn`), balanced tags for `div/section/table`, and that every figure string from the consensus appears at least once — and state that browser rendering was not verified.
- **Final number re-check:** after writing the HTML, diff its key figures (rating, base value, weighted value, scenario range, price ladder) against `consensus-analysis.md` and the verified workbook. Fix any mismatch before closing the phase. The HTML is a rendering of the consensus — it never introduces new numbers.

## Phase 5 — Verification & delivery

Run the completion checklist. All must pass before reporting done:

- [ ] `buffet-analysis.md`, `munger-analysis.md`, `damodaran-analysis.md`, `druckenmiller-analysis.md`, `soros-analysis.md` exist, each following its profile's framework with final rating + source links, and each passing the depth gate (source floor, coverage floor)
- [ ] `{TICKER}_Damodaran_Financial_Model.xlsx` exists and verifier printed `ALL_MATCH`
- [ ] `consensus-analysis.md` contains the full debate (fact base, openings, agreements, contentions with resolutions, rebuttals, Part II synthesis, rating, price ladder)
- [ ] `{ticker}-consensus-investment-report.html` renders cleanly and matches the consensus numbers
- [ ] **Numeric consistency:** the five scenario values are identical in the workbook, `damodaran-analysis.md`, `consensus-analysis.md`, and the HTML report
- [ ] Every number in the final deliverables traces to a source or is labeled as an estimate

Then summarize in chat: consensus rating, valuation range, weighted value, price ladder, and paths to each artifact.

## Cross-cutting rules

- **Research is mandatory.** Never analyze from memory. Every figure in an analysis must come from a fetched source (company IR page, EDGAR, press release, market data) and carry a URL. If a figure cannot be found, say so explicitly and use a labeled approximation — never invent a number, quote, or filing.
- **No fabricated sources.** Link references must resolve to real pages actually consulted.
- **Honesty over precision.** Profiles demand probability distributions and ranges; do not manufacture certainty. Ratings can be unanimous C — that is a feature, not a bug.
- **Three lenses stay independent.** Each subagent works from its own profile and its own research; no lens writes or reads another lens's draft. Reconcile only in Phase 3.
- **The workbook is the Damodaran lens's spine.** Its five scenario IV/share values must appear in `damodaran-analysis.md`'s scenario section and feed the consensus valuation matrix.
- **One number, one source.** The same figure must have the same value in every artifact. The verified workbook is authoritative for Damodaran scenario values; the consensus is authoritative for the final rating and price ladder. If artifacts disagree, fix the outlier before delivery.

## Failure & recovery

- **Ticker lookup fails or is ambiguous** → stop and ask the user to disambiguate.
- **Company has no EDGAR filings** (foreign/private) → use the primary-exchange regulator's filings or company disclosures; mark the substitution explicitly; if financials are unavailable, still produce the three lens analyses but state the limitation and skip the workbook only if the Damodaran subagent cannot source defensible inputs (record this decision in the consensus).
- **Verification engine unavailable** → fall back to openpyxl data_only checks + the independent recomputation; state which verification was used.
- **A subagent returns without writing its file** → relaunch it once with the same prompt before proceeding.
- **Web tools fail entirely** → stop and tell the user; do not fabricate a research-backed analysis offline.

## Minimum compliance

Do not claim the skill ran unless all of these are true: three independent lens analyses exist with sources; the workbook exists and verification printed `ALL_MATCH`; the consensus contains real debate rounds with cross-examination and resolutions; the HTML exists and renders; and a final rating + price ladder are delivered. If any item is missing, return to the failed phase instead of pretending the workflow happened.
