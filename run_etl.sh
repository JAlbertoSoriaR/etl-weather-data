#!/bin/bash

# Load environment variables from .env file
source /home/outis/Repositorios/etl-weather-data/.env

# Check if PROJECT_DIR is set
if [ -z "$PROJECT_DIR" ]; then
  echo "Error: PROJECT_DIR is not set in the .env file."
  exit 1
fi

# Navigate to the project directory
cd "$PROJECT_DIR" || { echo "Error: Could not change to directory $PROJECT_DIR"; exit 1; }

# Activate Poetry environment and run the script
if [ -z "$POETRY_PATH" ]; then
  echo "Error: POETRY_PATH is not set."
  exit 1
fi

"$POETRY_PATH" run python etl_weather_data/etl_script.py

