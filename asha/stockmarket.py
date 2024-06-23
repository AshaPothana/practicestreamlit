import streamlit as st
import yfinance as yf

msft = yf.Ticker("MSFT")
hist = msft.history(period="1d",start="2019-01-01",end="2024-06-23")
st.dataframe(hist)

st.line_chart(hist.Close)