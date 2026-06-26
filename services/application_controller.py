from models.trip_request import TripRequest
from models.trip_response import TripResponse
from services.route_optimizer import RouteOptimizer


class ApplicationController:
    """
    Main entry point for the application's business layer.
    """

    def __init__(self):
        self.optimizer = RouteOptimizer()

    def plan_trip(self, request: TripRequest) -> TripResponse:
        """
        Plans a trip using the Route Optimizer.
        """

        return self.optimizer.optimize(request)

    def health_check(self) -> str:
        return "Application Ready"

    def version(self) -> str:
        return "1.0.0"