"""
==================================================
Smart Travel Planning System
Module : Trip Response Model
Author : Nikki
==================================================
"""

from dataclasses import dataclass, field
from typing import List

from models.travel_metrics import TravelMetrics


@dataclass(slots=True)
class TripResponse:
    """
    Represents the complete response returned after
    planning a trip.
    """

    # Best route
    shortest_path: List[str]

    # Total distance (Graph distance)
    total_distance: float

    # Alternative routes
    alternative_routes: List[List[str]] = field(default_factory=list)

    # Calculated travel metrics
    metrics: TravelMetrics | None = None

    # -------- Milestone 5 --------

    # Weather information returned by Weather API
    weather: dict | None = None

    # Google Maps information
    distance_api: dict | None = None

    # Traffic multiplier
    traffic_factor: float = 1.0

    # -----------------------------

    status: str = "SUCCESS"
    message: str = ""

    def has_alternatives(self) -> bool:
        return len(self.alternative_routes) > 0

    def number_of_routes(self) -> int:
        return 1 + len(self.alternative_routes)

    def __str__(self) -> str:

        return (
            f"TripResponse("
            f"path={self.shortest_path}, "
            f"distance={self.total_distance}, "
            f"weather={self.weather}, "
            f"traffic={self.traffic_factor})"
        )