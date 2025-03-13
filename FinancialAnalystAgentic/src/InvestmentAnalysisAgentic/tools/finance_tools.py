
import yfinance as yf
from sec_edgar_downloader import Downloader
import os
from PyPDF2 import PdfReader

def get_ratios_yf(symbol):
    t = yf.Ticker(symbol)
    fin = t.financials
    bs = t.balance_sheet
    cf = t.cashflow
    try:
        revenue_growth = ((fin.loc["Total Revenue"][0] - fin.loc["Total Revenue"][1]) / fin.loc["Total Revenue"][1]) * 100
        net_margin = (fin.loc["Net Income"][0] / fin.loc["Total Revenue"][0]) * 100
        roe = (fin.loc["Net Income"][0] / bs.loc["Total Stockholder Equity"][0]) * 100
        fcf = cf.loc["Total Cash From Operating Activities"][0] - cf.loc["Capital Expenditures"][0]
        debt_equity = bs.loc["Total Liab"][0] / bs.loc["Total Stockholder Equity"][0]
    except Exception as e:
        return {"error": str(e)}
    return {
        "revenue_growth": f"{revenue_growth:.2f}%",
        "net_margin": f"{net_margin:.2f}%",
        "roe": f"{roe:.2f}%",
        "debt_equity": f"{debt_equity:.2f}",
        "free_cash_flow": f"{fcf/1e9:.2f} B"
    }

def parse_10k_summary(symbol):
    dl = Downloader(os.getcwd())
    dl.get("10-K", symbol, amount=1)
    path = f"sec-edgar-filings/{symbol}/10-K"
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                    return f.read()[:1000]
    return "10-K not available"
