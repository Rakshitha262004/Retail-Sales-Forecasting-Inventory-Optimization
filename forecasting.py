from prophet import Prophet
import pandas as pd
import os

def train_forecast(df):
    # Rename columns for Prophet
    df = df.rename(columns={'date': 'ds', 'sales': 'y'})
    
    # Initialize model
    model = Prophet()
    
    # Train model
    model.fit(df)
    
    # Future prediction
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    
    # Save output
    os.makedirs("outputs", exist_ok=True)
    forecast[['ds', 'yhat']].to_csv("outputs/forecast.csv", index=False)
    
    return forecast