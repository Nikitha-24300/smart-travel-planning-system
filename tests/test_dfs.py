from algorithms.graph_builder import GraphBuilder
from algorithms.dfs import DFS

builder = GraphBuilder()
graph = builder.build_graph()

dfs = DFS(graph)

routes = dfs.find_all_routes("Hyderabad", "Chennai")

print("\n===== DFS ROUTES =====\n")

for r in routes:
    print(" -> ".join(r))

print("\nTOTAL ROUTES:", len(routes))