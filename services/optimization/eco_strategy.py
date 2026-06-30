from .base_strategy import BaseStrategy


class EcoStrategy(BaseStrategy):

    def calculate_score(self, distance, duration, cost):

        return distance * 0.6 + cost * 0.4

    def get_priority_label(self):
        return "ECO"