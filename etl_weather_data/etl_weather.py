import requests
import json
import pandas as pd
from datetime import datetime

# Extract Weather Data
def extract_weather_data(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}")
        return None

# Transform Data
def transform_data(weather_data):

    # Extract specific fields from the JSON response
    city_name = weather_data['name']
    temperature = weather_data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
    humidity = weather_data['main']['humidity']
    weather_desc = weather_data['weather'][0]['description']

    data = {
    'city': [city_name],
    'temperature': [temperature],
    'humidity': [humidity],
    'weather_description': [weather_desc],
    'datetime': [datetime.now()]  # Record the timestamp
    }

    df = pd.DataFrame(data)
    return df


