from .base_strategy import BaseStrategy


class BalancedStrategy(BaseStrategy):

    def calculate_score(self, distance, duration, cost):

        return distance + duration * 10 + cost * 0.5

    def get_priority_label(self):
        return "BALANCED"