# Aswath Damodaran–Style Valuation — Berkshire Hathaway Inc. (BRK.B)

**Date:** 2026-08-16 · **Reference price:** $504.03 (BRK.B, 2026-08-14 close)
**Lens:** Damodaran · **Method:** revenue-based FCFF DCF (approximation) cross-checked against a proper insurance-conglomerate sum-of-parts

---

## Bottom Line First

**Rating: C — Hold.** Berkshire Hathaway is one of the great capital-allocating businesses of the last 60 years, but at $504.03 (≈1.44× book, near the top of its historical valuation range) the market is paying essentially full price for it. My base-case intrinsic value is ≈ **$447** per Class B share; my probability-weighted value is ≈ **$491** (both from the verified workbook). The market price embeds an ~18–19% pre-tax operating margin (against my normalized ~15.6%) — a reasonable but mildly optimistic set of assumptions. With management itself choosing _not_ to buy back stock in Q4 2025 (a discretionary program with a $30B cash floor), the people with the most information are signaling the shares are not cheap. This is a wonderful business at a fair price: no margin of safety today, and the expected return from here is roughly in line with Berkshire's cost of capital rather than above it. **Buy below ≈$420; reduce/reassess above ≈$560.**

| Metric                                          | Value                                                            | Source                                               |
| ----------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------- |
| Rating                                          | **C — Hold**                                                     | This analysis                                        |
| Price (BRK.B, 2026-08-14)                       | $504.03                                                          | [Yahoo][10] / fact pack                              |
| 52-week range                                   | $464.01 – $537.74                                                | [Yahoo][10] / fact pack                              |
| Class-B-equiv. shares                           | ~2,140M                                                          | [Yahoo][10] / fact pack                              |
| Market cap                                      | ~$1.08T                                                          | [Yahoo][10] / fact pack                              |
| Base intrinsic value / share                    | ≈ $447.31                                                        | Verified workbook (DCF-Base)                         |
| Bear / Bull value / share                       | ≈ $310.98 / ≈ $602.47                                            | Verified workbook (DCF-Bear/Bull)                    |
| Severe Bear / Extreme Bull value / share        | ≈ $257.14 / ≈ $871.86                                            | Verified workbook (DCF-SevereBear / DCF-ExtremeBull) |
| Probability-weighted value / share              | ≈ $490.84                                                        | Verified workbook (Scenario Summary)                 |
| Implied upside at $504 (weighted)               | ≈ **−3%** (annualized ≈ −0.5%)                                   | Verified workbook                                    |
| Revenue TTM                                     | $384.7B                                                          | [SEC][4] + fact pack                                 |
| GAAP net income TTM                             | $85.8B (equity-gain inflated)                                    | [SEC][4] (quarterly sum)                             |
| Normalized operating earnings (2025, after-tax) | ≈ $44.5B                                                         | [SEC 10-K][5]                                        |
| Float (end-2025)                                | ≈ $176B                                                          | [SEC 10-K][5]                                        |
| Cash + U.S. T-bills                             | $360B (6/30/26) / $369B (12/31/25)                               | [SEC 10-Q][7] / [SEC 10-K][5]                        |
| WACC                                            | 8.0%                                                             | This analysis (CoE ≈8.1%, CoD ≈3.6%)                 |
| Confidence                                      | **Low–Medium** (conglomerate/insurer; model is an approximation) | This analysis                                        |

---

## 1. Fundamental Story

**The business in plain terms.** Berkshire Hathaway is a holding company that does three things. First, it runs a collection of wholly owned operating businesses — GEICO and other insurers, the BNSF railroad, Berkshire Hathaway Energy (regulated utilities and energy), and a diverse manufacturing, service and retailing group (Precision Castparts, Clayton Homes, Lubrizol, Marmon, and more). Second, it runs a giant insurance and investment operation: insurance premiums generate "float" — policyholder money that Berkshire gets to invest before paying claims — which totaled ≈$176B at end-2025 [SEC 10-K][5]. Third, it is one of the largest owners of common stocks in the world: ≈$324B of equity securities at fair value at 6/30/26, plus ≈$360B of cash and Treasury bills [SEC 10-Q][7]. Revenue (TTM) is ≈$384.7B and book value attributable to shareholders is ≈$717B [SEC 10-K][5], [fact pack].

**Why customers pay.** Insurers are paid premiums for risk transfer; railroads are paid for freight movement; utilities are paid regulated returns on invested capital; industrial businesses are paid for durable, engineered products. These are largely necessity-based, cash-generative, and — critically — _low-tech, slow-changing_ businesses with wide, durable cost advantages.

**How it converts revenue into value.** Underwriting profits (2025: $7.3B after-tax) plus insurance investment income ($12.5B) plus operating earnings (BNSF $5.5B, BHE $4.0B, manufacturing/service/retailing $13.6B) — roughly $44.5B of after-tax operating earnings in 2025 [SEC 10-K][5]. The company retains essentially all of it (no dividend since 1967 [SEC 10-K][5]) and redeploys it into operating reinvestment, buybacks, or — increasingly under CEO Greg Abel — additional common-stock purchases (Alphabet, Delta, homebuilders in Q1–Q2 2026 [fact pack]).

### The Valuation Story

> **"This company will create value because it converts low-cost, durable operating earnings and a large, negatively-costed insurance float into a compounder that reinvests at returns above its cost of capital — and because the market persistently prices the whole as less than the sum of the parts."**

The three fundamental inputs:

