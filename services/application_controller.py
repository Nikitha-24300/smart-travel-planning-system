"""
==================================================
Smart Travel Planning System
Module: Application Controller
Author: Nikki

Description:
Acts as the entry point to the application's
business layer and handles DB + external APIs.
==================================================
"""

import logging

from models.trip_request import TripRequest
from models.trip_response import TripResponse

from services.route_optimizer import RouteOptimizer
from validation.trip_validator import TripValidator

# DATABASE
from database.repository import TripRepository

# EXTERNAL SERVICES (Milestone 5)
from services.external.weather_service import WeatherService
from services.external.maps_service import MapsService
from services.external.traffic_service import TrafficService


class ApplicationController:
    """
    Main entry point for business logic layer.
    """

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        # Core system
        self.optimizer = RouteOptimizer()
        self.validator = TripValidator()

        # Database layer
        self.repo = TripRepository()

        # External APIs (Milestone 5)
        self.weather = WeatherService()
        self.maps = MapsService()
        self.traffic = TrafficService()

    def plan_trip(self, request: TripRequest) -> TripResponse:

        self.logger.info(
            "Trip request received: %s -> %s",
            request.source,
            request.destination,
        )

        # STEP 1: Validate input
        self.validator.validate(request)

        # STEP 2: Compute best route
        response = self.optimizer.optimize(request)

        # STEP 3: External API enrichment (NEW)
        weather_info = self.weather.get_weather(request.source)
        distance_info = self.maps.get_distance(
            request.source,
            request.destination
        )
        traffic_factor = self.traffic.get_traffic_factor(
            request.source
        )

        # STEP 4: Attach extra intelligence (optional but powerful)
        response.weather = weather_info
        response.distance_api = distance_info
        response.traffic_factor = traffic_factor

        # STEP 5: Save to database
        try:
            self.repo.save_trip({
                "source": request.source,
                "destination": request.destination,
                "route": response.shortest_path,
                "total_distance": response.total_distance,
                "preference": request.preference,
                "status": response.status
            })

            self.logger.info("Trip saved to database successfully.")

        except Exception as e:
            self.logger.error("Database save failed: %s", str(e))

        self.logger.info("Trip planned successfully.")

        return response

    def health_check(self) -> str:
        return "Application Ready"

    def version(self) -> str:
        return "2.0.0"