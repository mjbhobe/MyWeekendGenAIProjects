
from phi.agent import Agent
from tools.finance_tools import get_ratios_yf, parse_10k_summary

class FinancialAnalysisAgent(Agent):
    def __init__(self):
        super().__init__(
            name="FinancialAnalysisAgent",
            description="Analyzes financials using Yahoo Finance and 10-K summary from EDGAR.",
            input_instructions="Input a company ticker (e.g., AAPL).",
            output_instructions="Returns financial ratios and 10-K summary.",
        )

    def run(self, symbol: str):
        ratios = get_ratios_yf(symbol)
        summary = parse_10k_summary(symbol)
        return {**ratios, "10k_summary": summary}
