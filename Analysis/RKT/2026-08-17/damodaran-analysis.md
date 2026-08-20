# Aswath Damodaran-Style Valuation — Rocket Companies, Inc. (NYSE: RKT)

**Valuation date:** 2026-08-17 · **Reference price:** $14.50 (2026-08-17 close, −21.75% over 52 weeks) · **Shares:** ~2,830M (2.83B — the 2025 up-C collapse reflects full economic ownership of the operating partnership, NOT dilution) · **Market cap:** ~$41.1B · **Fiscal year end:** Dec 31
**Lens:** Damodaran · **Primary framework:** FCFF DCF (10-year explicit forecast), cross-checked with reverse DCF, five-scenario probability weighting, sensitivity analysis and relative valuation.
**Net-debt convention (disclosed up front — the single most important judgment in this valuation):** I value RKT using an **economic corporate net-debt convention**. GAAP total debt of $33.2B is dominated by _matched_ financing: $16.6B of secured warehouse/repurchase/MSR/advance facilities (collateralized dollar-for-dollar by mortgage loans held for sale, MSRs and servicing advances) plus $5.8B of "loans subject to repurchase right from Ginnie Mae" (a matched Ginnie buyout obligation). Only the **$10.8B of senior notes** (net, weighted-average coupon 5.43% per the Q2-2026 10-Q) plus a $2.3B undrawn revolver constitute _corporate_ debt. Management reports **net corporate leverage of 0.9× EBITDA** and $11.2B of liquidity. I therefore use **net corporate debt ≈ $2.3B** (≈0.9× TTM EBITDA of ~$2.58B, per management) in the model, implemented as `debt_mm = $5,748M` less `cash_mm = $3,448M` (cash $3.1B + short-term investments $0.35B). A pure-GAAP corporate view (senior notes net of corporate cash) would imply ~$7.5B of net corporate debt (~2.9× EBITDA); using that instead would cut intrinsic value by roughly $1.8–2.0/share (~25% of base value) without changing the rating.

---

## Bottom Line First

**Rating: C — Hold / Wait (modestly overvalued; no margin of safety at $14.50).**

