
from agents.sentiment_analysis_agent import sentiment_analysis_agent

def generate_sentiment_analysis(symbol: str):
    prompt = f"""
        Generate sentiment analysis for {symbol}
    """
    return sentiment_analysis_agent.print_response(prompt, stream=True)



# try for various companies
# AAPL - Apple
# AMZN - Amazon
# MSFT - Microsoft Corp
# RELIANCE.NS - Reliance Industries
# TCS.NS - TCS
generate_sentiment_analysis("BAC")

# print(type(financial_analysis_agent))