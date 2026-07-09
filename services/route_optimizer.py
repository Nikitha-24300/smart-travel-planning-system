import logging

from algorithms.graph_builder import GraphBuilder
from algorithms.dfs import DFS

from models.trip_response import TripResponse

from services.route_scorer import RouteScorer

from services.optimization.fastest_strategy import FastestStrategy
from services.optimization.cheapest_strategy import CheapestStrategy
from services.optimization.eco_strategy import EcoStrategy
from services.optimization.balanced_strategy import BalancedStrategy


class RouteOptimizer:

    def __init__(self):

        self.logger = logging.getLogger(__name__)

        builder = GraphBuilder()

        self.graph = builder.build_graph()

        self.dfs = DFS(self.graph)

        self.scorer = RouteScorer(self.graph)

        self.strategies = {
            "fastest": FastestStrategy(),
            "cheapest": CheapestStrategy(),
            "eco": EcoStrategy(),
            "balanced": BalancedStrategy()
        }

    def optimize(self, request):

        self.logger.info(
            "Searching routes from %s to %s",
            request.source,
            request.destination
        )

        routes = self.dfs.find_all_routes(
            request.source,
            request.destination
        )

        if not routes:

            return TripResponse(
                shortest_path=[],
                total_distance=0,
                alternative_routes=[],
                status="FAILED",
                message="No route found"
            )

        strategy = self.strategies.get(
            request.preference.lower(),
            FastestStrategy()
        )

        scored_routes = []

        for route in routes:

            score = self.scorer.score_route(
                route,
                strategy
            )

            scored_routes.append(
                (
                    route,
                    score
                )
            )

        scored_routes.sort(
            key=lambda x: x[1]
        )

        best_route = scored_routes[0][0]

        alternative_routes = [
            r[0]
            for r in scored_routes[:5]
        ]

        total_distance = 0

        for i in range(len(best_route) - 1):

            current_city = best_route[i]
            next_city = best_route[i + 1]

            for neighbor, edge in self.graph[current_city]:

                if neighbor == next_city:

                    total_distance += edge["distance"]
                    break

        return TripResponse(
            shortest_path=best_route,
            total_distance=round(total_distance, 2),
            alternative_routes=alternative_routes,
            status="SUCCESS",
            message=f"Route optimized using {request.preference.title()} Strategy"
        )