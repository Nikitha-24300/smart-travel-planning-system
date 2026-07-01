from dataclasses import dataclass, field
from typing import List, Optional
from models.travel_metrics import TravelMetrics


@dataclass
class TripResponse:

    shortest_path: List[str]
    total_distance: float
    alternative_routes: List[List[str]]
    status: str
    message: str

    metrics: Optional[TravelMetrics] = None

    # NEW (Milestone 6)
    explanation: str = ""
    budget: Optional[object] = None