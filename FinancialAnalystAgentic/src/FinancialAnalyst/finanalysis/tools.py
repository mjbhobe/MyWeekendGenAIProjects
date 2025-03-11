import json

from agno.tools import Toolkit
from agno.utils.log import logger

try:
    import yfinance as yf
except ImportError:
    raise ImportError("`yfinance` not installed. Please install using `pip install yfinance`.")
from .ratios import (
    liquidity_ratios,
    profitability_ratios,
    efficiency_ratios,
    valuation_ratios,
    leverage_ratios,
    performance_and_growth_metrics,
)

class FinancialAnalysisTools(Toolkit):
    def __init__(self):
        super().__init__(name="finanalysis_tools")

        # register all functions
        self.register(liquidity_ratios)
        self.register(profitability_ratios)
        self.register(efficiency_ratios)
        self.register(valuation_ratios)
        self.register(leverage_ratios)
        self.register(performance_and_growth_metrics)

