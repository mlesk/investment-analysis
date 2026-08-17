# Aswath Damodaran-Style Valuation Analysis — Rocket Lab Corporation (NASDAQ: RKLB)

**Analysis date:** 2026-08-16 · **Reference price:** $80.25 (Aug 14, 2026 close) · **Market cap:** ~$48.0B · **EV:** ~$45.8B · **Fiscal year end:** Dec 31
**Lens:** Damodaran quantitative spine · **Prepared by:** GitHub Copilot (analyze-company skill)

---

## BOTTOM LINE FIRST

### Rating: **D — AVOID / SIGNIFICANTLY OVERVALUED**

**One-paragraph verdict:** Rocket Lab is a genuinely excellent, founder-led space company — the #2 most-launched orbital rocket in 2025, a vertical integrator with $2.36B of record backlog, a medium-lift Neutron on the pad, and an $8.0B pending Iridium acquisition that would make it a self-launching tier-1 space power. But at $80.25 the market is paying 62× trailing sales for a company that lost $198M in FY2025, burned $321M of free cash flow, and has a 5-year beta of 2.63 — and the price embeds outcomes the fundamentals do not support. My five-scenario, 10-year FCFF DCF — using Damodaran's current inputs (risk-free 4.74%, implied ERP 4.28%, forward-adjusted beta ~1.7 → WACC ~12.0%, terminal growth 3.0%) — produces a **base intrinsic value of ~$11.00/share** and a **probability-weighted value of ~$16.82/share**, about **79% below** the current price. The model is brutal for a reason: a pre-profit hyper-grower must reinvest 100%+ of its operating profit (growth ÷ ROIC) into new launch vehicles, factories, and acquisitions for years, so value concentrates almost entirely in a heavily discounted terminal value. A reverse DCF shows $80.25 is only justified if Rocket Lab reaches **~$25–30 billion of terminal revenue at 22–25% operating margins — a company larger than SpaceX's entire $18.7B today** — a "second SpaceX" outcome with <10% probability in my framework. I would not initiate a position at $80.25; value emerges only below ~$25–30, with real margin of safety below ~$20.

---

## Executive Summary Table

| Item                                     | Value                                                                                  |
| ---------------------------------------- | -------------------------------------------------------------------------------------- |
| **Current price**                        | $80.25                                                                                 |
| **Rating**                               | **D — Avoid / Significantly Overvalued**                                               |
| **WACC**                                 | ~12.0% (Rf 4.74% + β~1.7 × ERP 4.28%; net cash → no debt weight)                       |
| **Terminal growth**                      | 3.0% (< WACC in every scenario)                                                        |
| **Tax rate**                             | 21% (normalized; full valuation allowance on U.S. DTAs)                                |
| Base intrinsic value / share             | ≈ $11.00                                                                               |
| Bear / Bull value / share                | ≈ $5.94 / ≈ $25.09                                                                     |
| Severe Bear / Extreme Bull value / share | ≈ $4.91 / ≈ $50.22                                                                     |
| Probability-weighted value / share       | ≈ $16.82                                                                               |
| Implied upside at $80.25                 | ≈ **−79%** (annualized ≈ −26.8%)                                                       |
| **Margin of safety at $80.25**           | None (negative ~79%)                                                                   |
| **Buy zone**                             | First tranche ≤ $30; accumulate $22–30; conviction < $20                               |
| **Valuation confidence**                 | **Low-to-Medium** (economic uncertainty extreme; direction of overvaluation is robust) |

---

# 1. Business Understanding & Fundamental Story

### Business Model (plain English)

Rocket Lab is an end-to-end space company: it **designs, builds, launches, and operates spacecraft**. It sells (1) **Launch Services** — the Electron small-lift rocket (up to 300 kg to LEO, 21 launches in 2025, ~$8.5M revenue per launch), the HASTE suborbital testbed, and the in-development Neutron medium-lift rocket (13,000 kg reusable to LEO, ~$50–55M ASP); and (2) **Space Systems** — spacecraft design and manufacturing, spacecraft components (reaction wheels, star trackers, solar cells via SolAero, radios, separation systems, batteries), optical/EO-IR payloads (GEOST), laser communications (Mynaric), and the Flatellite/Photon spacecraft platforms [SEC 10-K][2]. The pending $8.0B acquisition of Iridium (66-satellite L-band constellation, ~2.5M subscribers, >$870M annual revenue, profitable) would add a self-launching, high-margin recurring communications business [SEC 10-Q][1][11].

Who pays? Governments (US DoW/Space Force, NASA, NRO, DARPA — ~47% of FY2025 revenue), and commercial satellite operators (BlackSky, Planet, Synspective, iQPS, Kuiper-adjacent constellations). Why? Rocket Lab's Electron is one of only a few commercial vehicles with frequent, reliable, dedicated access to orbit; its space-systems stack is vertically integrated — one vendor can design, build, launch, and operate a spacecraft. Revenue converts into cash poorly _today_ (TTM OCF −$222M) because growth requires massive reinvestment: Neutron development (R&D $270.7M in FY2025, 45% of revenue), launch infrastructure (LC-3 pad), factories, and acquisitions.

### Economic Structure

- **Revenue drivers:** launch cadence × price per launch; spacecraft manufacturing contracts (space systems, 70% of FY2025 revenue); components backlog; recurring (Iridium post-close). Backlog $2.36B (45.5% converts within 12 months) provides unusually high near-term visibility [SEC 10-Q][1].
- **Unit economics (FY2025):** launch segment gross margin ~40.9% ($81.3M GP / $199.0M rev); space systems ~31.3% ($125.9M / $402.8M). Cost per launch fell to $4.8M vs $8.5M revenue per launch — launch is profitable at the gross level [SEC 10-K][2].
- **Gross margin:** 34.4% FY2025 → 36.1% Q2'26 GAAP (41.5% non-GAAP) — improving with scale, but far below software economics [SEC 10-Q][1].
- **Operating margin:** deeply negative — FY2025 EBIT −38.1% (R&D 45% of revenue); Q2'26 EBIT −24.6%. The company is structurally pre-profit until R&D normalizes and Neutron/Iridium scale.
- **Capital intensity:** very high — capex $156.3M FY2025 (26% of revenue); Neutron + LC-3 + factories. Capital is the constraint on growth.
- **Working capital:** contract-heavy; contract liabilities $195M at YE25 (customer advances) partly fund operations; inventories $158M.
- **Tax economics:** full valuation allowance on U.S. deferred tax assets ($304M) — the company pays almost no cash tax and has $841M federal NOLs; a 21% normalized tax rate is appropriate for valuation but the cash tax rate is ~0% for years [SEC 10-K][2].
- **Financing:** essentially unlevered — $157M total debt (convertible notes 4.25% due 2029, largely converted) vs ~$2.4B cash+securities at Q2'26 (net cash ~$2.25B) after a $1.08B ATM raise in Q2'26 to fund Iridium [SEC 10-Q][1].
- **Competitive dynamics:** launch is a duopoly-plus (SpaceX dominant; ULA, Blue Origin, Firefly, Chinese/Russian/Indian/European providers); spacecraft manufacturing is fragmented (Airbus, Maxar, Thales, L3Harris, Redwire, York). Rocket Lab competes on cadence, cost, vertical integration, and responsiveness.

### Fundamental Story (the valuation narrative)

> "This company will create value because it becomes the vertically-integrated, self-launching tier-1 space power of the commercial era — compounding launch + space systems + Iridium's recurring revenue to multi-billion scale at aerospace-class margins, with a rare combination of founder-led engineering and real backlog."

The three fundamental inputs:

