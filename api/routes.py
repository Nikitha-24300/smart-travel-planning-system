"""
==================================================
Smart Travel Planning System
API Routes Layer
Author: Nikki
==================================================
"""

from fastapi import APIRouter

from services.application_controller import ApplicationController
from api.schemas import TripRequestSchema, TripResponseSchema

# NEW IMPORT (DATABASE)
from database.repository import TripRepository

router = APIRouter()

controller = ApplicationController()
repo = TripRepository()


# -----------------------------
# PLAN TRIP ENDPOINT
# -----------------------------
@router.post("/plan-trip", response_model=TripResponseSchema)
def plan_trip(request: TripRequestSchema):

    response = controller.plan_trip(request)

    return TripResponseSchema(
        route=response.shortest_path,
        total_distance=response.total_distance,
        alternative_routes=response.alternative_routes,
        status=response.status,
        message=response.message
    )


# -----------------------------
# HEALTH CHECK
# -----------------------------
@router.get("/health")
def health():

    return {
        "status": "OK",
        "service": "Smart Travel Planning System"
    }


# -----------------------------
# VERSION
# -----------------------------
@router.get("/version")
def version():

    return {
        "version": controller.version()
    }


# -----------------------------
# 🚀 STEP 8: TRIP HISTORY API (NEW)
# -----------------------------
@router.get("/history")
def get_history():

    trips = repo.get_all_trips()

    return [
        {
            "id": t.id,
            "source": t.source,
            "destination": t.destination,
            "route": t.route,
            "distance": t.total_distance,
            "preference": t.preference,
            "status": t.status
        }
        for t in trips
    ]