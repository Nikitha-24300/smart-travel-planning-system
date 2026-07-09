"""
==================================================
Smart Travel Planning System
Cheapest Strategy
==================================================
"""

from .base_strategy import BaseStrategy


class CheapestStrategy(BaseStrategy):

    def calculate_score(
        self,
        distance,
        duration,
        cost
    ):
        return cost

    def get_priority_label(self):
        return "CHEAPEST"