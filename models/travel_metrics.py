"""
==================================================
Smart Travel Planning System
Module : Travel Metrics Model
Author : Nikki
==================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class TravelMetrics:
    """
    Stores all calculated travel metrics.

    This model is returned by MetricsService and later
    becomes part of TripResponse.
    """

    estimated_time: float
    estimated_cost: float
    carbon_emission: float
    route_score: float

    def __str__(self) -> str:
        return (
            f"TravelMetrics("
            f"time={self.estimated_time} hrs, "
            f"cost=₹{self.estimated_cost}, "
            f"co2={self.carbon_emission} kg, "
            f"score={self.route_score})"
        )