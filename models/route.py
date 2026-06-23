class Route:

    def __init__(
        self,
        source,
        destination,
        distance,
        duration,
        cost
    ):

        self.source = source
        self.destination = destination

        self.distance = distance

        self.duration = duration

        self.cost = cost

    def to_dict(self):

        return {

            "source": self.source,

            "destination": self.destination,

            "distance": self.distance,

            "duration": self.duration,

            "cost": self.cost
        }

    def __str__(self):

        return (
            f"{self.source}"
            f" -> "
            f"{self.destination}"
        )