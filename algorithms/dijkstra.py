import heapq


class Dijkstra:

    def __init__(self, graph):

        self.graph = graph

    def find_shortest_path(

        self,

        start,

        end

    ):

        distances = {

            city: float("inf")

            for city in self.graph
        }

        previous = {

            city: None

            for city in self.graph
        }

        distances[start] = 0

        priority_queue = [

            (0, start)
        ]

        while priority_queue:

            current_distance, current_city = heapq.heappop(

                priority_queue
            )

            if current_city == end:

                break

            for neighbor, distance in self.graph[current_city]:

                new_distance = (

                    current_distance

                    + distance
                )

                if new_distance < distances[neighbor]:

                    distances[neighbor] = new_distance

                    previous[neighbor] = current_city

                    heapq.heappush(

                        priority_queue,

                        (

                            new_distance,

                            neighbor

                        )
                    )

        path = []

        city = end

        while city:

            path.insert(

                0,

                city
            )

            city = previous[city]

        return (

            path,

            distances[end]

        )