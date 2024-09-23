from etl_weather_data.etl_weather import extract_weather_data, transform_data

def main():
    api_key = 'e8697333cd273b1093da4a10421f4c56'  
    city = 'Mexico City'  

    weather_data = extract_weather_data(api_key, city)

    if weather_data:
        transformed_data = transform_data(weather_data)  

        print(transformed_data)

if __name__ == "__main__":
    main()

