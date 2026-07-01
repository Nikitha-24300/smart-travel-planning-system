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
    Stores all travel intelligence generated for a trip.
    """

    # Existing metrics
    estimated_time: float = 0.0
    estimated_cost: float = 0.0
    carbon_emission: float = 0.0
    route_score: float = 0.0

    # Live Maps API
    real_distance: float = 0.0
    real_duration: float = 0.0

    # Weather API
    weather: str = "Unknown"
    temperature: float = 0.0

    # Traffic
    traffic_factor: float = 1.0
    traffic_status: str = "Normal"

    def __str__(self):

        return (
            f"TravelMetrics("
            f"time={self.estimated_time}, "
            f"cost={self.estimated_cost}, "
            f"co2={self.carbon_emission}, "
            f"score={self.route_score}, "
            f"real_distance={self.real_distance}, "
            f"real_duration={self.real_duration}, "
            f"weather={self.weather}, "
            f"temperature={self.temperature}, "
            f"traffic={self.traffic_status})"
        )