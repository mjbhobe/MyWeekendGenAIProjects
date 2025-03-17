from agents.financial_analysis_agent import financial_analysis_agent

def generate_financial_analysis(symbol: str):
    prompt = f"""
        Generate financial analysis for {symbol}
    """
    return financial_analysis_agent.print_response(prompt, stream=True)



# try for various companies
# AAPL - Apple
# AMZN - Amazon
# MSFT - Microsoft Corp
# RELIANCE.NS - Reliance Industries
# TCS.NS - TCS
generate_financial_analysis("TCS.NS")

# print(type(financial_analysis_agent))