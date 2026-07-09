"""
==================================================
Smart Travel Planning System
Application Controller
Version : 3.0
Author  : Nikki
==================================================
"""

import logging

from database.repository import TripRepository

from models.trip_request import TripRequest
from models.trip_response import TripResponse

from services.route_optimizer import RouteOptimizer
from services.travel_intelligence_service import TravelIntelligenceService
from services.budget_planner import BudgetPlanner

from validation.trip_validator import TripValidator


class ApplicationController:
    """
    Main controller of the Smart Travel Planning System.

    Workflow

    1. Validate Request
    2. Route Optimization
    3. Travel Intelligence
    4. Budget Analysis
    5. Save Trip
    6. Return Response
    """

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self.validator = TripValidator()
        self.route_optimizer = RouteOptimizer()
        self.intelligence = TravelIntelligenceService()
        self.budget_planner = BudgetPlanner()

        self.repo = TripRepository()

    # =====================================================
    # PLAN TRIP
    # =====================================================

    def plan_trip(self, request: TripRequest) -> TripResponse:

        self.logger.info(
            "Trip Request : %s -> %s",
            request.source,
            request.destination
        )

        # ---------------------------------------------
        # Step 1 : Validation
        # ---------------------------------------------

        self.validator.validate(request)

        # ---------------------------------------------
        # Step 2 : Route Optimization
        # ---------------------------------------------

        response = self.route_optimizer.optimize(request)

        # ---------------------------------------------
        # Step 3 : Travel Intelligence
        # ---------------------------------------------

        metrics = self.intelligence.generate_metrics(request)

        response.metrics = metrics

        # ---------------------------------------------
        # Step 4 : Budget Planning
        # ---------------------------------------------

        budget = self.budget_planner.analyze(

            max_budget=request.max_budget,

            estimated_cost=metrics.estimated_cost,

            transport_mode=request.transport_mode

        )

        response.budget = budget

        # ---------------------------------------------
        # Step 5 : AI Explanation
        # ---------------------------------------------

        response.explanation = self._generate_explanation(
            response
        )

        # ---------------------------------------------
        # Step 6 : Save Trip
        # ---------------------------------------------

        try:

            self.repo.save_trip({

                "source": request.source,

                "destination": request.destination,

                "route": response.shortest_path,

                "total_distance": response.total_distance,

                "preference": request.preference,

                "transport_mode": request.transport_mode,

                "status": response.status,

                "metrics": metrics,

                "budget": budget

            })

            self.logger.info("Trip Saved Successfully")

        except Exception as e:

            self.logger.error(
                "Database Error : %s",
                str(e)
            )

        return response

    # =====================================================
    # AI EXPLANATION
    # =====================================================

    def _generate_explanation(
        self,
        response: TripResponse
    ) -> str:

        metrics = response.metrics
        budget = response.budget

        explanation = []

        explanation.append(
            f"Selected route covers "
            f"{response.total_distance:.1f} km."
        )

        explanation.append(
            f"Estimated travel time is "
            f"{metrics.estimated_time:.1f} hours."
        )

        explanation.append(
            f"Estimated travel cost is "
            f"₹{metrics.estimated_cost:.2f}."
        )

        explanation.append(
            f"Traffic condition is "
            f"{metrics.traffic_status.lower()}."
        )

        explanation.append(
            f"Current weather is "
            f"{metrics.weather.lower()}."
        )

        if budget.status == "WITHIN_BUDGET":

            explanation.append(
                "Trip is within your specified budget."
            )

        elif budget.status == "BUDGET_EXCEEDED":

            explanation.append(
                f"Trip exceeds your budget by "
                f"₹{budget.exceeded_amount:.2f}."
            )

        explanation.append(metrics.recommendation)

        return " ".join(explanation)

    # =====================================================
    # ANALYTICS
    # =====================================================

    def get_trip_history(self):

        return self.repo.get_all_trips()

    def get_total_trips(self):

        return self.repo.total_trips()

    def get_average_distance(self):

        return self.repo.average_distance()

    def get_successful_trips(self):

        return self.repo.successful_trips()

    def get_budget_exceeded(self):

        return self.repo.budget_exceeded()

    def clear_history(self):

        self.repo.clear_history()

    # =====================================================
    # HEALTH
    # =====================================================

    def health_check(self):

        return "Application Ready"

    def version(self):

        return "3.0.0"