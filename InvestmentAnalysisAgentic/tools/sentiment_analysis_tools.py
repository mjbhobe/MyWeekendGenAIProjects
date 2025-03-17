import json
import yfinance as yf
from bs4 import BeautifulSoup
from textblob import TextBlob
from typing import List

from agno.tools import Toolkit
from agno.utils.log import logger


class SentimentAnalysisTools(Toolkit):
    def __init__(self):
        super().__init__(name="sentiment_analysis_tools")

        # register functions as tools
        logger.debug("Registering analyze_sentiment function")
        self.register(self.analyze_sentiment)


    def analyze_sentiment(self, symbol:str) -> str:
        """use this function to analyze market sentiment for a given stock symbol
           it downloads 25 market headlines from Yahoo News and analyzes sentiment.

        Args:
            symbol (str): The stock symbol.

        Returns:
           str: JSON string containing following info
            {
                "sentiment" (string): "Positive" or "Negtive" or "Neutral",
                "avg_score" (float): average sentiment score (float),
                "scores" (List[float]) : [list of sentiment score for each headline]
                "headlines" (List[str]): list of news headlines (strings)
            }
        """
        try:
            # fetch latest headlines
            ticker = yf.Ticker(symbol)
            news = ticker.get_news(count=25)
            headlines = [h["content"]["summary"] for h in news]
            # headlines = self.__fetch_news_yahoo(symbol)
            # polarity is a float in range [-1.0, 1.0]
            scores = [TextBlob(h).sentiment.polarity for h in headlines]
            logger.debug(f"analyze_sentiment scores: {scores}")
            avg = sum(scores) / len(scores) if scores else 0
            logger.debug(f"analyze_sentiment average sentimen score: {avg:.3f}")
            # this is my scoring criteria - usually a >0 value is positive sentiment
            # =0 value is neutral and <0 value is negative sentiment
            tone = "Positive" if avg > 0.1 else "Negative" if avg < -0.1 else "Neutral"
            sentiment_analysis = {
                "sentiment": tone, 
                "avg_score": round(avg, 3), 
                "scores": scores, 
                "headlines": headlines,
            }
            return json.dumps(sentiment_analysis, indent=2)
        except Exception as e:
            return f"Error fetching company news for {symbol}: {e}"


if __name__ == "__main__":
    from rich import print
    # testing harness - will never be called directly
    #symbols = ["AAPL", "RELIANCE.NS", "TCS.NS", "MSFT", "MS", "BAC"]
    symbols=["BAC"]
    sat = SentimentAnalysisTools()
    for symbol in symbols:
        print(f"Fetching sentiments for {symbol}", flush=True)
        print(sat.analyze_sentiment(symbol))
