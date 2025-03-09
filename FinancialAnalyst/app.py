"""
app.py - Financial Analysis of a company stock using Google Gemini
    and Llamaindex.

NOTE: this example uses Google Gemini it's LLM.
You'll need to get a Gemini API key from Google AI Studio (aistudio.google.com/app/apikey)
and save it to local .env file as GOOGLE_API_KEY=XXXXX....

Author: Manish Bhobe
My experiments with Python, AI and Generative AI
Code is meant for learning purposes ONLY!
"""

import yfinance as yf
import pandas as pd
import numpy as np
import streamlit as st
import os, sys
from dotenv import load_dotenv, find_dotenv
import pathlib
from datetime import datetime
import streamlit as st

# local modules
import fin_analysis.ratios as fira

# for supported LLMs
from llama_index.llms.gemini import Gemini
import google.generativeai as genai

# load all the LLM keys from local .env file
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# instantiate the LLM & ask a question
llm = Gemini(model="models/gemini-1.5-flash")


def main():
    st.title("Financial Analysis of a company with LlamaIndex 🦙 and Google Gemini ♊")
    ticker_symbol = st.text_input(
        "Enter the Company Ticker as used by Yahoo! Finance (e.g AAPL, PERSISTENT.NS):"
    )

    if ticker_symbol:
        if not fira.is_valid_ticker(ticker_symbol):
            st.error(
                f"{ticker_symbol} appears to be an invalid ticker symbol. Please enter a valid ticker symbol"
            )
            st.stop()

        ticker = yf.Ticker(ticker_symbol)

        basic_info = f"## Basic Info for {ticker_symbol}"
        st.markdown(basic_info)

        company_name = f"**Company Name:** {ticker.info['longName']}"
        st.markdown(company_name)

        business_summary = f"**Business Summary:**"
        st.markdown(business_summary)
        long_business_summary = f"{ticker.info['longBusinessSummary']}"
        st.markdown(long_business_summary)

        ratios_title = f"## Financial Ratios"
        st.markdown(ratios_title)

        liquidity_ratios_title = f"### Liquidity Ratios:"
        st.markdown(liquidity_ratios_title)
        liquidity_ratios = fira.liquidity_ratios(ticker_symbol)
        st.dataframe(liquidity_ratios)

        # TODO: ask LLM to analyze liquidity ratios & print summary

        profitability_ratios_title = f"### Profitability Ratios:"
        st.markdown(profitability_ratios_title)
        profitability_ratios = fira.profitability_ratios(ticker_symbol)
        st.dataframe(profitability_ratios)

        # TODO: ask LLM to analyze profitability ratios & print summary

        efficiency_ratios_title = f"### Efficiency Ratios:"
        st.markdown(efficiency_ratios_title)
        efficiency_ratios = fira.efficiency_ratios(ticker_symbol)
        st.dataframe(efficiency_ratios)

        # TODO: ask LLM to analyze efficiency ratios & print summary

        valuation_ratios_title = f"### Valuation Ratios:"
        st.markdown(valuation_ratios_title)
        valuation_ratios = fira.valuation_ratios(ticker_symbol)
        st.dataframe(valuation_ratios)

        # TODO: ask LLM to analyze valuation ratios & print summary

        leverage_ratios_title = f"### Leverage Ratios:"
        st.markdown(leverage_ratios_title)
        leverage_ratios = fira.leverage_ratios(ticker_symbol)
        st.dataframe(leverage_ratios)

        # TODO: ask LLM to analyze leverage ratios & print summary

        performance_and_growth_metrics_title = f"### Performance & Growth Metrics:"
        st.markdown(performance_and_growth_metrics_title)
        performance_and_growth_metrics = fira.performance_and_growth_metrics(
            ticker_symbol
        )
        st.dataframe(performance_and_growth_metrics)

        # TODO: ask LLM to analyze performance & growth metrics & print summary


if __name__ == "__main__":
    main()
