import json
from pathlib import Path


class GraphBuilder:

    def __init__(self):
        self.graph = {}

    def load_routes(self):

        project_root = Path(__file__).resolve().parent.parent
        routes_file = project_root / "data" / "routes.json"

        with open(routes_file, "r", encoding="utf-8") as file:
            routes = json.load(file)

        return routes

    def build_graph(self):

        routes = self.load_routes()

        for route in routes:

            source = route["source"]
            destination = route["destination"]

            # NEW multi-weight structure
            edge_data = {
                "distance": route["distance"],
                "duration": route["duration"],
                "cost": route["cost"]
            }

            if source not in self.graph:
                self.graph[source] = []

            if destination not in self.graph:
                self.graph[destination] = []

            # bidirectional graph
            self.graph[source].append((destination, edge_data))
            self.graph[destination].append((source, edge_data))

        return self.graph

    def display_graph(self):

        for city, connections in self.graph.items():
            print("\n", city)
            for conn in connections:
                print("   ", conn)