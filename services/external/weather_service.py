import requests
import os


class WeatherService:

    def __init__(self):

        self.api_key = os.getenv("WEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str):

        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }