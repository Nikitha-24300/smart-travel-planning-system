class DFS:

    def __init__(self, graph):
        self.graph = graph

    def find_all_routes(self, start, end):

        routes = []

        self._dfs(start, end, [], set(), routes)

        return routes

    def _dfs(self, current, destination, path, visited, routes):

        visited.add(current)
        path.append(current)

        if current == destination:
            routes.append(path.copy())

        else:
            for neighbor, _ in self.graph[current]:

                if neighbor not in visited:

                    self._dfs(
                        neighbor,
                        destination,
                        path,
                        visited,
                        routes
                    )

        path.pop()
        visited.remove(current)