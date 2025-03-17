
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

def fetch_news_yahoo(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}?p={symbol}"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    headlines = [a.text for a in soup.find_all("a") if a.text and len(a.text) > 40][:5]
    return headlines

def analyze_sentiment(headlines):
    scores = [TextBlob(h).sentiment.polarity for h in headlines]
    avg = sum(scores) / len(scores) if scores else 0
    tone = "Positive" if avg > 0.1 else "Negative" if avg < -0.1 else "Neutral"
    return {"sentiment": tone, "score": round(avg, 3), "headlines": headlines}