**Verdict:** Rocket Companies is the largest mortgage lender _and_ servicer in the US — a genuinely dominant, vertically integrated homeownership platform with ~$2.0T of servicing UPB, a ~$1B-per-quarter servicing cash-flow engine, record market share (purchase 6.2%, refi 14.3%), 70%+ recurring or rate-insensitive revenue, and real integration optionality from the Mr. Cooper and Redfin acquisitions. But at $14.50 the market is paying ~$41B for a company whose _normalized_ earnings power — after treating $430M TTM of stock-based compensation and ~$440M/yr of acquired-intangible amortization as the real costs they are — is only ~$1.6B of economic EBIT (≈16% margin) on a $10.2B revenue run-rate that is _declining_ quarter-over-quarter (Q3 guidance of $2.5–2.7B adjusted revenue is below Q2's $2.76B; 30-yr fixed at ~6.8%). My five-scenario, 10-year FCFF DCF — with a risk-free rate of 4.7%, ERP of 4.4%, an unlevered beta of ~1.0 for a mortgage platform at 0.9× corporate leverage (→ WACC ≈ 9.0%), terminal growth 3.0% and economic ROIC of 30%→25% — produces a **base intrinsic value of ≈$8.24/share** and a **probability-weighted value of ≈$15.07/share**, i.e. **~4% above the current price** (+0.8% annualized over 5 years). A reverse DCF shows the market at $14.50 is implicitly assuming RKT roughly **doubles revenue to ~$20B at ~20% EBIT margins** — an aggressive but not impossible bet on a return of the refinance cycle plus continued share gains. I would not initiate or add at $14.50; value becomes genuinely interesting only **below ~$10**, with real margin of safety below ~$8.

---

## Executive Summary

| Metric                                   | Value                          | Source                                             | Basis / note                                                |
| ---------------------------------------- | ------------------------------ | -------------------------------------------------- | ----------------------------------------------------------- |
| Reference price                          | $14.50                         | [Fact pack][9]                                     | Close 2026-08-17; −21.75% over 52 wks                       |
| Diluted shares                           | ~2,830M                        | [10-Q][2]                                          | 2.84B weighted avg; 2.83B total (2025 recap, not dilution)  |
| Market cap                               | ~$41.1B                        | [Fact pack][9]                                     | $14.50 × 2,830M                                             |
| Enterprise value (mcap + net corp debt)  | ~$43.4B                        | This analysis                                      | mcap + $2.3B economic net corporate debt                    |
| Base intrinsic value / share             | ≈ $8.24                        | Verified workbook (DCF-Base)                       | 10-yr FCFF; WACC 9.0%; tg 3.0%                              |
| Bear / Bull value / share                | ≈ $4.39 / ≈ $19.46             | Verified workbook (DCF-Bear/Bull)                  | Scenario DCF sheets                                         |
| Severe Bear / Extreme Bull value / share | ≈ $2.04 / ≈ $73.62             | Verified workbook (DCF-SevereBear/DCF-ExtremeBull) | Scenario DCF sheets                                         |
| Probability-weighted value / share       | ≈ $15.07                       | Verified workbook (Scenario Summary)               | Σ prob × IV per scenario                                    |
| Implied upside at $14.50                 | ≈ **+4%** (annualized ≈ +0.8%) | Verified workbook                                  | weighted / price − 1; 5-yr horizon                          |
| Normalized revenue run-rate              | ~$10.2B TTM                    | [Fact pack][9], [10-Q][2]                          | Q2'26 adj rev $2.76B annualizes ~$11.0B; Q3 guide lower     |
| Economic EBIT margin (Y1 → terminal)     | 17% → 20%                      | This analysis ([10-Q][2])                          | After SBC + acquired-intangibles amort as real costs        |
| Appropriate WACC                         | ≈ 9.0%                         | This analysis                                      | rf 4.7% + β~1.04 × ERP 4.4%; CoD 5.43% pre-tax              |
| Stable growth (terminal)                 | 3.0%                           | This analysis                                      | Below WACC in every scenario                                |
| Economic ROIC (initial → terminal)       | 30% → 25%                      | This analysis ([Fact pack][9])                     | On tangible capital; GAAP ROIC 2.75% goodwill-distorted     |
| Net corporate debt convention            | ≈ $2.3B                        | [10-Q][2], [Fact pack][9]                          | 0.9× EBITDA; GAAP total debt $33.2B excluded (matched)      |
| Valuation confidence                     | **Low–Medium**                 | This analysis                                      | Cyclical/rate-sensitive lender; net-debt judgment dominates |
| Buy zone / Sell-or-reduce zone           | **< $10 / > $18**              | This analysis                                      |
| Rating at $14.50                         | **C — Hold / Wait**            | This analysis                                      |

---

# 1. What Rocket Companies Actually Is

In plain terms: **Rocket is the giant of the American mortgage — it both makes mortgages and, since the Mr. Cooper deal closed in late 2025, services more of them than anyone else on earth.** It makes money in four connected ways:

1. **Origination (Rocket Mortgage + Rocket Pro + Correspondent)** — it originates and sells mortgage loans into the secondary market and earns a gain-on-sale margin (~311 bps excluding correspondent in Q2'26). ([10-Q][2])
2. **Servicing (Rocket Mortgage + Mr. Cooper)** — it collects a servicing fee (~0.29% of UPB annually) on ~$2.0T of loans it services, a large, stable, contractually-backed cash stream (~$1B cash flow in Q2'26 alone). ([10-Q][2], [Fact pack][9])
3. **Adjacent products** — home equity (Rocket Home Equity, 250k borrowers / $24B accessed), personal loans (Rocket Loans), subscription fintech (Rocket Money, ~5.0M paying subscribers), and title/closing (Rocket Close). ([10-Q][2])
4. **Brokerage/search (Redfin)** — ~50M monthly users, real estate brokerage commission revenue, and a mortgage lead-attach engine (attach rate 0.47 → 0.50 target). ([10-Q][2], [Fact pack][9])

Who pays? Borrowers (through origination fees and servicing fees), the secondary market (GSEs/government = ~83% of loans sold), serviced clients (retention 97%), and subscribers. Why do they pay? Brand, speed (AI-powered digital closing), a 97% client-retention servicing base, and the "recapture engine" — RKT already services the loan, so when rates change it can win the refi (57% of serviced clients who refi choose Rocket). ([Fact pack][9])

**Revenue-to-cash conversion:** origination revenue is high-volume, low-margin, rate-cyclical; servicing revenue is annuity-like and grows with the ~$2T UPB book. Warehouse lines fund loans in transit (matched, self-liquidating). The balance sheet is dominated by _matched_ assets and liabilities — which is exactly why the raw GAAP "net debt" of −$29.7B is a meaningless measure of corporate leverage and why I use the economic net-debt convention disclosed above.

### The Valuation Story

> **"This company will create value because it converts the largest mortgage-servicing franchise in the world — a $2T UPB annuity that throws off ~$1B of cash per quarter — into durable share gains across origination, home equity, personal loans and brokerage, at a scale and cost advantage competitors cannot easily match."**

The three Damodaran inputs:

- **Cash flows:** ~$2.6B TTM EBITDA and ~$1.6B economic EBIT (after SBC + acquired-intangible amortization), with a stable servicing cash floor of ~$1B/quarter. ([10-Q][2], [Fact pack][9])
- **Growth:** the near-term market is _shrinking_ (Q3 guide down QoQ for the first time since 2022; 30-yr ~6.8%; existing-home sales ~4M annualized), but RKT is _gaining share fast_ (purchase share 6.2% vs 5.5% in Q4'25; refi share 14.3% vs 12.2%; D2C purchase volume +45% YoY), and analysts forecast a 3-yr revenue CAGR of ~+21.75%. ([Fact pack][9])
- **Risk:** high for a non-bank lender — rates, prepayment/MSR fair-value swings, GSE/regulatory exposure, integration execution, and a 2.21 five-year beta that reflects the 2021–22 crash far more than the company's 0.9× _corporate_ leverage. ([Fact pack][9])

**Lifecycle classification: Mature (cyclical) with a growth overlay.** Origination is a mature, commodity, rate-driven business; servicing is a stable utility-like annuity; the Redfin/home-equity/Rocket Money layer is the growth option. The appropriate model is a **two-stage FCFF DCF** (10-year explicit forecast converging to stable growth), which is what the shared workbook implements.

---

# 2. Historical Fundamental Analysis

| Year | Revenue ($M) | Note                                                     |
| ---- | ------------ | -------------------------------------------------------- |
| 2021 | 13,176       | Refinance boom (record low rates)                        |
| 2022 | 6,005        | Fed hikes; market halved                                 |
| 2023 | 4,005        | Rate-driven trough                                       |
| 2024 | 5,416        | Recovery in purchase; market low                         |
| 2025 | 7,071        | Redfin (Jul) + Mr. Cooper (Oct) acquisitions consolidate |
| TTM  | 10,243       | Q3'25–Q2'26; +98.8% YoY, acquisition-inflated            |

[Fact pack][9]. **What actually caused the growth:** (i) the 2021 refi boom, (ii) the 2022–23 rate-driven collapse, (iii) the 2025 all-stock acquisitions of Redfin ($1.74B consideration) and Mr. Cooper ($16.97B consideration, ~$11.6B of MSRs and $8.25B of goodwill acquired), and (iv) — in the last two quarters — genuine _share gains_ within a shrinking market ([10-Q][2], [Fact pack][9]). **The +98.8% TTM growth number is an acquisition arithmetic artifact, not an organic growth rate.** I do not extrapolate it.

**Profitability:** TTM operating margin 20.04% (GAAP op income $2,053M) and adjusted EBITDA margin ~25.2% ($2,580M TTM) — but GAAP **net margin is only 4.6%** ($471M TTM net income) because of $430M of SBC, ~$440M/yr of acquired-intangible amortization ($110M/quarter), and net interest. Adjusted net margin is ~16% (Q2'26 adj NI $441M on $2.76B adj revenue). The truth is between: **economic EBIT ≈ $1.6B ≈ 16% of revenue** after treating SBC and acquired-intangible amortization as real costs. ([10-Q][2], [Fact pack][9])

**Capital intensity & reinvestment:** capex is tiny (~$138M TTM; $77M H1'26) — this is a _working-capital/fee_ business, not a capital hog. The capital in the model is not physical plant; it is MSR investment, technology, marketing and Redfin integration. On the _tangible_ capital base (book equity $23.5B less $10.6B goodwill less $20.9B intangibles = **negative ~$8.0B tangible book**), the economic returns on capital are very high — the company's GAAP ROIC of 2.75% is a goodwill/intangibles artifact. ([Fact pack][9])

**ROIC vs cost of capital:** economic ROIC on tangible capital (≈30% my estimate) comfortably exceeds WACC (≈9%). Growth _can_ create value — but only if the growth comes from share gains and cross-sell at thin incremental capital, not from pricey acquisitions paid in stock. That is the judgment this model encodes.

---

# 3. Competitive Advantage & Industry Economics

**Industry structure:** US mortgage origination is ~$2T+/yr of volume in a normal market, fragmented, low-margin, commodity-priced, and brutally rate-cyclical. Servicing is more concentrated, annuity-like, and sticky (servicer ratings and GSE/regulatory approval are barriers). Competitive intensity in origination is severe (banks, independent brokers, fintechs, and now a resurgent refi competitor set if rates fall). Barriers to entry in _servicing at scale_ are high — regulatory minimum-net-worth, master-servicer ratings, and the capital/liquidity to carry a $2T book.

**Competitive advantages (each asked: does it show up in margins, growth, ROIC, or lower risk?):**

- **Scale + cost advantage (Strong):** the largest origination + servicing base means the lowest per-loan servicing cost, and the recapture engine (57% refi share of serviced clients) is a self-reinforcing flywheel no one else has at this scale. It shows up in the 28% adjusted EBITDA margin and record share gains. ([Fact pack][9])
- **Brand (Moderate):** "Rocket" is the best-known consumer mortgage brand; brand-driven D2C volume was up 45% YoY. Real but not a pricing-moat (margins are still commodity-like).
- **Data/network effects (Moderate, growing):** Redfin's ~50M MAU + mortgage leads (2× YoY) + attach rate toward 0.50 is becoming a genuine owned-distribution advantage — 25k exclusive listings. ([Fact pack][9])
- **Switching costs (Moderate):** 97% net client retention in servicing; high frictions in refinancing away.
- **Regulatory/capital advantage (Moderate):** only investment-grade-rated US mortgage company; $11.2B liquidity; 0.9× net corporate leverage lets it fund through cycles that break weaker lenders. ([Fact pack][9])

**Excess returns:** economic ROIC ≈ 30% on tangible capital vs ~9% WACC — a large, durable positive spread, but on a tiny capital base and heavily dependent on _servicing_ economics rather than origination. The moat is **Moderate** (I would not call it strong/exceptional): origination is commodity, servicing is defensible, and the integrated-platform optionality is unproven over a full cycle.

---

# 4. Management & Capital Allocation

**Rating: Good — with a "show me the returns" caveat.**

Observable economic consequences: management has (1) consolidated the market (#1 lender + #1 servicer) and bought Mr. Cooper for $17.0B in stock (equity consideration, not cash) — a strategically coherent acquisition (servicing scale + recapture) that created $8.25B of goodwill and $20.9B total intangibles; (2) paid a one-time $0.80/share special dividend to Class A holders as part of the up-C collapse (2025); (3) run a tight corporate balance sheet (0.9× net corporate leverage, $11.2B liquidity); (4) targeted $400M+ of Cooper cost synergies ($100M realized, $100M extra in H1'27); and (5) guided to a disciplined Q3 (expenses $2.35B vs adjusted revenue $2.5–2.7B). ([10-Q][2], [Fact pack][9])

Concerns: the acquisitions were paid largely in **stock** (economically, RKT bought growth by selling ownership in itself — value creation depends on ROIC on the acquired assets exceeding the dilution cost); buybacks are trivial (−$177M TTM) despite the stock being cheap; and SBC of $430M TTM (vs $471M net income) is economically material — it is real dilution of the equity that shareholders are paying for. The 2025 up-C collapse and special dividend were structured to benefit the controlling shareholder (Dan Gilbert, ~62% voting control via Class L) — a governance consideration, not a value-add. Management quality: **Good**, execution-focused, but the burden of proof is on incremental ROIC.

---

# 5. Accounting & Earnings Normalization

**Earnings quality: Low-to-Medium on GAAP; the non-GAAP "adjusted" numbers are directionally useful but overstate cash earnings.**

Key normalization decisions (each changes what I put in the model):

- **Stock-based compensation ($430M TTM ≈ $471M GAAP net income):** a real expense. I do **not** add it back to derive economic EBIT. Damodaran's rule: SBC is a cost of doing business and (for a company with a meaningful employee-option overhang) a claim on future equity value. ([Fact pack][9])
- **Acquired-intangible amortization (~$110M/quarter, ~$440M/yr):** real, if non-cash. The acquired intangibles ($20.9B gross: customer relationships, trade names, developed tech) will not be replaced at zero cost; treating the amortization as a real charge keeps the 20% terminal EBIT margin honest. ([10-Q][2])
- **Fair-value MSR swings:** the "Change in fair value of MSRs, net" (−$616M in Q2'26) is a real economic _prepayment_ cost (borrowers paying off = your servicing fee stream shortens) but lumpy and rate-driven. Management's adjusted numbers net it out; I start from adjusted EBITDA and then subtract SBC + D&A + intangibles amortization to reach economic EBIT (~$1.6B, ~16% margin). ([10-Q][2])
- **One-time acquisition costs** (Q2'26: ~$99M), **litigation accrual** (~$28M, HouseCanary $175M verdict not yet entered): non-recurring; excluded.
- **Normalized tax rate: 26%** — management's long-term non-GAAP rate is 25.6%; the TTM effective rate is 29.3%. ([10-Q][2], [Fact pack][9])
- **Negative GAAP operating cash flow (TTM −$634M, FY25 −$3.9B):** a mortgage-lender artifact (warehouse/loan-sale swings), _not_ evidence of business-model failure — servicing alone generated ~$1B cash flow in Q2'26. I exclude warehouse financing from the net-debt bridge. ([Fact pack][9])
- **Normalized CapEx:** ~$140M/yr TTM (light); I treat incremental reinvestment through the growth/ROIC relationship rather than a fixed capex line.

**Numbers I do NOT use directly in valuation:** GAAP net income ($471M), raw GAAP total debt ($33.2B), negative TTM FCF (−$772M), GAAP ROIC (2.75%), P/B (1.74× on goodwill-inflated book), and the headline −$29.7B "net cash."

---

# 6. Growth Analysis

**Growth decomposition (TTM $10.2B):** the growth engines are (a) **market share** — purchase share 6.2%, refi share 14.3%, D2C purchase +45% YoY; (b) **servicing scale** — the $2T UPB base grows via origination retention and MSR purchases; (c) **adjacent revenue** — home equity ($24B accessed, 250k borrowers), Rocket Money (5.0M subscribers), Rocket Loans; (d) **Redfin integration** — 2× YoY mortgage leads, attach rate 0.47 → 0.50. Offsetting: the **market** is shrinking QoQ (Q3 guide down; 30-yr ~6.8%; "one of the toughest spring housing markets in years"). ([Fact pack][9])

**Fundamental growth check (reinvestment × ROIC):** with my economic ROIC of ~30% on incremental capital and a target reinvestment of ~30–45% of NOPAT in the first years, the implied sustainable growth is roughly 10–14%/yr early — which matches my Y1 growth of 10%. **Analysts' 3-yr revenue CAGR of +21.75% would require either a major refi wave or sustained ~25%+ ROIC reinvestment at ~60%+ retention — aggressive.** ([Fact pack][9])

**Growth quality: Moderate.** Share gains and servicing annuity growth are high quality; acquisition arithmetic and rate-cycle tailwinds are lower quality. **What causes growth to slow:** rates staying elevated (no refi cycle), share gains saturating near regulatory/practical ceilings, Redfin attach plateauing, and competition. My base case compounds revenue at ~10% Y1 decaying to ~3.5% terminal — well below the analyst forecast.

---

# 7. Risk Analysis

- **Interest-rate/prepayment risk (business):** the dominant risk. Rates at ~6.8% compress origination volume; if rates fall sharply, MSR fair values drop (every −100bps adverse OAS move ≈ −$692M to −$1,333M on the MSR book per the 10-Q sensitivity). ([10-Q][2])
- **Cyclicality:** origination revenue can halve in a year (2021→2022: $13.2B→$6.0B). ([Fact pack][9])
- **Regulatory/structural risk:** GSE/Ginnie Mae selling/servicing requirements, minimum net worth (~$3.5B) and liquidity (~$1.5B) requirements, CFPB/state regulation, and the risk that GSE reform or a government refi program reshapes the market.
- **Financial risk (low at corporate level):** 0.9× net corporate leverage, $11.2B liquidity, only $10.8B senior notes with a 5.43% weighted coupon — interest coverage is adequate; refinancing risk is laddered (first big senior-note maturity 2030+). ([10-Q][2])
- **Integration/execution risk:** Mr. Cooper + Redfin integration (Nationstar merged into Rocket Mortgage in Q1'26) could miss the $400M synergy target or disrupt the servicing engine.
- **Valuation risk:** at $14.50 the market embeds a large growth/margin assumption (reverse DCF: ~2× revenue to ~$20B at ~20% margins); value is sensitive to WACC (±1pt ≈ ±$1/share) and to the fat right-tail refi scenario.
- **Failure risk (low, but real tail):** probability of financial distress is low given liquidity and IG rating; probability of permanent value impairment is meaningful (a prolonged high-rate cycle + MSR compression + competition), which is what the Severe-Bear scenario prices at $2.04.

---

# 8. Cost of Capital & Required Return

**WACC ≈ 9.0%** (this is my judgment, not StockAnalysis's 10.29%, which mechanically feeds a 2.21 five-year beta distorted by the 2021–22 crash):

- **Risk-free rate: 4.7%** — 10-year Treasury, consistent with 30-yr mortgage at ~6.8% and Damodaran's ~4.2% early-2026 T-bond now higher. ([Fact pack][9])
- **Equity risk premium: 4.4%** — Damodaran's implied ERP for the US was **4.23%** at the start of 2026 (fetched from his NYU implied-ERP table, T-bond 4.18%); I round to 4.4% for mid-2026. ([Damodaran][7])
- **Beta:** an _unlevered_ beta of ~1.0 for a mortgage-services platform (mortgage banking has fundamental cyclicality but low operating leverage vs. banks) re-levered at ~0.9× net corporate debt-to-EBITDA and 94.7/5.3 market-value debt/equity weights → **levered β ≈ 1.04**. This is far below the raw 2.21 5-yr beta, which measures the 2021–22 up-C stock collapse, not the operating company. ([Fact pack][9])
- **Cost of equity:** 4.7% + 1.04 × 4.4% ≈ **9.3%**.
- **Cost of debt:** 5.43% pre-tax (weighted-average senior-note coupon per 10-Q; IG-rated) × (1 − 0.26) ≈ **4.0% after-tax**. ([10-Q][2])
- **Weights:** E/V ≈ 94.7% ($41.1B market cap), D/V ≈ 5.3% ($2.3B economic net corporate debt).
- **WACC = 0.947 × 9.3% + 0.053 × 4.0% ≈ 9.0%.**

**ROIC vs WACC:** economic ROIC (~30%) >> WACC (9%) → growth is value-creating at the margin, _provided_ it is organic share-gain growth rather than stock-funded acquisitions. This is the fundamental test I would watch.

---

# 9. Intrinsic Valuation — Primary FCFF DCF

**Base-year normalization:** revenue run-rate $10,243M (TTM); Y1 EBIT margin 17% (economic, after SBC + intangibles amortization); tax 26%; economic ROIC 30%→25%; WACC 9.0%; terminal growth 3.0%; net corporate debt $2.3B.

**Base-case explicit forecast (10 years; $M):**

| Year | Revenue | Growth | EBIT margin | EBIT  | NOPAT | Reinvest. | FCFF  |
| ---- | ------- | ------ | ----------- | ----- | ----- | --------- | ----- |
| Y1   | 11,267  | 10.0%  | 17.0%       | 1,915 | 1,417 | 481       | 936   |
| Y2   | 12,169  | 8.0%   | 17.5%       | 2,130 | 1,576 | 436       | 1,140 |
| Y3   | 12,899  | 6.0%   | 18.0%       | 2,322 | 1,718 | 364       | 1,354 |
| Y4   | 13,415  | 4.0%   | 18.5%       | 2,482 | 1,836 | 264       | 1,572 |
| Y5   | 13,884  | 3.5%   | 19.0%       | 2,638 | 1,952 | 251       | 1,701 |
| Y6   | 14,370  | 3.5%   | 19.5%       | 2,802 | 2,074 | 272       | 1,801 |
| Y7   | 14,873  | 3.5%   | 20.0%       | 2,975 | 2,201 | 295       | 1,906 |
| Y8   | 15,394  | 3.5%   | 20.0%       | 3,079 | 2,278 | 312       | 1,966 |
| Y9   | 15,933  | 3.5%   | 20.0%       | 3,187 | 2,358 | 330       | 2,028 |
| Y10  | 16,490  | 3.5%   | 20.0%       | 3,298 | 2,441 | 342       | 2,099 |

_(Workbook-consistent; figures rounded.)_ **Reinvestment is tied to growth** — reinvestment rate = growth/ROIC (e.g., Y1: 10%/30% ≈ 33% of NOPAT), so forecast FCFF is not independent of growth. **The assumption that matters most is the EBIT margin path and the reinvestment discipline, not the near-term revenue line.**

**Result:** PV of explicit FCFF ≈ $10.0B; PV of terminal value ≈ $15.6B; **EV ≈ $25.6B; less $2.3B net corporate debt → equity ≈ $23.3B → base IV ≈ $8.24/share** (−43% vs $14.50).

---

# 10. Terminal Value

- Terminal FCFF = NOPAT₁₀ × (1+g) × (1 − g/ROIC_terminal) = $2,441M × 1.03 × (1 − 3%/25%) ≈ **$2,212M**.
- TV = $2,212M / (9.0% − 3.0%) = **~$36.9B**; PV of TV ≈ **$15.6B ≈ 61% of EV**.
- Stable-state assumptions are internally consistent: 3.0% growth < nominal GDP; terminal ROIC 25% > WACC 9%; terminal reinvestment rate 12% (= 3%/25%).

**What the terminal value assumes 10–20 years out:** RKT keeps ~20% EBIT margins, grows ~3%/yr (above the industry, which is roughly flat in nominal terms), and earns a 25% return on the incremental capital it deploys — i.e., its share gains and servicing annuity persist for decades. That is defensible but not a small assumption; TV ≈ 61% of EV is a normal share for a mature compounder, and I flag the uncertainty it introduces.

---

# 11. Relative Valuation

The obvious peers are other mortgage/origination platforms and asset-light financials, not mega-cap tech. Using the shared fact pack and its sources:

| Company                                        | Business                | Trailing P/E | Forward P/E | P/B   | EV/EBITDA | EV/Sales |
| ---------------------------------------------- | ----------------------- | ------------ | ----------- | ----- | --------- | -------- |
| RKT                                            | #1 lender + #1 servicer | 81.9×        | 20.2×       | 1.74× | 27.4×     | 6.9×     |
| (typical non-bank mortgage / fintech peer set) |                         | high         | 12–18×      | 1–2×  | 10–15×    | 2–4×     |

[Fact pack][9]. **Why RKT's multiples differ:** its GAAP P/E (81.9×) is meaningless (SBC + intangibles + MSR marks crush GAAP net income to $471M); the _adjusted_ forward P/E (~20× on ~$1.76B annualized adjusted net income) is what the market actually uses; P/B (1.74×) is on a goodwill-inflated book; EV/EBITDA (27×) embeds the acquisition-inflated EBITDA but also the model's low terminal-return base. Fundamentally, RKT's multiple is justified **only if** the growth story (share gains + refi cycle + Redfin attach) converts into durable 20%+ _economic_ EBIT margins. On my normalized ~16% economic EBIT and ~$8.24 base value, the stock trades at a premium to what its current fundamentals support; the multiple is a bet on growth, not a reflection of it.

---

# 12. Reverse DCF — What Does the Market Price Assume?

Starting from $14.50 (mcap $41.1B + $2.3B net corporate debt ≈ $43.4B EV), holding my WACC (9.0%) and terminal growth (3.0%), I solve for the revenue/margin combination that justifies the price:

- At **20% terminal EBIT margin**: the market needs revenue run-rate ≈ **$20B (≈2.0× today's $10.2B)**.
- At **15% terminal EBIT margin**: the market needs revenue run-rate ≈ **$25B (≈2.4× today's $10.2B)**.

(These are my pure-Python recomputes; the workbook's reverse-DCF tab reproduces the same relationship.)

**"At today's price, the market is implicitly assuming Rocket approximately doubles its revenue to ~$20B while holding 20% EBIT margins — i.e., a return of the refinance cycle and/or sustained share gains powerful enough to nearly double a $10.2B base that is currently shrinking quarter-over-quarter."** On my framework (base terminal revenue $16.5B at 20% margins, i.e., ~1.6× current), the market's embedded assumption is **aggressive but not impossible** — it is essentially the Bull scenario (16.5% of the probability mass) plus a piece of the Extreme-Bull refi-wave scenario. It is not what a base case should be.

---

# 13. Scenario Valuation (Five Scenarios)

Scenario parameters are applied as adjustments to the base inputs (revenue growth, EBIT margin, WACC, terminal growth, ROIC); probabilities sum to **1.00**, and **terminal growth < WACC in every scenario**. Values are the **verified workbook** outputs (DCF-SevereBear … DCF-ExtremeBull, Scenario Summary). _Note: the model floors revenue growth at `min_growth` 3.5%, so the bear scenarios express their downside through margin, WACC, terminal growth and ROIC rather than negative revenue growth._

| Scenario         | Prob. | Rev. growth (Y1) | Margin (Y1) | WACC  | Term. growth | Term. ROIC | **IV/share** | vs $14.50 |
| ---------------- | ----- | ---------------- | ----------- | ----- | ------------ | ---------- | ------------ | --------- |
| **Severe Bear**  | 10%   | 3.5% (floor)     | 9.0%        | 12.0% | 1.0%         | 18.0%      | **$2.04**    | −86%      |
| **Bear**         | 20%   | 5.0%             | 14.0%       | 10.5% | 2.0%         | 22.0%      | **$4.39**    | −70%      |
| **Base**         | 45%   | 10.0%            | 17.0%       | 9.0%  | 3.0%         | 25.0%      | **$8.24**    | −43%      |
| **Bull**         | 15%   | 18.0%            | 21.0%       | 8.0%  | 3.5%         | 30.0%      | **$19.46**   | +34%      |
| **Extreme Bull** | 10%   | 30.0%            | 26.0%       | 7.5%  | 4.0%         | 35.0%      | **$73.62**   | +408%     |
| **Weighted**     | 100%  | —                | —           | —     | —            | —          | **≈$15.07**  | **+4%**   |

- **Severe Bear:** prolonged high-rate cycle + housing recession + MSR compression + integration failure; WACC jumps to 12%. Value collapses to ~$2.
- **Bear:** extended high rates, muted volumes, modest share gains, margin pressure — ~70% downside.
- **Base:** my honest view — share gains offset a shrinking market, economic margins 17%→20%, 9% WACC — ~43% below the market price.
- **Bull:** rates ease modestly, share gains accelerate, Redfin/home-equity scale, Cooper synergies exceed $400M — ~+34% upside.
- **Extreme Bull:** a genuine refi wave (2021-like) on a dominant 2-share platform — the fat right tail at +408%.

---

# 14. Sensitivity Analysis

**WACC × Terminal growth (base-case IV/share):**

| g \ WACC | 8.0%  | 8.5%  | 9.0% | 9.5% | 10.0% |
| -------- | ----- | ----- | ---- | ---- | ----- |
| 2.0%     | 9.17  | 8.33  | 7.62 | 7.00 | 6.47  |
| 2.5%     | 9.62  | 8.69  | 7.91 | 7.24 | 6.66  |
| 3.0%     | 10.16 | 9.11  | 8.24 | 7.50 | 6.87  |
| 3.5%     | 10.82 | 9.62  | 8.63 | 7.81 | 7.12  |
| 4.0%     | 11.65 | 10.23 | 9.10 | 8.18 | 7.41  |

**Margin × Revenue (terminal margin × revenue run-rate; base IV/share):**

| Rev \ Marg | 15%   | 18%   | 20%   | 22%   | 25%   |
| ---------- | ----- | ----- | ----- | ----- | ----- |
| $12B       | 7.32  | 8.95  | 10.04 | 11.12 | 12.75 |
| $15B       | 9.36  | 11.39 | 12.75 | 14.10 | 16.14 |
| $18B       | 11.39 | 13.83 | 15.46 | 17.09 | 19.53 |
| $21B       | 13.43 | 16.27 | 18.17 | 20.07 | 22.92 |
| $24B       | 15.46 | 18.71 | 20.88 | 23.05 | 26.31 |

(Full-DCF recomputes; the WACC×g center 8.0%/3.0% cell is the base case $8.24.) **Valuation-critical assumptions (ranked):** (1) **economic EBIT margin** — each ~2pts of terminal margin is worth roughly ~$1.5–2.5/share; (2) **WACC** — each 0.5pt is worth ~$0.5–0.9/share; (3) **terminal revenue/growth** — the revenue × margin table shows value only "rich" (>$14.50) at ~$21B+ revenue or ~22%+ margins; (4) **net-debt convention** — a move from $2.3B to the pure-GAAP $7.5B nets ~$1.8/share of value. I spend my analytical attention on these, not on terminal growth.

---

# 15. Market Expectations vs Fundamental Reality

- **A. Current price:** $14.50 (mcap $41.1B), −21.75% over 52 weeks, trading between $12.17 and $24.36; analysts: 17 covering, average Buy, PT $17.70 (+22%). ([Fact pack][9])
- **B. Market-implied fundamentals:** ~$20B revenue at ~20% margins (≈2× today), or a large refi-cycle bet — roughly my Bull + Extreme-Bull outcomes.
- **C. My fundamental forecast:** ~$16.5B terminal revenue at 20% margins, 9% WACC → $8.24 base / $15.07 probability-weighted.

**Price > Value on the base case (market ~1.8× my base equity value); Price slightly < Value on the probability-weighted case (+4%).** The market is paying for the right-tail scenario. Why might the market be wrong? (i) it is extrapolating Q2'26's "most profitable quarter in four years" and the acquisition-inflated TTM growth into a refi cycle that guidance itself says is not here (Q3 down); (ii) it underweights SBC + intangibles amortization as real costs (using ~$1.8B adjusted net income vs. my ~$1.6B economic EBIT); (iii) it may be underweighting the rate/volume cyclicality that cut revenue by 70% from 2021 to 2023. The market is **not** obviously crazy — the platform quality is real — but the price already embeds the good news.

---

# 16. Real Options & Optionality

Traditional DCF likely **understates** the value of one genuine option: **the refinance cycle**. When the 30-yr rate falls materially (below ~5%), RKT's 57% recapture share of a 2-million-loan servicing book converts an enormous latent demand into origination volume at near-zero marginal acquisition cost — the 2021 model. My Extreme-Bull scenario ($73.62) is a crude, probability-weighted proxy for that option. I do not add separate "optionality value" on top: the right tail is already inside the scenario distribution, and the same rate move that triggers the refi boom also crushes MSR fair values (an offsetting, often mispriced effect). Other real options — Redfin-led national share, home-equity scale, servicing sub-servicing expansion — are moderate and captured in the Bull scenario.

---

# 17. Special Valuation Situations

This is a **financial-services-ish mortgage platform**, which normally would scream "sum-of-the-parts / ROE-based valuation." I use an **FCFF model with an economic net-debt convention and tangible-capital economic ROIC** because (a) the balance sheet is dominated by _matched_ assets/liabilities that net out (warehouse, Ginnie buyout, MSR financing), so a banking-style leverage model would mislead; (b) the value engine is fee income and servicing cash flows, not net interest margin; and (c) the shared model treats reinvestment via growth/ROIC, which fits a low-capital-intensity platform. The main distortions I corrected: goodwill/intangibles (excluded from the ROIC base), SBC and intangibles amortization (treated as real costs in the margin), and the −$29.7B GAAP "net cash" (replaced with the $2.3B economic corporate net-debt convention). A sum-of-the-parts cross-check (servicing annuity + origination at normalized margins + Redfin + home equity) supports a base value in the ~$7–10 range, consistent with the FCFF.

---

# 18. Valuation Error & Uncertainty

- **Estimation uncertainty (high):** the net-debt convention, the economic margin path and the ROIC inputs are all judgment calls with wide credible ranges. My net-debt choice alone spans ~$1.8/share between the $2.3B and $7.5B conventions.
- **Economic uncertainty (high):** the single biggest driver is the interest-rate path and whether/when a refi cycle arrives; also housing recession vs recovery, MSR prepayment behavior, and Redfin/Mr. Cooper integration outcomes.
- **Information uncertainty (medium):** post-acquisition financials are only ~2–3 quarters old; segment reporting was just recast to one reportable segment, limiting trend visibility.
- **Model uncertainty (medium):** a 10-year FCFF with reinvestment = growth/ROIC is a reasonable fit for a platform business but is an approximation for a rate-cyclical mortgage lender whose cash flows are driven by mark-to-market MSR and gain-on-sale dynamics.

**Confidence: Low–Medium.** The _direction_ of the conclusion (base value well below the market; price embeds an aggressive refi/share-gain assumption) is robust across WACC 8–10% and margin 17–22%. The _magnitude_ is not precise. I present the $2.04–$73.62 distribution rather than a false point estimate.

---

# 19. Inversion: What Would Make This Investment Fail?

Working backward from permanent capital loss:

- **Rates stay ~7% for years** → origination volume stays depressed, share gains can't offset, and the market never reprices; book/float tied up; value drifts to the Bear/Severe-Bear range ($2–4).
- **A sharp rate _drop_ mishandled** → a refi wave could crush MSR values (every −100bps OAS adverse move ≈ −$700M to −$1.3B) exactly as it boosts volume — a hedging/execution failure at the worst moment.
- **Integration fails** → Mr. Cooper/Redfin synergies don't materialize, servicing quality slips (97% retention erodes), and the $8.3B of Cooper goodwill plus $20.9B intangibles force impairments.
- **Regulatory shock** → GSE reform, a national refi program, or servicing-capital rules that commoditize the servicing annuity.
- **Dilution/control risk** → the ~62%-controlled capital structure and SBC-rich compensation continue to transfer value to insiders even as operating results disappoint.

The model says these risks, weighted at 30% (Severe Bear + Bear), justify only ~$2–4/share in the downside scenarios — hence the wide distribution and the low median.

---

# 20. Probability-Weighted Investment Case

| Scenario     | Prob. | Value/share | Return at $14.50 | Key assumptions                                                                  |
| ------------ | ----- | ----------- | ---------------- | -------------------------------------------------------------------------------- |
| Severe Bear  | 0.10  | $2.04       | −86%             | Prolonged high rates + housing recession + MSR compression + integration failure |
| Bear         | 0.20  | $4.39       | −70%             | Extended high-rate cycle, muted volumes, margin pressure                         |
| Base         | 0.45  | $8.24       | −43%             | Share gains offset shrinking market; 17→20% margins; 9% WACC                     |
| Bull         | 0.15  | $19.46      | +34%             | Rates ease, share gains accelerate, synergies exceed target                      |
| Extreme Bull | 0.10  | $73.62      | +408%            | Refinance wave (2021-like) on a dominant platform                                |

- **Probability-weighted intrinsic value: ≈$15.07** (verified workbook)
- **Expected one-time return:** ≈ +4% (annualized ≈ +0.8%)
- **Expected annualized return over 3 years:** ≈ +1% — still _below_ the ~9% cost of capital; the expected return does not compensate for the risk.
- **Downside risk (30th percentile):** ≈ −70% to −86% (Bear / Severe Bear). **Upside (25th percentile):** ≈ +34% to +408% (Bull / Extreme Bull).
- **Asymmetry at $14.50: favorable only through the low-probability right tail.** The probability-weighted value ($15.07) sits just above the price, but the _base/median_ outcome (~$8.24) is far below it. The price only "works" if you weight the refi-cycle tail heavily.

---

# 21. Investment Decision

**Current price:** $14.50
**Bear value:** $4.39 · **Severe Bear:** $2.04 · **Base intrinsic value:** $8.24 · **Bull value:** $19.46 · **Extreme Bull:** $73.62
**Probability-weighted value:** $15.07
**Expected upside/downside:** +4% (weighted)
**Expected annualized return:** ≈ +0.8% (5-yr), ≈ +1% (3-yr) — below the ~9% cost of capital
**Margin of safety at $14.50:** price ~1.8× the $8.24 base value; ~4% _below_ the probability-weighted value
**Valuation confidence:** Low–Medium
**Buy zone:** **< $10** (≈20% below probability-weighted value; a genuine margin of safety starts to appear) — first tranche ≤ $10, add < $8.
**Sell/reduce zone:** **> $18** (≈10% above the Bull value; the price would then fully bank the refi-cycle scenario).
**Investment rating:** **C — Hold / Wait**

---

# 22. The Five Most Important Conclusions

1. **The business:** The single most important fact is that Rocket is now _two_ businesses fused: a rate-cyclical, commodity origination engine and a ~$2T-UPB servicing annuity that throws off ~$1B/quarter and feeds a 57% recapture flywheel — plus a growing Redfin/home-equity/consumer-finance layer. Value the annuity as an annuity, the origination as a cyclical, and the cross-sell as an option; never multiply the merged revenue line.
2. **The economics:** The driver of intrinsic value is the **economic EBIT margin after SBC and acquired-intangible amortization** and the **return on incremental capital**. At ~16% economic EBIT and ~30% tangible-capital ROIC vs a ~9% WACC, growth _can_ create value — but only if it is organic share-gain growth. Stock-funded acquisitions and 12% SBC-to-net-income dilution are the value leak.
3. **The market's expectations:** At $14.50 the market is implicitly assuming RKT **doubles revenue to ~$20B at ~20% margins** — i.e., a return of the refi cycle plus sustained share gains. That is an aggressive-but-possible right-tail bet, not a base case, and it is the reason the stock trades at a large premium to my base value.
4. **The valuation:** The most defensible estimate is **≈$8.24 base / ≈$15.07 probability-weighted per share** (verified workbook). The market at $14.50 is ~4% _below_ the weighted value but ~1.8× the base value. The wide $2.04–$73.62 spread is the honest answer, not a modeling failure.
5. **The investment decision:** At $14.50 I would **hold and wait, not buy**. The franchise is excellent but the price has already paid for the good news. Value emerges **below ~$10** and becomes compelling **below ~$8**; above ~$18 the refi-cycle scenario is fully priced and I would reduce.

---

# 23. Damodaran-Style Final Judgment

> **"At a price of $14.50, the market is effectively assuming Rocket Companies can nearly double a $10.2B revenue base that is currently shrinking quarter-over-quarter, hold ~20% EBIT margins after real costs like stock-based compensation and acquired-intangible amortization, and earn a 25% return on incremental capital — in other words, a return of the refinance cycle plus sustained share gains. My valuation implies ≈$8.24/share in the base case and ≈$15.07 on a probability-weighted basis because I expect only a ~10%-then-declining organic growth path, economic margins of 17%→20%, and a 9% cost of capital, and because I refuse to treat a $2T servicing annuity plus a cyclical origination engine as a 20%-margin compounder without proof. The biggest risks are a prolonged high-rate cycle, MSR/prepayment shocks in a rapid rate decline, integration execution, and regulation. Therefore, at today's price, I would hold and wait rather than buy; I become interested below ~$10 and substantially more interested below ~$8, where the margin of safety begins to compensate for the uncertainty."**

### The single most important thing to remember

**Do not watch Rocket's stock price. Watch its incremental ROIC and its economic EBIT margin.** If RKT can demonstrate that its share-gain and cross-sell growth is being earned at 25%+ economic ROIC while the economic EBIT margin holds ~20% through a full rate cycle, my valuation rises toward the Bull case. If revenue grows but economic EBIT margins sag toward ~14% and incremental ROIC drifts toward the cost of capital, the correct Damodaran conclusion is that the growth is destroying value — even if the stock is going up. That is the fundamental test.

---

## Sources

1. [SEC EDGAR — Rocket Companies submissions API (CIK 0001805284)](https://data.sec.gov/submissions/CIK0001805284.json) — filing index; confirmed FY2025 10-K (2026-03-02) and Q1/Q2 2026 10-Qs; CIK, SIC 6162 (Mortgage Bankers), fiscal year end.
2. [SEC EDGAR — Q2 2026 Form 10-Q (rkt-20260630.htm)](https://www.sec.gov/Archives/edgar/data/1805284/000162828026054577/rkt-20260630.htm) — primary source for the corporate debt breakdown (senior notes net $10,772M at 5.43% weighted avg; secured financing $16,639M; revolver $2,300M committed/$0 drawn; Ginnie repurchase $5,768M), balance sheet (cash $3,103M), Q2 income statement, adjusted-EBITDA/NI reconciliations, long-term non-GAAP tax rate 25.6%, EPS (2.84B weighted-avg shares), MSR/OAS sensitivities, liquidity $11.2B, segments, Mr. Cooper/Redfin purchase accounting (goodwill $8.25B/$1.23B), special dividend $0.80.
3. [SEC EDGAR — FY2025 Form 10-K index (0001628280-26-013283)](https://www.sec.gov/Archives/edgar/data/1805284/000162828026013283/index.json) — confirmed primary document `rkt-20251231.htm` and FY2025 filing.
4. [SEC EDGAR — FY2025 Form 10-K primary document (rkt-20251231.htm)](https://www.sec.gov/Archives/edgar/data/1805284/000162828026013283/rkt-20251231.htm) — annual report referenced for FY2025 context and accounting policies (confirmed via filing index; figures cited from the shared fact pack).
5. [SEC EDGAR — browse 10-K filings for CIK 0001805284](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001805284&type=10-K) — FY2025 10-K filing date/accession (2026-03-02).
6. [SEC EDGAR — browse 10-Q filings for CIK 0001805284](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001805284&type=10-Q) — historical 10-Q filing cadence.
7. [Aswath Damodaran — Historical Implied Equity Risk Premiums (NYU Stern)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histimpl.html) — US implied ERP **4.23% (2025)**, 10-yr T-bond 4.18% — basis for the 4.4% ERP used in the WACC.
8. [Aswath Damodaran — Country Default Spreads and Risk Premiums (NYU Stern)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html) — US ERP ~4.3–4.5% (Jan 2026 update); rate-limit prevented re-confirmation on the run date (flagged as a gap; 4.23% implied ERP from source 7 used instead).
9. [Shared fact pack — `Analysis/RKT/2026-08-17/fact-pack.json`](https://stockanalysis.com/stocks/rkt/) — market data (price $14.50, shares 2.83B, market cap $41.06B, beta 2.21, 52-wk range), TTM financials (rev $10,243M, op income $2,053M/20.0%, EBITDA $2,580M/25.2%, NI $471M/4.6%, SBC $430M), balance sheet (cash+ST inv $3,448M, total debt $33,179M, goodwill $10,611M, intangibles $20,900M, TBVPS −$2.81), Q2'26 metrics (adj rev $2,761M, adj NI $441M, adj EPS $0.16, adj EBITDA $766M/28%, GoS 311bps, purchase share 6.2%, refi 14.3%, $2T servicing UPB, $11.2B liquidity, 0.9x net corporate leverage, Q3 guide $2.5–2.7B), analyst data (17 Buy, PT $17.70, 3-yr rev CAGR +21.75%), and its bundled sources (StockAnalysis pages, PR Newswire Q2 release, Q2 earnings-call transcript, Macrotrends share count).

---

## Position Summary

- Rating: C — Hold / Wait (excellent mortgage platform; no margin of safety at $14.50 — price ~1.8× base value; buy below ~$10)
- Intrinsic value: bear=$4.39 base=$8.24 bull=$19.46 | weighted=$15.07 (Severe-Bear tail $2.04; Extreme-Bull tail $73.62) — verified workbook values
- Buy zone: <$10 (add <$8) | Sell/reduce zone: >$18
- Key metrics: economic EBIT margin ~16% TTM (after SBC $430M + acquired-intangibles amort ~$440M; GAAP op margin 20.0%, adj-EBITDA margin ~25-28%, GAAP net margin 4.6%) · economic ROIC ~30% on tangible capital (GAAP ROIC 2.75% goodwill-distorted; tangible book −$8.0B) · WACC ~9.0% (rf 4.7%, ERP 4.4%, levered β~1.04; StockAnalysis 10.29% rejected) · net corporate debt ~$2.3B (0.9× EBITDA; GAAP total debt $33.2B excluded as matched) · senior notes $10.8B net at 5.43% (10-Q) · TTM EBITDA $2.58B, TTM NI $471M
- Top risks: prolonged high-rate cycle (30-yr ~6.8%) compressing volumes · MSR/prepayment shocks (−$700M to −$1.3B per 100bps adverse OAS) · Mr. Cooper/Redfin integration below the $400M synergy target · regulatory/GSE reform on the servicing annuity · control-structure dilution / SBC (12% SBC-to-net-income ratio)
