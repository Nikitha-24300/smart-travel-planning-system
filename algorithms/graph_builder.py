"""
==================================================
Smart Travel Planning System
Module : Graph Builder
Version : 3.0
Author  : Nikki
==================================================
"""

import json
from pathlib import Path


class GraphBuilder:
    """
    Builds an undirected weighted graph from routes.json.
    Each edge stores:
        - distance
        - duration
        - cost
    """

    def __init__(self):
        self.graph = {}

    # ==================================================
    # LOAD ROUTES
    # ==================================================

    def load_routes(self):

        project_root = Path(__file__).resolve().parent.parent

        routes_file = project_root / "data" / "routes.json"

        if not routes_file.exists():
            raise FileNotFoundError(
                f"Routes file not found: {routes_file}"
            )

        with open(routes_file, "r", encoding="utf-8") as file:
            routes = json.load(file)

        return routes

    # ==================================================
    # BUILD GRAPH
    # ==================================================

    def build_graph(self):

        self.graph.clear()

        routes = self.load_routes()

        for route in routes:

            source = route["source"].strip()
            destination = route["destination"].strip()

            edge = {
                "distance": float(route["distance"]),
                "duration": float(route["duration"]),
                "cost": float(route["cost"])
            }

            self.graph.setdefault(source, [])
            self.graph.setdefault(destination, [])

            # Undirected Graph
            self.graph[source].append((destination, edge))
            self.graph[destination].append((source, edge))

        return self.graph

    # ==================================================
    # GET GRAPH
    # ==================================================

    def get_graph(self):

        if not self.graph:
            self.build_graph()

        return self.graph

    # ==================================================
    # GET ALL CITIES
    # ==================================================

    def get_all_cities(self):

        if not self.graph:
            self.build_graph()

        return sorted(self.graph.keys())

    # ==================================================
    # DISPLAY GRAPH
    # ==================================================

    def display_graph(self):

        if not self.graph:
            self.build_graph()

        print("\n========== GRAPH ==========\n")

        for city in sorted(self.graph.keys()):

            print(city)

            for destination, edge in self.graph[city]:

                print(
                    f"   -> {destination}"
                    f" | {edge['distance']} km"
                    f" | {edge['duration']} hr"
                    f" | ₹{edge['cost']}"
                )

            print()