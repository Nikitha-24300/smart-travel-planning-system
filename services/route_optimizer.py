"""
==================================================
Smart Travel Planning System
Module : Route Optimizer
Author : Nikki

Description:
Coordinates all routing algorithms and
travel metric calculations.
==================================================
"""

import logging

from algorithms.dijkstra import Dijkstra
from algorithms.dfs import DFS
from algorithms.graph_builder import GraphBuilder

from models.trip_request import TripRequest
from models.trip_response import TripResponse

from services.metrics.metrics_service import MetricsService


class RouteOptimizer:
    """
    Coordinates all routing algorithms and
    generates the final TripResponse.
    """

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        builder = GraphBuilder()

        self.graph = builder.build_graph()

        self.dijkstra = Dijkstra(self.graph)

        self.dfs = DFS(self.graph)

        self.metrics_service = MetricsService()

    def optimize(
        self,
        request: TripRequest
    ) -> TripResponse:
        """
        Executes all required services to
        generate an optimized travel plan.
        """

        self.logger.info(
            "Running Dijkstra algorithm."
        )

        shortest_path, total_distance = (
            self.dijkstra.find_shortest_path(
                request.source,
                request.destination
            )
        )

        self.logger.info(
            "Searching alternative routes."
        )

        alternative_routes = (
            self.dfs.find_all_routes(
                request.source,
                request.destination
            )
        )

        self.logger.info(
            "Calculating travel metrics."
        )

        metrics = (
            self.metrics_service.calculate_metrics(
                distance=total_distance,
                transport_mode=request.transport_mode
            )
        )

        self.logger.info(
            "Route optimization completed successfully."
        )

        return TripResponse(

            shortest_path=shortest_path,

            total_distance=total_distance,

            alternative_routes=alternative_routes,

            metrics=metrics,

            status="SUCCESS",

            message="Trip planned successfully."

        )