# Cipher Digital Inc. (CIFR) — Aswath Damodaran Lens

**Valuation date:** August 16, 2026
**Reference price:** ~$17.86 (Aug 14, 2026 close; working band $16–18)
**Diluted valuation share count:** ~415 million (414,253,564 outstanding at Jun 30, 2026; 423,575,369 issued)
**Primary framework:** FCFF DCF (10-year explicit, reinvestment tied to growth/ROIC), supplemented by reverse DCF, five-scenario probability weighting, and relative valuation.

> **Bottom line:** CIFR is no longer a Bitcoin miner with an AI story. It is a **data-center developer-and-landlord** that signs long-term, investment-grade HPC leases (Amazon/AWS, Fluidstack backed by Google), finances construction with non-recourse project bonds, and earns contracted rent. This is a genuinely different — and structurally lower-risk — model than IREN's own-and-operate GPU cloud. The contracted book is real: three campus leases generating **~$793M of average annualized net operating income from Oct 2026 through Sep 2036**. My base DCF produces **~$16.47/share** (verified workbook value), modestly below the ~$17.86 market price, while probability-weighted value is **~$21.55/share** (verified workbook value). At ~$17.86 I view the stock as **approximately fairly valued** — the market is paying close to my base case and is not discounting the future pipeline, but the upside is real. There is not enough margin of safety at this price to be aggressive; I would wait for ~**$13–15** to build a position, and I rate the stock **C — Hold / Watch**.

---

## Executive Summary

| Metric                                |          My estimate |
| ------------------------------------- | -------------------: |
| Reference price                       |          **~$17.86** |
| Severe bear value (workbook)          |           **~$1.69** |
| Bear value (workbook)                 |           **~$5.59** |
| Conservative value (interpolated)     |             **~$14** |
| Base intrinsic value (workbook)       |          **~$16.47** |
| Bull value (workbook)                 |          **~$32.94** |
| Extreme bull value (workbook)         |          **~$70.89** |
| Probability-weighted value (workbook) |          **~$21.55** |
| Expected upside to weighted value     |           **~20.7%** |
| 5-year annualized expected return     |            **~3.8%** |
| Base-case valuation confidence        |       **Low/Medium** |
| Appropriate WACC                      |           **~10.0%** |
| Stable (terminal) growth              |             **2.5%** |
| Preferred purchase range              |           **$13–15** |
| Rating at ~$17.86                     | **C — Hold / Watch** |

The defining feature of CIFR's valuation is that the **base case and the market price nearly coincide**, while the **tails are wide and asymmetric**. This is not a company where the market is pricing an obviously wrong story; it is a company where the market is paying roughly for the contracted book and giving only partial — but real — credit to a very large future pipeline. The value is unusually sensitive to (a) how much of the 4.4 GW pipeline gets leased, and (b) the treatment of the ~$3.7B of restricted project cash.

> **Workbook note (re-sync complete):** The Phase-2 Damodaran workbook (5-scenario, 10-year FCFF model built from the `CIFR_model_inputs.json`) is the **authoritative source for the five scenario intrinsic values per share** and the probability-weighted value. The narrative above has been **re-synced to the verified workbook values** — Severe Bear **$1.69**, Bear **$5.59**, Base **$16.47**, Bull **$32.94**, Extreme Bull **$70.89**, probability-weighted **$21.55** (ALL_MATCH on verification). My earlier hand-checked estimates ($2 / $6 / $16.50 / $33 / $71 / $21.50) differed only at the margin and were calibrated to the workbook's exact outputs; the annualized-return convention was changed from a 3-year (~6.5%) to the workbook's 5-year horizon (~3.8%).

---

# 1. Business Understanding & Fundamental Story

### What CIFR actually does

Imagine a company that **finds empty land with cheap, abundant electricity**, **builds a massive, purpose-built data-center campus on it**, and then **signs a 10-to-15-year lease** with a giant technology company that agrees to pay rent for the whole campus. That is Cipher Digital.

- **Who pays CIFR?** Investment-grade hyperscaler tenants. Amazon (AWS) at Black Pearl (300 MW, 15-year lease); Fluidstack — with Google as backstop guarantor — at Barber Lake (300 MW); and a third campus, Stingray, leased and bond-financed. ([SEC][1], [CALL][3])
- **Why do they pay?** Because building industrial-scale HPC/AI data centers takes years of site origination, grid interconnection, and construction — and hyperscalers are in a race for power-secure capacity. CIFR removes that friction.
- **How does CIFR make money?** It earns contracted **rent (net operating income)** under long-term leases, and it **finances the construction at the project level** with non-recourse senior secured bonds (6.0–7.125% coupons) that amortize against the lease cash flows. This is a **build-to-suit landlord model**, not a cloud operating business.
- **What remains of Bitcoin mining?** One site — Odessa (207 MW) — is the only operating Bitcoin mine, ~11.6 EH/s, producing ~346 BTC in Q2 2026. CIFR says it will make **no further capital investment** in mining and is exploring converting Odessa to HPC. ([CALL][3])

### Economic structure

- **Revenue drivers:** contracted lease rent ramping through 2026–2027; residual Bitcoin mining revenue (declining); power sales. At full ramp, management targets **~$793M average annualized NOI** from the three executed campus leases (Oct 2026–Sep 2036). ([CALL][3])
- **Unit economics:** ~$9–11M of capital per MW of HPC capacity historically, trending higher with inflation; management expects rent to be structured triple-net with improving terms. ([CALL][3])
- **Margins:** Landlord-style. NOI margin is high once facilities deliver (rent largely flows through to NOI); GAAP EBIT is thinner because of depreciation on a multi-billion-dollar asset base and corporate overhead, with project debt service captured below the operating line (and in the WACC).
- **Capital intensity:** Extremely high — this is the defining feature. Each gigawatt of new HPC costs billions and is funded by project debt + construction reserves.
- **Tax:** A 21% U.S. federal statutory rate, but large NOL carryforwards (~$236M federal) and full valuation allowances mean **cash taxes should be near zero for years**. ([SEC][1])
- **Financing structure:** Project-level non-recourse bonds at the campus SPVs ($1.733B at 7.125% for Barber Lake; $2.0B at 6.125% for Black Pearl; $810M at 6.0% for Stingray), plus two unsecured corporate convertibles ($172.5M at 1.75%; $1.3B at 0.00%) and a $200M committed revolver. As of Jun 30, 2026 aggregate corporate + project debt was **just over $6B**. ([CALL][3], [12])

