#!/usr/bin/env python3
"""Build a self-contained consensus investment report HTML from a JSON input.

Usage:
    python3 build_report.py <report_inputs.json> [output.html]
    python3 build_report.py --validate <report_inputs.json> [output.html]

Purpose (token optimization): the orchestrator authors a compact
report_inputs.json (~2-4KB, schema in report_inputs.example.json) and this
script renders the full single-file HTML, reusing the house CSS verbatim.
No manual HTML authoring; every figure in the JSON flows straight into the
markup, so numeric consistency is mechanical.

Text conventions (LLM-friendly, safe):
  - All text fields are HTML-escaped automatically: write literal & < >.
  - **bold**  -> <b>bold</b>
  - `code`    -> <code>code</code>

--validate runs structural checks on the generated file (single <style>,
no external URLs, balanced tags, all `figures` strings present).
"""
import html
import json
import re
import sys

REPORT_CSS = """
      :root {
        --navy: #0b1b33;
        --navy-2: #122a4d;
        --ink: #1a2332;
        --muted: #5b6675;
        --line: #e3e8ef;
        --bg: #f5f7fa;
        --card: #ffffff;
        --gold: #c9971c;
        --amber-bg: #fdf3dd;
        --green: #1d7a4f;
        --green-bg: #e8f4ee;
        --red: #b3402f;
        --red-bg: #fbeae7;
        --blue: #2563ab;
        --blue-bg: #eaf2fb;
        --radius: 14px;
        --shadow:
          0 1px 2px rgba(11, 27, 51, 0.06), 0 6px 18px rgba(11, 27, 51, 0.07);
      }
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      html {
        scroll-behavior: smooth;
      }
      body {
        font-family:
          -apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue",
          Arial, sans-serif;
        background: var(--bg);
        color: var(--ink);
        line-height: 1.6;
        font-size: 16px;
      }
      .wrap {
        max-width: 1060px;
        margin: 0 auto;
        padding: 0 24px;
      }

      /* ===== Header ===== */
      header.hero {
        background: linear-gradient(
          135deg,
          var(--navy) 0%,
          var(--navy-2) 60%,
          #1a3d6d 100%
        );
        color: #fff;
        padding: 56px 0 44px;
      }
      .hero .kicker {
        letter-spacing: 0.22em;
        text-transform: uppercase;
        font-size: 12px;
        color: #9fc0e8;
        font-weight: 600;
      }
      .hero h1 {
        font-size: 42px;
        line-height: 1.15;
        margin: 10px 0 6px;
        letter-spacing: -0.02em;
      }
      .hero .sub {
        font-size: 17px;
        color: #c9d8ec;
        max-width: 780px;
        margin-top: 8px;
      }
      .hero .meta-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 26px;
        align-items: center;
      }
      .chip {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 600;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.25);
        color: #e6eef9;
      }
      .rating-badge {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: var(--amber-bg);
        color: #7a5a08;
        border: 2px solid var(--gold);
        border-radius: 12px;
        padding: 10px 18px;
        font-weight: 800;
        font-size: 18px;
        letter-spacing: 0.04em;
      }
      .rating-badge .dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: var(--gold);
        box-shadow: 0 0 0 4px rgba(201, 151, 28, 0.25);
      }

      /* ===== Sections ===== */
      section {
        padding: 48px 0 8px;
      }
      h2.sec {
        font-size: 26px;
        letter-spacing: -0.01em;
        margin-bottom: 6px;
        color: var(--navy);
        padding-bottom: 10px;
        border-bottom: 2px solid var(--line);
      }
      h2.sec .num {
        color: var(--gold);
        font-weight: 800;
        margin-right: 10px;
      }
      h3 {
        font-size: 19px;
        margin: 26px 0 10px;
        color: var(--navy-2);
      }
      p.lead {
        color: var(--muted);
        font-size: 16.5px;
        margin-bottom: 20px;
      }
      .small {
        font-size: 13.5px;
        color: var(--muted);
      }

      /* ===== Cards ===== */
      .cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 16px;
      }
      .card {
        background: var(--card);
        border: 1px solid var(--line);
        border-radius: var(--radius);
        padding: 20px 22px;
        box-shadow: var(--shadow);
      }
      .card .label {
        font-size: 12.5px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--muted);
        font-weight: 700;
      }
      .card .value {
        font-size: 30px;
        font-weight: 800;
        margin: 4px 0 2px;
        color: var(--navy);
        letter-spacing: -0.02em;
      }
      .card .note {
        font-size: 13.5px;
        color: var(--muted);
      }

      /* ===== Profile cards ===== */
      .profiles {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
        gap: 18px;
      }
      .profile {
        background: var(--card);
        border: 1px solid var(--line);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        overflow: hidden;
        display: flex;
        flex-direction: column;
      }
      .profile .head {
        padding: 18px 22px 14px;
        border-bottom: 1px solid var(--line);
      }
      .profile .name {
        font-size: 18px;
        font-weight: 800;
        color: var(--navy);
      }
      .profile .role {
        font-size: 12.5px;
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 2px;
      }
      .profile .body {
        padding: 16px 22px 20px;
        flex: 1;
      }
      .profile .body p {
        font-size: 14.5px;
        margin-bottom: 10px;
      }
      .profile .tags {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 12px;
      }
      .tag {
        font-size: 12px;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 999px;
        background: var(--blue-bg);
        color: var(--blue);
      }
      .tag.amber {
        background: var(--amber-bg);
        color: #7a5a08;
      }
      .tag.green {
        background: var(--green-bg);
        color: var(--green);
      }
      .tag.red {
        background: var(--red-bg);
        color: var(--red);
      }
      .verdict-row {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        gap: 8px;
        margin-top: 4px;
      }
      .verdict-row .v {
        font-size: 15px;
        font-weight: 800;
      }

      /* ===== Tables ===== */
      .table-scroll {
        overflow-x: auto;
        border: 1px solid var(--line);
        border-radius: var(--radius);
        background: var(--card);
        box-shadow: var(--shadow);
      }
      table {
        width: 100%;
        border-collapse: collapse;
        font-size: 14.5px;
        min-width: 640px;
      }
      th {
        text-align: left;
        background: #eef2f8;
        color: var(--navy);
        font-size: 12.5px;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        padding: 12px 16px;
        border-bottom: 1px solid var(--line);
        white-space: nowrap;
      }
      td {
        padding: 11px 16px;
        border-bottom: 1px solid #eef1f6;
        vertical-align: top;
      }
      tr:last-child td {
        border-bottom: none;
      }
      tr.hl td {
        background: #fffaf0;
        font-weight: 700;
      }
      .right {
        text-align: right;
        font-variant-numeric: tabular-nums;
      }

      /* ===== Consensus box ===== */
      .consensus-box {
        background: linear-gradient(135deg, #fffdf5, #fdf6e3);
        border: 1.5px solid var(--gold);
        border-radius: var(--radius);
        padding: 26px 28px;
        box-shadow: var(--shadow);
      }
      .consensus-box h3 {
        margin-top: 0;
        color: #7a5a08;
      }
      .consensus-box .big {
        font-size: 15.5px;
      }

      /* ===== Agreement / contention lists ===== */
      .point-list {
        counter-reset: pt;
      }
      .point {
        display: flex;
        gap: 14px;
        background: var(--card);
        border: 1px solid var(--line);
        border-radius: 12px;
        padding: 14px 18px;
        margin-bottom: 10px;
        box-shadow: var(--shadow);
      }
      .point .n {
        counter-increment: pt;
        flex: 0 0 auto;
        width: 30px;
        height: 30px;
        border-radius: 8px;
        background: var(--green-bg);
        color: var(--green);
        font-weight: 800;
        font-size: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 2px;
      }
      .point .n::before {
        content: counter(pt);
      }
      .point.contention .n {
        background: var(--amber-bg);
        color: #7a5a08;
      }
      .point .txt {
        font-size: 14.5px;
      }
      .point .txt b {
        color: var(--navy);
      }

      /* ===== Price ladder ===== */
      .ladder {
        display: flex;
        flex-direction: column;
        gap: 8px;
        margin-top: 6px;
      }
      .ladder .rung {
        display: grid;
        grid-template-columns: 130px 1fr 220px;
        align-items: center;
        gap: 16px;
        background: var(--card);
        border: 1px solid var(--line);
        border-radius: 10px;
        padding: 10px 16px;
        box-shadow: var(--shadow);
      }
      .ladder .price {
        font-weight: 800;
        font-variant-numeric: tabular-nums;
        color: var(--navy);
      }
      .ladder .action {
        font-size: 14.5px;
        font-weight: 600;
      }
      .bar-track {
        height: 10px;
        border-radius: 999px;
        background: #eef1f6;
        overflow: hidden;
      }
      .bar-fill {
        height: 100%;
        border-radius: 999px;
      }
      .fill-red {
        background: linear-gradient(90deg, #d96c5b, var(--red));
      }
      .fill-amber {
        background: linear-gradient(90deg, #e6c35c, var(--gold));
      }
      .fill-green {
        background: linear-gradient(90deg, #4cae7f, var(--green));
      }
      .fill-deep {
        background: linear-gradient(90deg, #1d7a4f, #0e4d31);
      }
      .fill-slate {
        background: linear-gradient(90deg, #9fb0c4, #5b728c);
      }

      /* ===== Chart ===== */
      .chart-row {
        display: flex;
        align-items: stretch;
        gap: 14px;
        margin-top: 14px;
        flex-wrap: wrap;
      }
      .chart-col {
        flex: 1 1 130px;
        min-width: 110px;
        display: flex;
        flex-direction: column;
        align-items: center;
      }
      .chart-col .vbar {
        width: 100%;
        max-width: 72px;
        flex: 1;
        display: flex;
        align-items: flex-end;
      }
      .chart-col .bar {
        width: 100%;
        border-radius: 8px 8px 4px 4px;
        min-height: 6px;
        position: relative;
        transition: 0.25s;
      }
      .chart-col:hover .bar {
        opacity: 0.85;
      }
      .chart-col .scen {
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: var(--muted);
        text-align: center;
        margin-top: 10px;
      }
      .chart-col .val {
        font-size: 15px;
        font-weight: 800;
        color: var(--navy);
        text-align: center;
      }
      .chart-col .prob {
        font-size: 12.5px;
        color: var(--muted);
        text-align: center;
      }
      .chart-axis {
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: var(--muted);
        border-top: 1px solid var(--line);
        padding-top: 6px;
        margin-top: 4px;
      }

      /* ===== Pros / cons ===== */
      .proscons {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 18px;
      }
      @media (max-width: 720px) {
        .proscons {
          grid-template-columns: 1fr;
        }
      }
      .pc {
        background: var(--card);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        overflow: hidden;
        border: 1px solid var(--line);
      }
      .pc .head {
        padding: 14px 20px;
        font-weight: 800;
        font-size: 16px;
        letter-spacing: 0.02em;
      }
      .pc.for .head {
        background: var(--green-bg);
        color: var(--green);
      }
      .pc.against .head {
        background: var(--red-bg);
        color: var(--red);
      }
      .pc ul {
        list-style: none;
        padding: 12px 20px 18px;
      }
      .pc li {
        padding: 7px 0 7px 26px;
        position: relative;
        font-size: 14.5px;
        border-bottom: 1px dashed #edf1f6;
      }
      .pc li:last-child {
        border-bottom: none;
      }
      .pc.for li::before {
        content: "✓";
        position: absolute;
        left: 2px;
        color: var(--green);
        font-weight: 800;
      }
      .pc.against li::before {
        content: "✕";
        position: absolute;
        left: 2px;
        color: var(--red);
        font-weight: 800;
      }

      /* ===== Judgment ===== */
      .judgment {
        background: var(--navy);
        color: #eaf1fb;
        border-radius: var(--radius);
        padding: 34px 36px;
        box-shadow: var(--shadow);
        position: relative;
      }
      .judgment .qmark {
        font-size: 60px;
        line-height: 1;
        color: var(--gold);
        font-family: Georgia, serif;
        margin-bottom: 6px;
      }
      .judgment p {
        font-size: 17px;
        line-height: 1.75;
        font-style: italic;
      }
      .judgment p b {
        color: #ffd97a;
        font-style: normal;
      }

      .two-col {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 18px;
      }
      @media (max-width: 720px) {
        .two-col {
          grid-template-columns: 1fr;
        }
      }
      .note-box {
        background: var(--blue-bg);
        border-left: 4px solid var(--blue);
        border-radius: 0 10px 10px 0;
        padding: 16px 20px;
        font-size: 14.5px;
      }
      .warn-box {
        background: var(--amber-bg);
        border-left: 4px solid var(--gold);
        border-radius: 0 10px 10px 0;
        padding: 16px 20px;
        font-size: 14.5px;
      }

      footer {
        padding: 40px 0 60px;
      }
      footer .disc {
        background: var(--card);
        border: 1px solid var(--line);
        border-radius: 12px;
        padding: 18px 22px;
        font-size: 13px;
        color: var(--muted);
        box-shadow: var(--shadow);
      }
      @media print {
        body {
          background: #fff;
        }
        header.hero {
          padding: 30px 0;
        }
        .card,
        .profile,
        .pc,
        table,
        .point,
        .ladder .rung {
          box-shadow: none;
        }
      }
"""


