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
import yaml
from datetime import datetime

# local modules
import fin_analysis.ratios as fira

# for supported LLMs
from llama_index.llms.gemini import Gemini
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core import ChatPromptTemplate
import google.generativeai as genai

# load all the LLM keys from local .env file
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# instantiate the LLM & ask a question
llm = Gemini(model="models/gemini-1.5-flash")

config_file_path = pathlib.Path(__file__).parent / "config/prompts.yaml"
assert (
    config_file_path.exists()
), f"FATAL ERROR: configuration file {config_file_path} does not exist!"

# load prompts from config
config = None
with open(str(config_file_path), "r") as f:
    config = yaml.safe_load(f)

if config is None:
    raise RuntimeError(
        f"FATAL ERROR: unable to read from configuration file at {config_file_path}"
    )

def main():

    NL2 = "\n\n"
    report: str = ""

    st.title("Financial Analysis of a Company Stock")
    st.markdown("### With LlamaIndex 🦙 and Google Gemini ♊")
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
        report += basic_info + NL2

        company_name = f"**Company Name:** {ticker.info['longName']}"
        st.markdown(company_name)
        report += company_name + NL2

        business_summary = f"**Business Summary:**"
        st.markdown(business_summary)
        long_business_summary = f"{ticker.info['longBusinessSummary']}"
        st.markdown(long_business_summary)
        report += long_business_summary + NL2

        ratios_title = f"## Financial Ratios"
        st.markdown(ratios_title)
        report += ratios_title + NL2

        # ---- Liquidity Ratios --------------------------
        liquidity_ratios_title = f"### Liquidity Ratios:"
        st.markdown(liquidity_ratios_title)
        report += liquidity_ratios_title + NL2

        liquidity_ratios = fira.liquidity_ratios(ticker_symbol)
        st.dataframe(liquidity_ratios)
        report += liquidity_ratios.to_markdown() + NL2

        # LLM analysis of liquidity ratios

        # build the chat prompt (prompts text defined in config/prompts.yaml file)
        liquidity_ratios_messages = [
            ChatMessage(
                role=MessageRole.SYSTEM,
                content=config["prompts"]["system_prompt"],
            ),
            ChatMessage(
                role=MessageRole.USER,
                content=config["prompts"]["liquidity_ratios_analysis_prompt"],
            ),
        ]
        liquidity_ratios_template = ChatPromptTemplate(liquidity_ratios_messages)
        prompt = liquidity_ratios_template.format(
            company_name=ticker.info["longName"],
            liquidity_ratios_table=liquidity_ratios.to_markdown(),
        )
        response = llm.complete(prompt)
        st.markdown(str(response))
        report += str(response) + NL2

        # ---- Profitability Ratios --------------------------
        profitability_ratios_title = f"### Profitability Ratios:"
        st.markdown(profitability_ratios_title)
        report += profitability_ratios_title + NL2

        profitability_ratios = fira.profitability_ratios(ticker_symbol)
        st.dataframe(profitability_ratios)
        report += profitability_ratios.to_markdown() + NL2

        # LLM analysis of profitability ratios

        # build the chat prompt (prompts text defined in config/prompts.yaml file)
        profitability_ratios_messages = [
            ChatMessage(
                role=MessageRole.SYSTEM,
                content=config["prompts"]["system_prompt"],
            ),
            ChatMessage(
                role=MessageRole.USER,
                content=config["prompts"]["profitability_ratios_analysis_prompt"],
            ),
        ]
        profitability_ratios_template = ChatPromptTemplate(
            profitability_ratios_messages
        )
        prompt = profitability_ratios_template.format(
            company_name=ticker.info["longName"],
            profitability_ratios_table=profitability_ratios.to_markdown(),
        )
        response = llm.complete(prompt)
        st.markdown(str(response))
        report += str(response) + NL2

        # ---- Efficiency Ratios --------------------------
        efficiency_ratios_title = f"### Efficiency Ratios:"
        st.markdown(efficiency_ratios_title)
        report += efficiency_ratios_title + NL2

        efficiency_ratios = fira.efficiency_ratios(ticker_symbol)
        st.dataframe(efficiency_ratios)
        report += efficiency_ratios.to_markdown() + NL2

        # LLM analysis of efficiency ratios

        # build the chat prompt (prompts text defined in config/prompts.yaml file)
        efficiency_ratios_messages = [
            ChatMessage(
                role=MessageRole.SYSTEM,
                content=config["prompts"]["system_prompt"],
            ),
            ChatMessage(
                role=MessageRole.USER,
                content=config["prompts"]["efficiency_ratios_analysis_prompt"],
            ),
        ]
        efficiency_ratios_template = ChatPromptTemplate(
            efficiency_ratios_messages
        )
        prompt = efficiency_ratios_template.format(
            company_name=ticker.info["longName"],
            efficiency_ratios_table=efficiency_ratios.to_markdown(),
        )
        response = llm.complete(prompt)
        st.markdown(str(response))
        report += str(response) + NL2

        # ---- Valuation Ratios --------------------------
        valuation_ratios_title = f"### Valuation Ratios:"
        st.markdown(valuation_ratios_title)
        report += valuation_ratios_title + NL2

        valuation_ratios = fira.valuation_ratios(ticker_symbol)
        st.dataframe(valuation_ratios)
        report += valuation_ratios.to_markdown() + NL2

        # LLM analysis of valuation ratios

        # build the chat prompt (prompts text defined in config/prompts.yaml file)
        valuation_ratios_messages = [
            ChatMessage(
                role=MessageRole.SYSTEM,
                content=config["prompts"]["system_prompt"],
            ),
            ChatMessage(
                role=MessageRole.USER,
                content=config["prompts"]["valuation_ratios_analysis_prompt"],
            ),
        ]
        valuation_ratios_template = ChatPromptTemplate(
            valuation_ratios_messages
        )
        prompt = valuation_ratios_template.format(
            company_name=ticker.info["longName"],
            valuation_ratios_table=valuation_ratios.to_markdown(),
        )
        response = llm.complete(prompt)
        st.markdown(str(response))
        report += str(response) + NL2

        # ---- Leverage Ratios --------------------------
        leverage_ratios_title = f"### Leverage Ratios:"
        st.markdown(leverage_ratios_title)
        report += leverage_ratios_title + NL2

        leverage_ratios = fira.leverage_ratios(ticker_symbol)
        st.dataframe(leverage_ratios)
        report += leverage_ratios.to_markdown() + NL2

        # LLM analysis of leverage ratios

        # build the chat prompt (prompts text defined in config/prompts.yaml file)
        leverage_ratios_messages = [
            ChatMessage(
                role=MessageRole.SYSTEM,
                content=config["prompts"]["system_prompt"],
            ),
            ChatMessage(
                role=MessageRole.USER,
                content=config["prompts"]["leverage_ratios_analysis_prompt"],
            ),
        ]
        leverage_ratios_template = ChatPromptTemplate(
            leverage_ratios_messages
        )
        prompt = leverage_ratios_template.format(
            company_name=ticker.info["longName"],
            leverage_ratios_table=leverage_ratios.to_markdown(),
        )
        response = llm.complete(prompt)
        st.markdown(str(response))
        report += str(response) + NL2

        # ---- Performance & Growth Metrics --------------------------
        performance_and_growth_metrics_title = f"### Performance & Growth Metrics:"
        st.markdown(performance_and_growth_metrics_title)
        report += performance_and_growth_metrics_title + NL2

        performance_and_growth_metrics = fira.performance_and_growth_metrics(
            ticker_symbol
        )
        st.dataframe(performance_and_growth_metrics)
        report += performance_and_growth_metrics.to_markdown() + NL2

        # LLM analysis of performance_and_growth ratios

        # build the chat prompt (prompts text defined in config/prompts.yaml file)
        performance_and_growth_metrics_messages = [
            ChatMessage(
                role=MessageRole.SYSTEM,
                content=config["prompts"]["system_prompt"],
            ),
            ChatMessage(
                role=MessageRole.USER,
                content=config["prompts"]["performance_and_growth_metrics_prompt"],
            ),
        ]
        performance_and_growth_metrics_template = ChatPromptTemplate(
            performance_and_growth_metrics_messages
        )
        prompt = performance_and_growth_metrics_template.format(
            company_name=ticker.info["longName"],
            performance_and_growth_ratios_table=performance_and_growth_metrics.to_markdown(),
        )
        response = llm.complete(prompt)
        st.markdown(str(response))
        report += str(response) + NL2

        # --------------- FINAL RECOMMENDATION from LLM ---------------------------
        final_recommendation_messages = [
            ChatMessage(
                role=MessageRole.SYSTEM,
                content=config["prompts"]["system_prompt"],
            ),
            ChatMessage(
                role=MessageRole.USER,
                content=config["prompts"]["overall_assessment_prompt"],
            ),
        ]
        final_recommendation_template = ChatPromptTemplate(
            final_recommendation_messages
        )
        prompt = final_recommendation_template.format(
            company_name=ticker.info["longName"],
            performance_and_assessment=report,
        )
        response = llm.complete(prompt)
        st.markdown(str(response))
        report += str(response) + NL2

        # write the report to file
        if report != "":
            reports_dir = pathlib.Path(__file__).parent / "reports"
            reports_dir.mkdir(exist_ok=True)
            datetime_str = datetime.now().strftime("%d%b%Y_%H%M%S")
            report_file_path = (
                reports_dir / f"Analysis Report {ticker_symbol}_{datetime_str}.md"
            )
            with open(str(report_file_path), "w") as f:
                f.write(report)


if __name__ == "__main__":
    main()
