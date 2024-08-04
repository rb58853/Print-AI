# from src.app.chat.chat import Chat

# chat = Chat()

# while True:
#     query = input(">")
#     print(f"<{chat.process_query(query)}")


from src.app.open_weather_map.open_weather import get_weather_data

get_weather_data("London", "uk")
