"""
==================================================
Smart Travel Planning System
Travel Intelligence Service
Version : 3.1
Author  : Nikki
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

    # -------------------------------------------------
    # Transport Cost (₹ / km)
    # -------------------------------------------------

    TRANSPORT_COST = {
        "bus": 5,
        "train": 3,
        "flight": 12,
        "any": 8
    }

    # -------------------------------------------------
    # Carbon Emission (kg / km)
    # -------------------------------------------------

    CARBON_FACTOR = {
        "bus": 0.08,
        "train": 0.05,
        "flight": 0.25,
        "any": 0.12
    }

    # =====================================================
    # MAIN
    # =====================================================

    def generate_metrics(self, request):

        metrics = TravelMetrics()

        metrics.transport_mode = getattr(
            request,
            "transport_mode",
            "any"
        ).lower()

        # =====================================================
        # WEATHER
        # =====================================================

        try:

            weather = self.weather_service.get_weather(
                request.source
            )

            if weather:

                metrics.weather = weather.get("weather", "Unknown")
                metrics.temperature = weather.get("temperature", 0.0)
                metrics.humidity = weather.get("humidity", 0)
                metrics.wind_speed = weather.get("wind_speed", 0.0)

        except Exception as e:

            self.logger.warning("Weather API : %s", e)

        # =====================================================
        # MAPS
        # =====================================================

        try:

            maps = self.maps_service.get_distance(
                request.source,
                request.destination
            )

            if maps:

                metrics.real_distance = maps.get(
                    "distance_km",
                    0.0
                )

                metrics.real_duration = maps.get(
                    "duration_hr",
                    0.0
                )

        except Exception as e:

            self.logger.warning("Maps API : %s", e)

        # =====================================================
        # TRAFFIC
        # =====================================================

        try:

            metrics.traffic_factor = self.traffic_service.get_traffic_factor(
                request.source
            )

        except Exception:

            metrics.traffic_factor = 1.0

        factor = metrics.traffic_factor

        if factor <= 1:
            metrics.traffic_status = "Light"

        elif factor <= 1.3:
            metrics.traffic_status = "Moderate"

        elif factor <= 1.6:
            metrics.traffic_status = "Heavy"

        else:
            metrics.traffic_status = "Severe"

        # =====================================================
        # CALCULATIONS
        # =====================================================

        distance = metrics.real_distance

        if distance > 0:

            cost_factor = self.TRANSPORT_COST.get(
                metrics.transport_mode,
                8
            )

            carbon_factor = self.CARBON_FACTOR.get(
                metrics.transport_mode,
                0.12
            )

            metrics.estimated_cost = round(
                distance * cost_factor,
                2
            )

            metrics.carbon_emission = round(
                distance * carbon_factor,
                2
            )

            metrics.route_score = round(
                max(
                    0,
                    100 - (distance / 25)
                ),
                2
            )

            metrics.route_efficiency = round(
                max(
                    0,
                    100 - ((factor - 1) * 35)
                ),
                2
            )

        if metrics.real_duration > 0:

            metrics.estimated_time = round(
                metrics.real_duration * factor,
                2
            )

        # =====================================================
        # RISK LEVEL
        # =====================================================

        weather = metrics.weather.lower()

        if metrics.traffic_status == "Severe":

            metrics.risk_level = "High"

        elif weather in [
            "storm",
            "thunderstorm",
            "heavy rain"
        ]:

            metrics.risk_level = "High"

        elif weather in [
            "rain",
            "drizzle",
            "fog"
        ]:

            metrics.risk_level = "Medium"

        else:

            metrics.risk_level = "Low"

        # =====================================================
        # AI Recommendation
        # =====================================================

        tips = []

        if metrics.route_score >= 90:
            tips.append("Excellent route selected.")

        elif metrics.route_score >= 70:
            tips.append("Good route selected.")

        else:
            tips.append("Consider an alternative route.")

        if metrics.traffic_status == "Heavy":
            tips.append("Expect delays due to traffic.")

        elif metrics.traffic_status == "Severe":
            tips.append("Avoid peak hours if possible.")

        if weather in [
            "rain",
            "storm",
            "heavy rain"
        ]:
            tips.append("Carry rain protection.")

        if metrics.transport_mode == "flight":
            tips.append("Arrive at the airport 2 hours early.")

        elif metrics.transport_mode == "train":
            tips.append("Check platform information before departure.")

        elif metrics.transport_mode == "bus":
            tips.append("Reach the boarding point 15 minutes early.")

        metrics.recommendation = " ".join(tips)

        self.logger.info(
            "Travel intelligence generated successfully."
        )

        return metrics