# investment-analysis

Multi-lens investment analysis of individual companies. This repo hosts the **`analyze-company` agent skill** (the engine that runs the analyses) plus the **dated analysis output** it produces, organized under `Analysis/`.

---

## The skill in this folder

The skill lives at **`.github/skills/analyze-company/`** and is invoked with:

```
/analyze-company <name-or-ticker>
```

or by simply asking to "analyze a company / a stock / a ticker". It analyzes **one company per run**, resolves the ticker (with a web-search identity check), and produces a full report set in a dated output folder.

### Skill layout

```
.github/skills/analyze-company/
├── SKILL.md                       # The workflow: 5 phases, output contract, gates, rules
├── profiles/                      # Persona templates, read verbatim by each lens subagent
│   ├── buffet.md                  #   Warren Buffett  — value investing & owner earnings
│   ├── munger.md                  #   Charlie Munger — multidisciplinary quality
│   ├── damodaran.md               #   Aswath Damodaran — fundamental valuation (DCF)
│   ├── druckenmiller.md           #   Stanley Druckenmiller — macro / timing
│   └── soros.md                   #   George Soros — reflexivity / market psychology
├── scripts/
│   ├── build_model.py             # Builds the 5-scenario DCF workbook from model_inputs JSON
│   ├── verify_model.py            # Recomputes every formula (formulas engine) + independent
│   │                              #   Python DCF re-derivation; must print ALL_MATCH
│   └── model_inputs.example.json  # Shape reference for the Damodaran model inputs
└── reference/
    ├── IREN/                      # The gold-standard example run (mirror this quality)
    ├── example-report.html        # The report design system, reused verbatim (navy/gold)
    ├── html-design.md             # Design-system notes for the HTML report
    └── rubric.md                  # Quality rubric used to score the run
```

---

## The approach to analysis

Each run moves through five phases; every phase has an explicit gate that must pass before the next begins.

**Phase 0 — Parse the invocation.** Resolve the ticker (uppercase; name → ticker via web search), confirm the company identity, and create the output folder. Never overwrite an existing dated folder for the same ticker.

