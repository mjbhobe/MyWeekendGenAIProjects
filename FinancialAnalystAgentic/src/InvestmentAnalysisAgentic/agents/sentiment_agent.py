
from phi.agent import Agent
from tools.sentiment_tools import fetch_news_yahoo, analyze_sentiment

class SentimentAnalysisAgent(Agent):
    def __init__(self):
        super().__init__(
            name="SentimentAnalysisAgent",
            description="Fetches recent news and performs sentiment analysis.",
            input_instructions="Input a stock symbol (e.g., AAPL).",
            output_instructions="Returns sentiment tone, score, and top headlines.",
        )

    def run(self, symbol: str):
        headlines = fetch_news_yahoo(symbol)
        sentiment = analyze_sentiment(headlines)
        return sentiment
