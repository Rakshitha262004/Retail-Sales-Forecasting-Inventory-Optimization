import pandas as pd
import numpy as np

dates = pd.date_range(start="2023-01-01", periods=365)

np.random.seed(42)

sales = []
for i in range(len(dates)):
    base = 50
    trend = i * 0.1
    seasonality = 15 * np.sin(i * (2 * np.pi / 30))
    noise = np.random.normal(0, 5)
    
    sales.append(base + trend + seasonality + noise)

df = pd.DataFrame({
    "date": dates,
    "sales": sales
})

df.to_csv("data/raw/sales.csv", index=False)

print("Dataset created successfully!")