**Phase 1 — Research + parallel persona analyses.** Three to five lens subagents run **in parallel and independently** (no lens reads or writes another's draft). Each reads its profile verbatim, researches with web tools (company IR page, SEC EDGAR, market data, competitors), and writes its own analysis file. All analyses open **bottom-line-first**: the rating + one-paragraph verdict, then an executive-summary table. A **depth gate** is enforced: source floor (≥12 distinct fetched sources for large caps, ≥8 for small caps), full coverage of every profile section, and a research budget of at most 5 extra search rounds. The Damodaran lens additionally returns a `model_inputs` JSON block so Phase 2 can build the workbook.

**Phase 2 — Damodaran financial model workbook.** `model_inputs.json` is saved, then `scripts/build_model.py` builds a `.xlsx` from scratch: README, Inputs, Scenarios, five complete 10-year FCFF DCF sheets (`DCF-SevereBear` → `DCF-ExtremeBull`), a circularity-free **Scenario Summary** (probability-weighted value, expected upside, annualized return), Reverse DCF, two sensitivity grids, and a Checks sheet. `scripts/verify_model.py` then recomputes every formula with the `formulas` engine plus an independent Python re-derivation — the **gate** is that it prints `ALL_MATCH`. The workbook is the **source of truth** for Damodaran's numbers, and the narrative is re-synced to it if they drift.

**Phase 3 — Deliberative debate & consensus.** A single subagent writes `consensus-analysis.md` — a structured debate, not a merge: shared fact base → opening statements → points of agreement → **at least 5 contentions** (each with arguments, cross-examination, an explicit named concession, and a resolution) → final rebuttals → debate conclusion, then **Part II — The Consensus Synthesis** (business, economics, management score, consensus valuation matrix, probability-weighted value, reverse-DCF check, pros/cons, a **rating A–E**, a **price ladder** of bands → actions, upgrade/downgrade triggers, five conclusions). No new valuation math is introduced; the debate only synthesizes the lenses.

**Phase 4 — Polished HTML report.** A single-file, self-contained report (`{ticker}-consensus-investment-report.html`) reusing the navy/gold design system from `reference/example-report.html`. No external CSS/fonts/JS. Every number must match the consensus and the verified workbook exactly, and it is re-checked after writing.

**Phase 5 — Verification & delivery.** A completion checklist confirms all artifacts exist, the verifier printed `ALL_MATCH`, and the five scenario values are **identical** across the workbook, `damodaran-analysis.md`, `consensus-analysis.md`, and the HTML report ("one number, one source").

### Cross-cutting rules

- **Research is mandatory** — never analyze from memory; every figure carries a URL or an explicit "estimate" label.
- **No fabricated sources** — links must resolve to pages actually consulted.
- **Honesty over precision** — ranges and probability distributions beat false certainty; a unanimous C is a feature, not a bug.
- **Lenses stay independent** until the Phase 3 debate.
- **The workbook is the Damodaran lens's spine**; the consensus is authoritative for the final rating and price ladder.

---

## Output location

All deliverables are written under **`Analysis/`**, one dated folder per ticker:

```text
Analysis/{TICKER}/{YYYY-MM-DD}/
├── buffet-analysis.md                  # Warren Buffett lens
├── munger-analysis.md                  # Charlie Munger lens
├── damodaran-analysis.md               # Aswath Damodaran lens (scenario DCF)
├── druckenmiller-analysis.md           # Stanley Druckenmiller lens (macro/timing)
├── soros-analysis.md                   # George Soros lens (reflexivity)
├── {TICKER}_model_inputs.json          # Damodaran model inputs (saved from Phase 1)
├── {TICKER}_Damodaran_Financial_Model.xlsx  # 5-scenario FCFF DCF workbook (ALL_MATCH)
├── consensus-analysis.md               # Deliberative debate + consensus synthesis
└── {ticker}-consensus-investment-report.html # Polished single-file report
```

Existing runs (all dated 2026-08-16):

| Ticker | Company                                                     | Consensus                |
| ------ | ----------------------------------------------------------- | ------------------------ |
| `CIFR` | Cipher Digital (data-center dev/landlord; ex-Cipher Mining) | C — HOLD/WATCH @ ~$17.86 |
| `IREN` | IREN (AI infrastructure, ex-Bitcoin miner)                  | C — HOLD/WATCH @ ~$40–45 |
| `NFLX` | Netflix                                                     | C — HOLD/WATCH @ ~$78    |
| `NOW`  | ServiceNow                                                  | C — HOLD/WATCH @ ~$124   |

> **Note on the IREN run:** it was the first full execution and its workbook/narrative drifted slightly (weighted value $118 vs narrative $57). The skill now enforces "the workbook is the source of truth" and re-syncs the narrative — later runs (NFLX, NOW, CIFR) all verified `ALL_MATCH` with no drift.

---

## Running a build locally

The workbook scripts are JSON-driven and run via `uv` (no project install needed). From the repo root:

```bash
# Build the workbook
UV_CACHE_DIR="$PWD/.uv-cache" uv run --no-project --python 3.13 --with openpyxl -- \
  python3 .github/skills/analyze-company/scripts/build_model.py \
  "Analysis/{TICKER}/{YYYY-MM-DD}/{TICKER}_model_inputs.json" \
  "Analysis/{TICKER}/{YYYY-MM-DD}/{TICKER}_Damodaran_Financial_Model.xlsx"

# Verify it (formulas engine + independent re-derivation) — must print ALL_MATCH
UV_CACHE_DIR="$PWD/.uv-cache" uv run --no-project --python 3.13 --with openpyxl --with formulas -- \
  python3 .github/skills/analyze-company/scripts/verify_model.py \
  "Analysis/{TICKER}/{YYYY-MM-DD}/{TICKER}_model_inputs.json" \
  "Analysis/{TICKER}/{YYYY-MM-DD}/{TICKER}_Damodaran_Financial_Model.xlsx"
```

(Environment note: this Mac has no LibreOffice, so the `formulas` package is the verification path; `uv` needs `--no-project` plus a workspace-local `UV_CACHE_DIR`.)

---

## Disclaimer

These analyses are research artifacts — "estimates of estimates" produced by a deliberative multi-lens process. They are **not investment advice**. Every deliverable ends with this caveat; treat any valuation or rating accordingly.
