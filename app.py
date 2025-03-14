import os
os.environ['GROQ_API_KEY'] = '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'

import streamlit as st
from components.tools import fetch_stock_data, analyze_stock
from components.agents import StockAnalysisAgent


agent = StockAnalysisAgent()

st.title("📈 Stock Analysis with AI Insights")

ticker = st.text_input("Enter a stock ticker (e.g., AAPL, MSFT):")
st.markdown("Note: Use official ticker symbols only. [Find ticker symbols here](https://finance.yahoo.com/lookup).")
if ticker:
    stock_data = fetch_stock_data(ticker)
    if isinstance(stock_data, str):
        st.error(stock_data)
    else:
        analysis = analyze_stock(stock_data)
        detailed_analysis = agent.generate_analysis(stock_data=analysis)
        
        st.subheader("Detailed Stock Analysis")
        
        st.write(detailed_analysis)
        
        custom_query = st.text_input("Do you have any specific questions about this stock?")
        if custom_query:
            custom_response = agent.generate_custom_insight(detailed_analysis, custom_query)
            st.subheader("Custom Insight")
            st.write(custom_response)