- **Cash Flows:** Today — deeply negative: FY2025 OCF −$165.5M, FCF −$321.8M; TTM FCF −$371M; SBC $71.1M (FY2025) / $81.6M (TTM) is a real, growing shareholder cost. Expected change — cash flow turns positive only after Neutron amortizes R&D and Iridium's recurring revenue (FY2028+) is consolidated; the model does not reach positive FCFF until Year 7 of the 10-year forecast. Evidence — improving gross margins (21% → 34% → 36%+), record backlog, Iridium's profitable >$870M revenue base [SEC 10-Q][1]. What could go wrong — Neutron slips or fails; Iridium integration dilutes; R&D stays structurally high.
- **Growth:** Today — very high: FY2025 +38%, TTM +52%, Q2'26 +62% (space systems +94%). Expected change — 45% Y1 (FY27 ≈ consensus $1.35B) decaying ~4.5pts/yr to ~4% by 2036, reaching ~$8.2B revenue in the base case (Iridium + Neutron 1-3-5 ramp + space systems compounding). Evidence — $2.36B backlog, 90+ launch manifest, Iridium >$870M, SDA Tranche 3 ($816M), Space Force contracts [SEC 10-Q][1][10-K][2]. What could go wrong — launch cadence stalls, constellation demand saturates, competition (SpaceX price cuts, Firefly) caps pricing.
- **Risk:** High and binary — beta 2.63 (5-yr); launch failure tail risk (3 failures in history, incl. Sept 2023); Neutron first-launch risk (Stage-1 tank qualification failure Jan 2026 pushed launch to Q4'26); customer concentration (top-5 = 49% of revenue, 77% of backlog); US-government funding dependence; FX (NZ$); key-person (Sir Peter Beck); heavy dilution (shares +15.7% YoY; 141.8M shares reserved for future issuance under equity plans) [SEC 10-K][2][DEF 14A][3].

### Business Lifecycle

**Young / high-growth** (transitioning from development to scale). Revenue compounding 38–62%, gross margins rising, structurally pre-profit, negative free cash flow, huge optionality. The appropriate model is a **two-stage FCFF DCF** (10-year explicit high-growth-then-fading phase + Gordon stable-growth terminal value), exactly what the official workbook builds. This is not a stable-growth or distressed situation; it is the hardest-to-value quadrant — young, fast, capital-hungry — which is why scenario weighting matters more than a point estimate.

---

# 2. Historical Fundamental Analysis

### Revenue ($M) [SEC 10-K][2][StockAnalysis][6]

| Year         | Revenue | Growth | Gross Mgn | Net Income | Diluted EPS |
| ------------ | ------- | ------ | --------- | ---------- | ----------- |
| FY2021       | 62.1    | —      | ~15%      | −117.3     | −0.34       |
| FY2022       | 210.9   | +239%  | ~12%      | −135.9     | −0.33       |
| FY2023       | 244.6   | +16%   | 21.0%     | −182.6     | −0.38       |
| FY2024       | 436.2   | +78%   | 26.6%     | −190.2     | −0.38       |
| FY2025       | 601.8   | +38%   | 34.4%     | −198.2     | −0.37       |
| TTM (Jun-26) | 769.2   | +52%   | 37.3%     | −165.5     | −0.28       |

**What actually caused growth:** FY2024's +78% was launch cadence (16 vs 10 launches) plus space-systems spacecraft manufacturing (+$138M). FY2025's +$165.6M split: space systems +$91.9M (+30%, organic — spacecraft manufacturing) and launch +$73.7M (+59%, 21 launches at higher price). **This is high-quality, organic, execution-driven growth** — Electron became the second most-launched orbital rocket in 2025, and backlog grew from $1.07B to $1.85B to $2.36B [SEC 10-K][2][10-Q][1]. Unlike acquisition-inflated growth stories, Rocket Lab's growth is real product demand (with acquisitions like GEOST adding optical capability on top).

### Profitability

| Metric (FY)   | FY2023 | FY2024 | FY2025 | Q2'26  |
| ------------- | ------ | ------ | ------ | ------ |
| Gross margin  | 21.0%  | 26.6%  | 34.4%  | 36.1%  |
| EBIT margin   | −72.8% | −43.6% | −38.1% | −24.6% |
| R&D / revenue | 48.7%  | 40.0%  | 45.0%  | ~35%   |
| Net margin    | −74.7% | −43.7% | −33.1% | −21.0% |
| ROIC (TTM)    | n/m    | n/m    | ~−10%  | ~−5.5% |

Margins are **improving rapidly on the gross line** (21% → 34% → 36%) as launch cost per mission fell from $7.0M to $4.8M, but **still deeply negative at the operating line** because R&D (~45% of revenue, +55% in FY2025) is financing Neutron. The critical question is not whether margins improve — they clearly are — but whether **R&D can compress from 45% of revenue toward a single-digit percentage while the company grows fast enough to absorb it**, and whether the growth can be funded without endless dilution.

### Capital Intensity

- CapEx/Revenue: **~26%** (FY2025 $156.3M) — genuinely capital-hungry (factories, launch pads, test infrastructure). [SEC 10-K][2]
- Depreciation + amortization: $43.9M FY2025, rising.
- Working-capital: contract assets + inventories grew ~$60M in FY2025 — growth consumes working capital.
- Acquisitions: GEOST ($290M, Aug 2025), plus Mynaric and Motiv (Q2'26); Iridium pending ($8.0B EV) — a step-change in capital allocation.
- R&D: $270.7M FY2025 — **the single largest line item after cost of revenue**; mostly Neutron + spacecraft platforms.
- **Stock-based compensation: $71.1M FY2025 (~11.8% of revenue), $81.6M TTM (~10.6%)** — growing faster than revenue and now approaching the net loss in magnitude [SEC 10-K][2].

**Accounting earnings vs economic earnings vs cash flows:** Reported net loss (−$198M) _understates_ cash burn because D&A ($44M) and SBC ($71M) are non-cash; reported OCF (−$165.5M) is the real cash drain, and FCF (−$321.8M) includes the capex the growth model needs. **Economic FCFF for a shareholder is more negative than GAAP FCF** if SBC is treated as a true cost: OCF −$165.5M − capex $156.3M − SBC $71.1M ≈ **−$393M** of economic cash consumption in FY2025 — funded entirely by the ATM equity raises ($1.12B net in 2025) [SEC 10-K][2]. This is the crux: **growth is being funded by shareholders, not by the business.**

### Return on Invested Capital

- **ROIC (NOPAT / Invested Capital):** ~−5.5% TTM (fact pack; StockAnalysis −6.99% for peer RDW is comparable). With ~$3.5B of equity and negative NOPAT, ROIC is negative.
- **ROIC vs cost of capital (~12%):** ROIC is far below WACC — **every dollar of growth today destroys value** until margins and returns turn. The model therefore uses a low initial ROIC (10%) that transitions to 18% (mature aerospace) — deliberately generous, yet still insufficient to justify the price.

---

# 3. Competitive Advantage & Industry Economics

### Industry Structure

- **Market:** global space economy ~$400B and growing; launch ~$15–30B by 2035 (small+medium lift); spacecraft manufacturing ~$30–40B; satellite services (Iridium's segment) the largest layer.
- **Concentration:** launch is a tight oligopoly — SpaceX dominates; Rocket Lab is the #2-most-launched orbital rocket (2025); ULA/Blue Origin/Firefly follow; China (CALT/CASC) and Russia compete with subsidies. Spacecraft components are fragmented (Redwire, York, Maxar, Thales).
- **Barriers to entry:** extremely high — flight heritage, regulatory licensing (FAA/DoT, NZ Space Agency, FCC), orbital launch ranges (Rocket Lab owns LC-1 in NZ with a US-NZ treaty advantage), integrated manufacturing, and years of capital. **This is a genuine structural barrier.**
- **Substitutes / customer power:** customers (especially US government) hold procurement power and can re-scope; commercial constellation operators can switch between SpaceX rideshare, Firefly, or other vehicles, but dedicated small-lift supply is scarce.
- **Supplier power:** moderate — sole-source items (composites, IMUs, rare earths) with long lead times [SEC 10-K][2].

### Competitive Advantage

- **Flight heritage / reliability:** Electron has 75+ successful missions and 3 failures (~96% success); first-mover in dedicated small-lift. Real and durable — customers pay a premium for schedule certainty.
- **Vertical integration:** designs, builds, launches, operates — controls cost, quality, and cadence. Real cost/margin advantage (launch GM 41%).
- **Proprietary technology:** 3D-printed Rutherford/Archimedes engines, carbon-composite structures, electric turbopump cycle, kick stage. Real but imitable over time (Firefly, Relativity, ABL).
- **Distribution/infrastructure:** private launch range in NZ (treaty-based), LC-2/LC-3 at Wallops — scarce, hard-to-replicate assets.
- **Network effects / switching costs:** weak — launch contracts are project-based; Iridium (pending) would add genuine subscriber lock-in and switching costs.
- **Does it show up economically?** Yes in growth and gross margin (34–37%, above most peers) and in backlog visibility — but **not yet in ROIC**, which is negative. The moat shows up as durable growth + improving unit economics, not as current excess returns on capital.

### Excess Returns

**ROIC (~−5.5%) − WACC (12%) ≈ −17.5pts today.** The spread is deeply negative and will only turn positive when (a) R&D normalizes, (b) Neutron/Iridium scale, and (c) the equity-funded reinvestment stops consuming NOPAT. The moat is real but its payoff is a decade away. **Competitive Advantage Rating: Strong** (structural barriers, flight heritage, vertical integration — among the best in the sector), but the economics are immature.

---

# 4. Management & Capital Allocation

### Capital Allocation (observable record)

- **Internal reinvestment:** excellent operational execution — 21→24 Electron builds/yr, cost per launch down 31%, gross margin up 13pts in 3 years, backlog tripled. The reinvestment engine works [SEC 10-K][2].
- **Acquisitions:** GEOST ($290M), Mynaric, Motiv, and the pending **$8.0B EV Iridium** (funded partly by a $3.6B bridge + a $1.08B ATM raise). Iridium is a strategically coherent but **enormous, risky, debt-funded bet** — $8B is ~17% of Rocket Lab's own market cap, roughly 9× Iridium's ~$870M revenue, and it changes the risk profile (post-transaction indebtedness, integration, regulatory approval). The company's own 10-Q lists 5 "HIGH" risk factors for the deal [SEC 10-Q][1][11].
- **Dividends:** none; restricted by Dept. of Commerce Direct Funding Agreement (buybacks and dividends require approval) [SEC 10-K][2].
- **Buybacks:** effectively none (restricted); buyback yield −15.7% (i.e., net issuance).
- **Debt:** minimal — $133.7M total at Q2'26 (convertible notes mostly converted/retired); net cash ~$2.25B _pre-Iridium_. Post-Iridium, net leverage will rise substantially.
- **Dilution — the structural concern:** shares outstanding +15.7% YoY (+4.0% QoQ) to 598.5M; $1.12B ATM raises in FY2025, $1.08B in Q2'26; 141.8M shares reserved for future equity-plan issuance (vs 598M outstanding — ~24% overhang); CFO Adam Spice exercised 1.87M options and realized **$86M** in 2025 [SEC 10-K][2][DEF 14A][3]. Management's answer to "how do we fund the dream" is "raise equity," and shareholders pay the price in per-share value.

### Incentives

- Sir Peter Beck (founder, CEO, Chairman): 2025 comp $6.83M — $800K salary + $6.03M RSU grant; 2024 total was $20.1M; ~88:1 CEO-to-median pay ratio; 2025 Say-on-Pay support ~80% [DEF 14A][3].
- Compensation is RSU-heavy (long-term, aligned), with no base-salary increases and no cash bonuses in 2025 — **incentives skew toward long-term stock price appreciation**, which encourages the "keep investing, keep raising" flywheel even when near-term returns are negative.
- Beck's alignment is strong through the Equatorial Trust (45.95M Series A preferred, ~7.5% voting power, convertible 1:1); he is also the **key-person risk** (no key-man insurance) [SEC 10-K][2][DEF 14A][3].

**Management Quality Rating: Excellent operationally, Good on capital allocation** — world-class founder execution, but the equity-funded growth model and the Iridium leverage push risk onto shareholders; SBC and dilution are the price of the ambition.

---

# 5. Accounting & Earnings Normalization

### Earnings Quality

- **Net income vs OCF:** FY2025 NI −$198M vs OCF −$165.5M — both negative; the gap is D&A + SBC. Neither is a positive earnings signal.
- **SBC — the key adjustment:** $71.1M FY2025 / $81.6M TTM (~10.6% of revenue). **Do not add it back.** It is a real cost that dilutes shareholders; the model treats it as an operating expense via its margin assumptions.
- **One-time / non-cash items:** $10.6M gain on contingent-consideration revaluation (GEOST earnout markdown); $5.9M loss on debt extinguishment; $132M cash + $137.7M stock for GEOST. None materially distort the core loss.
- **Revenue recognition:** long-term fixed-price contracts recognized point-in-time (launch) or over-time (spacecraft build, input method). Audit critical-matter on cost-to-complete estimates; FY2025 had a $7.9M net downward catch-up (incl. $12.8M on one contract) [SEC 10-K][2]. Judgment risk exists but is not egregious.
- **Goodwill/intangibles:** $206M goodwill + $225M intangibles at YE25 — modest vs $3.5B equity; no impairments; the Iridium deal will add substantially more goodwill.
- **Deferred tax assets:** full valuation allowance ($304M) — no recognized tax assets, ~$841M federal NOLs.

### Normalized Earnings (my base-year set)

- Normalized revenue run-rate: **$951M (FY2026 consensus)** — I anchor Y0 to the forward FY26 revenue (~annualizing Q2'26 $234M + Q3 guide $250–265M) and let Y1 growth (45%) carry to ~$1.38B in FY27 (slightly above the $1.35B consensus to reflect the Neutron ramp and partial Iridium H2 contribution).
- Normalized EBIT margin (Y1): **5.0%** — a deliberate judgment: below Q2'26 non-GAAP (which is ~−8% EBIT), reflecting that GAAP R&D still overwhelms revenue in FY27; the model's "margin" is a normalized operating margin that implicitly nets the SBC-adjusted reality. Even this is generous vs today's −25% GAAP EBIT margin.
- Normalized tax rate: **21%** (federal statutory; the company's cash tax rate is ~0% on NOLs, but 21% is the correct long-run normalized rate).
- Normalized capex: ~26% of revenue initially, declining as Neutron infrastructure completes (embedded in the g/ROIC reinvestment).
- **Numbers to NOT use directly:** GAAP FY2025 EBIT (−38% margin) and net loss — both are Neutron-development-distorted; TTM FCF (−$371M) — includes SBC add-back that is a real cost.

### Special Issues

- **Dilution / equity overhang:** Material — modeled by holding the share count at 598.5M (a conservative-to-generous treatment given 141.8M shares reserved for future issuance and +15.7% YoY creep).
- **Convertible notes:** 4.25% notes due 2029, $155.7M principal at YE25, largely converted in 2025–26; ~$133.7M total debt at Q2'26. Included in the debt line.
- **Series A Preferred (Equatorial Trust):** 45.95M shares, convertible 1:1, votes with common — effectively common; included in share count via 598.5M? (Preferred converts on transfer/CEO departure; treated as common for EPS purposes) [DEF 14A][3].
- **Leases:** ~$111M total lease liabilities (operating+finance) at YE25 — modest; finance leases included in the $133.7M debt line.
- **Cross-holdings / minority interests:** none material.
- **Contingent liabilities:** GEOST earnout (up to $50M, marked at $7.6M); securities class action (Neutron-related, MTD granted Nov 2025, amended complaint pending); post-Iridium financing risk.
- **Excess cash:** ~$2.4B cash+securities at Q2'26 — the model treats net cash of ~$2.17B as value-additive _pre-Iridium_; the Iridium deal will consume most of it (and add ~$3.6B bridge debt), a swing I capture in the bear scenarios rather than the base (deal closes mid-2027).

---

# 6. Growth Analysis

### Growth Decomposition

- **Organic:** FY2025 space systems +$91.9M and launch +$73.7M — genuinely organic, volume/price-driven (21 launches vs 16; higher revenue per launch) [SEC 10-K][2]. This is high-quality growth.
- **Acquisition:** GEOST (added ~$12M FY2025 revenue, back-end weighted); Iridium (pending, adds >$870M/yr from 2028) — transformative but separate from organic.
- **Forward visibility:** backlog $2.36B (record), 45.5% converts in 12 months; 90+ launches on manifest; SDA Tranche 3 $816M; Space Force Flatellite $397M; >$160M GEO deals [SEC 10-Q][1].

### Fundamental Growth

Expected growth = Reinvestment Rate × ROIC. At 45% Y1 growth with 18% terminal ROIC (flat in the model), the implied reinvestment rate is ~250% of NOPAT — i.e., Rocket Lab must reinvest **more than its entire operating profit** into growth for years. That is exactly what it does (FCF −$371M), and it is the fundamental reason the DCF is terminal-heavy. The base case (45% → 4% over 10 years, ~24% CAGR) requires Rocket Lab to grow from $0.95B to ~$8.2B — roughly 3.4× SpaceX's _revenue-growth pace_, but on a far smaller base, and it embeds Iridium + Neutron + space systems all firing.

### Growth Quality

**Moderate-to-High quality** — this is the rare growth story that is real (backlog, launches, organic segment growth) rather than accounting-driven. It is penalized, however, by (1) the capital required (capex + R&D + acquisitions), (2) the dilution that funds it, and (3) the binary execution risk on Neutron and Iridium.

### Growth Duration

- High-growth: ~8 years (FY27–FY34), 45% → ~9%
- Transition: FY35–FY36, ~4%
- Stable: terminal 3%
- **What causes growth to slow:** launch cadence limits (120/yr LC-1 capacity), constellation market saturation, Neutron ramp execution, competition, and the natural deceleration of a company scaling past $5B. Growth _will_ slow; the question is only the level it reaches.

---

# 7. Risk Analysis

### Business Risk

- **Launch failure:** 3 of 78 orbital missions failed; each failure grounds the fleet and can cost contracts/insurance. Binary tail risk.
- **Neutron execution:** Stage-1 tank qualification failure (Jan 2026) already slipped first launch to Q4'26; a failed or delayed Neutron is the single biggest value risk (it is the medium-lift growth engine and the Iridium launch rationale).
- **Iridium deal risk:** closing conditions (HSR lapsed, FCC, foreign approvals, stockholder vote), $3.6B bridge financing, post-transaction indebtedness, integration — the 10-Q flags 5 HIGH risks [SEC 10-Q][1][11].
- **Customer concentration:** top-5 customers = 49% of FY2025 revenue, 77% of backlog; US government-related ~47%; a funding-constrained government (DOGE-era cuts, shutdowns — the Oct 2025 shutdown already delayed awards) is a real headwind [SEC 10-K][2].
- **Competition:** SpaceX scale and price cuts; Firefly/Blue Origin in medium-lift; subsidized foreign launchers.
- **Key person:** Peter Beck (no key-man insurance) [SEC 10-K][2].
- **Regulatory/FX:** ITAR, FAA/NZ licensing, tariff exposure, NZ$ (~15% of spend).

### Financial Risk

- Debt is tiny today ($133.7M, net cash $2.25B); **post-Iridium, leverage rises materially** (up to ~$3.6B bridge). Currently low financial risk, rising sharply if the deal closes.
- Operating leverage is extreme (fixed R&D/factories) — revenue swings amplify EBIT swings.
- Failure risk (distress): **low near-term** (Altman Z 32.5, ~$2.4B cash); **moderate-to-high for per-share value** via dilution if the equity-funded model keeps printing shares.

### Valuation Risk

Value is extraordinarily sensitive to (1) the discount rate, (2) terminal revenue scale, and (3) how long the cash burn lasts (§14). The market's price embeds the most optimistic end of every distribution.

### Failure Risk

- Probability of severe financial distress: **low** (cash-rich, growing).
- Probability of permanent impairment to _per-share value_: **moderate-to-high** — a 62× sales stock with negative FCF and relentless dilution can de-rate to a 10–20× growth multiple (it already fell from $151 to $37.57 within 52 weeks, a −75% drawdown).
- Probability of needing substantial external capital: **high** (Iridium alone requires ~$3.6B bridge; ongoing burn).

---

# 8. Cost of Capital & Required Return

### Cost of Equity

- **Risk-free rate: 4.74%** (US 10-year Treasury, Damodaran's Aug 2026 convention) [Damodaran][5].
- **Equity risk premium: 4.28%** (implied ERP, trailing-12-mo adjusted payout, Aug 1 2026) [Damodaran][5].
- **Beta:** raw 5-year beta 2.63 [StockAnalysis][6]. A raw CAPM cost of equity = 4.74% + 2.63×4.28% = **16.0%**. For valuation I use a **forward/adjusted beta of ~1.70** — reflecting Damodaran's mean-reversion of betas and the de-risking that profitability, Iridium's recurring revenue, and product diversification should bring. This yields cost of equity = 4.74% + 1.70×4.28% = **~12.0%**. (Using the full 2.63 would push WACC to ~16% and make the stock _more_ overvalued — so 12% is the lenient, conservative choice.)
- No country-risk premium (US-listed, US-centric revenue); no arbitrary company-specific premium (captured via scenario WACC adjustments).

### Cost of Debt

- Pre-tax: **~5.0%** (convertible notes 4.25–5.0% effective; equipment financing ~10% but negligible) [SEC 10-K][2].
- Tax rate 21% → **after-tax cost of debt ≈ 3.95%** — but debt is a tiny weight.

### Capital Structure (market values)

- Equity: ~$48.0B (99.7%) · Debt: ~$0.13B (0.3%). Net cash means the WACC ≈ cost of equity ≈ **12.0%** (used). Post-Iridium, if the company levered to a ~15% debt weight, WACC would fall modestly — a tailwind I do not credit in the base case.

### WACC

**WACC ≈ 12.0%** (used; scenario adjustments: 15.0% Severe Bear → 10.5% Extreme Bull). Cross-check: StockAnalysis computes WACC 18.68% [fact pack][6] — mine is deliberately lower (lenient), which makes the overvaluation conclusion conservative.

**ROIC (−5.5%) vs WACC (12%):** growth is currently **value-destroying** — this is the crux. Rocket Lab creates value only if incremental ROIC eventually clears 12%, which the model assumes happens (initial 10% → terminal 18%) but only after years of burn.

---

# 9. Intrinsic Valuation — Primary Analysis (FCFF DCF)

**Model:** Two-stage FCFF DCF, 10-year explicit period, Gordon terminal value, g/ROIC-consistent reinvestment, WACC = scenario-adjusted cost of capital. Cash flows are NOPAT × (1 − g/ROIC). This is the exact structure of the official workbook (`RKLB_Damodaran_Financial_Model.xlsx`), so the numbers below reproduce it.

### Base-Year Normalization (Y0 = FY2026 run-rate)

- Revenue: $951M (FY2026 consensus — between TTM $769M and the annualized Q3'26 guide ~$1.0B)
- EBIT margin (Y1): 5.0% → NOPAT margin ~3.95% (after 21% tax)
- Tax rate: 21% · ROIC: initial 10% → terminal 18%
- Reinvestment: via g/ROIC (at 45% growth / 18% ROIC → ~250% of NOPAT in Y1 — the company reinvests more than it earns)
- Terminal growth 3% < WACC 12%

### 10-Year Base-Case Forecast ($M) — matches workbook DCF-Base

| Year | Revenue | Growth | EBIT Margin | EBIT  | NOPAT | Reinvest. | FCFF  | PV @12% |
| ---- | ------- | ------ | ----------- | ----- | ----- | --------- | ----- | ------- |
| 1    | 1,379   | 45.0%  | 5.0%        | 69    | 54    | 136       | −82   | −73     |
| 2    | 1,937   | 40.5%  | 6.9%        | 134   | 106   | 238       | −132  | −105    |
| 3    | 2,635   | 36.0%  | 8.8%        | 232   | 183   | 366       | −183  | −130    |
| 4    | 3,465   | 31.5%  | 10.7%       | 371   | 293   | 513       | −220  | −140    |
| 5    | 4,400   | 27.0%  | 12.6%       | 554   | 438   | 657       | −219  | −124    |
| 6    | 5,391   | 22.5%  | 14.5%       | 782   | 617   | 772       | −154  | −78     |
| 7    | 6,361   | 18.0%  | 16.4%       | 1,043 | 824   | 824       | −0    | −0      |
| 8    | 7,220   | 13.5%  | 18.3%       | 1,321 | 1,044 | 783       | 261   | 105     |
| 9    | 7,869   | 9.0%   | 20.2%       | 1,590 | 1,256 | 628       | 628   | 226     |
| 10   | 8,223   | 4.5%   | 22.0%       | 1,809 | 1,429 | 357       | 1,072 | 345     |

**Key assumptions:** Revenue compounds ~24% a year to **$8.2B by 2036** (~8.6× today) — Electron cadence, Neutron 1-3-5 ramp at $50–55M ASP, Iridium >$870M recurring, space systems compounding. Margins ramp 5% → 22% EBIT as R&D normalizes (Neutron amortized) and Iridium's high-margin recurring revenue consolidates — a 22% terminal EBIT margin is generous (SpaceX's own disclosed 2025 adjusted EBITDA margin is ~35% on $18.7B, but on far larger scale). **Reinvestment consumes 100%+ of NOPAT for the first six years** — FCFF is negative through Year 6, only turning positive at Year 7, which is why almost all value sits in the terminal.

### Terminal Value & Equity Value (Base)

- Terminal FCFF = NOPAT₁₀ × (1+g) × (1 − g/ROIC_term) = 1,429 × 1.03 × (1 − 0.03/0.18) = **$1,227M**
- **Terminal value = $1,227M / (12% − 3%) = $13,631M** → PV = **$4,389M**
- **PV of explicit FCFF = $26M** (negative years 1–6 roughly cancel positive years 7–10)
- **Enterprise value = $4,415M**
- Add net cash $2,168M (cash $2,302M − debt $134M) → **Equity value = $6,583M**
- **Intrinsic value = $6,583M / 598.46M shares = $11.00/share**
- **Terminal value / EV = 99%** — an extreme concentration of value in the terminal, highlighting how assumption-sensitive this is (§10, §18).

---

# 10. Terminal Value

- **Stable growth = 3.0%** (< WACC in every scenario; enforced by the workbook checks). Below long-run nominal GDP (~4%) — appropriate for a mature aerospace leader.
- Stable margin: 22% EBIT — generous vs the aerospace norm (SpaceX ~35% adj-EBITDA margin is the exception; launch primes run 10–20%).
- Stable ROIC: 18% > WACC 12% — the terminal state assumes Rocket Lab keeps a durable excess return (moat survives).
- Terminal reinvestment rate = g/ROIC = 3%/18% = 17% — internally consistent.
- **What does TV assume about 2036?** That Rocket Lab is an ~$8.2B-revenue, 22%-EBIT-margin, stable-growth space titan — Iridium's successor constellation in service, Neutron a mature workhorse, space systems a global leader — **but still less than half of SpaceX's 2025 revenue scale**. That is a fair, non-heroic central assumption for a "good execution" base case.
- **TV/EV = 99%** — the largest single value component and therefore the most assumption-sensitive; this alone caps confidence in the base case (Low-to-Medium).

---

# 11. Relative Valuation

| Metric           | **RKLB** | ASTS  | LUNR (Intuitive) | RDW (Redwire) | Read                                  |
| ---------------- | -------- | ----- | ---------------- | ------------- | ------------------------------------- |
| Revenue (TTM)    | $769M    | $115M | $490M            | $426M         | RKLB is the largest of the group      |
| Revenue growth   | +52%     | n/m   | high             | ~27% (3-yr)   | RKLB fastest at scale                 |
| Gross margin     | 37.3%    | 38.9% | 16.4%            | 22.7%         | RKLB ≈ ASTS, far above LUNR/RDW       |
| Operating margin | −27.6%   | −410% | −32.7%           | −39.5%        | All pre-profit; RKLB least bad        |
| P/S (TTM)        | **62.4** | 239.6 | 8.9              | 7.9           | **2nd-most expensive**                |
| EV/Sales         | **59.5** | 245.7 | 9.1              | 6.8           | Massive premium vs launch/space peers |
| Beta (5-yr)      | 2.63     | 2.74  | 1.83             | 3.07          | High-beta across the group            |
| ROIC (TTM)       | −5.5%    | −8.4% | −16.4%           | −7.0%         | RKLB least-bad                        |

[StockAnalysis][6][7][8][9]; fact pack.

**Why do the multiples differ?** RKLB trades at a premium to every _operating_ space company (LUNR 8.9×, RDW 7.9× sales) and is only cheaper than ASTS — a pre-revenue satellite-communications story at 240× sales. The market is paying for Rocket Lab's _narrative_: the only vertically-integrated, self-launching launch+satellite company with real revenue, real backlog, a rocket about to fly, and an Iridium deal that would add recurring revenue. On a **fundamental-multiple basis** (growth × margin × ROIC vs risk), a justified EV/Sales for a high-growth but pre-profit, capital-hungry space company is ~8–15× — implying ~$6–12B EV — consistent with my DCF range ($4.4B base EV) and a fraction of the $45.8B market EV. **RKLB is priced like a quasi-ASTS "story stock" but with 6.7× the revenue — and neither price is supported by the cash-flow math.**

---

# 12. Reverse DCF — What Does the Market Price Assume?

**Starting price:** $80.25 → equity value $48.0B + net cash $2.17B = **implied EV $45.9B** (matches the ~$45.8B market EV).

Using the same DCF structure (WACC 12%, terminal g 3%, terminal ROIC 18%), the terminal-value identity EV = Rev × Margin × 7.315 means the market's $45.9B EV requires:

1. **Terminal revenue ~$25.1B at 25% EBIT margin, or ~$28.5B at 22% margin, or ~$20.9B at 30% margin.** Even at a heroic 25% terminal margin, that is **~26× today's revenue** — a company _larger than SpaceX's entire FY2025 revenue of $18.7B_ [SpaceX][10]. My base case reaches only $8.2B.
2. **The reverse-DCF grid** (workbook) shows: $20B revenue at 25% margin → $36.6B EV; $24B at 25% → $43.9B; $28B at 20% → $41.0B. Only the top-right corner (large revenue AND high margin) gets near the $45.9B implied EV.
3. **Implied WACC:** even at an unsustainably low 8.5% cost of capital with my base fundamentals, value is only ~$15–17/share — **no plausible discount rate justifies $80.25 with base-case fundamentals.**
4. **At WACC 12% and a 22% terminal margin, $80.25 requires ~$28.5B terminal revenue** — a "second SpaceX" outcome that even my **Extreme Bull scenario ($32B revenue → $50.22/share) does not fully justify**, because the early-year cash burn and high discount rate consume most of the value.

> **"At today's price of $80.25, the market is implicitly assuming Rocket Lab grows to ~$25–30 billion of terminal revenue — larger than SpaceX's entire current revenue — at 22–25% operating margins, a decade out, after funding years of cash burn and dilution at a cost of capital far below what a 2.63-beta, launch-failure-exposed, equity-hungry business warrants."**

These assumptions are **aggressive to implausible.** The market is not pricing the base case; it is pricing a sustained Extreme-Bull outcome (which my own Extreme Bull only values at $50).

---

# 13. Scenario Valuation

Five scenarios (probabilities sum to 1.0; terminal growth < WACC in every scenario; values from the official workbook model). WACC/margin/growth adjustments as in `RKLB_model_inputs.json`.

| Scenario                                                                                                      | Prob | Y1 Growth | Terminal EBIT mgn | WACC  | Term. g | **Value/share** | vs $80.25 |
| ------------------------------------------------------------------------------------------------------------- | ---- | --------- | ----------------- | ----- | ------- | --------------- | --------- |
| **Severe Bear** — Neutron fails/delays, Iridium deal collapses, space downturn, margins compress, risk spikes | 10%  | 20%       | 18%               | 15.0% | 2.0%    | **$4.91**       | −94%      |
| **Bear** — Neutron delayed, Iridium integration drags, slower growth & weaker margins, higher risk            | 20%  | 30%       | 20%               | 14.0% | 2.5%    | **$5.94**       | −93%      |
| **Base** — Execution + Neutron + Iridium compound ~24% CAGR to ~$8B rev; 22% margins; returns clear WACC      | 35%  | 45%       | 22%               | 12.0% | 3.0%    | **$11.00**      | −86%      |
| **Bull** — Neutron scales 1-3-5, Iridium accretive, space systems global leader; 25% margins                  | 25%  | 55%       | 25%               | 11.0% | 3.5%    | **$25.09**      | −69%      |
| **Extreme Bull** — "Second-SpaceX" outcome; ~$32B revenue; sustained excess returns                           | 10%  | 63%       | 27%               | 10.5% | 3.75%   | **$50.22**      | −37%      |

- **Probability-weighted intrinsic value = 0.10×4.91 + 0.20×5.94 + 0.35×11.00 + 0.25×25.09 + 0.10×50.22 = $16.82**
- **Expected upside/downside vs $80.25 = −79.04%**
- **Even the Extreme Bull case ($50.22) is 37% below the current price** — the market is paying above my best-case scenario. Only an outcome beyond "second SpaceX" makes new buyers whole.

---

# 14. Sensitivity Analysis

**WACC × Terminal Growth (base-case share value):**

| WACC \ g  | 2.0%       | 2.5%       | 3.0%       | 3.5%       | 4.0%       |
| --------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| 10.0%     | $13.55     | $14.20     | $14.96     | $15.83     | $16.84     |
| 11.0%     | $11.69     | $12.16     | $12.69     | $13.29     | $13.98     |
| **12.0%** | **$10.27** | **$10.61** | **$11.00** | **$11.43** | **$11.92** |
| 13.0%     | $9.16      | $9.42      | $9.71      | $10.02     | $10.38     |
| 14.0%     | $8.27      | $8.48      | $8.69      | $8.93      | $9.20      |

**Terminal EBIT Margin × Mature Revenue (terminal EV, $B):**

| Margin \ Rev | 6B   | 8B   | 10B  | 12B  | 14B  | 16B  |
| ------------ | ---- | ---- | ---- | ---- | ---- | ---- |
| 10%          | 4.4  | 5.9  | 7.3  | 8.8  | 10.2 | 11.7 |
| 15%          | 6.6  | 8.8  | 11.0 | 13.2 | 15.4 | 17.6 |
| 20%          | 8.8  | 11.7 | 14.6 | 17.6 | 20.5 | 23.4 |
| 25%          | 11.0 | 14.6 | 18.3 | 21.9 | 25.6 | 29.3 |
| 30%          | 13.2 | 17.6 | 21.9 | 26.3 | 30.7 | 35.1 |

**Key findings:**

- **Base value is $8.27–$16.84 across a deliberately wide and generous WACC (10–14%) × terminal-growth (2–4%) space** — even the top-left corner (10% WACC, 4% g) is ~79% below the current price.
- **Discount rate is the dominant lever:** every +100bps of WACC ≈ −$1.2–1.6/share on the base.
- **Terminal revenue scale is the real driver of the gap:** even at 20% margins, reaching $14B revenue (the upper end of plausible "great outcome") is worth only ~$20.5B EV — about $34/share gross — versus the $45.9B the market pays.
- **Valuation-critical assumptions (ranked):** (1) terminal revenue scale / growth duration, (2) WACC, (3) terminal EBIT margin. Reinvestment/ROIC matters but is second-order given the terminal-dominated structure.

---

# 15. Market Expectations vs Fundamental Reality

- **A. Market price:** $80.25 = 62.4× TTM sales, 41.9× forward sales, ~35× FY2027 revenue, and an EV/Sales of 59.5× — the second-most-expensive space stock by revenue multiple.
- **B. Market-implied fundamentals (reverse DCF):** ~$25–30B terminal revenue at 22–25% margins (a company larger than SpaceX's $18.7B), sustained for a decade, at a sub-8.5% discount rate — or some combination thereof.
- **C. My fundamental forecast:** ~45% Y1 growth decaying to ~4%, 5% → 22% margins, ROIC 10% → 18%, WACC 12%, terminal g 3% → **$11.00 base**, **$16.82 weighted**.

**Price ($80.25) >> Value (weighted $16.82) — the market is dramatically more optimistic than reasonable fundamentals support.** The market's error is treating Rocket Lab's excellent _operational_ story (record backlog, Neutron, Iridium) as if the cash flows will arrive quickly enough and at enough scale to justify the multiple, while ignoring (a) the ~6 years of continued cash burn, (b) the ~12% cost of capital a 2.63-beta, equity-hungry business demands, and (c) the relentless dilution. The market is also paying a premium that even the most favorable reasonable inputs (WACC 10%, g 4%) cannot support (~$17).

---

# 16. Real Options & Optionality

- **Neutron (medium-lift):** the largest real option — a successful Neutron unlocks constellation-scale launch ($50–55M ASP, 1-3-5 cadence) and self-launch for Iridium. **But** its value is already embedded in the Bull/Extreme-Bull scenarios and partially priced by the market; the market pays for it as if it were certain.
- **Iridium (recurring satellite services):** a genuine strategic option — converts Rocket Lab from project-based to recurring-revenue, adds spectrum (L-band) and a defensible subscription base. Priced-in as near-certainty at these levels; the 10-Q's own 5 HIGH risk factors say otherwise [SEC 10-Q][1].
- **Space applications / constellation management:** a long-dated, unquantifiable option on the largest layer of the space economy.
- **Abandonment/flexibility:** the business could be broken up (launch, space systems, Iridium are separable) but there is no indication management would monetize.
- **Verdict:** Optionality is real but **already paid for** — the market's $45.9B EV _is_ the option value being charged upfront. I do not add an optionality premium, because doing so would double-count what the reverse DCF already shows is priced in.

---

# 17. Special Valuation Situations

- **Young/high-growth, pre-profit, negative-FCF company:** Yes — this is why a scenario-weighted fundamentals-driven DCF (rather than a multiple) is the right framework, and why confidence is Low-to-Medium rather than High.
- **Heavy reinvestment + dilution:** modeled via g/ROIC reinvestment (growth consumes NOPAT) and a conservative (unchanged) share count; the 141.8M-share overhang and ATM cadence would lower per-share value further — I am being generous.
- **Upcoming transformative M&A (Iridium):** handled through scenarios (base assumes it closes mid-2027 and contributes to the revenue path; bear scenarios assume it falters or burdens the balance sheet). The $3.6B bridge and post-deal leverage are captured in the risk framing, not as a base-case balance-sheet benefit.
- **Not** distressed, financial, commodity, or conglomerate. A standard two-stage FCFF DCF with scenario weighting is appropriate. No model switch required.

---

# 18. Valuation Error & Uncertainty

- **Estimation uncertainty (inputs):** extreme — margins (5% → 22%), growth duration, terminal revenue ($8.2B base vs $25B+ market-implied), and ROIC path are all judgment calls with wide bands. The model's terminal-dominated structure (TV/EV 99%) amplifies every terminal input.
- **Economic uncertainty (business can change):** very high — Neutron first flight, Iridium close/integration, government funding, launch-failure tail, competition.
- **Information uncertainty:** moderate — filings are timely and audited, but Iridium terms are still being finalized (S-4, FCC), and Neutron economics are unproven.
- **Model uncertainty:** moderate — g/ROIC reinvestment is the correct Damodaran structure, but it treats all reinvestment as return-seeking capital; R&D is expensed (not capitalized), which the model handles via margins but means the "reinvestment" proxy is imperfect.
- **Robustness:** base value stays $8–$17 across a deliberately wide WACC/g grid, and $4.91–$50.22 across scenarios. **The conclusion — price far above value — is robust:** even the most favorable reasonable input set (WACC 10%, g 4%) yields ~$17, still ~79% below the price. What is NOT robust is the _exact_ value: this is a Low-to-Medium-confidence point estimate inside a high-confidence overvaluation.

**Valuation confidence: LOW-TO-MEDIUM** (direction high-confidence; magnitude wide error band).

---

# 19. Inversion: What Would Make This Investment Fail?

Work backward from permanent capital loss at $80.25 (the stock already fell ~75% from $151 to $37.57 within 52 weeks):

1. **Neutron fails or slips years.** If first flight slips beyond 2027 or fails, the medium-lift engine stalls, Iridium's launch rationale is weakened, R&D keeps burning, and the 62× sales multiple de-rates toward the 10–15× of an Electron-only small-lift business. That alone produces my Severe-Bear (~$5) outcome.
2. **Iridium deal fails or burdens the balance sheet.** $8B is ~17% of Rocket Lab's market cap; a failed close (regulatory/HSR/stockholder) or a post-close integration failure plus ~$3.6B bridge debt turns a net-cash company into a leveraged one, with goodwill risk on top.
3. **The dilution treadmill continues.** Every ATM raise funds the burn but dilutes per-share value; at +15.7% share growth and 141.8M reserved shares, per-share value growth lags revenue growth badly. Shareholders effectively pay for the dream twice (price + dilution).
4. **Government funding contraction.** US government-related revenue ~47% and 77% of backlog concentrated in top-5 customers; a prolonged shutdown or DOGE-style cuts directly hit awards and payments (already visible in the Oct 2025 shutdown and the GEOST earnout markdown).
5. **A launch failure at the wrong moment** — grounds the fleet, hits backlog conversion, and re-rates the reliability premium.

**The three assumptions whose failure most damages the thesis:** (1) sustained ~24%+ CAGR to $8B+ revenue, (2) margin ramp to 22% EBIT as R&D normalizes, (3) successful Iridium close without value-destroying leverage/integration. All three are binary-event-laden and outside management's full control.

---

# 20. Probability-Weighted Investment Case

| Scenario     | Prob | Value/Share | Return vs $80.25 | Key Assumptions                                         |
| ------------ | ---- | ----------- | ---------------- | ------------------------------------------------------- |
| Severe Bear  | 10%  | $4.91       | −94%             | Neutron fails/Iridium collapses; margins ~18%; WACC 15% |
| Bear         | 20%  | $5.94       | −93%             | Neutron delayed; Iridium drags; margins ~20%; WACC 14%  |
| Base         | 35%  | $11.00      | −86%             | Execution + Iridium; ~$8B rev; 22% margins; WACC 12%    |
| Bull         | 25%  | $25.09      | −69%             | Neutron 1-3-5; Iridium accretive; 25% margins; WACC 11% |
| Extreme Bull | 10%  | $50.22      | −37%             | "Second SpaceX"; ~$32B rev; 27% margins; WACC 10.5%     |

- **Probability-weighted intrinsic value: ≈$16.82** (expected return **−79.04%** from $80.25)
- **Expected annualized return (5-yr): ≈ −26.84%**
- Downside risk: a 30% combined probability of −93% outcomes (Severe Bear/Bear); upside: 35% combined probability of −69% to −37% outcomes (Bull/Extreme Bull). **The payoff is symmetrically bad: even the best case loses money from today's price.**
- **Asymmetry: fundamentally unfavorable.** The expected value is ~79% below the price; there is no scenario at $80.25 that compensates a new buyer for the risk. The stock becomes a fair-to-attractive proposition only below ~$25–30 (where base+weighted value ≈ price with a margin), and compelling below ~$20.

---

# 21. Investment Decision

### Valuation Rating

**D — AVOID / SIGNIFICANTLY OVERVALUED.**

The price ($80.25) embeds expectations (~$25–30B terminal revenue at 22–25% margins — larger than SpaceX's entire revenue; or a sub-8.5% discount rate; or a decade of ~50% compounding) that are materially more optimistic than reasonable fundamentals (~$8.2B terminal revenue, 22% margin, 12% WACC). The risk/reward is poor: probability-weighted value is −79% below price, expected annualized return is negative, and **even my Extreme-Bull case ($50) is below the market price**. This is not a "good company, buy it" situation — it is a genuinely great company whose share price already capitalizes the most favorable scenario, with dilution and binary execution risk stacked on top. The opportunity is at the price, not the company.

### Final Outputs

**Current Price:** $80.25
**Severe Bear Value:** $4.91
**Bear (Conservative) Value:** $5.94
**Base Intrinsic Value:** $11.00
**Bull Value:** $25.09
**Extreme Bull Value:** $50.22
**Probability-Weighted Value:** $16.82
**Expected Upside/Downside:** −79.04%
**Expected Annualized Return (5-yr):** −26.84%
**Margin of Safety at $80.25:** None (negative ~79%)
**Buy zone:** First tranche ≤ $30 · accumulate $22–30 · conviction < $20
**Valuation Confidence:** Low-to-Medium
**Investment Rating:** **D — Avoid / Significantly Overvalued**

---

# 22. The Five Most Important Conclusions

1. **The Business:** Rocket Lab is one of the best real assets in the private-and-public space economy — the #2-most-launched orbital rocket, a vertically integrated design-build-launch-operate stack, record backlog, a medium-lift Neutron close to first flight, and a pending Iridium acquisition that would add >$870M of recurring revenue. The quality and momentum are genuine.
2. **The Economics:** The decisive driver of long-term value is whether Rocket Lab can turn its excellent top-line story into cash — ROIC must clear a ~12% cost of capital. Today ROIC is ~−5%, and the g/ROIC mechanics force it to reinvest 100%+ of NOPAT for ~6 years; value exists only in a far-off, heavily discounted terminal state. **This is a story stock in the cash-flow sense, whatever its operational brilliance.**
3. **The Market's Expectations:** At $80.25 (62× sales, 59.5× EV/Sales), the market implicitly prices ~$25–30B terminal revenue at 22–25% margins — a company larger than SpaceX's current $18.7B. That is beyond my Extreme-Bull scenario, which is worth only ~$50.
4. **The Valuation:** The most defensible estimate is a probability-weighted intrinsic value of **~$16.82/share** (base ~$11.00, range $4.91–$50.22), from a scenario-weighted 10-year FCFF DCF at a ~12% WACC. The estimate is robust in direction: even the most favorable reasonable input set (WACC 10%, g 4%) yields only ~$17.
5. **The Investment Decision:** At $80.25 the expected return is negative (−79% to probability-weighted value; −27% annualized), and no plausible scenario compensates a new buyer. **Avoid at current levels; the stock becomes interesting only below ~$30 and compelling below ~$20.**

---

# 23. Damodaran-Style Final Judgment

> **"At a price of $80.25, the market is effectively assuming Rocket Lab grows to ~$25–30 billion of terminal revenue — a company larger than SpaceX's entire 2025 revenue of $18.7 billion — at 22–25% operating margins, a decade out, while funding years of cash burn and relentless dilution at a discount rate far below what a 2.63-beta, launch-failure-exposed, equity-hungry business warrants. My valuation implies ~$16.82 (weighted; ~$11 base) because I expect growth to converge toward ~4% after a brilliant decade that takes revenue to only ~$8 billion, margins to rise to ~22% as R&D normalizes, and the cost of capital to be ~12%, not 7%. The biggest risk to this valuation is that I am too bearish on Rocket Lab's terminal scale — that Neutron and Iridium genuinely make it a tier-1, multi-billion-revenue, self-launching space power that keeps compounding well past $8 billion — a real, if ~10%-probability, outcome that my Extreme Bull only values at ~$50. Therefore, at today's price, I would avoid the stock because the market has already paid for the Bull and Extreme-Bull cases, leaving a negative expected return and no margin of safety. The opportunity is at the price, not the company: wait for ~$30, get interested below ~$20."**

---

## Sources

1. SEC Form 10-Q Q2 FY2026 (Rocket Lab Corp, CIK 0001819994, filed 2026-08-10, acc. 0001819994-26-000062): https://www.sec.gov/Archives/edgar/data/1819994/000181999426000062/rklb-20260630.htm — Q2'26 financials, backlog $2.36B, Iridium $8.0B EV/$3.6B bridge, Neutron Q4'26, 5 HIGH risk factors.
2. SEC Form 10-K FY2025 (filed 2026-02-26, acc. 0001819994-26-000013): https://www.sec.gov/Archives/edgar/data/1819994/000181999426000013/rklb-20251231.htm — FY25 P&L/cash flows, R&D $270.7M, capex $156.3M, SBC $71.1M, backlog, segment economics, customer concentration, funding.
3. SEC DEF 14A 2026 (filed 2026-04-06, acc. 0001628280-26-023922): https://www.sec.gov/Archives/edgar/data/1819994/000162828026023922/rklb-20260406.htm — NEO comp (Beck $6.83M), pay ratio 88:1, Say-on-Pay ~80%, Series A preferred exchange, 141.8M shares reserved for equity plans.
4. SEC EDGAR company index, Rocket Lab Corp (CIK 0001819994, formerly 0001849874 "Rocket Lab USA, Inc."): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001819994 — filing index; also Rocket Lab IR https://investors.rocketlabcorp.com.
5. Damodaran — implied equity risk premium (Aug 1, 2026 = 4.28%; US 10-yr risk-free 4.74%): https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/implpr.html and https://pages.stern.nyu.edu/~adamodar/.
6. StockAnalysis RKLB statistics/market data (beta 2.63, PS 62.4, EV/S 59.5, WACC 18.68%, shares, price): https://stockanalysis.com/stocks/rklb/statistics/ (per shared fact pack).
7. StockAnalysis Redwire (RDW) statistics (mcap $3.38B, PS 7.9, EV/S 6.8, beta 3.07, rev $426M): https://stockanalysis.com/stocks/rdw/statistics/.
8. StockAnalysis Intuitive Machines (LUNR) statistics (mcap $4.35B, PS 8.9, EV/S 9.1, beta 1.83, rev $490M): https://stockanalysis.com/stocks/lunr/statistics/.
9. StockAnalysis AST SpaceMobile (ASTS) statistics (mcap $27.6B, PS 239.6, EV/S 245.7, beta 2.74, rev $115M): https://stockanalysis.com/stocks/asts/statistics/.
10. SpaceX FY2025 financials (S-1 filed May 2026): revenue $18.674B (+33%), Starlink $11.4B, adj EBITDA ~$6.6B — https://spacexchart.com/financials and https://stockanalysis.com/stocks/spcx/revenue/.
11. EarningsLens RKLB Q2 FY2026 10-Q analysis (segment gross margins, Iridium terms, backlog split, MD&A): https://www.earningslens.ai/report/rklb/2026-Q2.
12. Rocket Lab Q2 2026 earnings release coverage (record revenue $234M, record backlog, Q3 guide $250–265M): https://markets.businessinsider.com/news/stocks/rocket-lab-announces-second-quarter-2026-financial-results-posts-record-revenue-and-record-backlog-guides-to-another-record-revenue-quarter-in-q3-2026-1036437907.
13. StockAnalysis RKLB Q2 2026 earnings-call transcript (guidance, headcount 3,217, ATM raise, Neutron/Iridium cadence): https://stockanalysis.com/stocks/rklb/transcripts/662835-q2-2026/ (per shared fact pack).

_Every figure above traces to a cited source or is explicitly labeled an estimate (notably: forward-adjusted beta 1.70, normalized Y1 EBIT margin 5%, terminal EBIT margin 22%, ROIC path 10%→18%, terminal revenue $8.2B base, scenario probabilities, and all scenario IVs). FY2026 revenue run-rate $951M is the analyst consensus (fact pack); Q2'26 figures ($234.1M, GM 36.1%, op margin −24.6%, backlog $2,355.9M, Iridium $8.0B EV) are from the 10-Q [1][11]._

---

## Position Summary

- Rating: **D — Avoid / Significantly Overvalued** — a genuinely excellent space company whose $80.25 price embeds a "second SpaceX" outcome that the cash-flow math does not support.
- Intrinsic value: bear=$5.94 base=$11.00 bull=$25.09 | weighted=$16.82 (Severe Bear $4.91 / Extreme Bull $50.22)
- Buy zone: ≤$30 (first tranche), $22–30 (accumulate), <$20 (conviction) | Sell/reduce zone: ≥$50 (trim), ≥$80 (avoid/do-not-initiate)
- Key metrics: TTM rev $769M (+52%), GM 37.3%, EBIT margin −27.6%, net loss −$165M TTM, OCF −$222M / FCF −$371M TTM, SBC $81.6M (~10.6% rev), net cash ~$2.25B, backlog $2.36B, beta 2.63, shares 598.5M (+15.7% YoY), 141.8M shares reserved for future issuance [SEC][1][2][3]
- Top risks: (1) Neutron first-flight failure/delay; (2) Iridium $8.0B deal close/integration + ~$3.6B bridge leverage; (3) dilution treadmill (ATM raises, +15.7% share growth); (4) US government funding contraction (47% of revenue, 77% of backlog in top-5); (5) launch-failure tail risk re-rating the reliability premium.
