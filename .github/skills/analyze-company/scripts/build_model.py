"""Build a Damodaran-style 5-scenario FCFF DCF workbook from scratch.

Usage:
    python3 build_model.py <model_inputs.json> <output.xlsx>

Architecture (mirrors the IREN_Damodaran_Financial_Model v2 workbook):
  - Inputs            : yellow user-editable base assumptions + market facts
  - Scenarios         : five scenario rows (probability + adjustment points)
  - DCF-SevereBear .. DCF-ExtremeBull
                      : each a complete 10-year FCFF DCF pulling its own
                        scenario row; margin ramps base->terminal, ROIC
                        transitions initial->terminal, effective WACC/terminal
                        growth = base + scenario adjustment
  - Scenario Summary  : probability-weighted value/share + outputs block;
                        only READS the five DCF results -> no circular refs
  - Reverse DCF       : market-implied fundamentals grid
  - Sensitivity       : WACC x terminal-growth share value; margin x mature
                        revenue implied terminal EV
  - Checks            : workbook-wide validation formulas
"""
import json
import sys

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.comments import Comment
from openpyxl.utils import get_column_letter

# ---------------------------------------------------------------- styles
FILL_OUT = PatternFill("solid", start_color="00E2F0D9")      # green = formula
FILL_INPUT = PatternFill("solid", start_color="00FFF2CC")    # yellow = editable
FILL_GRIDHDR = PatternFill("solid", start_color="00D9EAF7")  # light blue
FILL_HDR = PatternFill("solid", start_color="001F4E78")      # navy header
FONT_INPUT = Font(name="Calibri", color="009C6500")
FONT_LINK = Font(name="Calibri", color="00008000")
FONT_BOLD = Font(name="Calibri", bold=True)
FONT_NOTE = Font(name="Calibri", color="00666666")
FONT_PLAIN = Font(name="Calibri")
FONT_HDR = Font(name="Calibri", color="00FFFFFF", bold=True)
PCT = "0.0%"
USD = "$#,##0.00"
USD0 = "$#,##0"
USD_B = '0.0"B"'

YCOLS = list("BCDEFGHIJK")  # Y1..Y10
SCEN_SHEETS = ["DCF-SevereBear", "DCF-Bear", "DCF-Base", "DCF-Bull",
               "DCF-ExtremeBull"]


def navy(ws, cell, text):
    ws[cell] = text
    ws[cell].font = FONT_HDR
    ws[cell].fill = FILL_HDR


