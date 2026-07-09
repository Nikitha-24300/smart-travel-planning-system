"""
==================================================
Smart Travel Planning System
Travel Metrics Model
Version : 4.0
Author  : Nikki
==================================================
"""

from dataclasses import dataclass


@dataclass
class TravelMetrics:
    """
    Stores all travel intelligence generated
    for a planned trip.
    """

    # ==================================================
    # Journey Estimates
    # ==================================================

    estimated_time: float = 0.0
    estimated_cost: float = 0.0
    carbon_emission: float = 0.0

    # ==================================================
    # Route Performance
    # ==================================================

    route_score: float = 0.0
    route_efficiency: float = 0.0

    # ==================================================
    # Maps Information
    # ==================================================

    real_distance: float = 0.0
    real_duration: float = 0.0

    # ==================================================
    # Weather
    # ==================================================

    weather: str = "Unknown"
    temperature: float = 0.0
    humidity: float = 0.0
    wind_speed: float = 0.0

    # ==================================================
    # Traffic
    # ==================================================

    traffic_factor: float = 1.0
    traffic_status: str = "Normal"

    # ==================================================
    # Safety
    # ==================================================

    risk_level: str = "Low"

    # ==================================================
    # AI Recommendation
    # ==================================================

    recommendation: str = ""

    # ==================================================
    # Transport
    # ==================================================

    transport_mode: str = "Any"

    # ==================================================
    # Convenience
    # ==================================================

    is_budget_friendly: bool = False
    is_fastest_route: bool = False
    is_eco_friendly: bool = False

    # ==================================================
    # Display
    # ==================================================

    def __str__(self):

        return (
            "TravelMetrics("
            f"distance={self.real_distance}, "
            f"time={self.estimated_time}, "
            f"cost={self.estimated_cost}, "
            f"weather={self.weather}, "
            f"traffic={self.traffic_status}, "
            f"risk={self.risk_level})"
        )