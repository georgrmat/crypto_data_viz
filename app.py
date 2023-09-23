import streamlit as st
import plotly.express as px
import pandas as pd

# Create a Streamlit app
st.title("Trading Chart App")

# Load and display your trading data (you can replace this with your data)
data = pd.read_csv(r"df.csv")
st.line_chart(data)

# Add drawing capabilities (for user annotations)
st.subheader("Draw on the Chart")
drawn_chart = st.plotly_chart(px.scatter())
