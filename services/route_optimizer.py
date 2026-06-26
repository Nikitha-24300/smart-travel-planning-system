from algorithms.graph_builder import GraphBuilder
from algorithms.dijkstra import Dijkstra
from algorithms.dfs import DFS
from models.trip_request import TripRequest
from models.trip_response import TripResponse


class RouteOptimizer:
    """
    Responsible for coordinating all routing algorithms.
    """

    def __init__(self):
        builder = GraphBuilder()
        self.graph = builder.build_graph()

        self.dijkstra = Dijkstra(self.graph)
        self.dfs = DFS(self.graph)

    def optimize(self, request: TripRequest) -> TripResponse:
        """
        Calculates the best route and alternative routes.
        """

        shortest_path, total_distance = self.dijkstra.find_shortest_path(
            request.source,
            request.destination
        )

        alternative_routes = self.dfs.find_all_routes(
            request.source,
            request.destination
        )

        return TripResponse(
            shortest_path=shortest_path,
            total_distance=total_distance,
            alternative_routes=alternative_routes
        )