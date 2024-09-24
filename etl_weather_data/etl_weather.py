import requests
import json
import pandas as pd
from datetime import datetime
import psycopg2 

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
    'description': [weather_desc],
    'datetime': [datetime.now()]  # Record the timestamp
    }

    df = pd.DataFrame(data)
    return df

# Load Data
def load_data_to_postgresql(df, db_name, user, password, host='localhost', port='5432'):
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            city VARCHAR(50),
            temperature FLOAT,
            humidity INT,
            description VARCHAR(100),
            timestamp TIMESTAMP
        );
        ''')
        
        # Insert the weather data into the table
        for index, row in df.iterrows():
            insert_query = '''
            INSERT INTO weather (city, temperature, humidity, description, timestamp)
            VALUES (%s, %s, %s, %s, %s);
            '''
            cursor.execute(insert_query, (row['city'], row['temperature'], row['humidity'], row['description'], row['datetime']))

        # Commit the transaction
        conn.commit()
        
        print("Data loaded into PostgreSQL successfully!")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()


