class BaseStrategy:

    def calculate_score(self, distance, duration, cost):
        raise NotImplementedError

    def get_priority_label(self):
        return "BASE"