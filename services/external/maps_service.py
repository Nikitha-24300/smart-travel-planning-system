import requests
import os


class MapsService:

    def __init__(self):

        self.api_key = os.getenv("MAPS_API_KEY")

    def get_distance(self, origin: str, destination: str):

        url = "https://maps.googleapis.com/maps/api/distancematrix/json"

        params = {
            "origins": origin,
            "destinations": destination,
            "key": self.api_key
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return None

        data = response.json()

        try:
            element = data["rows"][0]["elements"][0]

            return {
                "distance": element["distance"]["value"] / 1000,
                "duration": element["duration"]["value"] / 60
            }

        except:
            return None