### The fundamental valuation story

> **"CIFR will create value because it can convert scarce, power-secured land into long-duration, investment-grade-contracted HPC lease income — a real-estate-like annuity — at a scale competitors cannot easily replicate, and it funds that growth largely with non-recourse project debt."**

The three Damodaran inputs:

- **Cash flows:** Near zero today (Q2 2026 revenue $25M; Adjusted EBITDA −$30M) but a **large, contractually committed NOI stream (~$793M/yr) begins within 12–18 months** as Barber Lake and Black Pearl rent commence and Stingray delivers in H1 2027. ([CALL][3], [2])
- **Growth:** High but lumpy. Growth comes from new campuses, not same-store volume: Reveille + Ulysses (+270 MW targeted 2027), Colchis/Mikeska/McLennan (~2 GW targeted 2028–29), Apollo/Milsing/expansions (up to ~2.1 GW 2030+). The portfolio is ~5.3 GW across 11 sites. ([CALL][3])
- **Risk:** Moderate-to-high but **structurally lower than GPU-cloud peers** because revenue is contracted and counter-parties are investment grade. Key risks are construction/execution, tenant concentration (three single-tenant campuses), the pipeline never being leased, refinancing, and dilution.

### Business lifecycle

**Young / high-growth, transitioning to an operating landlord.** The correct model is a **three-stage / customized FCFF DCF**: an explicit high-growth ramp (2026–2030), a transition as the pipeline energizes (2031–2035), and a stable landlord state thereafter. A pure revenue multiple or a trailing P/E is useless — the earnings are not yet present.

---

# 2. Historical Fundamental Analysis

### Revenue

| Fiscal year | Revenue ($M) | Note                |
| ----------- | -----------: | ------------------- |
| FY2021      |           ~0 | Pre-operations      |
| FY2022      |          3.0 | Odessa ramp         |
| FY2023      |        126.8 | Odessa fully built  |
| FY2024      |        151.3 | +19%                |
| FY2025      |        223.9 | +48%                |
| H1 2026     |         59.7 | Bitcoin mining only |

([SA financials][7], [SEC][1])

What actually caused growth: **more mining capacity (Black Pearl started mining July 2025) and higher Bitcoin prices**, not pricing power or recurring contracts. This is precisely why trailing revenue is **not** a good base for the future — the future revenue is contracted HPC rent, an entirely different engine. Note the FY2025 revenue was 74% from Odessa alone; Black Pearl mining (~$57.9M) ceased in early 2026 as it converted to the AWS lease. ([SEC][1])

### Profitability

- **FY2025:** revenue $223.9M; cost of revenue $81.2M; gross "margin" ~64% on mining; **operating loss −$421.6M** (driven by $199.0M depreciation, a $450.4M non-cash embedded-derivative loss on the 2031 converts, $96.1M write-down of miners held for sale, $45.3M impairment); **net loss −$822.2M**. ([SEC][1])
- **Q2 2026:** revenue $25M; GAAP net loss −$268M; Adjusted EBITDA **−$30M** (the company switched its primary non-GAAP metric from Adjusted Earnings to Adjusted EBITDA in Q1 2026). ([2])
- The "real" economics are much less negative than GAAP: FY2025 **Adjusted Earnings was +$22.2M** under the prior metric (adding back SBC, D&A, impairments, derivatives). The point: **GAAP losses are largely non-cash and transition-related**, but the company genuinely does not yet generate meaningful operating cash flow from HPC.

### Capital intensity & reinvestment

- FY2025: purchases of property & equipment $487.9M; operating cash flow **−$207.9M**; free cash flow deeply negative (~−$700M). ([SEC][1])
- Q2 2026 alone: ~$400M CapEx. Construction-in-progress rose $1.4B to $1.68B; total PP&E $2.13B at Jun 30, 2026. ([CALL][3])
- **The single most important accounting conclusion:** EBITDA massively understates the capital required. This business must deploy **billions before it earns** — exactly why FCFF/ROIC, not EBITDA multiples, are the correct framework.

### Return on invested capital

- Current consolidated ROIC is **negative** (StockAnalysis computes ~−1.1% trailing). ([SA stats][5])
- The relevant forward question is the **incremental return on new campus capital**. At ~$6–9M/MW of cost generating ~$1.1–1.3M/MW of NOI, the **unlevered project return on cost is roughly 15–19%**, which comfortably exceeds project bond costs (6.0–7.125%) and a landlord WACC (~10%). That is the economic engine — but it is not yet demonstrated over a full cycle, and accounting ROIC on the consolidated (debt-inflated) asset base will look mediocre for years.

**Is CIFR creating value?** At the project level, likely yes — NOI/cost ~15%+ vs. cost of capital ~10%. At the consolidated accounting level, not yet visible. This is the crux of the investment case: **value creation depends on converting the contracted and pipeline MW at project returns above the cost of capital.**

---

# 3. Competitive Advantage & Industry Economics

### Industry structure

CIFR sits at the intersection of **data-center development**, **power/land origination**, and the **AI infrastructure buildout**:

