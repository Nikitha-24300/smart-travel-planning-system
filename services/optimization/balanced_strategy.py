"""
==================================================
Smart Travel Planning System
Balanced Strategy
==================================================
"""

from .base_strategy import BaseStrategy


class BalancedStrategy(BaseStrategy):

    def calculate_score(
        self,
        distance,
        duration,
        cost
    ):
        return (
            distance * 0.30 +
            duration * 0.40 +
            cost * 0.30
        )

    def get_priority_label(self):
        return "BALANCED"