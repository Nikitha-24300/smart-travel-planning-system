from algorithms.graph_builder import GraphBuilder
from algorithms.dfs import DFS
from services.route_scorer import RouteScorer
from services.optimization.fastest_strategy import FastestStrategy

builder = GraphBuilder()
graph = builder.build_graph()

dfs = DFS(graph)
routes = dfs.find_all_routes("Hyderabad", "Chennai")

scorer = RouteScorer(graph)
strategy = FastestStrategy()

print("\n===== ROUTE SCORES =====\n")

for r in routes:

    score = scorer.score_route(r, strategy)

    print(r, "=> Score:", score)