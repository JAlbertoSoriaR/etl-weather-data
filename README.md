# ETL Weather Data Pipeline

## Project Overview
This project implements an ETL (Extract, Transform, Load) pipeline to collect weather data from the OpenWeather API and load it into a PostgreSQL database for further analysis and visualization.

## Features
- Data extraction from OpenWeather API
- Data transformation (e.g., temperature conversion, timestamping)
- Data loading into PostgreSQL for persistence
- Automation of the ETL process using cron jobs

## Setup Instructions

### Prerequisites
- Python 3.12+
- PostgreSQL
- Poetry for package management

### Installation

1. Clone the repository:
   git clone https://github.com/yourusername/etl-weather-data.git
   cd etl-weather-data

2. Install dependencies using Poetry:
   poetry install

### Setup

Set up the .env file with your API key and database credentials:
   touch .env

Add the following to .env:
   API_KEY=your_api_key
   DB_NAME=weather_data
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   PROJECT_DIR=/path/to/your/project
   POETRY_PATH=/path/to/poetry

### Usage

To run the ETL script, use:
   poetry run python etl_weather_data/etl_script.py

### Automation 

To automate the ETL process, set up a cron job that runs the script at your desired interval. For example:
   0 0 * * * /path/to/run_etl.sh >> /path/to/etl.log 2>&1

### Future Improvements

- Add error handling for API requests.
- Implement data visualization.
- Improve database performance with indexing.
