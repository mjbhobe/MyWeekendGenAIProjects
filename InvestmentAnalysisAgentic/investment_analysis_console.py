
from textwrap import dedent
from agents.investment_analysis_agent import investment_analysis_agent

def generate_investment_analysis(symbol: str):
    prompt = dedent(f"""
        Generate investment analysis for {symbol}
    """)
    return investment_analysis_agent.print_response(prompt, stream=True)



# try for various companies
# AAPL - Apple
# AMZN - Amazon
# MSFT - Microsoft Corp
# RELIANCE.NS - Reliance Industries
# TCS.NS - TCS
generate_investment_analysis("BAC")

# print(type(financial_analysis_agent))