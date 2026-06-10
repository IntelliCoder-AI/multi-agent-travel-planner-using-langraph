import requests

from config import OPENWEATHER_API_KEY


def get_weather(city: str):

    try:

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
        )

        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        data = response.json()

        return {
            "city": city,
            "temperature":
                data["main"]["temp"],
            "condition":
                data["weather"][0]["main"],
            "humidity":
                data["main"]["humidity"]
        }

    except Exception as e:

        return {
            "error": str(e)
        }
    