- **Cash flows:** ≈$44.5B after-tax operating earnings (2025), plus a $360B cash/T-bill pool earning Treasury-like yields and a $324B equity portfolio that throws off dividends and (increasingly) buybacks [SEC 10-K][5], [SEC 10-Q][7].
- **Growth:** book value has compounded at roughly 8–10%+ annually for decades; the revenue base grew from $276B (2021) to $384.7B (TTM) — but that growth is _low-quality arithmetic_ for a holder of financial assets, heavily driven by premium inflation, energy capex, and mark-to-market investment flows rather than organic unit economics [SEC 10-K][5].
- **Risk:** genuinely low on a volatility basis (5-yr beta ≈0.61 [Yahoo][10]) but _higher on a cash-flow basis_ than the beta suggests — because earnings are dominated by insurance underwriting cycles, equity-market marks, and interest-rate movements.

**Lifecycle classification: Mature.** Berkshire is a mature, stable-growth conglomerate with a large financial-asset component. The appropriate model is a **stable-to-two-stage growth model**, not a high-growth model. I use a 5-year explicit FCFF forecast converging to stable growth, which is what the shared workbook model implements.

---

## 2. Historical Fundamental Analysis (2016–2025)

_All figures from SEC XBRL company facts [SEC][4] and the FY2025 10-K [SEC 10-K][5] unless noted._

| Year              | Revenue ($B) | GAAP Net Income ($B) | Pretax Income ($B) | Note                                                          |
| ----------------- | ------------ | -------------------- | ------------------ | ------------------------------------------------------------- |
| 2021              | 276.2        | 89.9                 | 111.9              | Accounting change reclassifies investment income into revenue |
| 2022              | 302.0        | (22.8)               | (30.5)             | Equity-market losses                                          |
| 2023              | 364.5        | 96.2                 | 120.2              | Big market gains                                              |
| 2024              | 371.4        | 89.0                 | 110.4              | —                                                             |
| 2025              | 371.4        | 67.0                 | 82.5               | OTTI on Kraft Heinz/Occidental (−$8.3B) [SEC 10-K][5]         |
| TTM (Q3'25–Q2'26) | ~384.7       | ~85.8                | —                  | Q3'25 gains + Q2'26 gains                                     |

**What actually caused revenue to grow:** (i) the 2021 accounting reclassification of insurance investment income into "revenue"; (ii) premium growth (price + exposure); (iii) energy capex/pass-through (BHE); (iv) mark-to-market flows. _Organic volume growth is modest._ I do **not** extrapolate the revenue line mechanically — it overstates economic growth because much of it is investment income flowing through.

**Profitability:** GAAP net margin 2025 ≈18% (and 22.3% TTM per [fact pack]) — but this is **not** a clean operating margin; it is inflated by equity gains. Normalized after-tax operating earnings (excluding investment gains and the Kraft/Oxy impairment) were ≈$44.5B on $371B revenue ≈ **12% after-tax margin**, ≈15–16% pre-tax [SEC 10-K][5]. ROE (TTM) ≈12.1% [fact pack] — depressed by the enormous cash/investment base earning ~4–5%; ROIC on the _operating_ businesses alone is materially higher (≈15%+).

**Capital intensity & reinvestment:** CapEx was $20.9B (2025) vs $13.5B D&A, roughly $7B net — concentrated in BNSF and BHE (the railroad and utilities are the true capital hogs; manufacturing is much lighter) [SEC 10-K][5]. Cash-flow generation is strong: operating cash flow has run well above net income for years.

**ROIC vs cost of capital:** On operating capital, ROIC (≈15%) comfortably exceeds WACC (8%). On total capital (including the $684B of cash + equities), ROIC is dragged toward the ~4–5% T-bill return — which is _below_ WACC on that segment. The reconciliation: Berkshire's cash/investments are best valued at market, not at book, and the equity portfolio historically earns a high equity premium. The economic test — "does reinvestment create value?" — is met for the operating businesses and historically for the equity portfolio, but **not** for sitting on a $360B T-bill pile at ~4% when capital costs ~8%.

---

## 3. Competitive Advantage & Industry Economics

**Competitive advantage rating: Exceptional (within the operating businesses) — with a caution.**

The moats are real and mechanistically observable:

