"""
==================================================
Smart Travel Planning System
Module: Application Controller
Author: Nikki
Description:
Acts as the entry point to the application's
business layer.
==================================================
"""

import logging

from models.trip_request import TripRequest
from models.trip_response import TripResponse
from services.route_optimizer import RouteOptimizer
from validation.trip_validator import TripValidator


class ApplicationController:
    """
    Main entry point for the application's business layer.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.optimizer = RouteOptimizer()
        self.validator = TripValidator()

    def plan_trip(self, request: TripRequest) -> TripResponse:
        """
        Validates the request and plans the trip.
        """

        self.logger.info(
            "Trip request received: %s -> %s",
            request.source,
            request.destination,
        )

        self.validator.validate(request)

        response = self.optimizer.optimize(request)

        self.logger.info("Trip planned successfully.")

        return response

    def health_check(self) -> str:
        """
        Checks whether the application is ready.
        """
        return "Application Ready"

    def version(self) -> str:
        """
        Returns application version.
        """
        return "1.0.0"