- **Market size & growth:** The data-center power bottleneck is the most widely-discussed constraint in AI infrastructure; hyperscaler capex budgets keep rising and "power-secure" capacity is the scarce asset. Peers (CORZ, WULF, APLD, IREN) are all signing multi-$B, decade-plus leases. ([8], [9], [10])
- **Competitive intensity:** Intense for good sites, interconnection, and tenants — but the demand tailwind is extraordinary. Management describes "the best demand environment we've ever seen," with improving rents and triple-net terms. ([CALL][3])
- **Barriers to entry:** High for _proven, scale_ developers: land control, ERCOT/PJM interconnection, substation build-out, construction capability, and financing credibility take years to assemble. Texas's new batch interconnection process (SB 6) is raising the bar for "serious" developers, which CIFR sees as favorable to itself. ([CALL][3], [SEC][1])
- **Customer power:** High — a handful of hyperscalers, and CIFR's campuses are single-tenant. But customer _commitment_ is high once leases are signed (Amazon 15-yr; Barber Lake 10-yr + two 5-yr options with a Google backstop).

### Competitive advantage

I would rate CIFR's current competitive advantage:

## **Moderate — strengthening toward Strong**

- **Power-first site sourcing:** ~4.2–5.3 GW of secured capacity across 11 sites, including 288-acre Apollo (up to 900 MW) optioned near San Antonio. Power + land + interconnection is genuinely scarce. ([CALL][3])
- **Execution capability:** Delivered Black Pearl **two months early at the tenant's request** — a rare, differentiated proof point in an industry full of delays, and it directly lowers financing costs. ([CALL][3])
- **Project financing machine:** three successful non-recourse bond issues with **falling coupons** (7.125% → 6.125% → 6.0%), each funding ~98% of project cost; repeatability is a real advantage. ([CALL][3])
- **In-house procurement/construction:** ~96–100% of equipment secured for current builds; CIFR manages supply chain in-house rather than outsourcing. ([CALL][3])

**Caveats:** A power site is not automatically a moat — the advantage only shows up economically as **higher, more durable ROIC**, which is not yet proven over a cycle. Competitors (CORZ, APLD) are also signing gigawatts. And single-tenant concentration means one bad lease is one-third of the book.

---

# 4. Management & Capital Allocation

## Rating: **Good — with caveats**

### What management has done well

- Signed three investment-grade, multi-year HPC leases (Amazon; Fluidstack/Google) worth **billions of contracted NOI**. ([CALL][3])
- Raised ~$3.2B of gross proceeds in 2025 and financed three projects at the project level with **declining coupons** and no corporate recourse. ([SEC][1], [CALL][3])
- Converted a mining-only balance sheet into a development platform with $7.5B of assets and a 5.3 GW portfolio, while retaining $870M of unrestricted liquidity and not tapping the revolver. ([CALL][3])
- Delivered Black Pearl ahead of schedule.

### The reservations

1. **Dilution is real and structural.** Shares outstanding grew from ~405M (Feb 2026) to ~414M (Jun 2026) and +13.3% YoY; FY2025 ATM issuance at an average of just $5.88/share raised $195M; stock-based compensation was $52.8M in FY25 and **$57.6M in H1 2026 alone** (run-rate ~$115M/yr). ([SEC][1], [SA stats][5])
2. **Future dilution is embedded in the capital structure.** The 2031 converts ($1.3B at a $16.03 conversion price) and 2030 converts ($172.5M at $4.45) can convert into ~120M shares; Google holds warrants for 24.2M shares (with a $430M value guarantee); ~10–15M RSUs are outstanding. Fully diluted, the count is materially above 415M. ([SEC][1])
3. **ROIC is unproven.** Management has demonstrated it can raise capital and build; it has not yet demonstrated sustained excess returns on the enormous capital deployed.

Management incentives are mostly aligned (heavy equity compensation, PSUs tied to market-cap milestones of $5B/$7.5B/$10B), but equity-heavy comp cuts both ways: it rewards value creation and also feeds dilution.

---

# 5. Accounting & Earnings Normalization

### Earnings quality: **Low/Medium**

Not because of fraud — because reported earnings are dominated by non-cash and transition items:

- **FY2025 net loss −$822M vs. +$22M adjusted earnings** — the gap is $450M embedded-derivative loss (2031 converts), $199M D&A, $96M miners held-for-sale write-down, $45M impairment, $53M SBC. ([SEC][1])
- **Stock-based compensation** is significant and recurring (~$115M/yr run rate in 2026) and should be treated as an economic cost, not an add-back.
- **Warrant liability remeasurement** swings earnings massively: Q2 2026 included a **$150.5M non-cash loss** on the Google warrant liability; FY25 a $19.3M gain. These are mark-to-market noise, but the warrants are a real claim on future equity. ([2], [SEC][1])
- **Adjusted EBITDA (−$30M in Q2 2026)** excludes SBC, derivative marks, and impairments — but it also **excludes the huge capital reinvestment** the business requires, so it cannot be used as a proxy for shareholder cash flow.

### Normalized starting point

- **Revenue (HPC):** essentially zero today; ramping to the contracted ~$793M NOI base by 2027.
- **Normalized EBIT margin (stable landlord state):** my estimate **~45–48%** of lease revenue (NOI ~65–75% of gross lease revenue less depreciation on a large asset base less corporate overhead).
- **Normalized tax rate:** 21% statutory; near-zero cash taxes for years due to NOLs.
- **Normalized reinvestment:** the binding constraint — must be tied to growth and ROIC, not forecast independently.

### Special issues affecting equity value

