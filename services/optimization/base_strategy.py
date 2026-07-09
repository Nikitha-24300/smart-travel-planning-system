"""
==================================================
Smart Travel Planning System
Module : Base Optimization Strategy
Version : 3.0
Author  : Nikki
==================================================
"""


class BaseStrategy:
    """
    Base class for all optimization strategies.
    """

    def calculate_score(
        self,
        distance,
        duration,
        cost
    ):
        raise NotImplementedError(
            "Strategy must implement calculate_score()"
        )

    def get_priority_label(self):
        return "BASE"