"""
==================================================
Smart Travel Planning System
Fastest Strategy
==================================================
"""

from .base_strategy import BaseStrategy


class FastestStrategy(BaseStrategy):

    def calculate_score(
        self,
        distance,
        duration,
        cost
    ):
        return duration

    def get_priority_label(self):
        return "FASTEST"