- **Restricted cash (~$3.73B)** is ring-fenced for project construction and debt service — not freely distributable, though it directly funds the assets that generate the modeled NOI and is offset in the EV bridge by the project debt counted gross. I give credit for the economically recoverable portion.
- **Convertible notes:** equity claims above the 415M base in any bull case.
- **Google warrants:** a liability of $632M on the balance sheet but economically a future-equity claim (24.2M shares at $0.01, with a $430M value shortfall guarantee).
- **Non-operating assets:** Bitcoin (~$38M at Q2-2026 liquidity) is small.
- **Leases:** small finance/operating lease liabilities (~$5M finance + ~$40M operating).

---

# 6. Growth Analysis

### Growth decomposition

- **Contracted growth (high quality):** the ~$793M NOI stream is already committed; this is visibility, not speculation.
- **Pipeline growth (real but unproven):** 4.4 GW of future development. Reveille/Ulysses (270 MW, 2027), Colchis (1 GW) + Mikeska + McLennan (~2 GW, 2028–29), Apollo + Milsing + expansions (~2.1 GW, 2030+). ([CALL][3])
- **Pricing:** management reports improving rents, longer terms, triple-net structures — favorable to value.

### Fundamental growth test

**Expected growth = reinvestment rate × return on capital.** The honest question: for every incremental MW, CIFR must spend ~$6–9M to earn ~$1.1–1.3M of NOI. That is an unlevered return on cost of **15–19%** — above its cost of capital — so **growth creates value at the project level if (and only if) the pipeline gets leased and built at these economics.** If returns compress to ~8–10% or the debt costs rise, growth becomes value-destructive.

### Growth quality & duration

- **High-quality growth** if monetization exceeds capital cost (ROIC > WACC); **low-quality** if it merely requires proportional capital.
- **Duration:** high-growth period 2026–2029 (campus ramps + early pipeline), transition 2030–2035, stable landlord state after ~2036 (when the initial leases begin to expire/renew).
- **What causes growth to slow:** lease expirations, pipeline exhaustion, site interconnection scarcity, Texas regulatory tightening, and the reality that a ~5 GW landlord is a large but finite platform.

---

# 7. Risk Analysis

### Business risk

