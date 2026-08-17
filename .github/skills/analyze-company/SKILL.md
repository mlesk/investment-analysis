---
name: analyze-company
description: Runs a complete five-lens investment analysis of a company and produces a full report set: parallel Buffett, Munger, Damodaran, Druckenmiller, and Soros persona analyses built on web research (company site, SEC EDGAR, investor releases, market data), a Damodaran-style scenario-DCF financial model spreadsheet, a deliberative-debate consensus synthesis with an investment recommendation, and a polished single-file HTML report. Use when the user asks to "analyze a company/stock/ticker", names a company or ticker to evaluate, or invokes /analyze-company <name-or-ticker>.
---

# analyze-company

Analyze one company through five investment lenses (Buffett, Munger, Damodaran, Druckenmiller, Soros), then reconcile them into a single investment recommendation. Input is a company name or ticker symbol. Output is a dated folder of durable artifacts in the current workspace.

`{SKILL_DIR}` = the folder containing this SKILL.md (`.github/skills/analyze-company` in this repo; `~/.copilot/skills/analyze-company` if installed as a user skill). Every script command below uses `{SKILL_DIR}/scripts/...`. The compact format rules for every deliverable live in `{SKILL_DIR}/reference/format-spec.md` — subagents should read that instead of re-reading the full IREN anchor.

## Output contract

For `{TICKER}` analyzed on `{YYYY-MM-DD}`, create in the workspace under `Analysis/` (repo convention; `{folder}` = `Analysis/{TICKER}/{YYYY-MM-DD}/`):

```text
Analysis/{TICKER}/{YYYY-MM-DD}/
├── buffet-analysis.md                 # Warren Buffett lens
├── munger-analysis.md                 # Charlie Munger lens
├── damodaran-analysis.md              # Aswath Damodaran lens
├── druckenmiller-analysis.md          # Stanley Druckenmiller lens
├── soros-analysis.md                  # George Soros lens
├── {TICKER}_Damodaran_Financial_Model.xlsx   # 5-scenario FCFF DCF workbook
├── consensus-analysis.md              # deliberative debate + consensus
└── {ticker}-consensus-investment-report.html # polished single-file report
```

The gold standard for every artifact is the IREN example run. Read `./reference/IREN/` in this skill folder before starting; the compact format rules are in `./reference/format-spec.md`. The house CSS is embedded in `scripts/build_report.py` and rendered from a `report_inputs.json` — never hand-author HTML or redesign the CSS.

## Phase 0 — Parse the invocation

