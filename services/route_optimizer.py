import logging

from algorithms.graph_builder import GraphBuilder
from algorithms.dfs import DFS

from models.trip_request import TripRequest
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

    def _get_strategy(self, preference: str):

        return self.strategies.get(
            preference.lower(),
            self.strategies["fastest"]
        )

    def optimize(self, request: TripRequest) -> TripResponse:

        self.logger.info("Generating all possible routes using DFS.")

        all_routes = self.dfs.find_all_routes(
            request.source,
            request.destination
        )

        self.logger.info("Total routes found: %d", len(all_routes))

        strategy = self._get_strategy(request.preference)

        best_route = None
        best_score = float("inf")

        scored_routes = []

        for route in all_routes:

            score = self.scorer.score_route(route, strategy)

            scored_routes.append((route, score))

            if score < best_score:

                best_score = score
                best_route = route

        # Sort alternatives by best score
        scored_routes.sort(key=lambda x: x[1])

        alternatives = [r[0] for r in scored_routes]

        self.logger.info(
            "Best route selected using %s strategy",
            strategy.get_priority_label()
        )

        total_distance = 0

        if best_route:

            for i in range(len(best_route) - 1):

                edge = next(
                    (
                        e for e in self.graph[best_route[i]]
                        if e[0] == best_route[i + 1]
                    ),
                    None
                )

                if edge:
                    total_distance += edge[1]["distance"]

        return TripResponse(
            shortest_path=best_route,
            total_distance=total_distance,
            alternative_routes=alternatives,
            status="SUCCESS",
            message=f"Optimized using {strategy.get_priority_label()}"
        )