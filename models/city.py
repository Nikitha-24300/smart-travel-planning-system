class City:

    def __init__(
        self,
        city_id,
        name,
        state,
        latitude,
        longitude
    ):

        self.city_id = city_id
        self.name = name
        self.state = state
        self.latitude = latitude
        self.longitude = longitude

    def to_dict(self):

        return {
            "city_id": self.city_id,
            "name": self.name,
            "state": self.state,
            "latitude": self.latitude,
            "longitude": self.longitude
        }

    def __str__(self):

        return f"{self.name}, {self.state}"