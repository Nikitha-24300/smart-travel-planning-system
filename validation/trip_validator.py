"""
==================================================
Smart Travel Planning System
Module: Trip Validator
Author: Nikki
Description:
Validates all trip requests before they are
processed by the Route Optimizer.
==================================================
"""

import logging

from algorithms.graph_builder import GraphBuilder
from exceptions.custom_exceptions import (
    EmptyFieldError,
    SameCityError,
    CityNotFoundError,
)
from models.trip_request import TripRequest


class TripValidator:
    """
    Responsible for validating trip requests.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        builder = GraphBuilder()
        self.graph = builder.build_graph()

    def validate(self, request: TripRequest) -> None:
        """
        Validates a TripRequest.

        Raises:
            ValidationError subclasses if validation fails.
        """

        self.logger.info("Validating trip request...")

        self._validate_required_fields(request)
        self._validate_same_city(request)
        self._validate_city_exists(request)

        self.logger.info("Validation completed successfully.")

    def _validate_required_fields(self, request: TripRequest) -> None:
        """
        Checks whether source and destination are provided.
        """

        if not request.source.strip():
            raise EmptyFieldError("Source city cannot be empty.")

        if not request.destination.strip():
            raise EmptyFieldError("Destination city cannot be empty.")

    def _validate_same_city(self, request: TripRequest) -> None:
        """
        Prevents users from selecting the same city.
        """

        if request.source.lower() == request.destination.lower():
            raise SameCityError(
                "Source and destination cannot be the same."
            )

    def _validate_city_exists(self, request: TripRequest) -> None:
        """
        Ensures both cities exist in the graph.
        """

        if request.source not in self.graph:
            raise CityNotFoundError(
                f"'{request.source}' does not exist."
            )

        if request.destination not in self.graph:
            raise CityNotFoundError(
                f"'{request.destination}' does not exist."
            )