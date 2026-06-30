class TrafficService:

    def get_traffic_factor(self, city: str):

        traffic_map = {
            "Hyderabad": 1.2,
            "Mumbai": 1.5,
            "Bangalore": 1.3,
            "Chennai": 1.1
        }

        return traffic_map.get(city, 1.0)