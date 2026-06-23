from algorithms.graph_builder import GraphBuilder

from algorithms.dijkstra import Dijkstra

from algorithms.dfs import DFS


def main():

    builder = GraphBuilder()

    graph = builder.build_graph()

    dijkstra = Dijkstra(graph)

    dfs = DFS(graph)

    path, distance = dijkstra.find_shortest_path(

        "Hyderabad",

        "Chennai"

    )

    print()

    print("Shortest Path")

    print(

        " -> ".join(path)

    )

    print()

    print(

        f"Distance: {distance} km"

    )

    print()

    print("Alternative Routes")

    all_routes = dfs.find_all_routes(

        "Hyderabad",

        "Chennai"

    )

    for route in all_routes:

        print(

            " -> ".join(route)

        )


if __name__ == "__main__":

    main()