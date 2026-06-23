from algorithms.graph_builder import GraphBuilder

from algorithms.dijkstra import Dijkstra


def main():

    builder = GraphBuilder()

    graph = builder.build_graph()

    algorithm = Dijkstra(graph)

    path, distance = algorithm.find_shortest_path(

        "Hyderabad",

        "Chennai"

    )

    print()

    print("Shortest Path:")

    print(

        " -> ".join(path)

    )

    print()

    print(

        f"Distance: {distance} km"

    )


if __name__ == "__main__":

    main()