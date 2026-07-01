"""
==================================================
Smart Travel Planning System
Module : OpenRouteService Maps Service
Author : Nikki

Description:
Uses OpenRouteService to calculate real road
distance and travel duration between cities.
==================================================
"""

import logging
import os

import requests
from dotenv import load_dotenv

from services.external.geocoding_service import GeocodingService

load_dotenv()


class MapsService:

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self.api_key = os.getenv("ORS_API_KEY")

        self.base_url = (
            "https://api.openrouteservice.org/v2/directions/driving-car"
        )

        self.geocoder = GeocodingService()

    def get_distance(self, source: str, destination: str):
        """
        Returns real road distance and estimated
        travel duration using OpenRouteService.
        """

        if not self.api_key:

            self.logger.warning(
                "ORS API key not configured."
            )

            return {
                "distance_km": None,
                "duration_hr": None
            }

        source_coordinates = self.geocoder.get_coordinates(source)
        destination_coordinates = self.geocoder.get_coordinates(destination)

        if source_coordinates is None:

            self.logger.error(
                "Unable to locate source city: %s",
                source
            )

            return {
                "distance_km": None,
                "duration_hr": None
            }

        if destination_coordinates is None:

            self.logger.error(
                "Unable to locate destination city: %s",
                destination
            )

            return {
                "distance_km": None,
                "duration_hr": None
            }

        source_lat, source_lon = source_coordinates
        destination_lat, destination_lon = destination_coordinates

        body = {
            "coordinates": [
                [source_lon, source_lat],
                [destination_lon, destination_lat]
            ]
        }

        headers = {
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        }

        try:

            response = requests.post(
                self.base_url,
                json=body,
                headers=headers,
                timeout=20
            )

            response.raise_for_status()

            data = response.json()

            route = data["routes"][0]["summary"]

            distance = round(
                route["distance"] / 1000,
                2
            )

            duration = round(
                route["duration"] / 3600,
                2
            )

            self.logger.info(
                "ORS Distance: %.2f km | Duration: %.2f hrs",
                distance,
                duration
            )

            return {
                "distance_km": distance,
                "duration_hr": duration
            }

        except Exception as e:

            self.logger.error(
                "OpenRouteService Error: %s",
                str(e)
            )

            return {
                "distance_km": None,
                "duration_hr": None
            }