import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the CSV data
df = pd.read_csv("df.csv")

df.rename(columns={"open_time": "date"}, inplace=True)
df["date"] = pd.to_datetime(df["date"], unit="ms")
df.set_index("date", inplace=True)

# Initialize the candlestick chart
fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
candlestick_trace = go.Candlestick(
    x=df.index,
    open=df['open'],
    high=df['high'],
    low=df['low'],
    close=df['close'],
    name="Candlesticks"
)
fig.add_trace(candlestick_trace, row=1, col=1)

# Initialize drawing shapes
shapes = []

# Define the Streamlit app
st.title("Trading Chart with Drawing")

# Add buttons for drawing
draw_line = st.button("Draw Trend Line")
draw_rectangle = st.button("Draw Rectangle")

# Define a callback for drawing lines
if draw_line:
    st.write("Click on the chart to draw a trend line.")

    # Handle user interaction for drawing a line
    clicked_points = st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": False})

    # Store the clicked points in a list
    if st.button("Finish Drawing"):
        shapes.append(
            go.layout.Shape(
                type="line",
                x0=clicked_points.clickData["points"][0]["x"],
                y0=clicked_points.clickData["points"][0]["y"],
                x1=clicked_points.clickData["points"][1]["x"],
                y1=clicked_points.clickData["points"][1]["y"],
                line=dict(color="red", width=2)
            )
        )

# Define a callback for drawing rectangles
if draw_rectangle:
    st.write("Click and drag on the chart to draw a rectangle.")

    # Handle user interaction for drawing a rectangle
    drawn_shape = st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": False, "editable": True})

    # Store the drawn rectangle in a list
    if st.button("Finish Drawing"):
        shapes.append(
            go.layout.Shape(
                type="rect",
                x0=drawn_shape.to_dict()["props"]["figure"]["layout"]["dragmode"][0]["dragmode"]["x0"],
                y0=drawn_shape.to_dict()["props"]["figure"]["layout"]["dragmode"][0]["dragmode"]["y0"],
                x1=drawn_shape.to_dict()["props"]["figure"]["layout"]["dragmode"][0]["dragmode"]["x1"],
                y1=drawn_shape.to_dict()["props"]["figure"]["layout"]["dragmode"][0]["dragmode"]["y1"],
                fillcolor="rgba(0, 0, 255, 0.2)"
            )
        )

# Update the chart with the drawn shapes
fig.update_layout(shapes=shapes)

# Display the updated chart
st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": False})





