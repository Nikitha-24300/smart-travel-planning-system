class RouteFilter:

    def filter_routes(self, routes, max_length=None):

        filtered = []

        for route in routes:

            if max_length and len(route) > max_length:
                continue

            # remove duplicate or invalid routes
            if route not in filtered:
                filtered.append(route)

        return filtered