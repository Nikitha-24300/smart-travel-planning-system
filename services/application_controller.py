"""
==================================================
Smart Travel Planning System
Module: Application Controller (FIXED MILESTONE 6)
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

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        self.validator = TripValidator()
        self.optimizer = RouteOptimizer()
        self.intelligence = TravelIntelligenceService()
        self.budget_planner = BudgetPlanner()
        self.repo = TripRepository()

    def plan_trip(self, request: TripRequest) -> TripResponse:

        self.logger.info(
            "Trip request received: %s -> %s",
            request.source,
            request.destination
        )

        # 1. Validate
        self.validator.validate(request)

        # 2. Route optimization
        response = self.optimizer.optimize(request)

        # 3. Intelligence metrics
        response.metrics = self.intelligence.generate_metrics(request)

        # 4. Budget analysis (SAFE + CONSISTENT)
        try:
            response.budget = self.budget_planner.analyze(
                max_budget=getattr(request, "max_budget", None),
                estimated_cost=response.metrics.estimated_cost,
                transport_mode=getattr(request, "transport_mode", "any")
            )

            self.logger.info("Budget Analysis: %s", response.budget.status)

        except Exception as e:
            self.logger.error("Budget module failed: %s", str(e))
            response.budget = None

        # 5. Save to DB (safe)
        try:
            self.repo.save_trip({
                "source": request.source,
                "destination": request.destination,
                "route": response.shortest_path,
                "total_distance": response.total_distance,
                "preference": request.preference,
                "status": response.status,
                "budget_status": getattr(response.budget, "status", None)
            })

            self.logger.info("Trip saved successfully.")

        except Exception as e:
            self.logger.error("Database save failed: %s", str(e))

        return response

    def health_check(self):
        return "Application Ready"

    def version(self):
        return "2.1.0"