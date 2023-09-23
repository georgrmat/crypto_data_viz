import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load the CSV data
df = pd.read_csv("df.csv")

df.rename(columns={"open_time": "date"}, inplace=True)
df["date"] = pd.to_datetime(df["date"], unit="ms")
df.set_index("date", inplace=True)

# Define the Streamlit app
st.title("Candlestick Chart App")

# Create a candlestick chart using Plotly
candlestick_chart = go.Figure(data=[go.Candlestick(x=df.index,
                                                   open=df['open'],
                                                   high=df['high'],
                                                   low=df['low'],
                                                   close=df['close'])])

# Customize the chart layout
candlestick_chart.update_layout(title="OHLCV Candlestick Chart",
                                xaxis_title="Date",
                                yaxis_title="Price")

# Add a horizontal line
candlestick_chart.add_shape(
    type="line",
    x0=df.index[0],
    x1=df.index[-1],
    y0=150,  # Adjust the y-coordinate as needed
    y1=150,  # Adjust the y-coordinate as needed
    line=dict(
        color="red",  # Color of the line
        width=2,       # Line width
        dash="dash"   # Line style ('dash' for dashed line)
    ),
)

# Add a colored rectangle
candlestick_chart.add_shape(
    type="rect",
    x0=df.index[10],  # Adjust the x-coordinates as needed
    x1=df.index[20],
    y0=140,            # Adjust the y-coordinates as needed
    y1=160,
    line=dict(
        color="blue",   # Border color of the rectangle
        width=2,        # Border width
    ),
    fillcolor="rgba(0, 0, 255, 0.2)"  # Fill color of the rectangle (with opacity)
)

# Display the candlestick chart using Streamlit
st.plotly_chart(candlestick_chart)

