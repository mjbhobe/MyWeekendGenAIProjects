
import streamlit as st
from agents.financial_agent import FinancialAnalysisAgent
from agents.sentiment_agent import SentimentAnalysisAgent

st.set_page_config(page_title="📊 Company Analyzer", layout="wide")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2721/2721262.png", width=100)
st.sidebar.title("Company Analyzer")
symbol = st.sidebar.text_input("Enter Stock Symbol", "AAPL")
run = st.sidebar.button("🔎 Analyze")

st.title("📈 Company Investment Analysis")

if run:
    with st.spinner("Running analysis..."):
        fa = FinancialAnalysisAgent()
        sa = SentimentAnalysisAgent()
        fin = fa.run(symbol)
        sent = sa.run(symbol)

    st.success("Analysis Complete!")

    st.subheader("🧾 Financial Summary")
    st.markdown(f"""
- **Revenue Growth**: {fin['revenue_growth']}
- **Net Margin**: {fin['net_margin']}
- **ROE**: {fin['roe']}
- **Debt/Equity**: {fin['debt_equity']}
- **Free Cash Flow**: {fin['free_cash_flow']}

**10-K Summary:**  
> {fin['10k_summary']}
""")

    st.subheader("📰 Sentiment Analysis")
    st.markdown(f"""
- **Tone**: {sent['sentiment']}
- **Polarity Score**: {sent['score']}

**Top Headlines**:
""")
    for h in sent['headlines']:
        st.markdown(f"- {h}")
