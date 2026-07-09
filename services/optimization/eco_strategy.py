"""
==================================================
Smart Travel Planning System
Eco Strategy
==================================================
"""

from .base_strategy import BaseStrategy


class EcoStrategy(BaseStrategy):

    def calculate_score(
        self,
        distance,
        duration,
        cost
    ):
        carbon_emission = distance * 0.12

        return (
            distance * 0.60 +
            carbon_emission * 0.40
        )

    def get_priority_label(self):
        return "ECO"