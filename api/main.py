"""
==================================================
Smart Travel Planning System
API Layer (Milestone 6 Final Stable Version)
Author: Nikki
==================================================
"""

from fastapi import FastAPI
from pydantic import BaseModel

from models.trip_request import TripRequest
from services.application_controller import ApplicationController

app = FastAPI(
    title="Smart Travel Planning System",
    version="2.2.1"
)

controller = ApplicationController()


# =========================
# HEALTH CHECK
# =========================
@app.get("/health")
def health():
    return {
        "status": "OK",
        "system": "Smart Travel Planning System"
    }


# =========================
# SAFE SERIALIZER (FINAL FIX)
# =========================
def safe_serialize(obj):
    """
    Always returns JSON-safe dict or list.
    Never returns string.
    """

    if obj is None:
        return None

    # Pydantic v2
    if hasattr(obj, "model_dump"):
        return obj.model_dump()

    # Pydantic v1
    if hasattr(obj, "dict"):
        return obj.dict()

    # Dataclass / normal object
    if hasattr(obj, "__dict__"):
        return obj.__dict__

    # LAST RESORT: return raw object (NOT string)
    return obj

# =========================
# PLAN TRIP ENDPOINT
# =========================
@app.post("/plan-trip")
def plan_trip(request: TripRequest):

    response = controller.plan_trip(request)

    return {
        "route": response.shortest_path,
        "total_distance": response.total_distance,
        "alternative_routes": response.alternative_routes,
        "status": response.status,
        "message": response.message,

        # SAFE SERIALIZATION (FIXED)
        "metrics": safe_serialize(response.metrics),
        "budget": safe_serialize(response.budget)
    }
@app.get("/history")
def get_history():
    return controller.repo.get_all_trips()