# --------------------------------------------------------------- helpers
def fmt(text):
    """HTML-escape, then apply **bold** and `code` markdown."""
    t = html.escape(str(text), quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return t


def esc(text):
    return html.escape(str(text), quote=False)


# --------------------------------------------------------------- render
def render_hero(c):
    return f"""
    <header class="hero">
      <div class="wrap">
        <div class="kicker">{esc(c.get('kicker', 'Synthesized Consensus · Five-Lens Deliberative Debate'))}</div>
        <h1>{esc(c['title'])}</h1>
        <div class="sub">{fmt(c.get('subtitle', ''))}</div>
        <div class="meta-row">
          <span class="chip">{esc(c['exchange']) + ': ' + esc(c['ticker'])}</span>
          <span class="chip">Report date: {esc(c['date'])}</span>
          <span class="chip">Reference price: {esc(c.get('reference_price', ''))}</span>
          <span class="rating-badge"><span class="dot"></span> {esc(c['rating'])}</span>
        </div>
      </div>
    </header>
"""


def render_exec(es, num):
    cards = "\n".join(
        f"""          <div class="card">
            <div class="label">{fmt(card.get('label',''))}</div>
            <div class="value"{(' style="' + card['value_style'] + '"') if card.get('value_style') else ''}>{fmt(card.get('value',''))}</div>
            <div class="note">{fmt(card.get('note',''))}</div>
          </div>"""
        for card in es.get("cards", [])
    )
    return f"""
      <section>
        <h2 class="sec"><span class="num">{num}</span>Executive Summary</h2>
        <p class="lead">{fmt(es.get('lead',''))}</p>
        <div class="cards">
{cards}
        </div>
      </section>
"""


def render_profiles(c, num):
    cards = "\n".join(
        f"""          <div class="profile">
            <div class="head">
              <div class="name">{esc(p.get('name',''))}</div>
              <div class="role">{esc(p.get('role',''))}</div>
            </div>
            <div class="body">
              <div class="verdict-row">
                <span class="v" style="color: var(--gold)">{esc(p.get('verdict',''))}</span><span class="small">{esc(p.get('at',''))}</span>
              </div>
              <p>{fmt(p.get('paragraph',''))}</p>
              <div class="tags">
                {''.join(f'<span class="tag">{esc(t)}</span>' for t in p.get('tags', []))}
              </div>
            </div>
          </div>"""
        for p in c.get("profiles", [])
    )
    title = c.get("profiles_title")
    if not title:
        n = len(c.get("profiles", []))
        title = f"The {n} Positions at the Table"
    return f"""
      <section>
        <h2 class="sec"><span class="num">{num}</span>{esc(title)}</h2>
        <p class="lead">{fmt(c.get('profiles_lead',''))}</p>
        <div class="profiles">
{cards}
        </div>
      </section>
"""


def render_point_list(items, cls=""):
    rows = "".join(
        f"""          <div class="point{(' ' + cls) if cls else ''}">
            <div class="n"></div>
            <div class="txt">{fmt(item)}</div>
          </div>
"""
        for item in items
    )
    return rows


def render_debate(d, num):
    ag = render_point_list(d.get("agreements", []))
    co = render_point_list(d.get("contentions", []), "contention")
    return f"""
      <section>
        <h2 class="sec"><span class="num">{num}</span>{esc(d.get('title', 'The Debate'))}</h2>
        <p class="lead">{fmt(d.get('lead',''))}</p>
        <h3>{esc(d.get('agreements_title', 'Uncontested consensus core'))}</h3>
        <div class="point-list">
{ag}        </div>
        <h3>{esc(d.get('contentions_title', 'Contested points'))}</h3>
        <div class="point-list">
{co}        </div>
      </section>
"""


def render_matrix(m):
    thead = "".join(
        f"<th class=\"{'right' if i > 0 else ''}\">{esc(col)}</th>"
        for i, col in enumerate(m["columns"])
    )
    tbody = ""
    for r in m["rows"]:
        cls = ' class="hl"' if r.get("highlight") else ""
        tds = ""
        n = len(r["cells"])
        for i, cell in enumerate(r["cells"]):
            right = ' class="right"' if i > 0 else ""
            inner = f"<b>{fmt(cell)}</b>" if i == n - 1 else fmt(cell)
            tds += f"<td{right}>{inner}</td>"
        tbody += f"              <tr{cls}>\n{tds}\n              </tr>\n"
    return f"""        <div class="table-scroll">
          <table>
            <thead>
              <tr>
{thead}              </tr>
            </thead>
            <tbody>
{tbody}            </tbody>
          </table>
        </div>"""


def render_chart(ch):
    cols = "".join(
        f"""          <div class="chart-col">
            <div class="vbar">
              <div class="bar {esc(col['fill'])}" style="height: {col['height']}px"></div>
            </div>
            <div class="scen">{esc(col['scen'])}</div>
            <div class="val">{fmt(col['val'])}</div>
            <div class="prob">{esc(col['prob'])}</div>
          </div>
"""
        for col in ch.get("cols", [])
    )
    return f"""        <h3>Scenario distribution</h3>
        <div class="chart-row">
{cols}        </div>
        <div class="chart-axis">
          <span>{esc(ch.get('axis_left','$0'))}</span><span>{fmt(ch.get('axis_mid',''))}</span><span>{esc(ch.get('axis_right',''))}</span>
        </div>"""


def render_valuation(v, num):
    matrix = render_matrix(v["matrix"])
    chart = render_chart(v.get("chart", {})) if v.get("chart") else ""
    w = v.get("weighted", {})
    weighted = f"""        <h3>Probability-weighted value</h3>
        <div class="consensus-box">
          <h3>{fmt(w.get('formula',''))}</h3>
          <p class="big">{fmt(w.get('text',''))}</p>
        </div>""" if w else ""
    footnote = f"""        <p class="small" style="margin-top: 10px">{fmt(v.get('footnote',''))}</p>""" if v.get("footnote") else ""
    return f"""
      <section>
        <h2 class="sec"><span class="num">{num}</span>{esc(v.get('title', 'Consensus Valuation'))}</h2>
        <p class="lead">{fmt(v.get('lead',''))}</p>
{matrix}
{footnote}
{chart}
{weighted}
      </section>
"""


def render_ladder(l, num):
    rungs = "".join(
        f"""          <div class="rung">
            <span class="price">{esc(r.get('price',''))}</span>
            <div class="bar-track">
              <div class="bar-fill {esc(r.get('fill','fill-amber'))}" style="width: {r.get('width',50)}%"></div>
            </div>
            <span class="action"{(' style="color: ' + r['color'] + '"') if r.get('color') else ''}>{('<b>' + fmt(r.get('action','')) + '</b>') if r.get('bold') else fmt(r.get('action',''))}</span>
          </div>
"""
        for r in l.get("rungs", [])
    )
    return f"""
      <section>
        <h2 class="sec"><span class="num">{num}</span>{esc(l.get('title', 'Consensus Price Ladder'))}</h2>
        <p class="lead">{fmt(l.get('lead',''))}</p>
        <div class="ladder">
{rungs}        </div>
      </section>
"""


def render_proscons(pc, num):
    for_li = "".join(f"              <li>{fmt(x)}</li>\n" for x in pc.get("for", []))
    against_li = "".join(f"              <li>{fmt(x)}</li>\n" for x in pc.get("against", []))
    return f"""
      <section>
        <h2 class="sec"><span class="num">{num}</span>{esc(pc.get('title', 'Pros &amp; Cons'))}</h2>
        <div class="proscons">
          <div class="pc for">
            <div class="head">FOR the investment</div>
            <ul>
{for_li}            </ul>
          </div>
          <div class="pc against">
            <div class="head">AGAINST the investment</div>
            <ul>
{against_li}            </ul>
          </div>
        </div>
      </section>
"""


def render_triggers(t, num):
    up = "".join(f"              <li>{fmt(x)}</li>\n" for x in t.get("upgrade", []))
    down = "".join(f"              <li>{fmt(x)}</li>\n" for x in t.get("downgrade", []))
    dash = ""
    if t.get("dashboard"):
        rows = "".join(
            f"""              <tr>
                <td><b>{fmt(r.get('metric',''))}</b></td>
                <td>{fmt(r.get('why',''))}</td>
                <td class="right">{fmt(r.get('helps',''))}</td>
              </tr>
"""
            for r in t["dashboard"]
        )
        dash = f"""        <h3>{esc(t.get('dashboard_title', 'Consensus monitoring dashboard'))}</h3>
        <div class="table-scroll" style="margin-top: 14px">
          <table>
            <thead>
              <tr>
                <th>Metric</th>
                <th>Why it matters</th>
                <th class="right">Direction that helps</th>
              </tr>
            </thead>
            <tbody>
{rows}            </tbody>
          </table>
        </div>"""
    return f"""
      <section>
        <h2 class="sec"><span class="num">{num}</span>{esc(t.get('title', 'What Changes the Rating'))}</h2>
        <div class="two-col">
          <div class="note-box">
            <b style="color: var(--green)">{fmt(t.get('upgrade_title', 'Upgrade C → B/A when:'))}</b>
            <ol style="margin: 8px 0 0 20px; font-size: 14.5px">
{up}            </ol>
          </div>
          <div class="warn-box">
            <b style="color: #7a5a08">{fmt(t.get('downgrade_title', 'Downgrade C → D/E if:'))}</b>
            <ol style="margin: 8px 0 0 20px; font-size: 14.5px">
{down}            </ol>
          </div>
        </div>
{dash}
      </section>
"""


def render_conclusions(cl, num):
    items = "".join(
        f"""          <div class="point">
            <div class="n"></div>
            <div class="txt">{fmt(item)}</div>
          </div>
"""
        for item in cl.get("items", [])
    )
    return f"""
      <section>
        <h2 class="sec"><span class="num">{num}</span>{esc(cl.get('title', 'The Five Consensus Conclusions'))}</h2>
        <div class="point-list">
{items}        </div>
      </section>
"""


def render_judgment(j, num):
    return f"""
      <section>
        <h2 class="sec"><span class="num">{num}</span>{esc(j.get('title', 'Final Consensus Judgment'))}</h2>
        <div class="judgment">
          <div class="qmark">“</div>
          <p>{fmt(j.get('paragraph',''))}</p>
        </div>
      </section>
"""


def render_footer(c):
    return f"""
    <footer>
      <div class="wrap">
        <div class="disc">
          <b>Sources &amp; disclaimer.</b> {fmt(c.get('sources_note', ''))}
        </div>
      </div>
    </footer>
"""


def render_technical(t, num):
    rows = "".join(
        f"""              <tr>
                <td><b>{fmt(r.get('metric',''))}</b></td>
                <td class="right">{fmt(r.get('value',''))}</td>
                <td class="right">{fmt(r.get('delta',''))}</td>
              </tr>
"""
        for r in t.get("rows", [])
    )
    note = (f"""        <p class="small" style="margin-top: 10px">{fmt(t.get('note',''))}</p>"""
            if t.get("note") else "")
    return f"""
      <section>
        <h2 class="sec"><span class="num">{num}</span>{esc(t.get('title', 'Technical Analysis'))}</h2>
        <p class="lead">{fmt(t.get('lead',''))}</p>
        <div class="table-scroll">
          <table>
            <thead>
              <tr>
                <th>Indicator</th>
                <th class="right">Value</th>
                <th class="right">Position</th>
              </tr>
            </thead>
            <tbody>
{rows}            </tbody>
          </table>
        </div>
{note}
      </section>
"""


def render(c):
    """Assemble the full HTML document."""
    parts = []
    num = 1
    parts.append(render_hero(c))
    if c.get("exec_summary"):
        parts.append(render_exec(c["exec_summary"], f"{num:02d}")); num += 1
    if c.get("profiles"):
        parts.append(render_profiles(c, f"{num:02d}")); num += 1
    if c.get("debate"):
        parts.append(render_debate(c["debate"], f"{num:02d}")); num += 1
    if c.get("valuation"):
        parts.append(render_valuation(c["valuation"], f"{num:02d}")); num += 1
    if c.get("ladder"):
        parts.append(render_ladder(c["ladder"], f"{num:02d}")); num += 1
    if c.get("proscons"):
        parts.append(render_proscons(c["proscons"], f"{num:02d}")); num += 1
    if c.get("triggers"):
        parts.append(render_triggers(c["triggers"], f"{num:02d}")); num += 1
    if c.get("technical"):
        parts.append(render_technical(c["technical"], f"{num:02d}")); num += 1
    if c.get("conclusions"):
        parts.append(render_conclusions(c["conclusions"], f"{num:02d}")); num += 1
    if c.get("judgment"):
        parts.append(render_judgment(c["judgment"], f"{num:02d}"))
    body = "\n".join(parts)
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{esc(c['title'])}</title>
    <style>{REPORT_CSS}    </style>
  </head>
  <body>
{body}
{render_footer(c)}
  </body>
</html>
"""


# --------------------------------------------------------------- validate
def validate(html_text, figures=()):
    """Structural checks. Returns a list of failure strings (empty = pass)."""
    fails = []
    if html_text.count("<style>") != 1 or html_text.count("</style>") != 1:
        fails.append("expected exactly one <style> block")
    ext = re.findall(
        r'(?:href|src)=["\'](?:https?://|//|cdn)', html_text)
    if ext:
        fails.append(f"external urls found: {ext}")
    for tag in ("div", "section", "table", "ul", "ol", "span", "td", "tr"):
        opens = len(re.findall(rf"<{tag}(?=[\s>])", html_text))
        closes = len(re.findall(rf"</{tag}\s*>", html_text))
        if opens != closes:
            fails.append(f"tag <{tag}>: open={opens} close={closes}")
    for f in figures:
        if f not in html_text:
            fails.append(f"figure not present: {f!r}")
    return fails


def validate_inputs(c):
    """Two-way figures check. Every `figures` entry must render in the HTML
    *and* appear in the report inputs' own content (the JSON serialized
    without the figures array). A figure that is neither rendered nor present
    in the content is copy-paste drift and must be removed or fixed."""
    figs = c.get("figures", [])
    if not figs:
        return []
    payload = dict(c)
    payload.pop("figures", None)
    blob = json.dumps(payload, ensure_ascii=False, default=str)
    fails = []
    for f in figs:
        if f not in blob:
            fails.append(f"figure not in report inputs content: {f!r}")
    return fails


# --------------------------------------------------------------- main
def main():
    args = [a for a in sys.argv[1:]]
    do_validate = "--validate" in args
    args = [a for a in args if a != "--validate"]
    if len(args) < 1 or len(args) > 2:
        print(__doc__)
        sys.exit(2)
    in_path = args[0]
    with open(in_path) as f:
        c = json.load(f)
    if len(args) == 2:
        out_path = args[1]
    else:
        out_path = f"{c['ticker'].lower()}-consensus-investment-report.html"
    html_text = render(c)
    with open(out_path, "w") as f:
        f.write(html_text)
    print(f"WROTE {out_path} ({len(html_text)} bytes)")
    if do_validate:
        fails = validate(html_text, c.get("figures", []))
        fails += validate_inputs(c)
        if fails:
            print("VALIDATE FAIL:")
            for fl in fails:
                print("  -", fl)
            sys.exit(1)
        print("VALIDATE OK")


if __name__ == "__main__":
    main()
