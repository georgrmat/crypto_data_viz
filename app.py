import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load the CSV data
df = pd.read_csv("df.csv")

df.rename(columns={"open_time": "date"}, inplace=True)
df["date"] = pd.to_datetime(df["date"], unit="ms")
df.set_index("date", inplace=True)

# Define the Streamlit app
st.title("Trading Chart with Positions")

# Create a candlestick chart using Plotly
candlestick_trace = go.Candlestick(
    x=df.index,
    open=df['open'],
    high=df['high'],
    low=df['low'],
    close=df['close'],
    name="Candlesticks"
)

# Create a scatter trace for positions (stop loss and take profit)
positions_trace = go.Scatter(
    x=[df.index[10], df.index[20]],  # Adjust the x-coordinates for your positions
    y=[150, 160],  # Adjust the y-coordinates for your positions
    mode="markers+text",
    marker=dict(
        size=10,
        color=["red", "green"],  # Red for stop loss, green for take profit
    ),
    text=["Stop Loss", "Take Profit"],  # Labels for positions
    textposition="top right",
)

# Customize the chart layout
layout = go.Layout(
    title="OHLCV Candlestick Chart with Positions",
    xaxis_title="Date",
    yaxis_title="Price",
    showlegend=True,
    shapes=[],
)

# Add positions to the layout as rectangles
layout.shapes.extend([
    go.layout.Shape(
        type="rect",
        xref="x",
        yref="y",
        x0=df.index[10],  # Adjust x0 and x1 for the stop loss position
        y0=150,           # Adjust y0 and y1 for the stop loss position
        x1=df.index[12],  # Adjust x0 and x1 for the take profit position
        y1=160,           # Adjust y0 and y1 for the take profit position
        fillcolor="rgba(255, 0, 0, 0.2)",  # Red for stop loss
        line=dict(width=0),
    ),
    go.layout.Shape(
        type="rect",
        xref="x",
        yref="y",
        x0=df.index[20],  # Adjust x0 and x1 for the stop loss position
        y0=150,           # Adjust y0 and y1 for the stop loss position
        x1=df.index[22],  # Adjust x0 and x1 for the take profit position
        y1=160,           # Adjust y0 and y1 for the take profit position
        fillcolor="rgba(0, 255, 0, 0.2)",  # Green for take profit
        line=dict(width=0),
    ),
])

# Create the figure
fig = go.Figure(data=[candlestick_trace, positions_trace], layout=layout)

# Display the candlestick chart with positions using Streamlit
st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": False})
