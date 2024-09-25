from etl_weather_data.etl_weather import extract_weather_data, transform_data, load_data_to_postgresql
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def main():
    api_key = os.getenv('API_KEY')  
    city = 'Mexico City'  

    weather_data = extract_weather_data(api_key, city)

    if weather_data:
        transformed_data = transform_data(weather_data)  

        load_data_to_postgresql(
            transformed_data,
            db_name = os.getenv('DB_NAME'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD')
        )

if __name__ == "__main__":
    main()

