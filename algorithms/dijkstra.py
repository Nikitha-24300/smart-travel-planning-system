import heapq


class Dijkstra:

    def __init__(self, graph):
        self.graph = graph

    def find_path(self, start, end, weight="distance"):

        distances = {
            city: float("inf")
            for city in self.graph
        }

        previous = {
            city: None
            for city in self.graph
        }

        distances[start] = 0

        queue = [(0, start)]

        while queue:

            current_cost, current_city = heapq.heappop(queue)

            if current_city == end:
                break

            if current_cost > distances[current_city]:
                continue

            for neighbor, edge_data in self.graph[current_city]:

                edge_weight = edge_data.get(weight, 1)

                new_cost = current_cost + edge_weight

                if new_cost < distances[neighbor]:

                    distances[neighbor] = new_cost

                    previous[neighbor] = current_city

                    heapq.heappush(
                        queue,
                        (
                            new_cost,
                            neighbor
                        )
                    )

        if distances[end] == float("inf"):
            return [], float("inf")

        path = []

        city = end

        while city is not None:

            path.insert(0, city)

            city = previous[city]

        return path, distances[end]