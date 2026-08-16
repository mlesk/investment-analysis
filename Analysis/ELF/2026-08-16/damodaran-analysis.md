# Aswath Damodaran-Style Valuation Analysis — e.l.f. Beauty, Inc. (NYSE: ELF)

**Analysis date:** 2026-08-16 · **Reference price:** $91.44 (Aug 14, 2026 close) · **Market cap:** ~$5.40B · **Fiscal year end:** March 31
**Lens:** Damodaran quantitative spine · **Prepared by:** GitHub Copilot (analyze-company skill)

---

## BOTTOM LINE FIRST

### Rating: **D — AVOID / SIGNIFICANTLY OVERVALUED**

**One-paragraph verdict:** e.l.f. Beauty is a genuinely good, high-momentum brand with a real competitive position in value beauty, but at $91.44 the market is paying for outcomes that the fundamentals do not support. My five-scenario, 10-year FCFF DCF — using Damodaran's current inputs (risk-free rate 4.74%, implied ERP 4.28%, beta ~1.50 → WACC ~10.0%, terminal growth 3.0%) — produces a **base intrinsic value of ~$44/share** and a **probability-weighted value of ~$57/share**, about **38% below** the current price. The stock trades at 26x forward EPS and ~23x EV/EBITDA — the top of its peer set — while the underlying economics are distorted by acquisition drag (ROIC ~8–16% vs ~10% cost of capital), ~5% of revenue in stock-based compensation, a one-time ~$50M tariff refund masking core margin, and a core e.l.f. brand that is _declining_ organically (all of FY26's ~$323M growth and most of Q1 FY27's +36% came from the $897M Rhode acquisition, not organic demand). A reverse DCF shows the market price is only justified by ~30–35% year-one growth — roughly double management's own 18–20% FY27 guidance — sustained for a decade, or by terminal margins near 35%, neither of which is credible for a mass-market cosmetics brand. I would not initiate a position at $91.44; value emerges only below ~$55, with real conviction below ~$45.

---

## Executive Summary Table

| Item                                         | Value                                                                       |
| -------------------------------------------- | --------------------------------------------------------------------------- |
| **Current price**                            | $91.44                                                                      |
| **Rating**                                   | **D — Avoid / Significantly Overvalued**                                    |
| **WACC**                                     | ~10.0% (Rf 4.74% + β 1.50 × ERP 4.28%; after-tax CoD ~4.0%)                 |
| **Terminal growth**                          | 3.0% (< WACC in every scenario)                                             |
| **Tax rate**                                 | 25% (normalized; FY26 effective 35% was distorted by §162(m) limits)        |
| **Base intrinsic value**                     | **~$43.84**                                                                 |
| **Severe Bear / Bear / Bull / Extreme Bull** | ~$8.29 / ~$19.29 / ~$84.31 / ~$159.77                                       |
| **Probability-weighted value**               | **~$57.08**                                                                 |
| **Expected upside / downside**               | **−37.6%**                                                                  |
| **Expected annualized return (5-yr)**        | **−9.0%**                                                                   |
| **Margin of safety at $91.44**               | None (negative ~38%)                                                        |
| **Buy zone**                                 | First tranche ≤ $55; accumulate $45–55; conviction < $45                    |
| **Valuation confidence**                     | **Medium** (economic uncertainty high; model outputs robust to ±1 scenario) |

---

# 1. Business Understanding & Fundamental Story

### Business Model (plain English)

e.l.f. Beauty is the "premium quality at a $2–$13 price point" challenger in mass cosmetics. It designs, sources (via third-party manufacturers, mostly in China), and markets color cosmetics (e.l.f. Cosmetics), skincare (e.l.f. SKIN, Naturium, and — since Aug 2025 — Rhode, founded by Hailey Bieber), and clean-beauty (Well People; Keys Soulcare was transferred out in May 2026). It just entered haircare (e.l.f. Hair, June 2026). Consumers pay $5–$13 a product through mass retailers (Target, Walmart, Amazon, Sephora, Ulta) and direct e-commerce (elfcosmetics.com). The company converts revenue into cash by running a very high gross margin (~71–74% GAAP; 83% in Q1 FY27 including the tariff refund) with heavy but disciplined marketing (~24% of sales), an asset-light supply chain (capex <1.5% of sales), and low working capital intensity.

The economic engine is **prestige-quality product at value prices + social-media-native marketing**, driving share gains in a mass beauty category where e.l.f.'s average price point (~$7) undercuts mass peers (~$10) and prestige (~$30) by 30–75% [SEC 10-K][6]. Volume is won at the shelf and on TikTok; margins come from scale purchasing, pricing power built on share gains, and a marketing model that is cheaper than legacy TV-driven beauty advertising.

### Economic Structure