0. If no argument was provided, ask the user which company to analyze before doing anything else. If more than one company was provided, ask the user which single company to analyze first; this skill analyzes one company per run.
1. The argument is a company name or ticker (e.g. `iren` → IREN, `Walmart` → WMT).
2. If a ticker was given: uppercase it.
3. If a name was given: resolve the ticker with a web search ("{name} stock ticker"). Prefer the primary listing.
4. Confirm the identity against a web search before any analysis: "{Ticker} stock" must return the intended company. If the lookup is ambiguous, stop and ask the user to disambiguate.
5. Set `{TICKER}` (uppercase) and `{YYYY-MM-DD}` (today's date). Create the output folder, relative to workspace root under 'Analysis', so `{TICKER}/{YYYY-MM-DD}/` exists. If the folder already exists, stop and ask the user to confirm overwriting it.
6. Never reuse or overwrite an existing dated folder for the same ticker; create a new dated folder.

## Phase 1 — Research + parallel per persona analyses

**Shared fact pack (build once, before launching):** fetch the core market +
capital-structure facts a single time (reference price, shares, market cap,
revenue/margins, cash/debt, SBC, backlog/RPO or equivalent, 2–3 primary
source URLs, and **market technicals** — price vs 50/100/200-day SMA,
14-day RSI, 14-week RSI, 50-week RSI, and the 52-week high/low) and pass the
**same fact pack** to every lens subagent. This
kills numeric drift between lenses (they all start from identical numbers)
and stops five subagents from re-fetching the same sources. Optionally write
it to `{folder}/fact-pack.json`.

**Fetch budget (applies to every subagent, orchestrator included):** a hard
cap on research fetches — at most **15 fetches** per subagent, counted across
all research tools, before the initial write. After that, reuse the fact pack
and already-fetched pages; state a gap rather than fetching further. Never
paste raw SEC XBRL/companyfacts JSON, full 10-K text, or large page dumps
into a lens file, a subagent return, or the orchestrator context — extract
only the specific figures you need plus their URLs, then summarize. (The BRK
run showed a single companyfacts fetch can dump ~100k tokens into the
persistent orchestrator context; that is why this budget exists.)

Launch **five subagents in parallel**, one per lens. Each subagent:

- Reads its profile file **verbatim** before writing anything:
  - Buffett → `profiles/buffet.md`
  - Munger → `profiles/munger.md`
  - Damodaran → `profiles/damodaran.md`
  - Druckenmiller → `profiles/druckenmiller.md`
  - Soros → `profiles/soros.md`
- Reads `reference/format-spec.md` (compact) for output format
- Researches the company with web tools, seeded by the shared fact pack. Minimum sources, all with URLs:
  - company investor-relations site (latest 10-K/10-Q, earnings releases, investor decks)
  - SEC EDGAR filings (full-text search; DEF 14A for compensation)
  - market data (current price, shares outstanding, market cap)
  - competitor and industry data where the profile requires it
- Writes its full analysis to its output file in the dated folder, **ending with a `## Position Summary` block** (schema in `reference/format-spec.md`).
- **Returns** a compact structured summary only (~150–200 words): `RATING:` / `IV: bear=… base=… bull=… weighted=…` / `BUY_ZONE:` / `KEY_METRICS:` / `SOURCES: <count>`. Do **not** re-paste the file's tables, scenario tables, or full source lists — they live in the file and the consensus subagent reads them there. (A bloated return that duplicates the file wastes the orchestrator's context.)
- **Writes nothing else.** Rule: write ONLY your designated output file; do not write to memory, the skill folder, or any other file.
- The Damodaran subagent additionally returns the `model_inputs` JSON (schema below) — and **does not build or verify the workbook**; that is Phase 2, done by the orchestrator.

Depth gate — applies to all five analyses, checked in Phase 5:

- **Source floor:** large caps 8–12 distinct fetched sources with URLs; small caps 5–8. The exact count must respect the Phase 1 fetch budget — coverage quality over raw count. Every material number must trace to a source or carry an explicit "estimate" label. Link references must resolve to pages actually consulted.
- **Payload discipline:** when fetching, extract only the specific figures needed plus their URLs and summarize — never paste raw SEC XBRL/companyfacts JSON, full 10-K text, or large page dumps into a lens file, a subagent return, or the orchestrator context.
- **Coverage floor:** every numbered section of the profile must be addressed. A section may be declared "not applicable" only with a one-line reason.
- **Research budget:** at most 5 additional search rounds after the initial pass. If data is still missing, state the gap in the analysis rather than researching indefinitely.

Mandatory per-lens output requirements (checked in Phase 5):

All five analyses open with the **bottom line first**: the final rating and a one-paragraph verdict, then an executive summary table (scores per dimension / value estimates) before any detailed section. This mirrors the IREN example and makes the five analyses cross-comparable.

