"""
==================================================
Smart Travel Planning System
Module : Route Scorer
Version : 3.0
Author  : Nikki
==================================================
"""

import logging


class RouteScorer:
    """
    Calculates the score of a route based on the
    selected optimization strategy.
    """

    def __init__(self, graph):

        self.graph = graph
        self.logger = logging.getLogger(__name__)

    # =====================================================
    # PUBLIC METHOD
    # =====================================================

    def score_route(self, route, strategy):

        total_distance = 0.0
        total_duration = 0.0
        total_cost = 0.0

        if len(route) < 2:
            return float("inf")

        for i in range(len(route) - 1):

            current_city = route[i]
            next_city = route[i + 1]

            edge = self._get_edge(current_city, next_city)

            if edge is None:
                self.logger.warning(
                    "Missing edge: %s -> %s",
                    current_city,
                    next_city
                )
                return float("inf")

            total_distance += edge.get("distance", 0.0)
            total_duration += edge.get("duration", 0.0)
            total_cost += edge.get("cost", 0.0)

        score = strategy.calculate_score(
            distance=total_distance,
            duration=total_duration,
            cost=total_cost
        )

        self.logger.info(
            "%s | Distance: %.2f km | Duration: %.2f hr | Cost: %.2f | Score: %.2f",
            strategy.get_priority_label(),
            total_distance,
            total_duration,
            total_cost,
            score
        )

        return round(score, 2)

    # =====================================================
    # PRIVATE METHODS
    # =====================================================

    def _get_edge(self, source, destination):

        if source not in self.graph:
            return None

        for neighbor, edge_data in self.graph[source]:

            if neighbor == destination:
                return edge_data

        return None