"""
==================================================
Smart Travel Planning System
Module : Travel Intelligence Service
Author : Nikki

Description:
Collects data from all external services and
builds a unified TravelMetrics object.
==================================================
"""

import logging

from models.travel_metrics import TravelMetrics

from services.external.weather_service import WeatherService
from services.external.maps_service import MapsService
from services.external.traffic_service import TrafficService


class TravelIntelligenceService:

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self.weather_service = WeatherService()
        self.maps_service = MapsService()
        self.traffic_service = TrafficService()

    def generate_metrics(self, request):

        metrics = TravelMetrics()

        # -----------------------------------
        # Weather
        # -----------------------------------

        weather = self.weather_service.get_weather(
            request.source
        )

        if weather:

            metrics.weather = weather.get(
                 "weather",
                "Unknown"
            )

            metrics.temperature = weather.get(
                "temperature",
                0.0
            )

        # -----------------------------------
        # Maps
        # -----------------------------------

        maps = self.maps_service.get_distance(
            request.source,
            request.destination
        )

        if maps:

            metrics.real_distance = maps.get(
                "distance_km",
                0.0
            ) or 0.0

            metrics.real_duration = maps.get(
                "duration_hr",
                0.0
            ) or 0.0

        # -----------------------------------
        # Traffic
        # -----------------------------------

        traffic = self.traffic_service.get_traffic_factor(
            request.source
        )

        metrics.traffic_factor = traffic

        if traffic <= 1.0:

            metrics.traffic_status = "Light"

        elif traffic <= 1.3:

            metrics.traffic_status = "Moderate"

        elif traffic <= 1.6:

            metrics.traffic_status = "Heavy"

        else:

            metrics.traffic_status = "Severe"

        # -----------------------------------
        # Derived Metrics
        # -----------------------------------

        if metrics.real_distance:

            metrics.estimated_cost = round(
                metrics.real_distance * 8,
                2
            )

            metrics.carbon_emission = round(
                metrics.real_distance * 0.12,
                2
            )

            metrics.route_score = round(
                max(
                    0,
                    100 - (metrics.real_distance / 25)
                ),
                2
            )

            if metrics.real_duration > 0:

                metrics.estimated_time = round(
                    metrics.real_duration *
                    metrics.traffic_factor,
                    2
                )

        self.logger.info(
            "Travel intelligence generated successfully."
        )

        return metrics