- **Buffett** (`buffet-analysis.md`): bottom-line rating first; executive summary score table across the profile's dimensions; moat rating; management assessment; owner-earnings analysis; DCF with conservative/neutral/optimistic scenarios; margin-of-safety verdict; final A/B/C/D rating. Cite sources as `[SEC][1]`-style link references.
- **Munger** (`munger-analysis.md`): circle-of-competence rating; 3–5 mental models applied; inversion section (how the investment fails); quality standards checklist; earnings-quality tests; conservative DCF (WACC+3% discount, terminal growth ≤2%); scenario table with probabilities and expected return; final A/B/C/D rating.
- **Damodaran** (`damodaran-analysis.md`): the full profile arc — fundamental story, historical fundamentals, competitive advantage, accounting normalization, growth, risk, WACC, FCFF DCF, terminal value, relative valuation, reverse DCF, five-scenario valuation, sensitivity, market-expectations comparison, probability-weighted case, A–E rating, five conclusions, Damodaran-style final judgment. **Additionally** the Damodaran subagent must return a `model_inputs` JSON block (schema below) populated with the company's numbers, so Phase 2 can build the workbook without re-deriving inputs. **The JSON must be machine-valid:** every fraction field a decimal float (e.g. `margin_ramp: 0.005`, never `5.0`), probabilities summing to 1.0, and it must pass `python3 -m json.tool`. Ship the numbers that actually drove the narrative — the workbook built from them is authoritative in Phase 2.
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
- **Fraction fields are decimal floats, not whole numbers.** `margin_ramp` is a per-year step (e.g. `0.005` = 0.5 pts/yr), never `5.0`; same rule applies to `growth_y1`, `margin_y1`, `wacc`, `terminal_growth`, `roic_*`. A whole number where a fraction belongs is the #1 JSON bug (a `5.0` margin ramp breaks the verifier).
- Values come from the company's actual filings and market data, not placeholders.
- **Reproducibility guardrail:** before Phase 2, the JSON must (a) parse with `python3 -m json.tool`, (b) build a workbook with `build_model.py`, and (c) pass `verify_model.py` (`ALL_MATCH`). If it fails, fix the JSON — not the scripts.
- The example above is IREN's; the schema is also in `scripts/model_inputs.example.json`.

## Phase 2 — Damodaran financial model spreadsheet

**Division of labor:** the Damodaran subagent supplies `model_inputs` JSON only. The **orchestrator** builds and verifies the workbook below. If a subagent already built a workbook, the orchestrator MUST re-run `verify_model.py` and require `ALL_MATCH` before trusting it.

1. Save the Damodaran subagent's `model_inputs` JSON to `{TICKER}/{YYYY-MM-DD}/{TICKER}_model_inputs.json`.
2. Build the workbook:

```bash
UV_CACHE_DIR="$PWD/.uv-cache" uv run --no-project --python 3.13 --with openpyxl -- \
  python3 {SKILL_DIR}/scripts/build_model.py \
  "{TICKER}/{YYYY-MM-DD}/{TICKER}_model_inputs.json" \
  "{TICKER}/{YYYY-MM-DD}/{TICKER}_Damodaran_Financial_Model.xlsx"
```

3. Verify it (recomputes every formula with the `formulas` engine and independently recomputes the same DCF logic in pure Python):

```bash
UV_CACHE_DIR="$PWD/.uv-cache" uv run --no-project --python 3.13 --with openpyxl --with formulas -- \
  python3 {SKILL_DIR}/scripts/verify_model.py \
  "{TICKER}/{YYYY-MM-DD}/{TICKER}_model_inputs.json" \
  "{TICKER}/{YYYY-MM-DD}/{TICKER}_Damodaran_Financial_Model.xlsx"
```

4. **Gate:** the verifier must print `ALL_MATCH`. If not, fix the JSON inputs or the builder, rebuild, and re-verify. Do not continue with a failing workbook.
   - `ALL_MATCH` but a Checks-sheet cell is FALSE (e.g. terminal growth ≥ WACC in a scenario): lower that scenario's `tg_adj`, raise its `wacc_adj`, or lower the base `terminal_growth`, then rebuild and re-verify.
   - Builder or verifier raises a traceback: fix the JSON first (wrong types, missing keys, probabilities not summing to 1), then the script. Verify with `python3 -m json.tool` that the JSON is valid before rebuilding.
