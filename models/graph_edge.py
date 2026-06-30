"""
==================================================
Smart Travel Planning System
Module : Graph Edge Model
Author : Nikki

Description:
Represents a single connection (edge) between
two cities in the travel graph.
==================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class GraphEdge:
    """
    Represents one edge in the travel graph.
    """

    destination: str
    distance: float
    duration: float
    cost: float
    carbon_emission: float
    transport_mode: str
    available: bool = True
    average_delay: int = 0

    def __str__(self) -> str:
        return (
            f"GraphEdge("
            f"destination={self.destination}, "
            f"mode={self.transport_mode}, "
            f"distance={self.distance} km, "
            f"duration={self.duration} hrs, "
            f"cost=₹{self.cost})"
        )