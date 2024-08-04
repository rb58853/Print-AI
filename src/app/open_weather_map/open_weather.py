import requests
from src.config.config import WeatherDataConfig
import logging

api_key = WeatherDataConfig.API_KEY


def get_weather_data(city, country):
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={api_key}"
    )

    if response.status_code == 200:
        weather_data = response.json()

        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?lat={weather_data['coord']['lat']}&lon={weather_data['coord']['lon']}&appid={api_key}"
        )
        if response.status_code == 200:
            forecast_data = response.json()
            return {"weather": weather_data, "forecast": forecast_data}
        else:
            logging.warning("forecast data unfound")
            return {"weather": weather_data, "forecast": None}
    else:
        logging.warning("full data unfound")
        return {"weather": None, "forecast": None}


def decode_data(data):
    return data