5. Record the five scenario IV/share values and the probability-weighted value — the consensus debate will need them.
6. **Re-sync the narrative (mandatory, script-driven):** the workbook is the source of truth for Damodaran's numbers. Run the resync script — it recomputes every scenario IV/share, the weighted value, and the implied upside/annualized return from the verified workbook (falling back to the pure-Python recompute) and rewrites them into `damodaran-analysis.md`'s executive-summary table, §13 scenario table, §20 value table, and §20 weighted bullet:

```bash
python3 {SKILL_DIR}/scripts/resync_narrative.py "{TICKER}/{YYYY-MM-DD}"
```

It prints a unified diff and exits 0 only if every required pattern was found. If a pattern is reported MISSING, add/fix that spot in the narrative by hand, then re-run. If the narrative's earlier scenario figures differ materially from the workbook, keep the verified numbers and add one line noting the calibration. This rule exists because the IREN reference run itself drifted (workbook weighted value ≠ narrative weighted value) — do not reproduce that drift.

Workbook contents (built from scratch by `scripts/build_model.py`): README, Inputs, Scenarios, five complete 10-year FCFF DCF sheets (`DCF-SevereBear` … `DCF-ExtremeBull`), a circularity-free `Scenario Summary` (probability-weighted value, expected upside, annualized return), Reverse DCF, two sensitivity grids, and a Checks sheet. The summary never feeds back into any DCF.

Environment notes (from the IREN run): this Mac has no LibreOffice, so the `formulas` engine is the verification path. `uv` needs `--no-project` and a workspace-local `UV_CACHE_DIR` inside the sandbox. If the `formulas` package cannot be installed, verify sheet-by-sheet with openpyxl data_only reads plus the independent Python recomputation inside `verify_model.py` and state clearly which verification was used.

## Phase 3 — Deliberative debate & consensus synthesis

Launch **one subagent** to produce `consensus-analysis.md` **and** `report_inputs.json` (its two designated output files — see Cross-cutting rules). The subagent must:

