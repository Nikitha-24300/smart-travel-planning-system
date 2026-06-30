from fastapi import FastAPI

from models.trip_request import TripRequest
from services.application_controller import ApplicationController

app = FastAPI(
    title="Smart Travel Planning System",
    version="2.0.0"
)

controller = ApplicationController()


# -------------------------
# HEALTH CHECK
# -------------------------
@app.get("/health")
def health():

    return {
        "status": "OK",
        "system": "Smart Travel Planning System"
    }


# -------------------------
# PLAN TRIP API
# -------------------------
@app.post("/plan-trip")
def plan_trip(request: TripRequest):

    response = controller.plan_trip(request)

    return {
        "route": response.shortest_path,
        "total_distance": response.total_distance,
        "alternative_routes": response.alternative_routes,
        "status": response.status,
        "message": response.message
    }