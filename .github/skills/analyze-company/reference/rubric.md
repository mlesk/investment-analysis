# analyze-company skill — optimization rubric

Created by the loopify process on 2026-08-16. Saved here so the loop can resume
later with the same standard.

Threshold: **85/100**. Accept margin: **+2**. Stop rule: threshold, plateau
(after best-of-N escape), or 6 rounds.

Final state: **88.7/100 — stopped at threshold** after 3 improvement rounds
from a 73.1 baseline.

## Dimensions

### 1. Outcome fidelity (weight: 10)

- 2/10: Skill yields fewer than 5 of the 6 artifacts, or outputs are shallow summaries rather than analyses
- 10/10: All six artifacts (3 lens analyses, xlsx model, consensus md, HTML report) with IREN-comparable depth: rating systems, scenario tables, probability-weighted values, price ladders, cited sources

### 2. Trigger & invocation contract (weight: 7)

- 2/10: No frontmatter description, or the argument is never parsed
- 10/10: Description fires on `/analyze-company <ticker>`-style asks; explicit name-or-ticker resolution, ticker uppercasing, and unknown/missing/multiple-input handling

### 3. Execution fidelity / orchestration precision (weight: 9)

- 2/10: Vague "do the analyses" prose with no phases
- 10/10: Numbered phases with per-phase inputs, outputs, exit criteria; parallel 3-subagent launch specified exactly; dependency gates explicit (spreadsheet ← Damodaran scenario block; debate ← all three analyses)

### 4. Shortcut resistance (weight: 8)

- 2/10: An agent could claim completion after writing one summary file
- 10/10: Per-phase done criteria requiring concrete artifacts: formulas-engine verification must pass, debate must contain structured rounds with cross-examination, analyses must carry source links, HTML must be a real self-contained file

### 5. Persona fidelity (weight: 7)

- 2/10: Profiles ignored; generic "analysis" produced
- 10/10: Bundled profiles loaded verbatim; outputs structurally follow each framework (Buffett owner-earnings/moat, Munger mental models/inversion, Damodaran FCFF/scenarios) with the A–D rating scale

### 6. Tooling & self-containment (weight: 7)

- 2/10: No scripts; the agent must improvise the workbook and HTML from nothing
- 10/10: Bundled parameterized workbook builder + verifier (JSON-driven, company-agnostic), uv/openpyxl/formulas commands with sandbox notes, HTML design-system guidance; scripts run as-is for a new company

### 7. Recovery & robustness (weight: 6)

- 2/10: No fallback guidance
- 10/10: Explicit fallbacks: ticker lookup failure, sparse data/foreign companies, EDGAR inaccessible, verification engine unavailable, and when to stop researching

## Score trajectory

```
Baseline -> R1  -> R2   -> R3   (final)
73.1     -> 80.2 -> 84.8 -> 88.7
```

## Round log

- **Round 1 (73.1 → 80.2):** numeric-consistency law (workbook is source of truth; re-sync rule), depth gate (source floor ≥12/8, coverage floor, 3-round research budget), no-argument invocation handling.
- **Round 2 (80.2 → 84.8):** warning that example JSON values are IREN's and must be replaced; remediation paths for failing Checks cells and builder tracebacks; mandatory final number re-check of the HTML.
- **Round 3 (84.8 → 88.7):** multi-company invocation handling; ≥5 debate contentions with named concessions; bottom-line-first + executive summary table in all three analyses; browser-unavailable structural verification fallback.

## Remaining gap (below 100)

- The three lens analyses rely on the bundled profiles + IREN example for their full section structure rather than an explicit per-section checklist.
- The skill has been tooling-verified end-to-end (builder/verifier reproduce the IREN workbook exactly) but not yet executed against a new company's web research phases.
