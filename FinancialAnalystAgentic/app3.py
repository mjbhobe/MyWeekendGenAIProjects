import streamlit as st
from agno.agent import RunResponse
from agents.financial_analysis_agent import fa_agent
from PIL import Image  # For image handling

# Page configuration
st.set_page_config(
    page_title="Financial Analysis Assistant", page_icon="📊", layout="wide"
)

# Custom CSS
st.markdown(
    """
    <style>
    .stApp {
        max-width: 100%; /* Take full width */
    }
    .main-header {
        text-align: center;
        padding: 2rem 0;
    }
    .sidebar .sidebar-content {
        background-color: #f0f8ff; /* Light background for sidebar */
    }
    .full-width-output {
        width: 100%;
        padding: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def generate_financial_analysis(symbol: str, agent):
    prompt = f"Generate financial analysis for {symbol}"
    # return agent.print_response(prompt, stream=True)
    response: RunResponse = agent.run(prompt, markdown=True)
    return response.content


# Sidebar for parameters
st.sidebar.header("Analysis Parameters")

# Add a picture to the sidebar.
sidebar_image = Image.open("financial_analysis_sidebar.png")  # replace with your image.
st.sidebar.image(sidebar_image, use_column_width=True)

stock_symbol = st.sidebar.text_input(
    "Enter Stock Symbol",
    placeholder="e.g., TCS.NS",
    key="stock_input",
)

analyze_button = st.sidebar.button("Generate Analysis", type="primary")

# Main UI
st.markdown(
    "<h1 class='main-header'>Financial Analysis Assistant 📈</h1>",
    unsafe_allow_html=True,
)

main_image = Image.open("financial_analysis_main.png")  # replace with your image
st.image(main_image, use_column_width=True)

st.markdown(
    """
    This tool provides detailed financial analysis for publicly traded companies.
"""
)

# Analysis section
if analyze_button and stock_symbol:
    try:
        with st.spinner("Generating financial analysis..."):
            analysis = generate_financial_analysis(stock_symbol, fa_agent)

        st.success("Analysis completed!")

        # Display analysis in a full-width container
        with st.container():
            st.markdown("## Detailed Analysis", unsafe_allow_html=True)
            st.markdown(analysis, unsafe_allow_html=True)

        st.session_state.analysis_generated = True

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <small>Powered by Google Gemini AI • Built with Streamlit</small>
    </div>
""",
    unsafe_allow_html=True,
)
