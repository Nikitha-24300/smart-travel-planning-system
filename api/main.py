"""
==================================================
Smart Travel Planning System
FastAPI Backend
Version : 3.0
Author  : Nikki
==================================================
"""

from dataclasses import asdict, is_dataclass
from fastapi import FastAPI

from models.trip_request import TripRequest
from services.application_controller import ApplicationController

app = FastAPI(
    title="Smart Travel Planning System",
    version="3.0.0"
)

controller = ApplicationController()


# ==================================================
# HEALTH CHECK
# ==================================================

@app.get("/health")
def health():

    return {
        "status": "OK",
        "system": "Smart Travel Planning System",
        "version": "3.0.0"
    }


# ==================================================
# SAFE SERIALIZER
# ==================================================

def serialize(obj):
    """
    Converts dataclasses into JSON safely.
    """

    if obj is None:
        return None

    if is_dataclass(obj):
        return asdict(obj)

    if isinstance(obj, list):

        result = []

        for item in obj:

            if is_dataclass(item):
                result.append(asdict(item))
            else:
                result.append(item)

        return result

    if isinstance(obj, dict):
        return obj

    return obj


# ==================================================
# PLAN TRIP
# ==================================================

@app.post("/plan-trip")
def plan_trip(request: TripRequest):

    response = controller.plan_trip(request)

    return {

        "source": request.source,

        "destination": request.destination,

        "route": response.shortest_path,

        "distance": response.total_distance,

        "alternative_routes": response.alternative_routes,

        "status": response.status,

        "message": response.message,

        "explanation": response.explanation,

        "metrics": serialize(response.metrics),

        "budget": serialize(response.budget)

    }


# ==================================================
# HISTORY
# ==================================================

@app.get("/history")
def history():

    return controller.get_trip_history()


# ==================================================
# ANALYTICS
# ==================================================

@app.get("/analytics")
def analytics():

    return {

        "total_trips": controller.get_total_trips(),

        "average_distance": controller.get_average_distance(),

        "successful_trips": controller.get_successful_trips(),

        "budget_exceeded": controller.get_budget_exceeded()

    }


# ==================================================
# CLEAR HISTORY
# ==================================================

@app.delete("/history")
def clear_history():

    controller.clear_history()

    return {

        "status": "SUCCESS",

        "message": "Trip history cleared successfully."

    }