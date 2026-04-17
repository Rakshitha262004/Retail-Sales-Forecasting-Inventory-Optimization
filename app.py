import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_preprocessing import load_data, clean_data
from src.forecasting import train_forecast
from src.inventory import inventory_optimization

st.title("📊 Retail Sales Forecasting & Inventory Optimization")

# Upload file
uploaded_file = st.file_uploader("Upload your sales data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.write("### 📂 Dataset Preview")
    st.dataframe(df.head())

    # Clean data
    df = clean_data(df)

    # Forecast
    st.write("### 🔮 Forecasting...")
    forecast = train_forecast(df)

    st.write("### 📈 Forecast Output")
    st.line_chart(forecast[['ds', 'yhat']].set_index('ds'))

    # Inventory
    st.write("### 📦 Inventory Optimization")
    inventory = inventory_optimization(forecast)

    st.dataframe(inventory)

    st.success("✅ Process Completed Successfully!")