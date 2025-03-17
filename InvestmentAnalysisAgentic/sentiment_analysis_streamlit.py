import streamlit as st

from agno.agent import RunResponse
from agents.sentiment_analysis_agent import sentiment_analysis_agent

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis Assistant",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .main-header {
        text-align: center;
        padding: 2rem 0;
    }
    .stock-input {
        max-width: 400px;
        margin: 0 auto;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'analysis_generated' not in st.session_state:
    st.session_state.analysis_generated = False

def generate_sentiment_analysis(symbol: str, agent):
    prompt = f"Generate sentiment analysis for {symbol}"
    # return agent.print_response(prompt, stream=True)
    response: RunResponse = agent.run(prompt, markdown=True)
    return response.content

# Main UI
st.markdown("<h1 class='main-header'>Sentiment Analysis Assistant 📈</h1>", unsafe_allow_html=True)

st.markdown("""
    This tool provides sentiment analysis of the latest news headline for a stock symbol.
    Enter a stock symbol (e.g., TCS.NS for Tata Consultancy Services) to get started.
""")

# Stock symbol input
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        stock_symbol = st.text_input(
            "Enter Stock Symbol",
            placeholder="e.g., TCS.NS",
            key="stock_input"
        )
    with col2:
        analyze_button = st.button("Analyze", type="primary")

# Analysis section
if analyze_button and stock_symbol:
    try:
        with st.spinner("Generating sentiment analysis..."):
            analysis = generate_sentiment_analysis(stock_symbol, sentiment_analysis_agent)
            
        st.success("Analysis completed!")
        
        # Display analysis in an expandable container
        with st.expander("View Detailed Analysis", expanded=True):
            st.markdown(analysis)
            
        st.session_state.analysis_generated = True
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <small>Powered by Agno AGI &amp; Gemini AI • Built with Streamlit</small>
    </div>
""", unsafe_allow_html=True)