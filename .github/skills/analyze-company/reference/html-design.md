# HTML Investment Report — Design System

Use this design system for `{ticker}-consensus-investment-report.html`. The
bundled `reference/example-report.html` (the IREN report) is the concrete
anchor: **copy its entire `<style>` block verbatim** into the new report, then
rebuild the `<body>` content for the company being analyzed. Do not redesign
the CSS — consistency with the house style matters more than novelty.

## Hard constraints

- Single file, zero external dependencies: no CDN fonts, no CSS/JS includes,
  no web fonts. System font stack only.
- Must render correctly opened directly via `file://` in a browser. Verify by
  actually opening it in the browser after writing.
- Every number must match `consensus-analysis.md` and the verified workbook
  exactly. No new valuation math belongs in the HTML.

## Design tokens (from the IREN report CSS)

```text
--navy #0b1b33   --navy-2 #122a4d    --ink #1a2332
--muted #5b6675  --line #e3e8ef      --bg #f5f7fa
--card #ffffff   --gold #c9971c      --amber-bg #fdf3dd
--green #1d7a4f  --green-bg #e8f4ee  --red #b3402f
--red-bg #fbeae7 --blue #2563ab      --blue-bg #eaf2fb
--radius 14px
```

Typography: system font stack, body 16px/1.6, content max-width ~1060px in a
`.wrap` with 24px side padding.

## Page anatomy (in order)

1. **Hero header** — navy gradient, kicker ("CONSENSUS INVESTMENT REPORT"),
   H1 `{Company} — Consensus Investment Report`, subtitle (one-paragraph
   synthesis), meta chips row (`NASDAQ: {TICKER}`, report date, reference
   price band), and a `.rating-badge` (gold dot + rating text, e.g.
   `C — HOLD / WATCH`).
2. **Section 01 — Executive Summary** — `.cards` grid (6 cards): consensus
   base value, probability-weighted value, bear/bull range, confidence,
   consensus entry plan, valuation-critical metric. Each card: label, value,
   note.
3. **Section 02 — The Three Positions at the Table** — `.profiles` row of
   three `.profile` cards, one per lens: name, role, verdict (rating + price),
   short position paragraph, `.tags` (base value, weighted value, buy zone,
   confidence).
4. **Section 03 — Points of Agreement** — numbered list or styled two-column
   grid of the uncontested consensus core.
5. **Section 04 — Points of Contention & Resolution** — one block per
   contention: the question, each profile's argument, the resolution.
6. **Section 05 — Consensus Valuation** — styled table of the reconciled
   scenario matrix (scenario × each profile × consensus value × probability),
   the probability-weighted value formula in KaTeX-style text or plain text,
   reverse-DCF check note, confidence.
7. **Section 06 — Pros and Cons** — two-column green/red cards at the current
   price.
8. **Section 07 — Investment Recommendation** — large rating display,
   do-not-initiate statement, **price ladder table** (band → action), upgrade
   triggers, downgrade triggers.
9. **Section 08 — The Five Consensus Conclusions** — five numbered blocks.
10. **Section 09 — Final Judgment** — closing paragraph in a highlighted
    card.
11. **Footer** — disclaimer (estimate of estimates, not investment advice) and
    sources note.

## Component cheat sheet

| Component      | Markup pattern                                                                 |
| -------------- | ------------------------------------------------------------------------------ |
| Section header | `<h2 class="sec"><span class="num">0X</span>Title</h2>`                        |
| Cards          | `<div class="cards"><div class="card"><div class="label">…`                    |
| Profiles       | `<div class="profiles"><div class="profile"><div class="head">…`               |
| Tags           | `<span class="tag">…</span>` / `<span class="tag amber">…`                     |
| Chips          | `<span class="chip">…</span>`                                                  |
| Rating badge   | `<span class="rating-badge"><span class="dot"></span> C — HOLD / WATCH</span>` |
| Tables         | plain `<table>` with a `<thead>`, styled by the copied CSS                     |

Copy the exact class names from `example-report.html` rather than inventing
new ones; the CSS only styles the classes it defines.
