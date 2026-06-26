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

    This model is passed from the Service Layer
    back to the Presentation Layer.
    """

    # Best route returned by Dijkstra
    shortest_path: List[str]

    # Total distance (km)
    total_distance: float

    # Alternative routes returned by DFS
    alternative_routes: List[List[str]] = field(default_factory=list)

    # Travel statistics
    metrics: TravelMetrics | None = None

    # Response information
    status: str = "SUCCESS"
    message: str = ""

    def has_alternatives(self) -> bool:
        """
        Returns True if alternative routes exist.
        """

        return len(self.alternative_routes) > 0

    def number_of_routes(self) -> int:
        """
        Returns total number of routes including
        the shortest route.
        """

        return 1 + len(self.alternative_routes)

    def __str__(self) -> str:

        return (
            f"TripResponse("
            f"path={self.shortest_path}, "
            f"distance={self.total_distance}, "
            f"metrics={self.metrics})"
        )