def build(cfg):
    wb = Workbook()

    # ================================================================ README
    rm = wb.active
    rm.title = "README"
    rm["A1"] = f"{cfg['company']} \u2014 Damodaran-Style Scenario DCF Model"
    rm["A1"].font = Font(name="Calibri", size=14, bold=True)
    rm["A3"] = "Purpose"
    rm["B3"] = ("Scenario-driven FCFF model linking growth, margins, "
                "reinvestment, ROIC, WACC and terminal value.")
    rm["A4"] = "Core philosophy"
    rm["B4"] = ("Value = present value of expected cash flows. Price is an "
                "input for reverse DCF, not a valuation anchor.")
    rm["A5"] = "How to use"
    rm["B5"] = ("Change yellow cells on Inputs and Scenarios sheets. Each "
                "scenario has its own DCF sheet (DCF-SevereBear through "
                "DCF-ExtremeBull); the Scenario Summary sheet probability-"
                "weights their results. Green cells are formulas/links. Blue "
                "cells are labels/structure.")
    rm["A6"] = "Primary outputs"
    rm["B6"] = ("Five standalone scenario DCF values/share, probability-"
                "weighted value/share, expected upside/downside and "
                "annualized return, reverse-DCF implied growth/margin, "
                "sensitivity tables.")
    rm["A7"] = "Important"
    rm["B7"] = ("This is a modeling framework, not a live market-data feed. "
                "Replace the initial assumptions with the latest filing/price "
                "data before making an investment decision.")
    rm["A8"] = "Model convention"
    rm["B8"] = ("$ millions except per-share data, percentages. FCFF is "
                "calculated from NOPAT less reinvestment.")
    rm["A9"] = "Model structure"
    rm["B9"] = ("Five scenario DCF sheets, each a complete 10-year FCFF model "
                "with its own growth, margin, ROIC/reinvestment, WACC and "
                "terminal assumptions, feed a single probability-weighted "
                "Scenario Summary. The summary does not feed back into any "
                "DCF, so there are no circular references.")
    for a, b in (("A3", "B3"), ("A4", "B4"), ("A5", "B5"), ("A6", "B6"),
                 ("A7", "B7"), ("A8", "B8"), ("A9", "B9")):
        rm[a].font = FONT_BOLD
        rm[b].alignment = Alignment(wrap_text=True)
    rm.column_dimensions["A"].width = 22
    rm.column_dimensions["B"].width = 100

    # ================================================================ Inputs
    inp = wb.create_sheet("Inputs")
    v = cfg["inputs"]
    inp["A1"] = "Inputs & Current Facts"
    inp["A1"].font = Font(name="Calibri", size=14, bold=True)
    navy(inp, "A3", "Current Market / Capital Structure")
    rows = [
        (4, "Reference share price", v["price"], "$/share", "User-editable"),
        (5, "Diluted shares", v["shares_mm"], "mm", "Scenario assumption"),
        (6, "Cash", v["cash_mm"], "$mm", "Approximate latest-balance-sheet"),
        (7, "Debt + finance leases", v["debt_mm"], "$mm", "Approximate"),
        (8, "Net debt", "=B7-B6", "$mm", "Debt less cash"),
        (9, "Current revenue run-rate", v["revenue_run_rate_mm"], "$mm",
         "Management-target-style anchor; replace with latest"),
    ]
    for r, label, value, unit, note in rows:
        inp[f"A{r}"] = label
        inp[f"B{r}"] = value
        inp[f"C{r}"] = unit
        inp[f"D{r}"] = note
        inp[f"C{r}"].font = FONT_NOTE
        inp[f"D{r}"].font = FONT_NOTE
        if isinstance(value, str) and value.startswith("="):
            inp[f"B{r}"].fill = FILL_OUT
        else:
            inp[f"B{r}"].fill = FILL_INPUT
            inp[f"B{r}"].font = FONT_INPUT
    inp["B4"].number_format = USD
    inp["B8"].number_format = USD0
    navy(inp, "A12", "Base Operating / Valuation Assumptions")
    rows = [
        (13, "Base revenue growth Y1", v["growth_y1"], "%",
         "High-growth transition"),
        (14, "Growth decay per year", v["growth_decay"], "% pts",
         "Growth declines each year"),
        (15, "Base EBIT margin Y1", v["margin_y1"], "%", "Editable"),
        (16, "Terminal EBIT margin", v["margin_terminal"], "%", "Editable"),
        (17, "Tax rate", v["tax_rate"], "%", "Editable"),
        (18, "Base WACC", v["wacc"], "%", "Editable"),
        (19, "Terminal growth", v["terminal_growth"], "%",
         "Must remain below WACC"),
        (20, "Terminal ROIC", v["roic_terminal"], "%", "Stable-state "
         "assumption"),
        (21, "Initial ROIC", v["roic_initial"], "%", "Used for reinvestment"),
        (22, "Margin expansion per year", v["margin_ramp"], "% pts",
         "Until terminal margin"),
        (23, "Minimum revenue growth", v["min_growth"], "%",
         "Floor before terminal"),
    ]
    for r, label, value, unit, note in rows:
        inp[f"A{r}"] = label
        inp[f"B{r}"] = value
        inp[f"C{r}"] = unit
        inp[f"D{r}"] = note
        inp[f"B{r}"].fill = FILL_INPUT
        inp[f"B{r}"].font = FONT_INPUT
        inp[f"B{r}"].number_format = PCT
        inp[f"C{r}"].font = FONT_NOTE
        inp[f"D{r}"].font = FONT_NOTE
    navy(inp, "A26", "Scenario Multipliers / Overrides")
    inp["A27"] = "Use Scenario Sheet"
    inp["B27"] = True
    inp["B27"].fill = FILL_INPUT
    inp["B27"].font = FONT_INPUT
    scen = cfg["scenarios"]
    inp["A29"] = scen[1]["name"]
    inp["B29"] = (f"Growth {scen[1]['growth_adj']:+.0%}; "
                  f"Margin {scen[1]['margin_adj']:+.0%} pts; "
                  f"WACC {scen[1]['wacc_adj']:+.1%}")
    inp["A30"] = scen[2]["name"]
    inp["B30"] = "Base assumptions"
    inp["A31"] = scen[3]["name"]
    inp["B31"] = (f"Growth {scen[3]['growth_adj']:+.0%}; "
                  f"Margin {scen[3]['margin_adj']:+.0%} pts; "
                  f"WACC {scen[3]['wacc_adj']:+.1%}")
    for r in (29, 30, 31):
        inp[f"B{r}"].font = FONT_NOTE
    for col, width in zip("ABCD", (34, 16, 8, 40)):
        inp.column_dimensions[col].width = width
    inp.freeze_panes = "A4"

    # ============================================================= Scenarios
    sc = wb.create_sheet("Scenarios")
    sc["A1"] = "Scenario Controls"
    sc["A1"].font = Font(name="Calibri", size=14, bold=True)
    navy(sc, "A3", "Scenario Inputs")
    headers = ["Scenario", "Probability", "Growth Adj", "Margin Adj",
               "WACC Adj", "Terminal g Adj", "ROIC Adj", "Description"]
    for col, text in zip("ABCDEFGH", headers):
        c = sc[f"{col}4"]
        c.value = text
        c.font = FONT_BOLD
        c.fill = FILL_GRIDHDR
    for i, s in enumerate(scen):
        r = 5 + i
        sc[f"A{r}"] = s["name"]
        sc[f"B{r}"] = s["probability"]
        sc[f"C{r}"] = s["growth_adj"]
        sc[f"D{r}"] = s["margin_adj"]
        sc[f"E{r}"] = s["wacc_adj"]
        sc[f"F{r}"] = s["tg_adj"]
        sc[f"G{r}"] = s["roic_adj"]
        sc[f"H{r}"] = s["description"]
        sc[f"A{r}"].font = FONT_PLAIN
        for col in "BCDEFG":
            sc[f"{col}{r}"].fill = FILL_INPUT
            sc[f"{col}{r}"].font = FONT_INPUT
            sc[f"{col}{r}"].number_format = PCT
        sc[f"H{r}"].font = FONT_NOTE
    navy(sc, "A12", "Scenario DCF Sheets")
    for i, s in enumerate(scen):
        r = 13 + i
        sc[f"A{r}"] = s["name"]
        sc[f"B{r}"] = SCEN_SHEETS[i]
        sc[f"A{r}"].font = FONT_PLAIN
        sc[f"B{r}"].font = FONT_LINK
    sc["A19"] = ("Each scenario row feeds its own DCF sheet. Edit the five "
                 "scenario rows above; the Scenario Summary sheet "
                 "probability-weights the five DCF results.")
    sc["A19"].font = FONT_NOTE
    sc["A19"].alignment = Alignment(wrap_text=True)
    for col, width in zip("ABCDEFGH", (18, 12, 11, 11, 10, 12, 10, 44)):
        sc.column_dimensions[col].width = width

    # ========================================================== DCF sheets
    def add_dcf(sheet_name, srow, disp):
        ws = wb.create_sheet(sheet_name)
        ws["A1"] = f"FCFF DCF \u2014 {disp} Scenario"
        ws["A1"].font = Font(name="Calibri", size=14, bold=True)
        ws["A3"] = f"{disp} Scenario Assumptions"
        ws["A3"].font = FONT_BOLD
        ws["A4"] = "Scenario"
        ws["B4"] = f"=Scenarios!A{srow}"
        ws["B4"].font = FONT_LINK
        ws["D4"] = ("Each scenario has its own complete 10-year DCF sheet. "
                    "Adjustments pull from the matching row on the Scenarios "
                    "sheet. Edit yellow cells on Inputs and Scenarios; green "
                    "cells are formulas/links.")
        ws["D4"].font = FONT_NOTE
        ws["D4"].alignment = Alignment(wrap_text=True)
        labels = {
            5: "Probability", 6: "Growth adjustment", 7: "Margin adjustment",
            8: "WACC adjustment", 9: "Terminal g adjustment",
            10: "ROIC adjustment",
        }
        for r, label in labels.items():
            ws[f"A{r}"] = label
            ws[f"B{r}"] = f"=Scenarios!{get_column_letter(r - 3)}{srow}"
            ws[f"B{r}"].fill = FILL_OUT
            ws[f"B{r}"].number_format = PCT
        ws["A11"] = "Effective WACC"
        ws["B11"] = "=Inputs!$B$18+$B$8"
        ws["A12"] = "Effective terminal growth"
        ws["B12"] = "=Inputs!$B$19+$B$9"
        for coord in ("B11", "B12"):
            ws[coord].fill = FILL_OUT
            ws[coord].number_format = PCT
        ws["A13"] = "10-Year Forecast"
        ws["A13"].font = FONT_BOLD
        ws["A14"] = "Metric"
        ws["A14"].font = FONT_BOLD
        ws["A14"].fill = FILL_GRIDHDR
        for i, col in enumerate(YCOLS):
            c = ws[f"{col}14"]
            c.value = f"Y{i + 1}"
            c.font = FONT_BOLD
            c.fill = FILL_GRIDHDR
        # Revenue
        ws["A15"] = "Revenue"
        ws["B15"] = ("=Inputs!$B$9*(1+MAX(Inputs!$B$13+($B$6),"
                     "Inputs!$B$23))")
        for i in range(1, 10):
            prev = YCOLS[i - 1]
            col = YCOLS[i]
            ws[f"{col}15"] = (f"={prev}15*(1+MAX({prev}16-Inputs!$B$14,"
                              f"Inputs!$B$23))")
        # Growth
        ws["A16"] = "Growth"
        ws["B16"] = "=B15/Inputs!$B$9-1"
        for i in range(1, 10):
            prev = YCOLS[i - 1]
            col = YCOLS[i]
            ws[f"{col}16"] = (f"=MAX({prev}16-Inputs!$B$14,Inputs!$B$23)")
        # EBIT margin: ramp from base Y1 margin toward terminal
        ws["A17"] = "EBIT Margin"
        for i, col in enumerate(YCOLS):
            ws[f"{col}17"] = (f"=MIN(Inputs!$B$16+$B$7,"
                              f"Inputs!$B$15+$B$7+Inputs!$B$22*{i})")
        # EBIT
        ws["A18"] = "EBIT"
        for col in YCOLS:
            ws[f"{col}18"] = f"={col}15*{col}17"
        # Tax
        ws["A19"] = "Tax"
        for col in YCOLS:
            ws[f"{col}19"] = "=Inputs!$B$17"
        # NOPAT
        ws["A20"] = "NOPAT"
        for col in YCOLS:
            ws[f"{col}20"] = f"={col}18*(1-{col}19)"
        # ROIC: linear transition initial -> terminal
        ws["A21"] = "ROIC"
        for i, col in enumerate(YCOLS):
            ws[f"{col}21"] = (f"=MAX(Inputs!$B$20+$B$10,"
                              f"Inputs!$B$21+$B$10-"
                              f"(Inputs!$B$21-Inputs!$B$20)*{i}/9)")
        # Reinvestment rate / reinvestment / FCFF
        ws["A22"] = "Reinvestment Rate"
        ws["A23"] = "Reinvestment"
        ws["A24"] = "FCFF"
        for col in YCOLS:
            ws[f"{col}22"] = f"={col}16/{col}21"
            ws[f"{col}23"] = f"={col}20*{col}22"
            ws[f"{col}24"] = f"={col}20-{col}23"
        # Discount factor / PV
        ws["A25"] = "Discount Factor"
        ws["A26"] = "PV of FCFF"
        for i, col in enumerate(YCOLS):
            ws[f"{col}25"] = f"=1/(1+$B$11)^{i + 1}"
            ws[f"{col}26"] = f"={col}24*{col}25"
        # Terminal value block
        ws["A29"] = "Terminal Value & Equity Value"
        ws["A29"].font = FONT_BOLD
        ws["A30"] = "Terminal growth"
        ws["B30"] = "=$B$12"
        ws["A31"] = "Terminal ROIC"
        ws["B31"] = "=Inputs!$B$20+$B$10"
        ws["A32"] = "Terminal reinvestment rate"
        ws["B32"] = "=B30/B31"
        ws["A33"] = "Terminal FCFF"
        ws["B33"] = "=K20*(1+B30)*(1-B32)"
        ws["A34"] = "Terminal value"
        ws["B34"] = "=B33/($B$11-B30)"
        ws["A35"] = "PV of explicit FCFF"
        ws["B35"] = "=SUM(B26:K26)"
        ws["A36"] = "PV of terminal value"
        ws["B36"] = "=B34/(1+$B$11)^10"
        ws["A37"] = "Enterprise value"
        ws["B37"] = "=B35+B36"
        ws["A38"] = "Less net debt"
        ws["B38"] = "=Inputs!$B$8"
        ws["A39"] = "Equity value"
        ws["B39"] = "=B37-B38"
        ws["A40"] = "Diluted shares"
        ws["B40"] = "=Inputs!$B$5"
        ws["A41"] = "Intrinsic value / share"
        ws["B41"] = "=B39/B40"
        ws["A42"] = "Terminal value / EV"
        ws["B42"] = "=B36/B37"
        for col in YCOLS:
            for r in (15, 18, 20, 23, 24):
                ws[f"{col}{r}"].number_format = USD0
            for r in (16, 17, 19, 21, 22, 25):
                ws[f"{col}{r}"].number_format = PCT
            ws[f"{col}26"].number_format = USD0
        for coord in ("B30", "B31", "B32", "B42"):
            ws[coord].number_format = PCT
        for coord in ("B33", "B34", "B35", "B36", "B37", "B38", "B39"):
            ws[coord].number_format = USD0
        ws["B41"].number_format = USD
        for col in YCOLS:
            for r in (15, 18, 20, 23, 24, 26):
                ws[f"{col}{r}"].fill = FILL_OUT
            for r in (16, 17, 19, 21, 22, 25):
                ws[f"{col}{r}"].fill = FILL_OUT
        for coord in ("B30", "B31", "B32", "B33", "B34", "B35", "B36", "B37",
                      "B38", "B39", "B40", "B41", "B42"):
            ws[coord].fill = FILL_OUT
        ws["B41"].font = FONT_BOLD
        ws.column_dimensions["A"].width = 26
        for col in YCOLS:
            ws.column_dimensions[col].width = 13
        ws.freeze_panes = "B15"
        return ws

    add_dcf("DCF-SevereBear", 5, "Severe Bear")
    add_dcf("DCF-Bear", 6, "Bear")
    add_dcf("DCF-Base", 7, "Base")
    add_dcf("DCF-Bull", 8, "Bull")
    add_dcf("DCF-ExtremeBull", 9, "Extreme Bull")

    # ===================================================== Scenario Summary
    ss = wb.create_sheet("Scenario Summary")
    navy(ss, "A1", "Probability-Weighted Scenario Valuation")
    navy(ss, "A3", "Scenario Valuation Table")
    headers = ["Scenario", "Probability", "Standalone Intrinsic Value/Share",
               "Probability \u00d7 Value", "Key Case"]
    for col, text in zip("ABCDE", headers):
        cell = ss[f"{col}4"]
        cell.value = text
        cell.font = FONT_BOLD
    for i, sheet_name in enumerate(SCEN_SHEETS):
        r = 5 + i
        ss[f"A{r}"] = f"=Scenarios!A{r}"
        ss[f"A{r}"].font = FONT_LINK
        ss[f"B{r}"] = f"=Scenarios!B{r}"
        ss[f"B{r}"].font = FONT_LINK
        ss[f"B{r}"].number_format = PCT
        ss[f"C{r}"] = f"='{sheet_name}'!B41"
        ss[f"C{r}"].font = FONT_LINK
        ss[f"C{r}"].number_format = USD
        ss[f"D{r}"] = f"=B{r}*C{r}"
        ss[f"D{r}"].number_format = USD
        ss[f"E{r}"] = f"=Scenarios!H{r}"
        ss[f"E{r}"].font = FONT_NOTE
    ss["A10"] = "Total / Expected Value"
    ss["A10"].font = FONT_BOLD
    ss["B10"] = "=SUM(B5:B9)"
    ss["B10"].font = FONT_BOLD
    ss["B10"].number_format = PCT
    ss["C10"] = "\u2014"
    ss["D10"] = "=SUM(D5:D9)"
    ss["D10"].font = FONT_BOLD
    ss["D10"].fill = FILL_OUT
    ss["D10"].number_format = USD
    ss["D10"].comment = Comment(
        "Sum of Probability \u00d7 Standalone Intrinsic Value/Share across "
        "the five scenario DCF sheets.", "Copilot", height=60, width=280)
    navy(ss, "A12", "Outputs")
    ss["A13"] = "Probability-weighted intrinsic value / share"
    ss["B13"] = "=D10"
    ss["A14"] = "Current market price / share"
    ss["B14"] = "=Inputs!B4"
    ss["A15"] = "Expected upside / downside"
    ss["B15"] = "=B13/B14-1"
    ss["A16"] = "Investment horizon (years)"
    ss["B16"] = cfg["inputs"].get("horizon_years", 5)
    ss["A17"] = "Expected annualized return"
    ss["B17"] = "=(B13/B14)^(1/B16)-1"
    ss["B17"].comment = Comment(
        "Expected annualized return = (weighted value / price)^(1/horizon) "
        "\u2212 1.", "Copilot", height=60, width=280)
    for r in (13, 14, 15, 17):
        ss[f"B{r}"].fill = FILL_OUT
        ss[f"B{r}"].number_format = "0.0%" if r in (15, 17) else USD
    ss["B16"].fill = FILL_INPUT
    ss["B16"].font = FONT_INPUT
    ss["B16"].number_format = "0"
    ss["A19"] = ("Each scenario has its own complete 10-year FCFF DCF sheet "
                 "with its own revenue growth, EBIT margin, ROIC/reinvestment, "
                 "WACC and terminal assumptions. This summary only pulls the "
                 "five standalone DCF results and probability-weights them "
                 "\u2014 the summary never feeds back into any DCF, so there "
                 "are no circular references.")
    ss["A19"].font = FONT_NOTE
    ss["A19"].alignment = Alignment(wrap_text=True)
    ss.merge_cells("A19:H19")
    ss.row_dimensions[19].height = 40
    for col, width in zip("ABCDE", (40, 12, 17, 15, 46)):
        ss.column_dimensions[col].width = width

    # ========================================================= Reverse DCF
    rd = wb.create_sheet("Reverse DCF")
    rd["A1"] = "Reverse DCF \u2014 Market-Implied Fundamentals"
    rd["A1"].font = Font(name="Calibri", size=14, bold=True)
    navy(rd, "A3", "Market Inputs")
    rows = [
        (4, "Current price", "=Inputs!B4", USD),
        (5, "Diluted shares", "=Inputs!B5", "0"),
        (6, "Equity market value", "=B4*B5", USD0),
        (7, "Net debt", "=Inputs!B8", USD0),
        (8, "Enterprise value implied by price", "=B6+B7", USD0),
        (9, "WACC", "=Inputs!B18", PCT),
        (10, "Terminal growth", "=Inputs!B19", PCT),
    ]
    for r, label, formula, fmt in rows:
        rd[f"A{r}"] = label
        rd[f"B{r}"] = formula
        rd[f"B{r}"].fill = FILL_OUT
        rd[f"B{r}"].number_format = fmt
    navy(rd, "A13", "Reverse DCF Grid \u2014 terminal revenue and margin "
                    "combinations")
    rd["A14"] = "Terminal Revenue"
    rd["A14"].font = FONT_BOLD
    rev_start = cfg.get("reverse_dcf", {}).get("rev_start", 6)
    rev_end = cfg.get("reverse_dcf", {}).get("rev_end", 14)
    for j, rev in enumerate(range(rev_start, rev_end + 1)):
        c = rd[f"{get_column_letter(2 + j)}14"]
        c.value = rev
        c.font = FONT_BOLD
        c.fill = FILL_GRIDHDR
    m_start = cfg.get("reverse_dcf", {}).get("margin_start", 0.2)
    m_end = cfg.get("reverse_dcf", {}).get("margin_end", 0.5)
    m_step = cfg.get("reverse_dcf", {}).get("margin_step", 0.05)
    r = 15
    m = m_start
    while m <= m_end + 1e-9:
        rd[f"A{r}"] = m
        rd[f"A{r}"].number_format = PCT
        for j, rev in enumerate(range(rev_start, rev_end + 1)):
            col = get_column_letter(2 + j)
            rd[f"{col}{r}"] = (f"=({col}$14*$A{r}*(1-Inputs!$B$17)*"
                               f"(1-Inputs!$B$19/Inputs!$B$20))/"
                               f"((Inputs!$B$18)-Inputs!$B$19)")
            rd[f"{col}{r}"].number_format = USD_B
            rd[f"{col}{r}"].fill = FILL_OUT
        r += 1
        m += m_step
    rd[f"A{r}"] = ("Grid cells are terminal EV in $ billions. Compare against "
                   "implied EV above.")
    rd[f"A{r + 1}"] = ("This is a simplified inversion; use the full DCF "
                       "sheet for detailed annual assumptions.")
    for cell in (f"A{r}", f"A{r + 1}"):
        rd[cell].font = FONT_NOTE
    rd.column_dimensions["A"].width = 36
    for j in range(1, 10):
        rd.column_dimensions[get_column_letter(1 + j)].width = 13

    # ========================================================= Sensitivity
    sn = wb.create_sheet("Sensitivity")
    sn["A1"] = "Valuation Sensitivities"
    sn["A1"].font = Font(name="Calibri", size=14, bold=True)
    navy(sn, "A3", "WACC \u00d7 Terminal Growth \u2014 Approximate DCF Share "
                   "Value")
    sn["A4"] = "WACC \\ g"
    sn["A4"].font = FONT_BOLD
    g_vals = cfg.get("sensitivity", {}).get("g_values",
                                            [0.02, 0.025, 0.03, 0.035, 0.04])
    for j, g in enumerate(g_vals):
        c = sn[f"{get_column_letter(2 + j)}4"]
        c.value = g
        c.font = FONT_BOLD
        c.fill = FILL_GRIDHDR
        c.number_format = PCT
    w_vals = cfg.get("sensitivity", {}).get("wacc_values",
                                            [0.095, 0.105, 0.115, 0.125,
                                             0.135])
    for i, w in enumerate(w_vals):
        r = 5 + i
        sn[f"A{r}"] = w
        sn[f"A{r}"].number_format = PCT
        for j, g in enumerate(g_vals):
            col = get_column_letter(2 + j)
            sn[f"{col}{r}"] = (f"=('DCF-Base'!$B$35+('DCF-Base'!$B$33/"
                               f"($A{r}-{col}$4))/(1+$A{r})^10"
                               f"-Inputs!$B$8)/Inputs!$B$5")
            sn[f"{col}{r}"].number_format = USD
            sn[f"{col}{r}"].fill = FILL_OUT
    navy(sn, "A12", "Terminal EBIT Margin \u00d7 Mature Revenue")
    sn["A13"] = "Margin \\ Revenue"
    sn["A13"].font = FONT_BOLD
    rev_vals = cfg.get("sensitivity", {}).get("rev_values",
                                              [6, 7, 8, 9, 10, 11, 12])
    for j, rev in enumerate(rev_vals):
        c = sn[f"{get_column_letter(2 + j)}13"]
        c.value = rev
        c.font = FONT_BOLD
        c.fill = FILL_GRIDHDR
    mg_vals = cfg.get("sensitivity", {}).get("margin_values",
                                             [0.2, 0.25, 0.3, 0.35, 0.4,
                                              0.45, 0.5])
    for i, mg in enumerate(mg_vals):
        r = 14 + i
        sn[f"A{r}"] = mg
        sn[f"A{r}"].number_format = PCT
        for j, rev in enumerate(rev_vals):
            col = get_column_letter(2 + j)
            sn[f"{col}{r}"] = (f"=({col}$13*$A{r}*(1-Inputs!$B$17)*"
                               f"(1-Inputs!$B$19/Inputs!$B$20))/"
                               f"((Inputs!$B$18)-Inputs!$B$19)")
            sn[f"{col}{r}"].number_format = USD_B
            sn[f"{col}{r}"].fill = FILL_OUT
    sn.column_dimensions["A"].width = 30

    # =============================================================== Checks
    chk = wb.create_sheet("Checks")
    navy(chk, "A3", "Workbook-wide checks")
    chk["A4"] = "Probability sum"
    chk["B4"] = "=SUM(Scenarios!B5:B9)"
    chk["B4"].number_format = PCT
    chk["A5"] = "Probability sum = 100%"
    chk["B5"] = "=ABS(B4-1)<0.0001"
    chk["B5"].fill = FILL_OUT
    navy(chk, "A7", "Per-scenario checks")
    chk["A8"] = "Check"
    chk["A8"].font = FONT_BOLD
    chk["A8"].fill = FILL_GRIDHDR
    for j, sheet_name in enumerate(SCEN_SHEETS):
        col = get_column_letter(2 + j)
        c = chk[f"{col}8"]
        c.value = sheet_name.replace("DCF-", "")
        c.font = FONT_BOLD
        c.fill = FILL_GRIDHDR
    checks = {
        9: "Terminal growth < WACC",
        10: "Terminal reinvestment < 100%",
        11: "Terminal FCFF > 0",
        12: "Intrinsic value / share > 0",
    }
    formula_tpl = {
        9: "='{s}'!B30<'{s}'!B11",
        10: "='{s}'!B32<1",
        11: "='{s}'!B33>0",
        12: "='{s}'!B41>0",
    }
    for r, label in checks.items():
        chk[f"A{r}"] = label
        for j, sheet_name in enumerate(SCEN_SHEETS):
            col = get_column_letter(2 + j)
            cell = chk[f"{col}{r}"]
            cell.value = formula_tpl[r].format(s=sheet_name)
            cell.fill = FILL_OUT
    chk["A14"] = ("Green = pass. If a check fails, review assumptions before "
                  "using the valuation.")
    chk["A14"].font = FONT_NOTE
    chk.column_dimensions["A"].width = 30

    # ------------------------------------------------------------ finalize
    order = ["README", "Inputs", "Scenarios"] + SCEN_SHEETS + \
            ["Scenario Summary", "Reverse DCF", "Sensitivity", "Checks"]
    wb._sheets = [wb[n] for n in order]
    wb.active = wb.sheetnames.index("Scenario Summary")
    return wb


def main():
    if len(sys.argv) != 3:
        print("usage: build_model.py <model_inputs.json> <output.xlsx>")
        sys.exit(2)
    with open(sys.argv[1]) as f:
        cfg = json.load(f)
    wb = build(cfg)
    wb.save(sys.argv[2])
    print("saved:", sys.argv[2])
    print("sheets:", wb.sheetnames)


if __name__ == "__main__":
    main()
