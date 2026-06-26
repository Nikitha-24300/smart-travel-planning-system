"""
==================================================
Smart Travel Planning System
Module: Route Optimizer
Author: Nikki
Description:
Coordinates routing algorithms and returns
the optimized travel response.
==================================================
"""

import logging

from algorithms.dijkstra import Dijkstra
from algorithms.dfs import DFS
from algorithms.graph_builder import GraphBuilder
from models.trip_request import TripRequest
from models.trip_response import TripResponse


class RouteOptimizer:
    """
    Coordinates all routing algorithms.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        builder = GraphBuilder()
        self.graph = builder.build_graph()

        self.dijkstra = Dijkstra(self.graph)
        self.dfs = DFS(self.graph)

    def optimize(self, request: TripRequest) -> TripResponse:
        """
        Finds the best route and alternative routes.
        """

        self.logger.info("Running Dijkstra algorithm.")

        shortest_path, total_distance = self.dijkstra.find_shortest_path(
            request.source,
            request.destination,
        )

        self.logger.info("Searching for alternative routes.")

        alternative_routes = self.dfs.find_all_routes(
            request.source,
            request.destination,
        )

        self.logger.info("Route optimization completed.")

        return TripResponse(
            shortest_path=shortest_path,
            total_distance=total_distance,
            alternative_routes=alternative_routes,
        )