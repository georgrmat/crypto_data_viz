import streamlit as st
import mplfinance as mpf
import pandas as pd

# Load the CSV data
df = pd.read_csv("df.csv")
st.dataframe(df)
df.rename(columns = {"open_time": "date"}, inplace = True)
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

"""
# Define the Streamlit app
st.title("Candlestick Chart App")

# Define the style of the chart
style = mpf.make_mpf_style(base_mpf_style='binance', gridstyle='--')

# Display the candlestick chart using Streamlit's st.pyplot
fig, axlist = mpf.plot(df[0:10], type='candle', style=style, title="OHLCV Candlestick Chart", returnfig=True)

# Show the chart in Streamlit
st.pyplot(fig)
"""
