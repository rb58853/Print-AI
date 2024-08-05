from src.app.openai_.gpt import GPT
from src.app.open_weather_map.open_weather import WeatherData


class Chat:
    def __init__(self, gpt: GPT = GPT(), weather_data=WeatherData()) -> None:
        self.gpt: GPT = gpt
        self.history = []
        self.max_history_len = 5
        self.weather = weather_data

    async def send_query(self, query):
        return self.process_query(query)

    def process_query(self, query):
        self.history.append({"role": "user", "content": query})
        self.history = self.history[: self.max_history_len * 2]

        location = self.gpt.get_location(self.history)
        country, city = location["country"].lower(), location["location"].lower()

        info = {city: self.weather.get_and_decode_data(city=city, country=country)}

        response = self.gpt.information(self.history, info=info)
        self.history.append({"role": "assistant", "content": response})
        return response
