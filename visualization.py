import matplotlib.pyplot as plt
import os

def plot_forecast(forecast):
    
    os.makedirs("images", exist_ok=True)
    
    plt.figure(figsize=(10,5))
    
    # Plot predicted values
    plt.plot(forecast['ds'], forecast['yhat'], label='Forecast', color='blue')
    
    plt.title("Sales Forecast")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()
    
    plt.savefig("images/forecast.png")
    plt.close()