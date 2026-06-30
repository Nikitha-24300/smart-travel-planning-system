from algorithms.graph_builder import GraphBuilder

builder = GraphBuilder()
graph = builder.build_graph()

print("\n===== GRAPH DEBUG OUTPUT =====\n")

for city, edges in graph.items():
    print(city)

    for neighbor, data in edges:
        print(f"  -> {neighbor}")
        print(f"     distance: {data['distance']}")
        print(f"     duration : {data['duration']}")
        print(f"     cost     : {data['cost']}")

print("\nGRAPH LOADED SUCCESSFULLY")