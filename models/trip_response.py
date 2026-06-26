from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class TripResponse:
    """
    Represents the result returned after planning a trip.
    """

    shortest_path: List[str]
    total_distance: float
    alternative_routes: List[List[str]] = field(default_factory=list)
    estimated_cost: float = 0.0
    estimated_time: float = 0.0
    status: str = "SUCCESS"
    message: str = ""