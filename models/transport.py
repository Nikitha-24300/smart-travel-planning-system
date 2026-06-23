class Transport:

    def __init__(

        self,

        transport_type,

        average_speed,

        cost_per_km

    ):

        self.transport_type = transport_type

        self.average_speed = average_speed

        self.cost_per_km = cost_per_km

    def to_dict(self):

        return {

            "transport_type": self.transport_type,

            "average_speed": self.average_speed,

            "cost_per_km": self.cost_per_km
        }

    def __str__(self):

        return self.transport_type