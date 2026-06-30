from pydantic import BaseModel
from typing import List, Optional


class TripRequestSchema(BaseModel):
    source: str
    destination: str
    preference: str = "fastest"
    transport_mode: str = "any"
    travel_date: Optional[str] = None
    max_budget: Optional[float] = None


class TripResponseSchema(BaseModel):
    route: List[str]
    total_distance: float
    alternative_routes: List[List[str]]
    status: str
    message: str