"""
==================================================
Smart Travel Planning System
Module : Metrics Service
Author : Nikki

Description:
Calculates travel-related metrics such as
estimated travel time, estimated cost,
carbon emission and route score.

Future Enhancements:
- Dynamic pricing
- Live fuel prices
- Weather impact
- Traffic analysis
==================================================
"""

import logging


class MetricsService:
    """
    Calculates various travel metrics.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        # Average Speeds (km/hr)
        self.average_speed = {
            "bus": 55,
            "train": 80,
            "flight": 600,
            "any": 65
        }

        # Cost Per KM (₹)
        self.cost_per_km = {
            "bus": 2.2,
            "train": 1.4,
            "flight": 8.5,
            "any": 2.5
        }

        # CO₂ Emission (kg/km)
        self.co2_per_km = {
            "bus": 0.09,
            "train": 0.04,
            "flight": 0.25,
            "any": 0.08
        }

    def calculate_metrics(
        self,
        distance: float,
        transport_mode: str
    ) -> dict:
        """
        Returns all travel metrics.
        """

        self.logger.info(
            "Calculating travel metrics."
        )

        speed = self.average_speed.get(
            transport_mode,
            self.average_speed["any"]
        )

        cost_rate = self.cost_per_km.get(
            transport_mode,
            self.cost_per_km["any"]
        )

        emission_rate = self.co2_per_km.get(
            transport_mode,
            self.co2_per_km["any"]
        )

        estimated_time = round(
            distance / speed,
            2
        )

        estimated_cost = round(
            distance * cost_rate,
            2
        )

        carbon_emission = round(
            distance * emission_rate,
            2
        )

        route_score = self.calculate_route_score(
            distance,
            estimated_time,
            estimated_cost
        )

        self.logger.info(
            "Travel metrics calculated successfully."
        )

        return {
            "estimated_time": estimated_time,
            "estimated_cost": estimated_cost,
            "carbon_emission": carbon_emission,
            "route_score": route_score
        }

    def calculate_route_score(
        self,
        distance: float,
        time: float,
        cost: float
    ) -> float:
        """
        Calculates a simple route score.

        Higher score means a better route.
        """

        score = 100

        score -= distance * 0.02
        score -= time * 0.8
        score -= cost * 0.01

        return round(
            max(score, 0),
            2
        )