from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class TripRequest:
    """
    Represents a user's travel planning request.

    This object is passed from the Presentation Layer (UI)
    to the Application Layer (Application Controller).
    """

    source: str
    destination: str
    preference: str = "fastest"
    transport_mode: str = "any"
    travel_date: Optional[str] = None
    max_budget: Optional[float] = None