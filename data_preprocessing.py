import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    # Convert date column
    df['date'] = pd.to_datetime(df['date'])
    
    # Sort by date
    df = df.sort_values('date')
    
    # Handle missing values
    df = df.fillna(0)
    
    return df