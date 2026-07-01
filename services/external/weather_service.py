"""
==================================================
Smart Travel Planning System
Module : Weather Service
Author : Nikki

Description:
Fetches live weather information from the
OpenWeatherMap API.
==================================================
"""

import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()


class WeatherService:

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self.api_key = os.getenv("WEATHER_API_KEY")

        self.base_url = (
            "https://api.openweathermap.org/data/2.5/weather"
        )

    def get_weather(self, city: str):

        if not self.api_key:

            self.logger.warning(
                "Weather API key not found."
            )

            return None

        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:

            response = requests.get(
                self.base_url,
                params=params,
                timeout=15
            )

            response.raise_for_status()

            data = response.json()

            # ---------- DEBUG ----------
            self.logger.info(
                "Weather API Response: %s",
                data
            )
            # ---------------------------

            description = (
                data.get("weather", [{}])[0]
                .get("description", "Unknown")
                .title()
            )

            temperature = (
                data.get("main", {})
                .get("temp", 0.0)
            )

            humidity = (
                data.get("main", {})
                .get("humidity", 0)
            )

            self.logger.info(
                "Weather: %s | Temp: %.1f°C",
                description,
                temperature
            )

            return {
                "city": city,
                "weather": description,
                "temperature": temperature,
                "humidity": humidity
            }

        except Exception as e:

            self.logger.error(
                "Weather API Error: %s",
                str(e)
            )

            return None