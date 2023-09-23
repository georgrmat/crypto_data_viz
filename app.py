import streamlit as st
import mplfinance as mpf
import pandas as pd
import plotly.graph_objects as go

# Load the CSV data
df = pd.read_csv("df.csv")

df.rename(columns = {"open_time": "date"}, inplace = True)
df["date"] = pd.to_datetime(df["date"], unit = "ms")
df.set_index("date", inplace=True)



# Define the Streamlit app
st.title("Candlestick Chart App")

# Add a date range slider to customize the data displayed
date_range = st.date_input("Select Date Range", min_value=df.index.min(), max_value=df.index.max())

# Filter the data based on the selected date range
filtered_df = df[(df.index >= date_range[0]) & (df.index <= date_range[1])]
st.dataframe(filtered_df)
# Create a candlestick chart using Plotly
candlestick_chart = go.Figure(data=[go.Candlestick(x=filtered_df.index,
                                                   open=filtered_df['open'],
                                                   high=filtered_df['high'],
                                                   low=filtered_df['low'],
                                                   close=filtered_df['close'])])

# Customize the chart layout
candlestick_chart.update_layout(title="OHLCV Candlestick Chart",
                                xaxis_title="Date",
                                yaxis_title="Price")

# Display the candlestick chart using Streamlit

st.plotly_chart(candlestick_chart)
