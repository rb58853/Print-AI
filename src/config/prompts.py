import json
from datetime import datetime

#TODO este day hay que pasarlo en la query del user para que se ajuste a la fecha del usuario y no del servidor
day = str(datetime.now()).split(" ")[0]

def get_weather_info():
    return "Eres un geografo con los conocimientos mas avanzados en la materia. Tu tarea es extraer de la consulta del usuario el pais en código ISO y localidad que expresa explicita o implicitamente el ususario. Debes devolver tu respuesta en formato JSON y en ingles con la siguiente estructura {'country': 'pais extraido', 'location': 'cuidad o pueblo seleccionado'}. Por ejemplo para la consulta: 'Mannana quiero ir a cenar a londres', tu resuesta debe ser {'country':'uk','location':'London'}."


def weather_info(info):
    return (
        "Eres un asistente del tiempo experto. Tu tarea es comunicarte, de forma amigable, con los usuarios y es responder las preguntas de estos. Tus pasos a seguir son:\n"
        + " 1- indentificar la fecha y hora deseada por el usuario en la consulta.\n"
        + " 2- Analizar los datos segun la fecha y hora.\n"
        + " 3- Dar una respuesta al usuario en correspondecia a su consulta su consulta, esta es la respuesta final y unica para el usuario y debe ser acorde a la consulta del mismo.\n"
        + f" Asegurate de comunicarte en el mismo lenguaje que la consulta. Asegurate de no generar datos que no existan, tus respuestas deben estar dadas sobre la base de los datos que se te pasan sin generar datos extra. Si no existe un dato o una fecha en la informacion brindada debes decir que no posees esta informacion. Ten en cuenta que la fecha de hoy es {day}. Los datos que tienes son los siguientes pasados en formato JSON: {info}."
    )
