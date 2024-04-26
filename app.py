import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Replace 'your_api_key_here' with your actual OpenWeatherMap API key
api_key = "4a3544f23ba44cccb8e183254242604"
lat, lon = 40.7128, -74.0060  # Example coordinates for New York City

# Function to get historical weather data
def get_historical_weather(lat, lon, dt, api_key):
    url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data:", response.status_code, response.text)
        return None  # Return None if there was an error fetching data

# Getting data for the last 5 days
dates = [datetime.now() - timedelta(days=i) for i in range(5)]
temp_data = []

for date in dates:
    timestamp = int(datetime.timestamp(date))
    data = get_historical_weather(lat, lon, timestamp, api_key)
    if data and 'current' in data:
        daily_temp = data['current']['temp']
        temp_data.append(daily_temp)
    else:
        print("Data not available for date:", date.strftime('%Y-%m-%d'))

# Plotting the data
if temp_data:  # Only plot if there is data
    plt.figure(figsize=(10, 5))
    plt.plot([date.strftime('%Y-%m-%d') for date in dates], temp_data, marker='o', linestyle='-', color='b')
    plt.title('Daily Temperatures for the Last 5 Days in New York City')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.gca().invert_xaxis()  # Invert x-axis to show the most recent date on the right
    plt.grid(True)
    plt.show()
else:
    print("No temperature data available for plotting.")
