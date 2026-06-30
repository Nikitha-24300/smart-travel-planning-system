from .base_strategy import BaseStrategy


class CheapestStrategy(BaseStrategy):

    def calculate_score(self, distance, duration, cost):

        return cost  # minimize cost

    def get_priority_label(self):
        return "CHEAPEST"