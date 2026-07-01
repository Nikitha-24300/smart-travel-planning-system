"""
==================================================
Smart Travel Planning System
Module : Trip Request Model
Author : Nikki
==================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class TripRequest:
    """
    Represents a user's trip planning request.
    """

    # Journey
    source: str
    destination: str

    # Optimization preference
    preference: str = "fastest"

    # Transport preference
    transport_mode: str = "any"

    # Optional travel date
    travel_date: str | None = None

    # NEW (Milestone 6)
    # Maximum budget specified by the user
    max_budget: float | None = None

    def __str__(self):

        return (
            f"TripRequest("
            f"source='{self.source}', "
            f"destination='{self.destination}', "
            f"preference='{self.preference}', "
            f"transport='{self.transport_mode}', "
            f"budget={self.max_budget})"
        )