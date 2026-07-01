class RouteExplainer:

    def explain(self, route, metrics, strategy):

        if not route:
            return "No route available."

        parts = []

        parts.append(
            f"Route selected using {strategy.upper()} strategy."
        )

        if metrics:

            if metrics.real_distance:
                parts.append(
                    f"Road distance is {metrics.real_distance:.2f} km."
                )

            if metrics.real_duration:
                parts.append(
                    f"Estimated drive time is {metrics.real_duration:.2f} hours."
                )

            if metrics.traffic_factor > 1.2:
                parts.append(
                    "Traffic is moderate to heavy, but this route remains optimal."
                )
            else:
                parts.append(
                    "Traffic conditions are light and favorable."
                )

            if metrics.carbon_emission < 70:
                parts.append(
                    "This route is eco-friendly with low emissions."
                )
            else:
                parts.append(
                    "This route balances performance and environmental impact."
                )

            if metrics.estimated_cost:
                parts.append(
                    f"Estimated cost is ₹{metrics.estimated_cost:.2f}."
                )

        return " ".join(parts)