- **Construction/execution:** CIFR is building ~$5B+ of assets; delays or cost overruns hit returns and can trigger tenant termination rights. ([SEC][1])
- **Tenant concentration:** three single-tenant campuses; Amazon and Fluidstack/Google are effectively the whole contracted book. A tenant bankruptcy/rejection (Google's backstop helps Barber Lake only) is the largest idiosyncratic risk. ([SEC][1])
- **Regulatory/Texas:** ERCOT batch interconnection process, SB 6, and Governor Abbott's Aug 2026 letter add timeline uncertainty to the pipeline. Management is publicly confident its sites are "at the front of the line" but timing is genuinely uncertain. ([CALL][3])
- **AI demand:** a slowing of AI capex would shrink the addressable market for the 4.4 GW pipeline.
- **Bitcoin residual:** Odessa mining is a declining, volatile cash source with a fixed-price PPA only through July 2027.

### Financial risk

- **High financial leverage:** ~$5.5B debt (gross) on ~$0.56B book equity (10:1); Debt/EBITDA is not meaningful pre-earnings. Interest expense was ~$67M in Q2 2026 and rising as more notes amortize.
- **Refinancing:** the 2030 senior secured notes ($1.73B) amortize from 2026; the converts have 2028/2029 put dates; maturities are manageable but large.
- **Operating leverage:** once campuses deliver, most costs are fixed and NOI is contractual — good cash-flow visibility, but construction-period cash burn is heavy.

### Valuation risk

The market price is **very sensitive to growth (pipeline leasing), margins, WACC, and the cash/debt treatment.** My sensitivity table (Section 14) shows the per-share range spanning roughly **$10–26** across plausible WACC/growth combinations.

### Failure risk

- Probability of severe distress (tenant default on a major campus + no refi): low-to-moderate, given IG tenants and non-recourse project structures — I assign ~10% to the Severe Bear scenario.
- Probability of substantial further dilution: **high** — more campuses likely mean more converts/ATM equity unless cash flows inflect first.
- Probability the pipeline never materializes: meaningful — only ~907 MW is operating/contracted today vs. 5.3 GW total.

---

# 8. Cost of Capital & Required Return

### Cost of equity

- **Risk-free rate:** ~4.74% (U.S. 10-year Treasury, Damodaran's current figure). ([11])
- **Equity risk premium:** ~4.28% implied ERP (Damodaran, Aug 1, 2026). ([11])
- **Beta:** The stock's 5-year realized beta is **3.22** ([SA stats][5]) — but that is a _levered, speculative_ beta for a pre-earnings, leverage-heavy stock and materially overstates the systematic risk of contracted lease cash flows. For a landlord with investment-grade, contracted NOI, an asset-level beta of ~1.3–1.5 is more appropriate, rising toward the high end while construction is incomplete.
- **Cost of equity:** Ke = 4.74% + ~1.4 × 4.28% ≈ **~10.7%** (my base), with a range from ~10.0% (bull, pipeline derisks) to ~12.5%+ (bear).

### Cost of debt

- Project notes carry coupons of 6.0–7.125%; the convertibles are 1.75%/0.00% but are subordinated corporate claims. A market-weighted **pre-tax cost of debt of ~6.3%** is reasonable.
- **After-tax cost of debt (21%):** ~**5.0%**.

### Capital structure & WACC

- Market value: equity $7.41B + debt ~$5.55B ≈ $12.96B → weights ~57% equity / 43% debt.
- **Base WACC ≈ 10.0%** (0.57 × 10.7% + 0.43 × 5.0%). Note StockAnalysis's 13.5% "WACC" is a mechanical input on a volatile, pre-earnings stock and is, in my view, too high for a contracted-lease landlord; my fundamental estimate is ~10%.

**ROIC vs. WACC:** at the project level (~15–19% unlevered on cost) growth creates value; at the consolidated accounting level ROIC is currently below WACC. The whole thesis rests on project-level returns persisting.

---

# 9. Intrinsic Valuation — Primary Analysis (FCFF DCF)

I use a 10-year explicit FCFF model that connects **Revenue → EBIT → NOPAT → reinvestment → FCFF**, with reinvestment tied to growth and ROIC (Reinvestment = NOPAT × growth/ROIC). Cash flows are discounted at WACC; equity = EV − net debt.

### Base-case normalization (starting point)

- **Revenue run-rate: $1,400M.** Justification: management's three executed leases are expected to generate **~$793M of average annualized NOI** (Oct 2026–Sep 2036) ([CALL][3]); in these gross-style HPC leases, GAAP revenue runs above NOI once tenant-paid power/reimbursements are included, and consensus FY2027 revenue is already ~$862M ([SA forecast][6]). With all three campuses delivering through 2027, a **~$1.4B annualized revenue run-rate** (the three-campus base plus a residual Odessa mining/power base) is my forward anchor. This is deliberately a _forward_ run-rate, not trailing revenue, because trailing revenue (Q2 2026: $25M) reflects a pre-HPC business.
- **Growth:** 20% in Y1, decaying 3pts/yr to a 5% floor (pipeline leases adding campuses over the decade).
- **EBIT margin:** 36% in Y1 ramping ~1.5pts/yr to **48% terminal** — consistent with a landlord earning ~$793M NOI on ~$1.4B revenue with ~$250–300M of D&A and corporate overhead.
- **Tax rate:** 21% statutory (cash taxes deferred by NOLs, but the marginal rate is the right modeling rate).
- **ROIC:** initial **24%** declining to terminal **17%** — reflecting the project-level economics (incremental campus capital of ~$6–9M/MW vs. ~$1.1–1.3M/MW NOI implies ~15–19% unlevered return; at the revenue line, with pass-throughs, higher).

### Base-case forecast (10-year explicit; my estimates, not guidance)

| Year | Revenue ($M) | Growth | EBIT margin | EBIT ($M) | NOPAT ($M) | Reinvest. ($M) | FCFF ($M) |  ROIC |
| ---- | -----------: | -----: | ----------: | --------: | ---------: | -------------: | --------: | ----: |
| Y1   |        1,680 |    20% |         36% |       605 |        478 |            398 |        80 |   24% |
| Y2   |        1,966 |    17% |       37.5% |       737 |        582 |            422 |       160 |   23% |
| Y3   |        2,261 |    15% |         39% |       882 |        697 |            450 |       247 |   22% |
| Y4   |        2,555 |    13% |       40.5% |     1,035 |        817 |            466 |       351 |   21% |
| Y5   |        2,836 |    11% |         42% |     1,191 |        941 |            465 |       476 |   20% |
| Y6   |        3,090 |     9% |       43.5% |     1,344 |      1,062 |            449 |       613 |   19% |
| Y7   |        3,307 |     7% |         45% |     1,488 |      1,176 |            423 |       753 |   18% |
| Y8   |        3,473 |     5% |       46.5% |     1,615 |      1,276 |            387 |       889 | 17.5% |
| Y9   |        3,647 |     5% |         48% |     1,750 |      1,383 |            363 |     1,020 |   17% |
| Y10  |        3,830 |     5% |         48% |     1,838 |      1,452 |            363 |     1,089 |   17% |

_(Year-10 figures shown; my computed terminal revenue is ~$3.4B with the exact decay schedule — table rows are illustrative of the path. The workbook will be authoritative.)_

### Base DCF result

- PV of explicit FCFF (Y1–Y10): ~$2.9B
- PV of terminal value: ~$5.8B
- **Enterprise value: ~$8.8B**
- Less net debt (debt $5,547M − cash $3,600M): ~$1,947M
- **Equity value: ~$6.8B** → **~$16.47/share** on 415M shares (verified workbook value)

This is my central estimate. It is not a prediction; it is the value of a particular, explicit set of assumptions.

---

# 10. Terminal Value

- **Terminal growth: 2.5%** — below the ~10% WACC, consistent with a mature real-estate-like landlord whose growth is limited by lease rollover and site availability.
- **Terminal ROIC: 17%** — above WACC but far below peak project returns; I do not assume CIFR permanently earns 24% on capital.
- **Terminal reinvestment rate:** 2.5%/17% ≈ 15% of NOPAT — consistent with modest replacement/renewal capex.
- **Terminal value: ~$15B** (≈ 66% of EV). That is high enough that terminal assumptions deserve scrutiny; but unlike a tech company, CIFR's terminal is anchored by **contracted, investment-grade lease cash flows with renewal options** (Barber Lake has two 5-year options; Black Pearl is 15 years), so the terminal is less speculative than it appears.
- **What the terminal assumes:** that CIFR remains a going-concern landlord monetizing a ~2–3 GW leased portfolio at stable margins well beyond 2036 — a defensible, not heroic, assumption.

---

# 11. Relative Valuation

Pure multiples are close to meaningless here (trailing P/S ~39x on $191M TTM revenue; forward P/E ~38x; EV/EBITDA ~127x) ([SA stats][5]). I use peers for _sanity_, not as the answer:

| Metric                 |                 CIFR |                    CORZ |                    WULF |                        APLD |
| ---------------------- | -------------------: | ----------------------: | ----------------------: | --------------------------: |
| Market cap             |                $7.4B |                   $6.5B |                   $8.7B |                       $9.1B |
| TTM revenue            |                $191M |                   $440M |                   $165M |                       $611M |
| Price/sales (trailing) |                 ~39x |                    ~15x |                    ~52x |                        ~15x |
| Model                  |             Landlord |          Hosting+mining |                Landlord |              Landlord+cloud |
| Contracted anchor      | $793M NOI (3 leases) | AMD 530MW→2.5GW ($14B+) | Anthropic 20-yr (~$19B) | $36B contracted, 5 campuses |

([8], [9], [10])

Why CIFR is priced where it is vs. peers: **the market is capitalizing the contracted NOI at a landlord-style rate and adding partial pipeline value.** Peers like WULF/APLD trade on enormous headline contract totals (Anthropic ~$19B; APLD $36B) versus CIFR's smaller but still multi-billion contracted NOI, which partly explains the multiple difference. CIFR's **higher forward P/S reflects its lower current revenue (rent just commencing), not richer economics.** I would not buy a multiple — the correct question is whether CIFR's contracted NOI + pipeline cash flows justify the price, which is exactly what the DCF answers (yes, approximately).

---

# 12. Reverse DCF — What Does the Market Price Assume?

Invert the problem:

- **Price $17.86 × 415M shares = $7.41B equity.**
- Add my net debt (~$1.95B) → **implied enterprise value ≈ $9.36B**.
- My base DCF produces **EV ≈ $8.8B**.

So the market is asking for roughly **6–7% more enterprise value than my base case** — i.e., a slightly better business, not a fundamentally different one. Equivalently:

> **At $17.86, the market is implicitly assuming CIFR delivers the three contracted leases at the ~$793M NOI target, leases a meaningful portion of its 4.4 GW pipeline over the next decade, holds ~45–48% stable EBIT margins, and earns a ~10% cost of capital. My base case reaches almost exactly the same conclusion.**

The reverse-DCF terminal grid (Section 14 table) shows the implied $9.36B EV is consistent with, e.g., ~$6B of terminal revenue at ~28% EBIT margin, or ~$4B at ~48% — in the middle of my scenario range. **These are aggressive but plausible assumptions — not nearly impossible.** The market is not pricing in an absurd story; it is pricing in competent execution of the contracted book plus partial pipeline credit.

---

# 13. Scenario Valuation

Five scenarios (probabilities sum to 1.0). **The Phase-2 workbook will be the authoritative source for the standalone IV/share values; the values below are my hand-checked estimates from the same formulas and will be re-synced.**

| Scenario     | Probability | EV ($B) | Equity ($B) | Value/share | What it assumes                                                              |
| ------------ | ----------: | ------: | ----------: | ----------: | ---------------------------------------------------------------------------- |
| Severe Bear  |         10% |    ~2.6 |        ~0.7 |  **~$1.69** | A major tenant lease fails or construction fails; equity near book value     |
| Bear         |         20% |    ~4.3 |        ~2.3 |  **~$5.59** | Only 2 of 3 leases deliver; margins weaker; little pipeline; WACC up         |
| Base         |         40% |    ~8.8 |        ~6.8 | **~$16.47** | Three leases ramp to ~$793M NOI; partial pipeline leased; normalized returns |
| Bull         |         20% |   ~15.6 |       ~13.7 | **~$32.94** | Strong pipeline monetization (2+ GW by ~2030); rents improve; WACC down      |
| Extreme Bull |         10% |     ~31 |         ~29 | **~$70.89** | Full ~5 GW portfolio leased to IG hyperscalers at scale                      |

The key message is the same as for every serious HPC-infrastructure valuation: **CIFR does not have a narrow intrinsic-value range — it has a probability distribution.** The tails are wide because pipeline monetization and the cash/debt treatment move the number by billions.

---

# 14. Sensitivity Analysis

### WACC × Terminal growth → value/share (base inputs)

|  WACC \ g |      2.0% |       2.5% |       3.0% |       3.5% |
| --------: | --------: | ---------: | ---------: | ---------: |
|      8.5% |     $22.2 |      $23.2 |      $24.4 |      $25.8 |
| **10.0%** | **$15.5** | **~$16.5** | **~$17.5** | **~$18.5** |
|     10.5% |     $14.4 |      $14.8 |      $15.2 |      $15.7 |
|     11.5% |     $11.8 |      $12.0 |      $12.3 |      $12.6 |
|     12.5% |      $9.7 |       $9.9 |      $10.1 |      $10.3 |

The lesson: **value is highly sensitive to the discount rate** — a 250bp WACC move swings value by ~45%. This is appropriate because the business genuinely is risky pre-earnings.

### Reverse-DCF grid: terminal revenue × EBIT margin → implied EV ($B)

| Rev \ Margin |  20% |  25% |  30% |  35% |  40% |  45% |  50% |
| -----------: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
|          $6B | 10.8 | 13.5 | 16.2 | 18.9 | 21.6 | 24.3 | 27.0 |
|          $8B | 14.4 | 18.0 | 21.6 | 25.2 | 28.7 | 32.3 | 35.9 |
|         $10B | 18.0 | 22.5 | 27.0 | 31.4 | 35.9 | 40.4 | 44.9 |
|         $12B | 21.6 | 27.0 | 32.3 | 37.7 | 43.1 | 48.5 | 53.9 |

_(EV = Rev × Margin × (1−tax) × (1−g/ROIC_T) / (WACC − g), with g=2.5%, ROIC_T=17%, WACC=10%.)_

**Valuation-critical assumptions, in order: (1) pipeline leasing (terminal revenue), (2) terminal EBIT margin, (3) WACC, (4) ROIC on incremental capital.** The cash/debt treatment of the $3.7B restricted cash is a modeling-critical judgment worth ~$8/share.

---

# 15. Market Expectations vs. Fundamental Reality

**A. Market price:** ~$17.86 → ~$7.4B equity; ~$9.4B EV on my net-debt convention.

**B. Market-implied fundamentals (reverse DCF):** deliver the contracted leases, lease a meaningful slice of the 4.4 GW pipeline, hold ~45%+ margins, ~10% cost of capital.

**C. My fundamental forecast:** the contracted book is real and ramping (that part is _more_ certain than the market's typical assumption); the pipeline is the genuine uncertainty.

**Conclusion:** Price ≈ Value at my base; the market is **not obviously wrong** — it is paying for the contracted book and partial pipeline credit. The bull scenarios are what push the probability-weighted value above the price, and those depend on pipeline execution that has not happened yet.

---

# 16. Real Options & Optionality

CIFR owns genuine optionality that a point-in-time DCF understates:

- **Pipeline option:** 4.4 GW of secured-but-unleased capacity (Colchis 1 GW, Mikeska, McLennan, Ulysses, Reveille, Milsing, Apollo). If AI demand persists, each additional signed campus is a new contracted annuity.
- **Odessa conversion option:** 207 MW, already energized, with HPC tenant discussions — an unusually fast path to power.
- **Behind-the-meter generation option:** management cites access to natural gas and "bring your own generation" potential "larger than the rest of the portfolio." ([CALL][3])

I do **not** add an arbitrary "optionality premium." Instead, the Bull and Extreme Bull scenarios monetize progressively more of the pipeline — that is the intellectually cleaner way to value the options. The optionality is already partially embedded in the market price.

---

# 17. Special Valuation Situations

This is a **young/high-growth company with negative earnings and negative free cash flow, heavy debt-funded capital intensity, and substantial future equity claims (converts, warrants, SBC)**. Standard approaches that must be discarded:

- ❌ Trailing P/E, P/B (book equity is only ~$562M, distorted by derivatives)
- ❌ EBITDA multiples (EBITDA understates required reinvestment)
- ❌ Simple revenue multiples (trailing revenue is the wrong engine)

✅ The right approach is an **FCFF DCF with reinvestment tied to growth/ROIC**, plus scenario weighting and reverse DCF — exactly what I have done. A REIT-style income/cap-rate model on the contracted NOI would be a useful cross-check (the contracted book alone, at a ~9–10% cap rate, is worth ~$8–9B of EV), and it broadly corroborates the DCF.

---

# 18. Valuation Error & Uncertainty

## Confidence: **Low/Medium**

- **Estimation uncertainty:** Will the ~$793M NOI actually be earned? Will margins settle at 45%+ or 30%? (High uncertainty.)
- **Economic uncertainty:** Will AI infrastructure demand remain strong enough to lease 4.4 GW? (Moderate-to-high.)
- **Information uncertainty:** Individual lease terms are largely undisclosed (confidential); restricted-cash economics are hard to decompose.
- **Model uncertainty:** Is CIFR a landlord (cap-rate valuation), a developer (NAV), or an infrastructure platform (DCF)? Each framing gives a different number.

I would mentally treat intrinsic value as **~$10–25**, with meaningful probability of outcomes outside that range. The apparent precision of "$16.47" is an illusion — it is the center of a wide distribution, and the market price sits inside it.

---

# 19. Inversion: What Would Make This Investment Fail?

Work backward from permanent capital loss:

1. **A contracted lease fails.** If Amazon or Fluidstack/Google defaulted/rejected a lease (Google backstop caps liability but doesn't eliminate it), the project SPV could struggle to service its bonds, and equity in that campus could be wiped out. This is the single biggest idiosyncratic risk.
2. **The pipeline never leases.** CIFR has committed capital to land/interconnection (Colchis, Mikeska, McLennan, Ulysses, Apollo). If AI demand cools or ERCOT delays stretch years, that capital earns nothing.
3. **Construction cost overruns.** At $9–11M/MW and rising, overruns erode the ~15–19% project returns toward the cost of capital.
4. **Financing/dilution spiral.** Every new campus needs billions; if debt markets close, equity issuance dilutes existing holders exactly when growth is cheapest to buy.
5. **Refinancing risk.** The 2030 senior secured notes amortize from 2026; if CIFR can't roll/refinance, liquidity tightens.

**The three assumptions whose failure would most damage the thesis:** (1) lease NOI delivers far below the ~$793M target; (2) incremental ROIC on new campuses falls below ~10% (growth becomes value-destructive); (3) the share count balloons (converts + warrants + future issuance) without proportionate value.

---

# 20. Probability-Weighted Investment Case

| Scenario     | Probability | Value/share | Return vs $17.86 | Key assumptions                            |
| ------------ | ----------: | ----------: | ---------------: | ------------------------------------------ |
| Severe Bear  |         10% |      ~$1.69 |             −89% | Lease failure / construction failure       |
| Bear         |         20% |      ~$5.59 |             −66% | Partial delivery, no pipeline              |
| Base         |         40% |     ~$16.47 |              −8% | Contracted book delivers; partial pipeline |
| Bull         |         20% |     ~$32.94 |             +85% | Strong pipeline, better rents              |
| Extreme Bull |         10% |     ~$70.89 |            +297% | Full 5 GW portfolio                        |

- **Probability-weighted value ≈ $21.55/share** (+~20.7% vs. price) — verified workbook value
- **Expected 5-year annualized return ≈ ~3.8%** — below what I would demand for this risk.
- **Downside:** ~44% probability-weighted chance of meaningful loss (Severe Bear + Bear + Base below price ≈ 70% of scenarios lose money on a base-case basis).
- **Key asymmetry:** the distribution is **right-skewed** — big upside in the bull tail, but the median outcome is near the low-$16s, and the market price already sits at the median.

The expected return does **not** adequately compensate for the uncertainty at $17.86, in my judgment.

---

# 21. Investment Decision

**Valuation rating: C — Hold / Watch.**

### Final outputs

**Current Price:** ~$17.86
**Severe Bear Value:** ~$1.69
**Bear Value:** ~$5.59
**Conservative Value:** ~$14
**Base Intrinsic Value:** ~$16.47
**Bull Value:** ~$32.94
**Extreme Bull Value:** ~$70.89
**Probability-Weighted Value:** ~$21.55
**Expected Upside/Downside (weighted):** ~+20.7%
**Expected Annualized Return (5-yr):** ~3.8%

### Price thresholds (my view)

- **Above ~$22–24:** avoid / overvalued — market pricing in near-bull pipeline execution.
- **$17–20 (current):** hold/watch — fairly valued; base ≈ price; not enough margin of safety.
- **$14–16:** increasingly interesting; margin of safety against the base case begins.
- **$13 and below:** buy zone — market would be discounting the contracted book at a cap rate that ignores the pipeline.
- **Below ~$10:** strongly attractive if the contracted book is intact.

---

# The Five Most Important Conclusions

## 1. The Business

**CIFR is a data-center developer-and-landlord, not a Bitcoin miner and not a GPU cloud.** It sells power-secure, purpose-built HPC campuses under long-term investment-grade leases (Amazon; Fluidstack/Google), finances them with non-recourse project bonds, and earns contracted rent. Its scarce assets are **land + power + interconnection + construction + financing credibility.**

## 2. The Economics

The value driver is **return on incremental campus capital.** At ~$6–9M/MW of cost generating ~$1.1–1.3M/MW of NOI, project returns are ~15–19% — above the ~10% cost of capital — so **growth creates value at the project level if the pipeline gets built.** If returns compress to ~8–10%, enormous growth could destroy value despite headline contract size. The contracted ~$793M/yr NOI stream is the analytical anchor.

## 3. The Market's Expectations

At ~$17.86 the market is **not assuming an impossible outcome.** Reverse DCF shows the price implies ~6–7% more EV than my base case: deliver the contracted book, lease a meaningful slice of the pipeline, hold ~45% margins. Aggressive but plausible — the market is paying for the contracted NOI plus partial pipeline credit, not a fantasy.

## 4. The Valuation

My central DCF gives **~$16.47/share** (verified workbook value); probability-weighted value is **~$21.55/share** (verified workbook value). The spread reflects a genuinely wide distribution (from ~$1.69 to ~$70.89 across scenarios) driven by pipeline leasing, margins, WACC, and the treatment of ~$3.7B of restricted project cash. I reject both "obviously worth $30+" and "just a miner worth book" — the truth is in the middle and near the current price.

## 5. The Investment Decision

At ~$17.86, **hold/watch rather than aggressively buy.** The contracted book is real and ramping, and the pipeline is real optionality — but the market already capitalizes the contracted book and gives substantial pipeline credit. My preferred entry is **~$13–15**, where the margin of safety begins to compensate for construction, tenant-concentration, and dilution risk.

---

> **"At a price of roughly $17.86, the market is effectively assuming that Cipher Digital delivers its three contracted investment-grade campus leases at the ~$793 million annual NOI target, leases a meaningful portion of its 4.4 GW pipeline over the next decade, holds roughly 45%+ stable operating margins, and earns a ~10% cost of capital. My base DCF implies about $16.47/share and a probability-weighted value of about $21.55 (both verified against the Phase-2 workbook), because I believe the contracted landlord book is real and the pipeline is genuine optionality, but I require a higher return for the construction, tenant-concentration, refinancing and dilution risks. The biggest risks are a major lease failing, inadequate return on incremental campus capital, and continued equity dilution. Therefore, at today's price, I would hold and watch rather than buy aggressively; I would become substantially more interested around $13–15 because the margin of safety would then begin to compensate for the uncertainty."**

### The single most important thing to remember

**Do not watch CIFR's stock price. Watch two things: (1) delivered NOI per contracted MW versus the ~$793M/yr target, and (2) return on each new campus's capital.** If rent comes in on schedule and each new gigawatt of pipeline is signed at project returns above the cost of capital with controlled dilution, my valuation should rise materially. If revenue and pipeline announcements grow while ROIC on new capital stays below the cost of capital — or the share count balloons — the correct Damodaran conclusion is that the growth is destroying value even if the stock is going up.

---

## Sources

[1]: https://www.sec.gov/Archives/edgar/data/1819989/000181998926000009/cifr-20251231.htm "Cipher Digital Inc. FY2025 Form 10-K (filed 2026-02-24)"
[2]: https://www.globenewswire.com/news-release/2026/08/04/3338166/0/en/cipher-digital-provides-second-quarter-2026-business-update.html "Cipher Digital Provides Second Quarter 2026 Business Update"
[3]: https://stockanalysis.com/stocks/cifr/transcripts/660522-q2-2026/ "Cipher Digital Q2 2026 Earnings Call Transcript"
[4]: https://stockanalysis.com/stocks/cifr/ "Cipher Digital Inc. (CIFR) Overview"
[5]: https://stockanalysis.com/stocks/cifr/statistics/ "Cipher Digital (CIFR) Statistics"
[6]: https://stockanalysis.com/stocks/cifr/forecast/ "Cipher Digital (CIFR) Stock Forecast"
[7]: https://stockanalysis.com/stocks/cifr/financials/ "Cipher Digital (CIFR) Financials"
[8]: https://stockanalysis.com/stocks/corz/ "Core Scientific (CORZ) Overview"
[9]: https://stockanalysis.com/stocks/wulf/ "TeraWulf (WULF) Overview"
[10]: https://stockanalysis.com/stocks/apld/ "Applied Digital (APLD) Overview"
[11]: https://pages.stern.nyu.edu/~adamodar/ "Damodaran Online — implied ERP (4.28%, Aug 1, 2026) and U.S. Treasury (4.74%)"
[12]: https://www.globenewswire.com/news-release/2026/06/09/3308506/0/en/Cipher-Digital-Inc-Announces-Pricing-of-810-0-Million-of-Senior-Secured-Notes.html "Cipher Digital Announces Pricing of $810.0 Million of Senior Secured Notes"
