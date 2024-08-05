import requests
from src.config.config import WeatherDataConfig
import logging


class WeatherData:
    def __init__(self, api_key=WeatherDataConfig.API_KEY) -> None:
        self.api_key = api_key

    def get_weather_data(self, city, country):
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={self.api_key}"
        )

        if response.status_code == 200:
            weather_data = response.json()

            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/forecast?lat={weather_data['coord']['lat']}&lon={weather_data['coord']['lon']}&appid={self.api_key}"
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

    def decode_data(self, data):
        if data["forecast"]:
            info = {}
            for item in data["forecast"]["list"]:
                date = item["dt_txt"].split(" ")
                if date[0] not in info:
                    info[date[0]] = {}
                current = {}

                for key, value in zip(item.keys(), item.values()):
                    if key in WeatherDataConfig.DELETE_FIELDS:
                        if key in WeatherDataConfig.SPECIAL_FIELDS:
                            value = value[0]
                        fields_to_delete = WeatherDataConfig.DELETE_FIELDS[key]
                        for field in fields_to_delete:
                            value.pop(field, None)

                current = {
                    key: value
                    for key, value in zip(item.keys(), item.values())
                    if key in WeatherDataConfig.BASIC_USABLE_FIELDS
                }

                for field in WeatherDataConfig.SPECIAL_FIELDS:
                    if field in current:
                        current[field] = current[field][0]

                for field in WeatherDataConfig.DIC_USABLE_FIELDS:
                    field = item[field]
                    for key, value in zip(field.keys(), field.values()):
                        current[key] = value

                info[date[0]][date[1]] = current
            return info
        else:
            return {
                "info": "No hay informacion sobre esta localidad, no puedes dar ningun dato, debes decir que no tienes datos"
            }

    def get_and_decode_data(self, city, country):
        data = self.get_weather_data(city, country)
        return self.decode_data(data)
