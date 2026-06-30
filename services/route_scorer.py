class RouteScorer:
    """
    Scores routes based on selected strategy.
    """

    def __init__(self, graph):
        self.graph = graph

    def score_route(self, route, strategy):

        total_distance = 0
        total_duration = 0
        total_cost = 0

        for i in range(len(route) - 1):

            current = route[i]
            next_node = route[i + 1]

            edge = self._get_edge(current, next_node)

            if edge is None:
                continue

            total_distance += edge["distance"]
            total_duration += edge["duration"]
            total_cost += edge["cost"]

        return strategy.calculate_score(
            distance=total_distance,
            duration=total_duration,
            cost=total_cost
        )

    def _get_edge(self, current, next_node):

        for neighbor, data in self.graph[current]:

            if neighbor == next_node:
                return data

        return None