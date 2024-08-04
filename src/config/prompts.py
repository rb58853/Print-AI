import json


def get_weather_info():
    return ""


def weather_info(info):
    return f"Eres un asistente del tiempo experto. Tu tarea es comunicarte con los usuarios y es responder las preguntas de estos segun la siguiente informacion que se te pasa en formato JSON: {json.dumps(info)}. \nAsegurate de comunicarte en el mismo lenguaje que la consulta. No puedes generar datos que no existan, da tus respuestas sobre la base de los datos que se te pasan."