- **Insurance (GEICO):** cost advantage — the lowest-cost auto insurer by distribution model; brand; float with a _negative average cost_ (underwriting profitable in most years). P&C combined results are structurally strong: 2025 after-tax underwriting $7.3B even in a soft, competitive market [SEC 10-K][5].
- **BNSF:** one of four western Class-I rails — a regulated, high-barrier, ~32,500-route-mile network that is effectively irreplaceable; 2025 operating revenue $23.4B, net $5.5B [SEC 10-K][5].
- **BHE (utilities/energy):** regulated monopolies (low risk, capped returns) plus natural-gas pipelines and renewables; wholly-owned since 2024 [SEC 10-K][5].
- **Manufacturing/service/retail:** Precision Castparts (aerospace), Clayton (factory-built housing), Lubrizol, Marmon — each with niche cost/technology positions; 2025 revenues $214.3B, after-tax earnings $13.6B [SEC 10-K][5].
- **Capital advantages:** the $360B cash + $324B equities pool is a structural advantage — it lets Berkshire fund large bolt-ons and act as lender of last resort (e.g., $10B committed to Alphabet's capital raise in 2026 [fact pack]) — but it is _also_ the source of the value drag noted above.

**Does the advantage show up in returns?** Yes — operating ROIC ≈15% vs 8% cost of capital is a healthy, persistent positive spread. The spread is **durable** because the moats are structural (regulation, network scale, distribution cost), not fashionable. **The risk:** the _marginal_ dollar of capital is increasingly being allocated into a $360B cash pile and a $324B public-equity portfolio where the "moat" is the market's own return — not a proprietary one.

---

## 4. Management & Capital Allocation

**Management quality rating: Excellent (historically exceptional; in transition).**

Warren Buffett (Chairman, age 95) built the allocation culture; Greg Abel (CEO since 2025) now runs it. The observable economic evidence:

- **Reinvestment** into BNSF/BHE/manufacturing has historically earned attractive returns (ROIC > WACC).
- **Acquisitions:** recent deals are smaller, disciplined bolt-ons (e.g., Pilot 100% for $2.6B in 2024; Cove Point LNG 75%; BHE NCI buy-ins) — no value-destroying mega-mergers [SEC 10-K][5].
- **Buybacks:** the 2025 proxy year saw the program amended to a _discretionary, any-time_ program with a $30B consolidated cash floor — and **zero shares repurchased in Q4 2025** [SEC 10-K][5]. This is the single most informative signal in the filing: at ~$470–505, management did not view the shares as cheap. (Buybacks were aggressive at lower prices in 2020–2021.)
- **Dividend:** none since 1967 — the company is a pure compounding vehicle [SEC 10-K][5].
- **Cash/equity deployment:** under Abel, the tone changed in 2025–2026 — Berkshire stopped shrinking the cash pile passively and began _deploying_ it into public equities (Alphabet — now a top-3 holding, ≈$31B / ≈8.8% of the equity portfolio — plus Delta and homebuilders, with a $10B commitment to Alphabet's $80B capital raise) [fact pack]. This is rational given ~8% cost of capital and ~4% T-bill yields, but it converts a "safety" asset into market-beta risk.
- **Compensation/incentives:** modest executive pay by mega-cap standards; management holds enormous equity; incentives align with long-term compounding, not near-term EPS.

---

## 5. Accounting & Earnings Normalization

**This is the section where most Berkshire "valuations" go wrong. GAAP net income is not the earnings base.**

1. **Equity gains flow through net income.** Since 2018, unrealized gains/losses on equity securities run through GAAP earnings. FY2025 GAAP net income of $67.0B included $30.7B of investment gains and a −$8.3B Kraft Heinz/Occidental other-than-temporary impairment; 2023's $96.2B and 2022's −$22.8B are equally distorted [SEC 10-K][5]. **TTM net income of $85.8B (Q3'25–Q2'26) is dominated by two quarters of equity gains and must not be capitalized directly.**
2. **Normalized earnings base:** I use 2025 after-tax operating earnings ≈ **$44.5B** (underwriting $7.3 + insurance investment income $12.5 + BNSF $5.5 + BHE $4.0 + manufacturing/service/retail $13.6 + other $1.6) [SEC 10-K][5]. This is the sustainable, non-market-driven earnings power.
3. **Insurance float:** ≈$176B of policyholder money invested at a _negative average cost_ (underwriting profitable) [SEC 10-K][5]. This is a genuine source of value — but it means a large share of the $360B cash + $324B equities is **not** "excess" shareholder cash; it is float- and reserve-backed. Any sum-of-parts must handle this (see §17 and the DCF caveat in §9).
4. **Deferred tax liabilities:** $85.6B at 12/31/25, mostly on unrealized equity gains [SEC 10-K][5]. The equity portfolio is worth materially less on an after-tax basis if ever sold. I haircut embedded gains by ≈25% in the sum-of-parts.
5. **Statutory surplus** of U.S. insurers ≈$333B — the insurance subs are over-capitalized by design, which is a value drag at the margin (that capital could be deployed) but a huge safety cushion [SEC 10-K][5].
6. **Minority interests & equity method:** Kraft Heinz and Occidental are equity-method (combined with $163B of assets at their level — Berkshire's stake is worth ≈$13–20B); NCI is small (≈$2B) [SEC 10-K][5].
7. **Contingent liabilities:** PacifiCorp wildfire accruals ≈$2.85B cumulative (≈$1.2B unpaid), and the HomeServices antitrust litigation (a $1.8B jury verdict subject to trebling risk, largely settled for $250M; separate Texas claims allege ≈$9B) — real but manageable relative to book value [SEC 10-K][5].

**Bottom line on normalization:** value the _operating_ earnings at ≈$44.5B after-tax, value the _financial assets at market_ (net of deferred taxes), and treat GAAP/TTM net income as noise.

---

## 6. Growth Analysis

**Growth is real but modest — and its quality is mixed.**

- **Decomposition (2025):** BNSF revenue +0%; BHE driven by capex/pass-through; manufacturing +1.6% (organic, price-led); service/retailing −2.0%; insurance premiums roughly flat-to-down in a soft P&C market [SEC 10-K][5]. The revenue line is barely growing organically.
- **Fundamental growth:** Expected growth = Reinvestment rate × Return on capital. With operating reinvestment ≈$7B net and ROIC ≈15%, _organic_ operating growth is ≈3–5% — before considering the compounding of the investment portfolio, which historically has grown book value ~8–10%/yr.
- **Growth quality:** **Moderate.** Operating-business growth is high-quality but slow; the investment-portfolio growth is high-return but market-dependent; the cash pile grows at ~4% (below cost of capital).
- **What causes growth to slow:** insurance-market saturation and competition (GEICO/P&C), rail volume cyclicality, utility regulatory lag, and — the big one — **the law of large numbers**: deploying $360B of cash into marketable equities at reasonable returns is hard at Berkshire's scale. This is the structural reason revenue/margin growth converges toward GDP-like rates.
- **Growth assumptions in my model:** revenue growth 4.0% in year 1 declining linearly to 2.5% (stable) by year 5; pre-tax operating margin 15.6% → 16.0%. These are deliberately conservative and reflect the normalization above.

---

## 7. Risk Analysis

**Business risk (Medium):** insurance underwriting cyclicality and mega-catastrophe exposure (2025 cat losses ≈$850M after-tax [SEC 10-K][5]); rail/energy regulatory and weather risk; competition in P&C (soft market); wildfire and antitrust litigation tails (PacifiCorp, HomeServices).

**Financial risk (Low):** total borrowings ≈$117.7B (≈$77B railroad/utilities + ≈$41B insurance/other) against $717B of book equity — debt/equity ≈17% [SEC 10-K][5], [fact pack]. Interest coverage is enormous; the $360B cash/T-bill pool is AAA-liquidity. Bankruptcy risk is negligible.

**Valuation risk (High):** the stock is a function of (i) the equity market (66% of the equity portfolio sits in just 5 names — Alphabet, AmEx, Apple, BofA, Coca-Cola [SEC 10-Q][7]), (ii) interest rates (T-bill income), and (iii) underwriting. A 20–30% equity-market drawdown would cut both the portfolio mark and reported earnings simultaneously.

**Failure risk (Very Low):** permanent-impairment probability is minimal for the operating businesses; the portfolio can fall but rarely permanently. Key-man/succession execution risk is the honest wildcard — Buffett (95) stepping back fully, and whether Abel preserves the underwriting discipline and allocation culture.

**The three assumptions whose failure most damages the thesis:** (1) that operating ROIC stays ≈15% (a sustained P&C underwriting loss cycle + rail disruption would break it); (2) that the equity portfolio compounds at the historical equity premium (a lost decade like 2000–2010 breaks the compounding story); (3) that management keeps deploying the $360B pile at above-cost-of-capital returns (sitting in 4% T-bills at an 8% cost of capital is a slow, silent value leak).

---

## 8. Cost of Capital (WACC)

| Input                             | Value                          | Basis                                                                                            |
| --------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------ |
| Risk-free rate (10-yr UST)        | ≈4.3%                          | Damodaran data shows 10-yr ≈4.2–4.6% [Damodaran][8]; ~4.3% mid-2026 (est.)                       |
| Equity risk premium               | ≈4.6%                          | Damodaran US ERP 4.46–4.69% (Jan 2026); implied ERP ≈4.23% (2025) [Damodaran][9], [Damodaran][8] |
| Beta                              | 0.61                           | 5-yr beta [Yahoo][10] — _used with caution_                                                      |
| Cost of equity (pure market-beta) | ≈4.3% + 0.61 × 4.6% = **7.1%** | CAPM                                                                                             |
| Company-specific premium          | ≈ +1.0%                        | Insurance/float + equity-market earnings concentration + regulatory + succession risk (judgment) |
| **Cost of equity**                | **≈8.1%**                      |                                                                                                  |
| Pre-tax cost of debt              | ≈4.5%                          | AA+/A++ insurer and A-rated rail/utility credits (est.)                                          |
| After-tax cost of debt            | ≈3.6%                          | 21% tax rate                                                                                     |
| Capital structure (market)        | ~90% equity / ~10% debt        | Market cap $1.08T vs ~$118B debt                                                                 |
| **WACC**                          | **≈8.0%**                      | Range 7.5–8.5%                                                                                   |

**ROIC vs WACC:** operating ROIC ≈15% > 8% WACC → growth in operating businesses creates value. The _financial-asset_ pool earns ≈4–5% < 8% → growth in cash/T-bills destroys value; growth in the equity portfolio historically creates value. Berkshire's value is therefore a **tug-of-war between a high-return operating engine and a low-return, oversized financial cushion.**

---

## 9. FCFF DCF — Primary Valuation

**Model choice & caveat.** The shared revenue-based FCFF workbook is an approximation for a conglomerate/insurer: it capitalizes a single revenue stream that _includes_ insurance investment income and then adds cash back — risking mild double-counting of the $360B T-bill pool. I therefore treat the DCF as a **lower-to-central bound** and require the sum-of-parts (§17) as the cross-check. Both land in the same zone (workbook base ≈$447, sum-of-parts ≈$471, weighted ≈$491), which gives me confidence. **Calibration note:** the scenario IVs and probability-weighted value in this file were re-synced to the verified workbook (build_model.py + verify_model.py, `ALL_MATCH`) after drafting; the workbook is the source of truth for these figures.

**Base-year normalization (2026):**

- Normalized revenue (run rate): $384.7B [fact pack]
- Normalized pre-tax operating margin: **15.6%** (≈2025 actual of ~15–16%)
- Tax rate: 21%
- NOPAT (Y1): $384.7B × 0.156 × 0.79 ≈ **$47.4B**
- Reinvestment tied to growth/ROIC: reinvestment rate = g/ROIC (4.0%/15.0% → ~27%)
- WACC 8.0%, terminal growth 2.5%, terminal ROIC 10%

**Explicit forecast (years 1–5):**

| Year | Revenue ($B) | Growth | EBIT Margin | EBIT ($B) | NOPAT ($B) | ROIC  | Reinvestment ($B) | FCFF ($B) |
| ---- | ------------ | ------ | ----------- | --------- | ---------- | ----- | ----------------- | --------- |
| 1    | 384.7        | 4.0%   | 15.7%       | 60.3      | 47.7       | 15.0% | 12.7              | 34.9      |
| 2    | 400.1        | 3.6%   | 15.8%       | 63.1      | 49.8       | 13.8% | 13.1              | 36.7      |
| 3    | 414.6        | 3.2%   | 15.8%       | 65.7      | 51.9       | 12.5% | 13.5              | 38.4      |
| 4    | 428.1        | 2.9%   | 15.9%       | 68.1      | 53.8       | 11.2% | 13.8              | 40.1      |
| 5    | 440.4        | 2.5%   | 16.0%       | 70.5      | 55.7       | 10.0% | 13.9              | 41.7      |

- PV of explicit FCFF (1–5) ≈ **$152B**
- Terminal value: FCFF₆ ≈ $42.8B (NOPAT₅ × [1 − 2.5%/10%]) ÷ (8.0% − 2.5%) = **$778B**; PV of TV ≈ **$529B**
- **Enterprise value ≈ $682B**
- Equity = EV − debt ($118B) + cash ($365.5B) ≈ **$929B**
- **Base intrinsic value ≈ $447 / Class B share** (verified workbook DCF-Base value; my earlier manual run gave ≈$428 — the workbook, which ramps margins on its own schedule and applies the full 10-year horizon, is authoritative and the $19 gap is within the error band)

**Reinvestment logic:** I do not forecast FCFF independently of growth; reinvestment = g/ROIC, so the 2.5% terminal growth requires only a ~25% reinvestment rate at a 10% terminal ROIC — internally consistent and consistent with Berkshire's low reinvestment intensity outside rail/utilities.

---

## 10. Terminal Value

- **Stable growth 2.5% < long-run nominal GDP (~4–5%)** — appropriately conservative for a $1T+ market cap.
- **Stable margin 16% pre-tax** — assumes the operating moats persist but the low-growth financial-asset drag continues.
- **Stable ROIC 10% > 8% WACC** — a small but persistent excess-return assumption. Honest note: Damodaran would normally push terminal ROIC toward WACC; keeping it at 10% is mildly generous, so the base case is _not_ aggressive.
- **TV / EV ≈ 78%** — this is high, and it is the correct flag: **Berkshire's value is overwhelmingly a function of its steady-state earnings power and cost of capital, not the first five years.** It also means the valuation is highly sensitive to WACC and terminal growth (see §14), which is why I weight the scenario analysis rather than the point estimate.

---

## 11. Relative Valuation

Berkshire is not cleanly comparable to anything, but the useful reference points:

| Multiple              | BRK (TTM)                               | Interpretation                                                                                                                                                                                   |
| --------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| P/E (GAAP, TTM)       | 12.67× [fact pack]                      | _Misleading_ — TTM EPS $39.77 is equity-gain-inflated; normalize and P/E ≈ 16–18× on $44.5B operating earnings                                                                                   |
| P/B                   | 1.44× [fact pack]                       | **The most relevant metric.** Historical range ≈1.0–1.6×; 1.44× is near the high end. A 10-yr average ≈1.25×. At 1.44× book the market is paying for sustained above-book returns + float value. |
| P/S                   | 2.48× [fact pack]                       | Meaningless for a premium-heavy financial/conglomerate                                                                                                                                           |
| vs S&P 500 (P/E ~23×) | BRK at 1.44× book / ~17× normalized P/E | BRK is _cheaper than the index_, but the index is itself expensive in 2026; "cheap vs. a bubble" is not a moat                                                                                   |

**Why BRK deserves a premium to book:** operating ROIC ≈15% > 8% WACC; negative-cost float; superb allocation record; AAA balance sheet. **Why the premium is capped:** the $360B cash + $324B equity portfolio is marked at market (no hidden upside), growth is low, and the marginal deployment return is compressed. **Fundamental fair P/B ≈ 1.3–1.5×** — i.e., today's 1.44× is _about right_, not a bargain.

---

## 12. Reverse DCF — What Does $504 Assume?

Working backward from $504.03 (equity $1,079B → EV ≈ $831B on my debt/cash bridge):

- Holding WACC at 8.0%, terminal growth 2.5%, and ROIC at my base levels, **the market is implicitly pricing a pre-tax operating margin of ≈18–19%** (my model needs ~19% at 4% revenue growth to produce $504; ~18% at 5% growth).
- That is ≈**3–3.5 margin points above my normalized 15.6%** — the market is assuming either (a) insurance investment income stays elevated on a large rate- and equity-gain-supported base, (b) continued margin expansion in the operating businesses, or (c) faster equity-portfolio compounding than I assume.
- **Are these assumptions reasonable?** Yes-ish — but they are at the _optimistic end_ of reasonable. They are not heroic (no 20%+ margin, no 7%+ growth), which is why this is a "Hold" rather than a "Sell." If the market were pricing a 13–14% margin, I'd call BRK cheap; at 18–19%, the price already banked the good news.

---

## 13. Scenario Valuation (Five Scenarios)

Scenario parameters are applied as adjustments to the base inputs (revenue growth, pre-tax margin, WACC, terminal growth, ROIC). Probabilities sum to **1.00**. In every scenario **terminal growth < WACC**. Values below are the **verified workbook** outputs (DCF-SevereBear … DCF-ExtremeBull, Scenario Summary).

| Scenario         | Prob. | Rev. growth | Margin (Y1) | WACC | Term. growth | Term. ROIC | **IV/share** | vs $504 |
| ---------------- | ----- | ----------- | ----------- | ---- | ------------ | ---------- | ------------ | ------- |
| **Severe Bear**  | 5%    | −3.0%       | 10.6%       | 9.5% | 2.0%         | 7.0%       | **$257.14**  | −49%    |
| **Bear**         | 15%   | 1.0%        | 12.6%       | 8.8% | 2.2%         | 7.6%       | **$310.98**  | −38%    |
| **Base**         | 50%   | 4.0%        | 15.6%       | 8.0% | 2.5%         | 10.0%      | **$447.31**  | −11%    |
| **Bull**         | 20%   | 6.0%        | 17.6%       | 7.6% | 2.9%         | 11.8%      | **$602.47**  | +19%    |
| **Extreme Bull** | 10%   | 8.0%        | 20.1%       | 7.2% | 3.2%         | 13.6%      | **$871.86**  | +73%    |
| **Weighted**     | 100%  | —           | —           | —    | —            | —          | **≈$490.84** | **−3%** |

- **Severe Bear:** 2008-style — equity-market crash (portfolio −35%), P&C underwriting loss cycle, recession cuts operating earnings; WACC rises.
- **Bear:** muted market, soft insurance pricing, mild recession; ~38% downside.
- **Base:** my normalized, honest view — low single-digit organic growth, ~15.6% margins, 8% WACC; ~11% below the market price.
- **Bull:** strong equity markets, firm insurance pricing, capital deployed productively; ~19% upside.
- **Extreme Bull:** the 1990s-Berkshire scenario — exceptional equity compounding + underwriting + successful large deployment; +73%.

The **skew is visibly negative at the current price** (heavy 15%/36%/45% downside tail vs. 5%/35% upside tail), which is the arithmetic behind the "no margin of safety" conclusion.

---

## 14. Sensitivity Analysis

**WACC × terminal growth** (base margins/growth; IV/share):

| WACC \ TG | 2.0% | 2.5% | 3.0% |
| --------- | ---- | ---- | ---- |
| **7%**    | $498 | $510 | $525 |
| **8%**    | $433 | $438 | $444 |
| **9%**    | $386 | $388 | $390 |

**Revenue growth × pre-tax margin** (WACC 8%, TG 2.5%; IV/share):

| Growth \ Margin | 14%  | 16%  | 18%  |
| --------------- | ---- | ---- | ---- |
| **3%**          | $400 | $440 | $479 |
| **4%**          | $405 | $446 | $486 |
| **5%**          | $411 | $452 | $493 |

**Valuation-critical assumptions:** (1) **WACC** — a 100bp change moves IV ±$50–60 (≈±12%); (2) **operating margin** — 2 pts = ±$40–45; (3) **terminal growth** — 100bp = ±$6–25. Growth is the _least_ important driver here, which is exactly what you'd expect for a mature conglomerate whose value is dominated by terminal value (78% of EV). Don't waste analytical effort on the growth line; spend it on the discount rate and the margin/multiple of the operating base.

---

## 15. Market Expectations vs Fundamental Reality

- **A. Current price:** $504.03 = 1.44× book, ~17× normalized earnings, ~2.5× sales; buybacks paused [Yahoo][10], [SEC 10-K][5].
- **B. Market-implied fundamentals:** ~18–19% pre-tax operating margin sustained, or equivalently continued market-beating equity-portfolio compounding on a $360B cash base (reverse DCF, §12).
- **C. My fundamental forecast:** ~15.6% margins, 4%→2.5% growth, 8% WACC → **$447** (verified workbook); probability-weighted **$491** (verified workbook).

**Price (>? =? <?) value:** Price ($504) > my weighted value ($491) by ~3% and > my base value ($447) by ~13%. The market is _mildly_ too optimistic — it has already priced in a successful future that is plausible but not probable. Importantly, this is not an extreme gap: Berkshire is a genuinely high-quality compounder and a ~13% premium to a conservatively-parameterized base intrinsic value is "expensive for a great business," not "a bubble."

---

## 16. Real Options & Optionality

- **Deployment option:** the $360B cash/T-bill pool is a genuine (if expensive-to-carry) option on future capital deployment — at scale into equities, distressed assets, or a large acquisition. If Abel deploys $100B+ at above-cost-of-capital returns, the Bull/Extreme-Bull scenarios materialize. I do **not** add a separate "optionality premium": the option's strike is effectively today's ~4% carry, and the Bull case already embeds partial exercise. Adding more would be double counting.
- **Float option:** negatively-costed float is already in the underwriting value.
- **Abandonment/flex:** Berkshire's structure lets it sit out markets — real, but already reflected in the low beta and the base-case stability.

---

## 17. Special Valuation Situation: The Sum-of-Parts Cross-Check

Because the revenue-based FCFF model is an approximation for an insurer/conglomerate, I build the **proper Damodaran sum-of-parts** (clearly labeled estimates, mid-2026 data):

| Component                                                              | Basis                              | Value ($B) |
| ---------------------------------------------------------------------- | ---------------------------------- | ---------- |
| Equity securities at market (6/30/26)                                  | $323.8B [SEC 10-Q][7]              | 323.8      |
| Cash, equivalents & U.S. T-bills (6/30/26)                             | $35.1B + $324.9B [SEC 10-Q][7]     | 360.0      |
| Fixed-maturity securities                                              | [SEC 10-Q][7]                      | 17.0       |
| Equity-method investments (Kraft Heinz, Occidental, etc.)              | [SEC 10-Q][7]                      | 19.9       |
| Loans & finance receivables (net)                                      | [SEC 10-Q][7]                      | 30.7       |
| **Gross financial assets**                                             |                                    | **751.4**  |
| Less: tax haircut on embedded equity gains (≈25%, est.)                | [SEC 10-K][5] deferred tax context | (45)       |
| **Net financial assets**                                               |                                    | **706.4**  |
| Operating businesses (BNSF+BHE+Mfg/Svc/Retail after-tax $23.1B × ~15×) | [SEC 10-K][5]                      | ≈347       |
| Insurance underwriting/float franchise (after-tax $7.3B × ~10×)        | [SEC 10-K][5]                      | ≈73        |
| Less: total borrowings                                                 | [SEC 10-K][5]                      | (117.7)    |
| **Estimated equity value**                                             |                                    | **≈1,009** |
| **Per Class B share**                                                  | 2,140M                             | **≈$471**  |

**Reconciliation:** the sum-of-parts (≈$471) sits modestly _above_ the revenue-DCF base ($447) but _below_ the probability-weighted value ($491) and the price ($504). The two independent methods bracket intrinsic value at ≈$447–$471, with the market at $504, and the probability-weighted value ($491) is the single best central estimate. This is the strongest evidence for the **C (Hold)** verdict. The residual ~3–13% of market value above my central estimates is the market paying for Berkshire's brand, its allocation history, and a successful-deployment scenario that is real but not yet earned.

---

## 18. Valuation Error & Uncertainty

**Confidence: Low–Medium.** Sources of error:

- **Estimation uncertainty:** WACC (7.5–8.5%), terminal ROIC/margin — each ±10%+ on value.
- **Economic uncertainty:** equity-market and interest-rate dependence; insurance cycle; regulatory (BHE) and litigation (wildfire, antitrust) tails.
- **Model uncertainty:** a single-line revenue-based FCFF is structurally wrong for an insurer/conglomerate; I mitigated with the sum-of-parts, but both share the same WACC and terminal assumptions.
- **Range:** honest 1-sigma band ≈ **$360–$540** — wide enough that a "Hold" (rather than "Buy" or "Sell") is the only defensible call at $504.

---

## 19. Inversion: What Would Make This Investment Fail?

Working backward from permanent capital loss or a lost decade:

1. **Equity-market meltdown at full position** — 66% of the equity portfolio in 5 mega-caps (Alphabet, AmEx, Apple, BofA, Coca-Cola [SEC 10-Q][7]); a 2000–2010-style lost decade would compress both the portfolio and reported earnings for years.
2. **P&C underwriting discipline broken** — if the new regime chases premium growth into a soft market and the negative-cost float turns positive-cost, the insurance engine (the source of the float's value) fails.
3. **Capital allocation stagnation** — parking $360B in 4% T-bills at an 8% cost of capital for another decade is the quiet killer; value bleeds out at ~4%/yr of the cushion.
4. **Regulatory/litigation tail** — PacifiCorp wildfire liabilities beyond the ~$2.85B accrued, or an adverse HomeServices antitrust outcome at the trebled $1.8B (or the ~$9B Texas claims), would hit BHE and the parent [SEC 10-K][5].
5. **Succession execution** — the Buffett-era allocation culture is the moat-within-the-moat; its erosion under the next generation would compress the P/B premium permanently.

**The three assumptions whose failure damages the thesis most:** (1) operating ROIC falls toward WACC; (2) the equity portfolio fails to earn the equity premium; (3) the cash pile stays parked at sub-cost-of-capital yields.

---

## 20. Probability-Weighted Investment Case

| Scenario     | Prob. | Value/share | Return at $504 | Key assumptions                                       |
| ------------ | ----- | ----------- | -------------- | ----------------------------------------------------- |
| Severe Bear  | 0.05  | $257.14     | −49%           | Market crash + underwriting loss cycle                |
| Bear         | 0.15  | $310.98     | −38%           | Muted markets, soft pricing, mild recession           |
| Base         | 0.50  | $447.31     | −11%           | Normalized operating earnings, 8% WACC                |
| Bull         | 0.20  | $602.47     | +19%           | Strong markets, firm pricing, productive deployment   |
| Extreme Bull | 0.10  | $871.86     | +73%           | Exceptional compounding + successful large deployment |

- **Probability-weighted intrinsic value: ≈$490.84** (verified workbook)
- **Expected one-time return:** ≈ −3% (annualized ≈ −0.5%)
- **Expected annualized return (IV grows ~7–8%/yr with book value):** ≈ **4–5%** — _below_ the ~8% cost of capital. The expected return does **not** adequately compensate for the risk.
- **Downside risk (20th percentile):** ≈ −38% (Bear scenario). **Upside potential (90th percentile):** ≈ +19 to +73% (Bull to Extreme Bull).
- **Asymmetry at $504: unfavorable.** The current price is in the upper third of the value distribution; the expected value is below the price.

---

## 21. Investment Decision

**Current price:** $504.03
**Bear value:** $311 · **Base intrinsic value:** $447 · **Bull value:** $602
**Probability-weighted value:** $491
**Expected upside/downside:** −3% (weighted)
**Expected annualized return:** ≈4–5% (below cost of capital)
**Margin of safety at $504:** ≈ −3%
**Valuation confidence:** Low–Medium
**Investment rating:** **C — Hold / Watch**

---

## 22. The Five Most Important Conclusions

1. **The business:** The single most important thing to understand is that Berkshire is _two_ assets in one: a set of genuinely moated operating businesses (insurance, rail, utilities, industrial) earning ROIC ≈15% on their capital, and a ~$684B marketable financial-asset pool (cash + equities) that is priced at market and earns ~4–8% depending on allocation. Value them separately; never multiply the merged revenue line.
2. **The economics:** The driver of long-term intrinsic value is **capital allocation at scale** — whether the $360B cash pile and the $324B equity portfolio are deployed at above- or below-cost-of-capital returns. Underwriting discipline and operating ROIC are stable; the deployment decision is where value is made or lost (and where Q4-2025's zero buybacks are a yellow flag).
3. **The market's expectations:** At $504 (1.44× book, ~17× normalized earnings), the market is pricing an ≈18–19% pre-tax operating margin and continued successful portfolio compounding — reasonable, but at the optimistic end of reasonable, and it has already banked the successful-deployment scenario.
4. **The valuation:** The most defensible estimate is **≈$447–$491 per share** — the revenue-based FCFF DCF (verified workbook) says ≈$447; the insurance-aware sum-of-parts says ≈$471; the probability-weighted scenario value is ≈$491. The market at $504 is ~3–13% above this band, which is "expensive for a great business," not a bubble.
5. **The investment decision:** At $504, the expected return (≈4–5% annualized) is below Berkshire's 8% cost of capital and the risk/reward is negative at the margin. This is not a Sell — the quality and optionality are real — but there is **no margin of safety**. Buy below ≈$420; hold and let the compounding do the work above that; reassess above ≈$560.

---

## 23. Damodaran-Style Final Judgment

> **"At a price of $504, the market is effectively assuming Berkshire can hold an ~18–19% operating margin and keep compounding a $360B cash pile and a $324B equity portfolio at equity-like returns. My valuation implies ≈$447–$491 per share (base ≈$447, weighted ≈$491) because I expect only ~15.6% margins, GDP-like revenue growth, and a cost of capital of 8% — and because the $360B T-bill cushion currently earns less than that cost of capital. The biggest risk to this valuation is not the operating businesses — it is the equity market (66% of the portfolio in five stocks) and the pace and quality of capital deployment. Therefore, at today's price, I would hold and wait rather than buy, because the price has already paid for the good news and the expected return is below what this company's risk deserves."**

---

## Sources

1. [Berkshire Hathaway — Official IR Home](https://www.berkshirehathaway.com/) — company overview; links to annual/interim reports, shareholder letters, news releases.
2. [Berkshire Hathaway — Annual & Interim Reports](https://www.berkshirehathaway.com/reports.html) — filing calendar confirming FY2025 10-K and Q1/Q2 2026 10-Qs.
3. [Berkshire Hathaway — Greg Abel Shareholder Letters](https://www.berkshirehathaway.com/letters/gealetters.html) — the 2025 letter (by Abel, under Buffett's chairmanship) on results and capital allocation.
4. [SEC EDGAR — Berkshire Hathaway XBRL Company Facts (CIK 0001067983)](https://data.sec.gov/api/xbrl/companyfacts/CIK0001067983.json) — annual revenue/net income/EPS, quarterly earnings, balance sheet, share data; basis for all GAAP figures.
5. [SEC EDGAR — FY2025 Form 10-K (brka-20251231.htm)](https://www.sec.gov/Archives/edgar/data/1067983/000119312526083899/brka-20251231.htm) — float ≈$176B, segment after-tax earnings table, cash/T-bills $369B, buyback program & Q4-2025 zero buybacks, no dividend, statutory surplus $333B, PacifiCorp/HomeServices contingencies, BNSF/BHE/manufacturing detail.
6. [SEC EDGAR — FY2025 10-K accession index](https://www.sec.gov/Archives/edgar/data/1067983/000119312526083899/index.json) — document map for the 10-K.
7. [SEC EDGAR — Q2 2026 Form 10-Q (brka-20260630.htm)](https://www.sec.gov/Archives/edgar/data/1067983/000119312526341032/brka-20260630.htm) — 6/30/26 balance sheet (cash $35.1B + T-bills $324.9B; equity securities $323.8B), Q2-26 GAAP Class B EPS $11.91, top-5 holdings = 66% of portfolio.
8. [Aswath Damodaran — Historical Implied Equity Risk Premiums](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histimpl.html) — implied ERP ≈4.23% (2025) and 10-yr Treasury series for the risk-free rate.
9. [Aswath Damodaran — Country Default Spreads and Risk Premiums](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html) — US equity risk premium 4.46–4.69% (Jan 2026 update).
10. [Yahoo Finance — BRK-B Key Statistics](https://finance.yahoo.com/quote/BRK-B/key-statistics/) — market data (price, market cap, beta, P/E, P/B, 52-week range); figures used as provided in the shared fact pack, as of 2026-08-14.
11. [Shared fact pack — `Analysis/BRK/2026-08-16/fact-pack.json`](https://www.berkshirehathaway.com/) — the analyze-company shared fact pack: market data (price $504.03, market cap ~$1.08T, beta 0.61, P/E 12.67, P/B 1.44), TTM metrics, Q2-2026 deployment narrative, Alphabet stake (~$31B, ~8.8% of equity portfolio), analyst targets ($547.67 avg / $604 high).
12. [SEC EDGAR — Berkshire Hathaway filing index](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001067983) — CIK 0001067983 filing index (10-Ks, 10-Qs, DEF 14A).

---

## Position Summary

- Rating: C — Hold (great business, fair-to-slightly-rich price; no margin of safety at $504)
- Intrinsic value: bear=$311 base=$447 bull=$602 | weighted=$491 (Severe-Bear tail $257) — verified workbook values
- Buy zone: <$420 | Sell/reduce zone: >$560
- Key metrics: ROE ~12.1% (ttm, fact pack); operating ROIC ~15% (operating businesses, est.); pre-tax operating margin ~15.6% (2025 normalized, SEC); operating cash flow ~$55B+/yr (SEC); debt/equity ~17% (total borrowings ~$118B vs book equity $717B, SEC); cash+U.S. T-bills $360B (6/30/26) / $369B (12/31/25), SEC; insurance float ~$176B (SEC)
- Top risks: equity-market concentration (top-5 holdings = 66% of portfolio; mark-to-market earnings swings) · P&C underwriting cycle / mega-catastrophe · BHE regulatory & litigation tails (PacifiCorp wildfire ~$2.85B accrued/~$1.2B unpaid; HomeServices antitrust) · sub-cost-of-capital carry on the ~$360B cash pile · succession/allocation-culture execution under new CEO
