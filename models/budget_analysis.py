"""
==================================================
Smart Travel Planning System
Budget Analysis Model
Version : 3.0
Author  : Nikki
==================================================
"""

from dataclasses import dataclass, asdict
from typing import Optional


@dataclass(slots=True)
class BudgetAnalysis:
    """
    Stores complete budget analysis for a planned trip.
    """

    # User Budget
    max_budget: Optional[float] = None

    # Estimated Trip Cost
    estimated_cost: float = 0.0

    # Budget Difference
    exceeded_amount: float = 0.0
    remaining_budget: float = 0.0

    # Budget Status
    status: str = "NO_BUDGET"

    # Budget Utilization
    budget_utilization: float = 0.0

    # Recommendation
    recommendation: str = ""

    # Savings Suggestion
    savings_suggestion: str = ""

    def to_dict(self):
        """
        Convert object into dictionary.
        """
        return asdict(self)

    def __str__(self):

        return (
            f"BudgetAnalysis("
            f"budget={self.max_budget}, "
            f"cost={self.estimated_cost}, "
            f"remaining={self.remaining_budget}, "
            f"utilization={self.budget_utilization}%, "
            f"status='{self.status}')"
        )