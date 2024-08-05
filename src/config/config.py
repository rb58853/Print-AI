import os


class ConfigGPT:
    MODEL_PRICE = {
        "gpt-3.5-turbo": {
            "input": 0.5 / 1000000,
            "output": 1.5 / 1000000,
        },
        "gpt-4o-mini": {
            "input": 0.15 / 1000000,
            "output": 0.60 / 1000000,
        },
    }

    DEFAULT_MODEL_NAME = "gpt-4o-mini"

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


class WeatherDataConfig:
    API_KEY = os.environ.get("WEATHERDATA_API_KEY")

    # Estos son los campos basicos que se usaran identico a como estan en la data
    BASIC_USABLE_FIELDS = ["weather", "clouds", "wind", "visibility"]

    # Estos campos seran separados y cada uno de los valores de este diccionario se usara como un key:value y no como diccionario completo.
    DIC_USABLE_FIELDS = ["main"]

    # Estos son los campos que se eliminaran de la informacion para cada campo
    DELETE_FIELDS = {"weather": ["id", "icon"]}

    # Estos son los campos que no son un diccionario sino que son una lista de un elemento, entonces al estar en especial se usara field[0]
    SPECIAL_FIELDS = ["weather"]