1. Read all five lens analyses in the dated folder (start with each file's `## Position Summary` block, then read the full files as needed) plus the verified model output (five scenario values, weighted value). Damodaran's column of the consensus valuation matrix **must use the verified workbook values verbatim at two decimals** (e.g. `$257.14/$310.98/$447.31/$602.47/$871.86`); if a narrative value contradicts the workbook, the workbook wins and the disagreement is a point of contention worth recording.
2. Run a **structured deliberative debate**, not a merge summary:
   - **Shared fact base** — a table of facts all five analyses agree on (price band, shares, revenue, key contracts/figures, cash/debt, compensation, share-count trajectory), each with its source.
   - **Opening statements** — each profile's position in its own voice.
   - **Points of agreement** — the uncontested consensus core.
   - **Points of contention** — **at least 5 contentions**, each with: each side's argument, cross-examination, an explicit named concession by at least one profile, and a recorded **resolution**. Contend at minimum on: reference price, base-case intrinsic value, right-tail credit, the price that compensates for uncertainty, and management quality. Fewer than 5 contentions means the debate was not actually run.
   - **Final rebuttals and concessions** — one paragraph each.
   - **Debate conclusion** — the unanimous rating and conditions.
3. Write **Part II — The Consensus Synthesis**: the business (what you own); the economics (the one valuation-critical variable, e.g. incremental ROIC vs WACC, with a monitoring hierarchy); management score; consensus valuation matrix (each scenario × each profile's value → consensus value + consensus probability); probability-weighted consensus value with confidence level; reverse-DCF check of what the market price assumes; pros and cons (for/against at the current price); **consensus investment recommendation** (rating A–E, do-not-initiate band, a **price ladder** table of bands → actions, what upgrades the rating, what downgrades it); the five consensus conclusions; and a final consensus judgment paragraph.
4. Rules: introduce **no new valuation math** — synthesize, challenge, and merge what the five profiles concluded. Flag any place the five disagree and why. End with a disclaimer that this is an estimate of estimates, not investment advice.
5. Add a **Technical analysis** section to `consensus-analysis.md` (before the disclaimer) **and** mirror it into `report_inputs.json` under `technical` (schema: `scripts/report_inputs.example.json`). Seven indicators, each with a value and its position: price vs **200-day SMA** (% above/below), vs **100-day SMA** (%), vs **50-day SMA** (%), **14-day RSI**, **14-week RSI**, **50-week RSI**, and price vs the **52-week high/low**. Use the technicals from the shared fact pack (fetched once in Phase 1) — never invent them — and keep the exact same numbers in both files (`verify_run.py` checks them).

Output format must mirror the IREN `consensus-analysis.md` structure (method note → shared fact base → debate rounds → Part II synthesis).

## Phase 4 — Polished HTML report

Produce `{ticker}-consensus-investment-report.html` (lowercased ticker) — a single-file, self-contained HTML report of the consensus.

Requirements:

- **Do not hand-author HTML.** `report_inputs.json` is authored by the consensus subagent at the end of Phase 3 (alongside `consensus-analysis.md`) from the schema `{SKILL_DIR}/scripts/report_inputs.example.json`; text fields support `**bold**` and `` `code` ``, write literal `&`, `<`, `>` — they are auto-escaped. Include a `figures` array of every key figure string (rating, base, weighted, scenario range, ladder bands) for validation.
- **Figures array rule (two-way):** every `figures` entry must be a string that actually renders in the final HTML **and** appears in the report inputs' own content. Unreferenced figure strings (e.g. a rating not used by any section) fail `--validate` — keep the array in exact sync with what the report displays. This catches copy-paste drift before the HTML is built.
- The report renders a **Technical analysis** section from `report_inputs.technical` (a table of the seven indicators) — the same numbers as the consensus file's Technical analysis section.
- Generate with the data-driven builder (embeds the house CSS verbatim, no external deps):

```bash
python3 {SKILL_DIR}/scripts/build_report.py --validate \
  "{folder}/report_inputs.json" "{folder}/{ticker}-consensus-investment-report.html"
```

- The `--validate` flag checks the output: single `<style>` block, no external URLs (`http://`, `https://`, `cdn`), balanced tags, every `figures` string present **and** (two-way) every figure also present in the report inputs' content. Fix any failure before proceeding.
- **Browser check (trimmed):** open via `file://` once to confirm it renders — verify the title, hero, and one section render, then close. Do **not** take screenshots unless a layout bug is suspected; the structural checks above are the primary gate.
- **Final number re-check:** run `{SKILL_DIR}/scripts/verify_run.py {folder}` (Phase 5) to confirm every figure matches `consensus-analysis.md` and the verified workbook. The HTML is a rendering of the consensus — it never introduces new numbers.

## Phase 5 — Verification & delivery

**Run the automated gate first:**

```bash
UV_CACHE_DIR="$PWD/.uv-cache" uv run --no-project --python 3.13 --with openpyxl --with formulas -- \
  python3 {SKILL_DIR}/scripts/verify_run.py "{TICKER}/{YYYY-MM-DD}"
```

It performs every check below and prints a PASS/FAIL checklist; the run must end `ALL_PASS` (exit 0) before reporting done. If `formulas` is unavailable it falls back to independent recompute-only and states so. The manual checklist (documentation of what the gate enforces):

- [ ] `buffet-analysis.md`, `munger-analysis.md`, `damodaran-analysis.md`, `druckenmiller-analysis.md`, `soros-analysis.md` exist, each following its profile's framework with final rating + source links + a `## Position Summary` block, and each passing the depth gate (source floor, coverage floor)
- [ ] `{TICKER}_Damodaran_Financial_Model.xlsx` exists and verifier printed `ALL_MATCH`
- [ ] `consensus-analysis.md` contains the full debate (fact base, openings, agreements, contentions with resolutions, rebuttals, Part II synthesis, rating, price ladder)
- [ ] `consensus-analysis.md` and the HTML each contain the **Technical analysis** section (≥7 indicators: 200/100/50-day SMA, 14-day/14-week/50-week RSI, 52-week high/low) with identical figures in both — enforced by `verify_run.py`
- [ ] `{ticker}-consensus-investment-report.html` renders cleanly and matches the consensus numbers
- [ ] **Numeric consistency:** the five scenario values are identical in the workbook, `damodaran-analysis.md`, `consensus-analysis.md`, and the HTML report
- [ ] Every number in the final deliverables traces to a source or is labeled as an estimate

Then summarize in chat: consensus rating, valuation range, weighted value, price ladder, and paths to each artifact.

## Cross-cutting rules

- **Research is mandatory.** Never analyze from memory. Every figure in an analysis must come from a fetched source (company IR page, EDGAR, press release, market data) and carry a URL. If a figure cannot be found, say so explicitly and use a labeled approximation — never invent a number, quote, or filing.
- **No fabricated sources.** Link references must resolve to real pages actually consulted.
- **Honesty over precision.** Profiles demand probability distributions and ranges; do not manufacture certainty. Ratings can be unanimous C — that is a feature, not a bug.
- **Five lenses stay independent.** Each subagent works from its own profile and its own research; no lens writes or reads another lens's draft. Reconcile only in Phase 3.
- **No subagent side effects.** Subagents write ONLY their designated output file(s): each lens writes its one analysis file (the Damodaran lens additionally returns its `model_inputs` JSON in its summary); the consensus subagent writes `consensus-analysis.md` **and** `report_inputs.json`. They do not write to memory, the skill folder, or any other file; they do not build or verify the workbook.
- **Compact returns.** Subagent summaries are bounded (~150–200 words); the orchestrator reads files directly for detail rather than receiving re-dumps.
- **The workbook is the Damodaran lens's spine.** Its five scenario IV/share values must appear in `damodaran-analysis.md`'s scenario section and feed the consensus valuation matrix.
- **One number, one source.** The same figure must have the same value in every artifact. The verified workbook is authoritative for Damodaran scenario values; the consensus is authoritative for the final rating and price ladder. If artifacts disagree, fix the outlier before delivery.

## Failure & recovery

- **Ticker lookup fails or is ambiguous** → stop and ask the user to disambiguate.
- **Company has no EDGAR filings** (foreign/private) → use the primary-exchange regulator's filings or company disclosures; mark the substitution explicitly; if financials are unavailable, still produce the five lens analyses but state the limitation and skip the workbook only if the Damodaran subagent cannot source defensible inputs (record this decision in the consensus).
- **Verification engine unavailable** → `verify_run.py` falls back to openpyxl data_only checks + the independent recomputation; state which verification was used.
- **A subagent returns without writing its file** → relaunch it once, reusing the shared fact pack and a leaner prompt (compact return only; do not re-fetch already-fetched sources). Keep the retry cheap — a relaunch must not duplicate a full research pass. If it fails again, proceed with the remaining lenses and flag the gap in the consensus.
- **`verify_run.py` reports a FAIL** → return to the failing phase (re-fix JSON, rebuild/re-verify the workbook, or fix the outlier artifact) and re-run the gate before proceeding.
- **Web tools fail entirely** → stop and tell the user; do not fabricate a research-backed analysis offline.

## Minimum compliance

Do not claim the skill ran unless all of these are true: five independent lens analyses exist with sources and `## Position Summary` blocks; the workbook exists and verification printed `ALL_MATCH`; the consensus contains real debate rounds with cross-examination and resolutions; the HTML exists, is generated by `build_report.py`, and passes `verify_run.py` (`ALL_PASS`); and a final rating + price ladder are delivered. If any item is missing, return to the failed phase instead of pretending the workflow happened.

**Validation must be fresh.** Run `verify_run.py` against **this run's** actual artifacts — a newly created folder, its own workbook, its own HTML. Do not replay a prior ticker's verification or reuse a previously-green result; the gate must exercise this run's real files and failure paths. (The NOW run's "verification" was a replay that never exercised the failure paths — treat green-on-replay as unverified.)
