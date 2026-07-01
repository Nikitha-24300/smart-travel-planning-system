"""
==================================================
Smart Travel Planning System
Module : Geocoding Service
Author : Nikki

Description:
Converts city names into latitude and longitude
using the OpenRouteService Geocoding API.
==================================================
"""

import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()


class GeocodingService:

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self.api_key = os.getenv("ORS_API_KEY")

        self.base_url = (
            "https://api.openrouteservice.org/geocode/search"
        )

    def get_coordinates(self, city: str):
        """
        Returns:
            (latitude, longitude)

        Returns None if city not found.
        """

        if not self.api_key:

            self.logger.warning(
                "ORS API key not configured."
            )

            return None

        headers = {
            "Authorization": self.api_key
        }

        params = {
            "text": city,
            "size": 1
        }

        try:

            response = requests.get(
                self.base_url,
                headers=headers,
                params=params,
                timeout=20
            )

            response.raise_for_status()

            data = response.json()

            features = data.get("features", [])

            if not features:

                self.logger.warning(
                    "City not found: %s",
                    city
                )

                return None

            longitude, latitude = (
                features[0]["geometry"]["coordinates"]
            )

            return (
                latitude,
                longitude
            )

        except Exception as e:

            self.logger.error(
                "Geocoding Error: %s",
                str(e)
            )

            return None