- **Revenue drivers:** retail shelf productivity, e-commerce/TikTok Shop, international (21% of FY26 sales; UK/Canada/Germany), new categories (haircare), and the Rhode/Naturium acquisitions.
- **Unit economics:** strong — GM 71–74% GAAP (70.7% FY26), ~83% in Q1 FY27 including a one-time ~1,050bps refund benefit; ex-refund Q1 GM ~72.7% (+350bps) [SEC 10-Q][7].
- **Operating margin:** GAAP FY26 EBIT only 4.5% (distorted by a $57.6M non-cash Rhode earnout mark); normalized ex-CC ~8%; TTM ~11.7% (includes the refund quarter); FY27 guided adj-EBITDA ~20.6%, implying ~13–16% EBIT ex-refund.
- **Capital intensity:** very low — capex $22.4M FY26 (~1.4% of sales); main "investment" is marketing (24% of sales) and retail display/shelf build-outs.
- **Working capital:** modest and negative-ish; negative 2–4 day cash conversion historically; inventory turns ~2.2×.
- **Tax economics:** 25% normalized cash rate (FY26 effective 35% was inflated by non-deductible §162(m) comp; FY25 23%; Q1 FY27 29.4%) [SEC 10-K][6][10-Q][7].
- **Financing:** ~$834M bank debt (term loan $577.5M + revolver $256.7M at ~5.4%), maturities back-loaded to 2030 ($744M); net debt ~$490M (incl. leases ~$585M), ~0.9× EBITDA; revolver capacity $243M.
- **Competitive dynamics:** concentrated industry (L'Oréal, Estée Lauder, Coty, Unilever, LVMH, Shiseido, Beiersdorf, P&G) + a wave of indie/celebrity brands; e.l.f. competes on value + speed.

### Fundamental Story (the valuation narrative)

> "This company will create value because it can compound a mass-beauty share-gainer into a multi-brand portfolio, expanding margins toward prestige-like levels while staying asset-light."

The three fundamental inputs:

- **Cash Flows:** Today — high gross margin, low capex, but FCFF held down by (a) ~$87M/yr SBC (~5% of revenue, treated as a real expense), (b) heavy marketing reinvestment, and (c) acquisition-driven growth that consumes NOPAT (g/ROIC reinvestment). Expected change — margins ramp from ~13% toward 15% as Rhode/Naturium mature and marketing leverages; FCFF grows as growth decelerates. Evidence — FY27 guidance (adj EBITDA $401–407M on ~$1.95B). What could go wrong — organic e.l.f. declining; marketing has to stay at ~24% of sales to hold share.
- **Growth:** Today — FY26 +25% but ~91% acquisition-driven (Rhode $293.5M of +$323M); organic legacy +~2%. Q1 FY27 +36% but ex-Rhode organic e.l.f. declined high-single-digit; price/mix +39pts vs volume −3pts [SEC 10-Q][7]. Expected change — FY27 guided +18–20% (mostly Rhode + pricing, less unit volume). What could go wrong — organic demand stalls; volume keeps falling; Rhode's celebrity halo fades.
- **Risk:** High and rising — beta 1.56, China-tariff exposure (Section 301 at 10–12.5% from Jul 2026, Section 122 litigation, IEEPA refund cliff), customer concentration (Target 18% + Walmart 13% + Amazon 11% + Sephora 10% = 52%, no firm contracts), 13.6% short interest, securities class action + 5 derivative suits, and a key-person dependency on Hailey Bieber for Rhode.

### Business Lifecycle

**Growth** (transitioning toward mature): revenue compounding 25%+ for four years, but growth is increasingly acquisition/price-driven rather than unit-volume-driven, and organic volume is now negative. A **two-stage FCFF model** is appropriate: ~10 years of explicit high-then-fading growth, then a stable-growth terminal value. The model used here is the skill's standard two-stage (10-yr explicit + Gordon terminal), which fits this lifecycle.

---

# 2. Historical Fundamental Analysis

### Revenue (FY = Apr–Mar; $M) [StockAnalysis][2]

| FY           | Revenue | Growth | Net Income | Diluted EPS |
| ------------ | ------- | ------ | ---------- | ----------- |
| FY2022       | 392.2   | +23.3% | 21.8       | 0.41        |
| FY2023       | 578.8   | +47.6% | 61.5       | 1.11        |
| FY2024       | 1,023.9 | +76.9% | 127.7      | 2.21        |
| FY2025       | 1,313.5 | +28.3% | 112.1      | 1.92        |
| FY2026       | 1,636.5 | +24.6% | 26.3       | 0.44        |
| TTM (Jun-26) | 1,762.1 | +31.2% | 59.6       | 0.99        |

**What actually caused growth:** The FY2024 (+77%) surge was organic e.l.f. brand momentum (TikTok virality, share gains) plus the Naturium acquisition. FY2026's +$323M was **$293.5M (91%) from Rhode** (acquired Aug 2025) and only ~$29.5M from the legacy business; price/mix contributed +$333.5M while **volume declined −$10.5M** [SEC 10-K][6]. Q1 FY27: +$125.6M (+36%), of which price/mix +$137.4M, volume **−$11.7M**, e-commerce +129% (Rhode is DTC-heavy), retailers +16% [SEC 10-Q][7]. **The legacy e.l.f. brand is growing on price, not units — and is shrinking organically once Rhode is excluded.** This is the single most important fact for growth projection: historical growth is NOT a reliable extrapolant.

### Profitability

| Metric (FY)     | FY2023 | FY2024 | FY2025 | FY2026 | TTM   |
| --------------- | ------ | ------ | ------ | ------ | ----- |
| Gross margin    | 67.4%  | 70.7%  | 71.2%  | 70.7%  | 74.4% |
| EBIT margin     | 11.8%  | 14.6%  | 12.1%  | 4.5%\* | 11.7% |
| Net margin      | 10.6%  | 12.5%  | 8.5%   | 1.6%   | 3.4%  |
| ROE             | ~26%   | ~28%   | ~16%   | 2.4%   | 6.0%  |
| ROIC (reported) | ~14%   | ~16%   | ~13%   | ~5%    | 8.3%  |

\*FY26 EBIT margin distorted by $57.6M non-cash Rhode contingent-consideration charge; normalized ~8.0%.

Margins have **deteriorated** since the FY2024 peak: gross margin fell ~50bps in FY26 (tariffs), SG&A rose (Rhode integration, marketing, D&A on acquired intangibles), and the earnout mark + interest on the $600M term loan crushed net margin. **The "margins expand with scale" story has not shown up on the income statement — it has been masked by acquisitions and one-time items.** Economies of scale exist (high GM + low capex) but are currently being recycled into growth spend rather than falling to the bottom line.

### Capital Intensity

- CapEx/Revenue: ~1.4% (FY26 $22.4M; TTM $16.8M) — genuinely asset-light.
- Depreciation + intangible amortization: $79.4M FY26 (incl. $35M retail displays + $35.5M finite intangibles + $13.3M cloud software) — rising with acquisitions.
- Working-capital investment: modest; FY26 WC change ~+$2.3M.
- Acquisitions: Naturium $333M (FY24), Rhode $897.5M (FY25) — funded with debt + stock.
- R&D: minimal (product innovation via third-party suppliers).
- **Stock-based compensation: $86.9M FY26 (5.3% of revenue), up from $40.5M FY24 — growing ~2× faster than revenue.** [SEC 10-K][6]

**Accounting earnings vs economic earnings vs cash flows:** Reported FY26 FCF $190M and TTM $280M **overstate distributable cash** because they add back SBC without treating it as the real shareholder cost it is (SBC is ~$87M/yr and shares outstanding are rising ~3%/yr despite $100M of buybacks). Economic FCFF for a shareholder ≈ OCF minus capex minus SBC ≈ $212.5M − $22.4M − $86.9M ≈ **~$103M** in FY26 — roughly half the headline number.

### Return on Invested Capital

- **ROIC (NOPAT / Invested Capital):** FY2024 ~16% → FY2025 ~13% → FY2026 ~5% → TTM ~8.3% [StockAnalysis][4]. The collapse is driven by Rhode goodwill ($853M goodwill + $542M intangibles now sit on the balance sheet) and the $600M term loan, not by deteriorating operations.
- **ROIC vs cost of capital (~10%):** Reported ROIC is now **below the cost of capital** — growth funded by goodwill-laden acquisitions is currently _destroying_ value on a GAAP-ROIC basis. On _incremental_ capital (excluding goodwill), returns remain high, which is why the model uses initial ROIC of 40% transitioning to 20% for the reinvestment rate — a deliberately generous treatment that still fails to justify the price.

---

# 3. Competitive Advantage & Industry Economics

### Industry Structure

- **Market:** US mass color cosmetics + skincare is a slow-growth (~2–4%/yr) but huge market; e.l.f. competes across eye/lip/face, tools, skincare, and now haircare. International beauty is larger but fragmented and slower.
- **Concentration:** High — a few multinationals (L'Oréal, EL, Coty, Unilever, LVMH, Shiseido, Beiersdorf, P&G) control most retail distribution; indie/celebrity brands flood in via social media.
- **Barriers to entry:** Low to moderate — anyone can launch a viral beauty brand (Rhode itself is a celebrity brand), but _scaling_ to mass-retail shelf space at e.l.f.'s productivity levels is hard. Shelf space is the scarce resource.
- **Substitutes / customer power:** Consumers can switch brands freely at $5–$13 price points (low switching costs); retailers (Target, Walmart) hold most of the power and have their own private-label beauty ambitions.
- **Supplier power:** Low — multiple China-based contract manufacturers, ample capacity; but concentration in China is a tariff/geopolitical risk.

### Competitive Advantage

- **Brand + value proposition:** Genuine and durable for the e.l.f. flagship — "prestige quality at mass price" (avg price ~$7 vs ~$30 prestige) is a powerful, defensible consumer proposition [SEC 10-K][6]. _This is a real moat, but it is a price/positioning moat, not a switching-cost or network-effect moat._
- **Marketing engine:** Genuine advantage — community-led, digital-first, low-cost vs legacy TV spend; four of the top-10 mass new products in 2025, six in 2024.
- **Distribution:** Productivity-led shelf model is a real advantage; DTC site is unique among top-5 mass brands.
- **Network effects / switching costs / IP:** Weak. Cosmetics have no lock-in; patents are limited (design patents); brand loyalty is fickle, especially for a Gen-Z audience.
- **Does the advantage show up economically?** Yes in gross margin (71–74% vs mass category norms) — but **not yet in ROIC** (8–16% vs ~10% cost of capital) because acquisitions loaded the balance sheet with goodwill. The advantage shows up as _high gross margin + growth_, not yet as _durable excess returns on total capital_.

### Excess Returns

**ROIC − WACC ≈ 8.3% − 10.0% ≈ −1.7% (TTM, reported).** The spread is currently _negative_ and has been shrinking from a +6pt FY2024 peak. It can only persist if (a) goodwill from Rhode is repaid by real incremental earnings and (b) the core brand keeps taking share at stable margins. The competitive advantage (value positioning, marketing) is **Moderate-to-Strong** — real, but narrower than the growth narrative implies, because it is a positioning advantage rather than a structural (cost/network/regulatory) one, and it faces a finite shelf-space ceiling plus relentless new entrants.

**Competitive Advantage Rating: Moderate** (flagship brand strong; structural durability limited).

---

# 4. Management & Capital Allocation

### Capital Allocation (observable record)

- **Internal reinvestment:** High — marketing ~24% of sales, R&D-ish product innovation, retail display capex. Attractive returns on this spend historically.
- **Acquisitions:** Naturium ($333M, Oct 2023) and **Rhode ($897.5M, Aug 2025)** — paid with $590M cash + $300M stock + earnout (max $200M, now marked at $80.8M). These are **large, debt-funded bets on celebrity/indie brands at rich multiples** that have ballooned goodwill to $853M and driven ROIC below cost of capital. Verdict: speculative capital allocation — accretive to _growth_ but dilutive to _returns on capital_.
- **Dividends:** None; no plans (credit agreement restricts).
- **Buybacks:** $100M deployed since FY25 ($50M @ $79.84 Dec-25; $50M @ $55.53 May-26 — the May repurchase at $55.53 was value-accretive; earlier ones less so). $350M remaining authorized. Modest, price-disciplined so far.
- **Debt:** $834M (term loan + revolver), all maturing ~2030, ~5.4% fixed-ish; net debt ~$490M (~0.9× EBITDA); interest coverage ~4.3–6.5×; covenant floor 3.5×. Manageable but limits buyback/dividend flexibility.
- **SBC / dilution:** **This is the weakest part of the story.** SBC $86.9M FY26 = **~3.3× net income**; ~1.5M RSUs outstanding + $102.8M (FY26) / $164.2M (Q1 FY27) unrecognized comp to vest over ~2.8 years; share count up ~3%/yr despite buybacks. Equity is being handed to employees at a pace that materially dilutes shareholders.
- **Does management understand cost of capital?** Partially — they raised debt at ~5.4% to buy growth that, on a GAAP-ROIC basis, returns below the ~10% cost of capital. The strategy optimizes revenue growth, not returns on invested capital.

### Incentives

- CEO Tarang Amin (Chairman & CEO); CFO Mandy Fields; all employees receive annual equity (a deliberate "team of owners" model).
- Compensation tied to financial performance + stock; base salaries frozen; ~94% of exec comp at-risk; PSUs tied to sales CAGR and share-price performance; ~95% say-on-pay support.
- **Incentive skew:** toward **revenue growth and stock price** (PSUs on sales CAGR), which encourages the acquisition-and-reinvest flywheel even when ROIC is below cost of capital. Insider selling via 10b5-1 plans (CEO/COO/CFO) is routine; insider ownership ~2.6% (low).

**Management Quality Rating: Good** (execution and brand-building excellent; capital allocation and SBC discipline mediocre).

---

# 5. Accounting & Earnings Normalization

### Earnings Quality

- **Net income vs OCF:** FY26 NI $26.3M vs OCF $212.5M — the gap is D&A, SBC, and the non-cash earnout charge. Reported NI understates underlying cash generation, but OCF also ignores SBC as a real cost.
- **SBC — the key adjustment:** $86.9M FY26 (5.3% of revenue), growing 2× revenue. **Do not add it back.** Treat it as an operating expense (which is how EBIT margin is computed here) — it genuinely dilutes shareholders.
- **One-time items:** (1) $57.6M non-cash Rhode contingent-consideration charge (FY26) and $16.1M (Q1 FY27) — a real economic claim (sellers get up to $200M) but non-cash and volatile; (2) **$50.1M one-time IEEPA tariff refund** (Q1 FY27, in COGS; +$2.1M interest) — **one-time, must be normalized out of margins** (Q1 GM 83% vs ~72.7% ex-refund); (3) $47.1M Rhode seller-expense assumption (FY26) and $7.7M acquisition costs; (4) $15M §162(m) non-deductible comp (inflated FY26 effective tax rate to 35%).
- **Goodwill/intangibles:** $853M goodwill + $542M intangibles (37% of assets) — no impairments recorded, but the balance sheet is goodwill-heavy; a Rhode disappointment would test it.
- **Contingent consideration:** $80.8M liability (earnout, max $200M) — a real future cash claim that should reduce equity value; not in the model's cash/debt line (noted qualitatively).
- **Receivables/inventory:** AR $175M (~36 DSO), inventory $247M (~46 DOI) with $15.5M excess/obsolete reserve — reasonable, no red flags.

### Normalized Earnings (my base-year set)

- Normalized revenue run-rate: **$1,636M (FY26)** — I anchor Y0 to the last audited year and let Y1 growth (19%) carry to FY27 guidance (~$1,947M), avoiding the double-count risk of using a refund-inflated TTM base.
- Normalized EBIT margin: **13.0%** (below FY27 guided ~13–16% ex-refund EBIT; above FY26 normalized ~8%; reflects full-year Rhode + pricing + tariff normalization) — an estimate, deliberately moderate.
- Normalized tax rate: **25%** (FY25 23% / Q1 FY27 29.4% / FY26 35%-distorted; cash taxes $21.4M on $40.5M pretax ≈ 53% cash rate FY26 but distorted by refund timing — 25% is the forward normalized estimate).
- Normalized capex: ~$25M/yr (~1.3–1.5% of sales).
- Normalized working capital: roughly neutral (~2–4% of sales).
- **Numbers to NOT use directly:** FY26 GAAP NI ($26.3M) and EBIT ($73.6M) — both distorted by the earnout mark and §162(m); Q1 FY27 GM (83%) — refund-inflated; TTM margins — include the one-time refund.

### Special Issues

- **Stock-based compensation / dilution:** Material — handled as an expense in margins; ~1.5M RSUs + ~0.55M options outstanding; unrecognized comp $164M.
- **Convertible/restricted stock:** No converts; RSUs only.
- **Leases:** $97M operating-lease liabilities (capitalized, included in the $929M debt line).
- **Minority interests / cross-holdings:** None material; Keys Soulcare transferred out (May 2026).
- **Contingent liabilities:** $80.8M Rhode earnout (up to $200M); securities class action (Nov-2024 statements survived MTD) + 5 derivative suits — downside legal exposure, unquantifiable.
- **Excess cash:** $344M cash vs $834M debt → net debt $490M (or ~$585M incl. leases). No excess cash beyond operating needs.

---

# 6. Growth Analysis

### Growth Decomposition (FY26: +$323M)

- **Rhode acquisition:** +$293.5M (91% of growth) [SEC 10-K][6]
- **Organic legacy (e.l.f./SKIN/Naturium/Well People):** +$29.5M (~+2%) — i.e., the _core_ brand grew ~2%, not 25%
- **Price/mix:** +$333.5M vs **volume: −$10.5M** — growth is 100% price, 0% units
- **Geography:** US +$228M (+21%), International +$94.6M (+38%) [10-K][6]

Q1 FY27: +$125.6M (+36%) — Rhode ~$160M of it; **organic ex-Rhode declined high-single-digit**; price/mix +$137.4M vs volume −$11.7M; US +29%, Intl +61% [10-Q][7].

### Fundamental Growth

Expected growth = Reinvestment Rate × ROIC. At a 19% Y1 growth assumption with 40% incremental ROIC, the implied reinvestment rate is ~47% of NOPAT — i.e., e.l.f. must recycle ~half its operating profit into growth each year. That is aggressive but consistent with a company reinvesting ~24% of sales in marketing plus acquisitions. The question is whether **19% growth at stable margins is achievable when (a) the core brand is shrinking on volume, (b) price increases are being walked back, and (c) Rhode's $293.5M contribution is a one-time acquisition comp.**

### Growth Quality

**Moderate-to-Low quality.** A large share of recent growth is (1) acquisition (Rhode), (2) price/mix (which has a ceiling when value is the whole brand promise), and (3) tariff-related accounting (refund). Unit-volume growth — the durable kind — is _negative_. This is the core reason my base case (19% → 3% over ~8 years) is more conservative than the market's.

### Growth Duration

- High-growth: ~5 years (FY27–FY31), 19% → ~5%
- Transition: FY32–FY36, ~3%
- Stable: terminal 3% (in line with long-run nominal GDP for a mature consumer brand)
- **What causes growth to slow:** organic unit volume is already negative; shelf space is finite; value-price positioning caps premiumization; Rhode is a fashion/celebrity cycle; international is real but slow; tariff-driven price increases are reversible.

---

# 7. Risk Analysis

### Business Risk

- **Cyclicality / consumer:** Beauty is discretionary; a consumer recession historically _helps_ e.l.f. (trade-down) but a deep one cuts units. Q1 FY27's +36% was partly a tariff/refund artifact, not a demand surge.
- **Competitive:** Intense — private label, L'Oréal/Coty value lines, and a flood of indie brands; e.l.f.'s price gap (vs prestige) is its moat but also caps its pricing power.
- **Technological / social:** TikTok/Social algorithm dependence; Gen-Z trend cycles are fast; a brand-loyalty shift (or influencer scandal) can move the needle quickly.
- **Customer concentration:** Target 18% + Walmart 13% + Amazon 11% + Sephora 10% = **52% of sales, with no firm purchase contracts** [SEC 10-K][6]. Losing or de-emphasizing one retailer is a double-digit revenue event. (Ulta fell from 16%→<10% of sales in two years.)
- **Supplier/geopolitical:** Majority of product sourced from China — Section 301 tariffs (10–12.5% since Jul 2026), Section 122 litigation, IEEPA refund cliff, port/supply risk. FX exposure to GBP/EUR/RMB.
- **Key-person:** Hailey Bieber is essential to Rhode; CEO succession risk.
- **Regulatory:** FDA/MoCRA cosmetics rules, OTC drug (sunscreen/acne) requirements, class-action/derivative litigation.

### Financial Risk

- Debt $834M (bank) at ~5.4% variable-ish; $744M due 2030 — back-loaded but manageable; net debt ~0.9× EBITDA; interest coverage ~4.3× (covenant 3.5×) — thin-ish buffer for a high-growth company that also funds buybacks and acquisitions.
- Operating leverage: high GM + fixed SG&A means small volume swings hit EBIT hard (FY26's 1.6% net margin demonstrates this).
- Failure risk (probability of severe distress): **low** — Altman Z 3.7, $344M cash + $243M revolver, and the business generates cash. Probability of _permanent capital impairment / multiple compression_: moderate (a 26x fwd P/E can de-rate toward a value-beauty multiple of 12–15x, as it did from $151→$49).

### Valuation Risk (how much optimism is embedded)

The price embeds Bull-case economics (see §12, §15): sustained ~30% Y1 growth or ~35% terminal margins, or a WACC far below the beta-1.56 CAPM. Value is highly sensitive to growth, margin, and discount rate (§14).

---

# 8. Cost of Capital & Required Return

### Cost of Equity

- **Risk-free rate: 4.74%** (US 10-year Treasury — Damodaran's current convention, Aug 2026) [Damodaran][9].
- **Equity risk premium: 4.28%** (implied ERP, trailing 12-mo adjusted payout, Aug 1 2026) [Damodaran][9]. (His alternate net-cash-yield estimate is 3.94%; using the headline 4.28%.)
- **Beta: ~1.50** (5-year 1.56 from market data [StockAnalysis][4]; slight mean-reversion toward 1.4 — the business is consumer staples but the growth story is high-volatility; a leveraged balance sheet raises it).
- **Cost of equity = 4.74% + 1.50 × 4.28% = ~11.2%.** No country-risk premium (US-only listing, US-centric revenue); no arbitrary company-specific premium (captured via scenario WACC adjustments).

### Cost of Debt

- Pre-tax: **~5.4%** (stated rate on the credit facilities at Mar/Jun-2026) [SEC 10-K][6][10-Q][7].
- Tax rate 25% → **after-tax cost of debt ≈ 4.05%.**

### Capital Structure (market values)

- Equity: $5,400M (85.3%) · Debt+leases: $929M (14.7%) → total $6,329M.
- Target structure assumed roughly stable (management prefers leverage for acquisitions).

### WACC

**WACC = 0.853 × 11.2% + 0.147 × 4.05% ≈ 10.1% → used 10.0%** (rounded; scenario adjustments raise it to 13% in Severe Bear and lower it to 9% in Extreme Bull). Cross-check: StockAnalysis computes WACC 11.5% — mine is modestly _lower_ (lenient), which makes the bearish conclusion conservative, not aggressive.

**ROIC (8–16%) vs WACC (10%):** growth is currently **value-neutral to value-destroying** on total capital. This is the crux of the whole valuation: e.l.f.'s reinvestment flywheel only creates value if incremental ROIC comfortably exceeds ~10%, which the goodwill-laden balance sheet now obscures.

---

# 9. Intrinsic Valuation — Primary Analysis (FCFF DCF)

**Model:** Two-stage FCFF DCF, 10-year explicit period, Gordon terminal value, g/ROIC-consistent reinvestment, WACC = scenario-adjusted cost of capital. Cash flows are NOPAT × (1 − g/ROIC). This is the exact structure of the official workbook (`ELF_Damodaran_Financial_Model.xlsx`), so the numbers below reproduce it.

### Base-Year Normalization (Y0 = FY2026)

- Revenue: $1,636.5M
- EBIT margin: 13.0% (Y1) → NOPAT margin ~9.75% (after 25% tax)
- Tax rate: 25% · ROIC (initial): 40% → terminal 20%
- Reinvestment: via g/ROIC (at 19% growth / 40% ROIC → 47.5% of NOPAT in Y1)
- Terminal growth 3% < WACC 10%

### 10-Year Base-Case Forecast ($M) — matches workbook DCF-Base

| Year | Revenue | Growth | EBIT Margin | EBIT | NOPAT | Reinvest. | FCFF | PV @10% |
| ---- | ------- | ------ | ----------- | ---- | ----- | --------- | ---- | ------- |
| 1    | 1,947   | 19.0%  | 13.0%       | 253  | 190   | 90        | 100  | 91      |
| 2    | 2,249   | 15.5%  | 13.4%       | 301  | 226   | 93        | 133  | 201     |
| 3    | 2,519   | 12.0%  | 13.8%       | 348  | 261   | 88        | 173  | 331     |
| 4    | 2,733   | 8.5%   | 14.2%       | 388  | 291   | 74        | 217  | 479     |
| 5    | 2,870   | 5.0%   | 14.6%       | 419  | 314   | 51        | 264  | 642     |
| 6    | 2,956   | 3.0%   | 15.0%       | 443  | 333   | 35        | 298  | 811     |
| 7    | 3,045   | 3.0%   | 15.0%       | 457  | 343   | 39        | 304  | 967     |
| 8    | 3,136   | 3.0%   | 15.0%       | 470  | 353   | 43        | 310  | 1,111   |
| 9    | 3,230   | 3.0%   | 15.0%       | 485  | 363   | 49        | 314  | 1,244   |
| 10   | 3,327   | 3.0%   | 15.0%       | 499  | 374   | 56        | 318  | 1,367   |

**Key assumptions:** Revenue compounds ~7.4% CAGR over 10 years to $3.33B (2.0× FY26) — sustained share gains in mass beauty + Rhode + international + haircare, but _nothing like_ the last four years. Margins ramp 13%→15% (below the 18–20% some bulls use, because marketing must stay ~24% of sales and Rhode margins normalize). Reinvestment falls from 47.5% to 15% of NOPAT as growth fades — the flywheel matures into a cash generator.

### Terminal Value & Equity Value

- Terminal FCFF = NOPAT₁₀ × (1+g) × (1 − g/ROIC_term) = 374 × 1.03 × (1 − 0.03/0.20) = **$313M**
- **Terminal value = $313M / (10% − 3%) = $4,681M** → PV = $1,805M
- **PV of explicit FCFF = $1,367M** → **Enterprise value = $3,172M**
- Less net debt $585M (debt $929M − cash $344M) → **Equity value = $2,587M**
- **Intrinsic value = $2,587M / 59.01M shares = $43.84/share**
- Terminal value / EV = 57% (reasonable — not a red flag; high-growth valuations legitimately concentrate value late).

---

# 10. Terminal Value

- **Stable growth = 3.0%** (< WACC 10% in every scenario; ✓ enforced by workbook checks). Below long-run nominal GDP (~4%), appropriate for a mature mass beauty brand facing a shelf-space ceiling.
- Stable margin: 15% EBIT (a high bar vs peers: EL 10.4% TTM/18% peak, ULTA 12.4%, COTY 6.1%) — already generous.
- Stable ROIC: 20% > WACC 10% — the terminal state assumes e.l.f. keeps a real (if modest) excess return, i.e., the brand moat survives.
- Terminal reinvestment rate = g/ROIC = 3%/20% = 15% — internally consistent.
- **What does TV assume about 2036?** That e.l.f. is a ~$3.3B-revenue, 15%-EBIT-margin, stable-growth mass beauty leader with a durable value positioning — not a declining relic, not a prestige powerhouse. That is a fair, non-heroic central assumption.
- TV/EV = 57% — highlighted as the largest single value component and thus the most assumption-sensitive.

---

# 11. Relative Valuation

| Metric         | **ELF**  | EL (Estée Lauder) | ULTA   | COTY  | Peer set read                       |
| -------------- | -------- | ----------------- | ------ | ----- | ----------------------------------- |
| Revenue (TTM)  | $1.76B   | $14.8B            | $12.7B | $5.8B | ELF is small — all upside is growth |
| Revenue growth | +31%     | +0.3%             | +11%   | −3.6% | ELF far faster                      |
| Gross margin   | 74.4%    | 74.7%             | 43.2%  | 63.2% | GM ≈ EL, way above ULTA             |
| EBIT margin    | 11.7%    | 10.4%             | 12.4%  | 6.1%  | Mid-pack                            |
| P/E (fwd)      | **29.5** | 28.5              | 17.2   | 8.8   | **~Top of set**                     |
| EV/EBITDA      | **23.0** | 15.9              | 12.7   | 7.0   | **≈2× the peer average**            |
| EV/Sales       | 3.39     | 2.10              | 1.73   | 0.43  | Top of set                          |
| ROIC (TTM)     | 8.3%     | low               | ~19%   | n/m   | Weak vs cost of capital             |

[StockAnalysis][2][3][4] and EL/ULTA/COTY pages [10][11][12].

**Why do the multiples differ?** ELF deserves a premium for growth and gross margin — but it trades at a **PEG ~2.4** and ~23x EV/EBITDA, i.e., the _price already pays full value for the growth_. Peers (EL 15.9x, ULTA 12.7x, COTY 7.0x) trade at 12–16x EV/EBITDA. On a fundamental-multiple basis (growth×margin×ROIC vs risk), a justified EV/EBITDA for ELF is ~15–18x, implying ~$55–70/share — consistent with my DCF range and well below $91.44. **ELF is the most expensive stock in its peer set on every operating multiple.**

---

# 12. Reverse DCF — What Does the Market Price Assume?

**Starting price:** $91.44 → equity value $5,396M + net debt $585M = **implied EV $5,981M** (matches the $5.98B market EV).

Using the same DCF structure (WACC 10%, terminal g 3%, terminal ROIC 20%), I solved for the fundamentals that make value = $91.44:

1. **Implied Y1 growth: ~33%** (vs. base 19%, and vs. management's own FY27 guidance of 18–20%). With a 3.5pt/yr decay, that means ~20%+ growth for 6–8 years — a decade of ~20% compounding on a base that grew only ~2% organically last year.
2. **Implied terminal EBIT margin: ~35%** (vs. base 15%) at base-case revenue — absurd for mass beauty (even premium peers peak ~20%).
3. **Implied terminal growth: ~8%** at base fundamentals — far above the 3% stable-growth norm and dangerously close to the discount rate.
4. **Implied WACC:** even at an unsustainably low 8.5% cost of capital, base fundamentals only produce ~$60/share — **no plausible discount rate justifies $91.44 with base-case fundamentals.**
5. **Frontier at WACC 10%:** to hit $91.44, Y1 growth must be ~32–36% across all plausible terminal margins (13–21%). That is my **Extreme Bull** territory.

> **"At today's price of $91.44, the market is implicitly assuming e.l.f. sustains ~30–35% year-one growth — roughly double management's own 18–20% guidance — compounding to >$8B of revenue (vs my ~$3.3B base) at 15%+ margins, or a ~35% terminal margin, or a cost of capital far below what a beta-1.56, China-exposed, 52%-customer-concentrated business warrants."**

These assumptions are **aggressive to implausible.** The market is not pricing the base case; it is pricing a sustained Bull-to-Extreme-Bull outcome.

---

# 13. Scenario Valuation

Five scenarios (probabilities sum to 1.0; terminal growth < WACC in every scenario; values from the official workbook model). WACC/margin/growth adjustments as in `ELF_model_inputs.json`.

| Scenario                                                                                                                | Prob | Y1 Growth | Terminal EBIT mgn | WACC  | Term. g | **Value/share** | vs $91.44 |
| ----------------------------------------------------------------------------------------------------------------------- | ---- | --------- | ----------------- | ----- | ------- | --------------- | --------- |
| **Severe Bear** — tariff regime returns, mass-beauty recession, Rhode turns, margins to high-single digits, risk spikes | 10%  | 6%        | 11%               | 13.0% | 2.0%    | **$8.29**       | −91%      |
| **Bear** — organic e.l.f. stays weak, Rhode normalizes, margins flat, higher risk                                       | 20%  | 12%       | 13%               | 11.5% | 2.5%    | **$19.29**      | −79%      |
| **Base** — FY27 guide 18–20%, margin ramp to 15%, ROIC erodes with goodwill                                             | 35%  | 19%       | 15%               | 10.0% | 3.0%    | **$43.84**      | −52%      |
| **Bull** — organic re-accelerates, Rhode scales, margin expansion, tariff relief                                        | 25%  | 25%       | 17.5%             | 9.5%  | 3.5%    | **$84.31**      | −8%       |
| **Extreme Bull** — global share gains, ~20% EBIT margin, durable low risk                                               | 10%  | 30%       | 20%               | 9.0%  | 4.0%    | **$159.77**     | +75%      |

- **Probability-weighted intrinsic value = 0.10×8.29 + 0.20×19.29 + 0.35×43.84 + 0.25×84.31 + 0.10×159.77 = $57.08**
- **Expected upside/downside vs $91.44 = −37.6%**
- Even the **Bull case ($84) is below the current price** — only the 10% Extreme-Bull outcome makes new buyers money.

---

# 14. Sensitivity Analysis

**WACC × Terminal Growth (base-case share value):**

| WACC \ g  | 2.0%    | 2.5%    | 3.0%    | 3.5%    | 4.0%    |
| --------- | ------- | ------- | ------- | ------- | ------- |
| 8.5%      | $55     | $57     | $60     | $63     | $67     |
| 9.0%      | $50     | $51     | $54     | $56     | $59     |
| 9.5%      | $45     | $47     | $48     | $50     | $53     |
| **10.0%** | **$41** | **$42** | **$44** | **$45** | **$47** |
| 10.5%     | $38     | $39     | $40     | $41     | $43     |
| 11.0%     | $35     | $36     | $37     | $38     | $39     |
| 11.5%     | $32     | $33     | $34     | $34     | $35     |

**Key findings:**

- **Base value is robust: $32–$67 across a wide and generous WACC (8.5–11.5%) × terminal-growth (2–4%) space.** Only the top-left corner (WACC 8.5% + g 4%) approaches $67 — still 26% below $91.44.
- **Discount rate is the dominant lever** (as always): every +100bps of WACC ≈ −$7–8/share.
- **Terminal growth** is second-order within the disciplined range (tg must stay < WACC).
- Growth and margin sensitivity (from the scenario ladder): value is roughly linear in margin (±$5/share per point of terminal EBIT margin) and highly convex in the _duration_ of high growth (Bull at 25% Y1 → $84; Base at 19% → $44).
- **Valuation-critical assumptions (ranked):** (1) sustained Y1 growth / growth duration, (2) WACC, (3) terminal EBIT margin. Reinvestment/ROIC matters but is secondary given the asset-light model.

---

# 15. Market Expectations vs Fundamental Reality

- **A. Market price:** $91.44 = 26x FY27 EPS guidance ($3.50–3.55), ~23x EV/EBITDA, PEG 2.4.
- **B. Market-implied fundamentals (reverse DCF):** ~30–35% Y1 growth sustained for a decade / ~$8B terminal revenue / ~35% terminal margin / or a sub-8.5% discount rate.
- **C. My fundamental forecast:** ~19% Y1 growth decaying to 3%, 13→15% margins, 40→20% ROIC, WACC 10%, terminal g 3% → **$43.84 base**, **$57.08 weighted**.

**Price ($91.44) > Value (weighted $57.08) — the market is materially more optimistic than reasonable fundamentals support.** The market's error is treating a price-led, acquisition-inclusive growth rate (+25–36%) as if it were durable organic volume growth, and paying for it at a beta-1.56 cost of capital it never discounts. It is also implicitly assuming the ~$50M tariff refund and the Rhode honeymoon repeat forever. Reality check: organic e.l.f. volume is negative; the market has already been wrong here once (stock −76% from its $151 high to the $49 low, then re-rated to $91 on one refund-flattered quarter).

---

# 16. Real Options & Optionality

- **International expansion:** Real but modest option — 21% of sales, growing; UK/Germany/Canada plus new markets (Brazil, 19-country Europe). Would add value if unit economics hold; currently priced in by the market, not a free option.
- **Adjacent categories:** e.l.f. Hair (June 2026) is a genuine, small option on a new aisle; skincare (Naturium, Rhode, e.l.f. SKIN) is the bigger runway. These are partially priced in.
- **DTC/Beauty Squad loyalty data:** A data/marketing advantage with option value, but not monetizable at scale like a tech platform.
- **Abandonment / put options:** The brand portfolio could be broken up (Rhode, Naturium are separable), but there is no evidence management would monetize.
- **Verdict:** Meaningful but _quantifiable optionality is modest_; I do not assign a premium because the market already prices a decade of ~20% growth, which _is_ the option value being paid for upfront. Any "optionality premium" would double-count.

---

# 17. Special Valuation Situations

- **Young/high-growth company with volatile earnings:** Yes — this is why a scenario-weighted, fundamentals-driven DCF (rather than a point multiple) is the right framework; FY26 GAAP earnings (1.6% net margin) are not representative, so normalization is essential.
- **Negative/one-time-distorted earnings:** Handled by normalizing margins (13%) and tax (25%), and by excluding the one-time tariff refund from margins.
- **Company with substantial intangibles/employee options:** Yes — $1.4B goodwill+intangibles and SBC ~5% of revenue. Handled by (a) treating SBC as an expense in margins and (b) using g/ROIC reinvestment so the goodwill-laden balance sheet's low ROIC constrains value-creation.
- **Not** distressed, financial, commodity, or conglomerate. A standard two-stage FCFF DCF with scenario weighting is appropriate. No model switch required.

---

# 18. Valuation Error & Uncertainty

- **Estimation uncertainty (inputs):** Moderate — margins (13→15%), growth duration, and ROIC path are estimates; the tariff regime is genuinely unpredictable (refund cliff, Section 301, Section 122 litigation).
- **Economic uncertainty (business can change):** High — organic volume is negative; Rhode is a celebrity-cycle business; retailer concentration is extreme; a recession could help (trade-down) or hurt (units).
- **Information uncertainty:** Moderate — 10-K/10-Q are timely and audited, but Rhode results are consolidated only ~11 months, PPA was just finalized, and the earnout math is opaque.
- **Model uncertainty:** Moderate — g/ROIC reinvestment is the right Damodaran structure but treats all "reinvestment" as return-seeking capital; marketing spend (the real reinvestment) is expensed, so the model likely _overstates_ reinvestment efficiency.
- **Robustness:** Base value stays $32–$67 across a deliberately wide WACC/g grid and $8–$160 across scenarios. The conclusion — price > value — is robust: **even the most favorable reasonable input set (WACC 8.5%, g 4%) yields $67, still below $91.44.**

**Valuation confidence: MEDIUM** (the direction — overvaluation — is high-confidence; the magnitude has a wide error band).

---

# 19. Inversion: What Would Make This Investment Fail?

Work backward from permanent capital loss at $91.44 (a 50%+ drawdown, which the stock already demonstrated over the past year):

1. **The price-led growth collapses.** If price increases are walked back (they already are) and Rhode's organic contribution fades while core e.l.f. volume stays negative, revenue growth falls to single digits — the 26x multiple de-rates to a 12–15x value-beauty multiple. This alone produces a $40–55 outcome (my Bear/Base) — a permanent −40–50% loss from today.
2. **Rhode disappoints.** It is ~$160M/quarter and the reason for $2B of market cap; it is a celebrity-brand cycle with an $80.8M earnout mark and an $897.5M purchase price. A Rhode stall (founder fatigue, trend shift) triggers earnout reversal, possible goodwill/intangibles impairment ($1.4B on the books), and a multiple reset.
3. **Tariff re-escalation + refund cliff.** The Q1 GM 83% was 1,050bps of one-time refund. If Section 301/122 tariffs re-ratchet costs and refunds stop, FY27 guidance (which already assumes GM flat ex-refund) is at risk — and the market is paying for _expansion_.
4. **Retailer concentration.** Target (18%) + Walmart (13%) + Amazon (11%) + Sephora (10%) = 52% with no contracts; a single retailer de-stocking or re-allotting shelf space is a double-digit revenue event (Ulta already fell 16%→<10%).
5. **SBC + dilution compounding.** ~3% annual share dilution means even flat value-per-share requires real cash-flow growth.

**The three assumptions whose failure most damages the thesis:** (1) sustained ~20%+ organic-compounded growth, (2) margin expansion to 15%+ while holding ~24% marketing, (3) no tariff re-escalation. All three are already under visible stress.

---

# 20. Probability-Weighted Investment Case

| Scenario     | Prob | Value/Share | Return vs $91.44 | Key Assumptions                                                       |
| ------------ | ---- | ----------- | ---------------- | --------------------------------------------------------------------- |
| Severe Bear  | 10%  | $8.29       | −90.9%           | Tariff shock; organic decline; Rhode reversal; margins ~11%; WACC 13% |
| Bear         | 20%  | $19.29      | −78.9%           | Organic weak; Rhode normalizes; flat margins; WACC 11.5%              |
| Base         | 35%  | $43.84      | −52.1%           | FY27 guide met; margin ramp to 15%; ROIC erodes                       |
| Bull         | 25%  | $84.31      | −7.8%            | Organic re-accelerates; margins 17.5%; WACC 9.5%                      |
| Extreme Bull | 10%  | $159.77     | +74.7%           | Global share gains; ~20% margins; low risk                            |

- **Probability-weighted intrinsic value: $57.08** (expected return **−37.6%** from $91.44)
- **Expected annualized return (5-yr): ≈ −9.0%**
- Downside risk: 45% probability-weighted loss of −79% to −91% if the two bear scenarios hit (30% combined probability) — a genuinely skewed payoff: the downside cases are large and the upside cases (Bull/Extreme Bull, 35% combined) are the only ones that pay.
- **Asymmetry: unfavorable.** The expected value is 38% below the price; the reward/risk is roughly 0.6:1 in a buyer's favor at current prices. The stock is a _sale/avoid_ at $91.44 and becomes interesting only below ~$55 (where weighted value ≈ price with a margin) and compelling below ~$45.

---

# 21. Investment Decision

### Valuation Rating

**D — AVOID / SIGNIFICANTLY OVERVALUED.**

The price ($91.44) embeds expectations (≈30–35% sustained Y1 growth or ≈35% terminal margins or <8.5% WACC) that are materially more optimistic than reasonable fundamentals (≈19% decaying growth, ≈15% terminal margin, ≈10% WACC). The risk/reward at the current price is poor: probability-weighted value is −38% below price, expected annualized return is negative, and even the Bull case does not clear the price. This is not a "good company, buy it" situation — it is a good company whose growth is largely acquired/price-led, whose ROIC sits below its cost of capital, and whose market price already capitalizes the most favorable scenario.

### Final Outputs

**Current Price:** $91.44
**Severe Bear Value:** $8.29
**Bear (Conservative) Value:** $19.29
**Base Intrinsic Value:** $43.84
**Bull Value:** $84.31
**Extreme Bull Value:** $159.77
**Probability-Weighted Value:** $57.08
**Expected Upside/Downside:** −37.6%
**Expected Annualized Return (5-yr):** −9.0%
**Margin of Safety at $91.44:** None (negative)
**Buy zone:** First tranche ≤ $55 · accumulate $45–55 · conviction < $45
**Valuation Confidence:** Medium
**Investment Rating:** **D — Avoid / Significantly Overvalued**

---

# 22. The Five Most Important Conclusions

1. **The Business:** e.l.f. is a genuinely strong _value_ beauty franchise — premium quality at a $5–$13 price point with a best-in-class social marketing engine — but its recent "growth" is largely acquisition-driven (Rhode = 91% of FY26 growth) and price-led (volume is negative). The core brand is not compounding at the headline rate.
2. **The Economics:** The decisive driver of long-term value is whether incremental ROIC comfortably exceeds the ~10% cost of capital. Right now reported ROIC (~8–16%) is _below_ the cost of capital because $897M of Rhode goodwill and $600M of debt weigh on the denominator — growth is currently value-neutral-to-destructive on total capital, and only a long margin ramp to 15%+ repairs that.
3. **The Market's Expectations:** At $91.44 (26x fwd EPS, ~23x EV/EBITDA — the top of its peer set), the market implicitly prices ~30–35% year-one growth sustained for a decade, ~35% terminal margins, or a sub-8.5% discount rate. That is Bull-to-Extreme-Bull economics being paid for today.
4. **The Valuation:** The most defensible estimate is a probability-weighted intrinsic value of **~$57/share** (base ~$44, range $8–$160), from a scenario-weighted 10-year FCFF DCF at a ~10% WACC. The estimate is robust: even a generous WACC-8.5%/g-4% input set yields only ~$67.
5. **The Investment Decision:** At $91.44 the expected return is negative (−38% to probability-weighted value; −9% annualized) — the price does not compensate for the risk. **Avoid at current levels; the stock becomes attractive only below ~$55 and compelling below ~$45.**

---

# 23. Damodaran-Style Final Judgment

> **"At a price of $91.44, the market is effectively assuming e.l.f. Beauty grows ~30–35% a year for the better part of a decade — roughly double management's own 18–20% FY27 guidance — and sustains ~15–20% margins, at a discount rate far below what a beta-1.56, China-exposed, 52%-concentrated-customer business warrants. My valuation implies ~$57 (weighted; ~$44 base) because I expect growth to converge toward ~3% as the acquisition and pricing tailwinds fade, margins to rise only to ~15%, and the cost of capital to be ~10%, not 7%. The biggest risk to this valuation is that I am too bearish on growth duration and e.l.f. genuinely becomes the mass L'Oréal — a real, if 10%-probability, outcome. Therefore, at today's price, I would avoid the stock because the market has already paid for the Bull case, leaving no margin of safety and a negative expected return. The opportunity is at the price, not the company: wait for $55, get interested at $45."**

---

## Sources

1. SEC EDGAR company filings index (CIK 0001600033): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001600033&type=10-K&dateb=&owner=include&count=40
2. StockAnalysis ELF overview: https://stockanalysis.com/stocks/elf/
3. StockAnalysis ELF financials: https://stockanalysis.com/stocks/elf/financials/
4. StockAnalysis ELF statistics (beta, ROIC, EV/EBITDA, WACC, short interest): https://stockanalysis.com/stocks/elf/statistics/
5. StockAnalysis ELF balance sheet: https://stockanalysis.com/stocks/elf/financials/balance-sheet/
6. SEC Form 10-K FY2026 (filed 2026-05-21): https://www.sec.gov/Archives/edgar/data/1600033/000160003326000020/elf-20260331.htm
7. SEC Form 10-Q Q1 FY2027 (filed 2026-08-06): https://www.sec.gov/Archives/edgar/data/1600033/000160003326000040/elf-20260630.htm
8. e.l.f. Beauty Investor Relations: https://investor.elfbeauty.com/
9. Damodaran — historical & current implied equity risk premium (implied ERP Aug 1 2026 = 4.28%; US 10-yr 4.74%): https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/implpr.html and https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm
10. StockAnalysis Estée Lauder (EL) financials: https://stockanalysis.com/stocks/el/financials/
11. StockAnalysis Ulta Beauty (ULTA) financials: https://stockanalysis.com/stocks/ulta/financials/
12. StockAnalysis Coty (COTY) financials: https://stockanalysis.com/stocks/coty/financials/
13. Reuters — e.l.f. Beauty raises annual forecasts: https://www.reuters.com/business/retail-consumer/elf-beauty-raises-annual-forecasts-value-bet-pays-off-2026-08-05/
14. CNBC — e.l.f. Beauty sees $50M windfall in tariff refunds, profits surge: https://www.cnbc.com/2026/08/05/elf-beauty-elf-q1-2027-earnings.html
15. Business Wire — e.l.f. Beauty Q1 FY2027 results: https://www.businesswire.com/news/home/20260805101140/en/e.l.f.-Beauty-Announces-First-Quarter-Fiscal-2027-Results/
16. WSJ — Hailey Bieber's Rhode Powers e.l.f. Beauty's Sales Growth: https://www.wsj.com/business/retail/hailey-biebers-rhode-powers-e-l-f-beautys-sales-growth-c3dd0a99

_Every figure above traces to a cited source or is explicitly labeled an estimate (notably: normalized EBIT margin 13%, normalized tax rate 25%, terminal margins 15%, ROIC path 40%→20%, scenario probabilities). FY27 guidance figures (sales $1.94–1.97B, adj EBITDA $401–407M, adj EPS $3.50–3.55) come from the Q1 FY27 earnings release [13][14][15]._
