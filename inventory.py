import pandas as pd
import numpy as np
import os

def inventory_optimization(forecast):
    
    # Use predicted demand
    demand = forecast['yhat']
    
    avg_demand = demand.mean()
    std_demand = demand.std()
    
    # Business assumptions
    lead_time = 7  # days
    service_level = 1.65  # 95% confidence
    
    # Safety Stock
    safety_stock = service_level * std_demand * np.sqrt(lead_time)
    
    # Reorder Point
    reorder_point = (avg_demand * lead_time) + safety_stock
    
    result = pd.DataFrame({
        "Average Demand": [avg_demand],
        "Std Dev Demand": [std_demand],
        "Safety Stock": [safety_stock],
        "Reorder Point": [reorder_point]
    })
    
    os.makedirs("outputs", exist_ok=True)
    result.to_csv("outputs/inventory_report.csv", index=False)
    
    return result