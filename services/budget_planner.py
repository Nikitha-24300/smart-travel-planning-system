"""
==================================================
Smart Travel Planning System
Module: Budget Planner (FIXED)
==================================================
"""

from models.budget_analysis import BudgetAnalysis


class BudgetPlanner:

    def analyze(
        self,
        max_budget: float | None,
        estimated_cost: float,
        transport_mode: str = "any"
    ) -> BudgetAnalysis:

        # No budget provided → skip analysis safely
        if max_budget is None or max_budget == 0:
            return BudgetAnalysis(
                max_budget=None,
                estimated_cost=estimated_cost,
                status="NO_BUDGET",
                exceeded_amount=0.0,
                recommendation="No budget provided"
            )

        # Budget check
        if estimated_cost <= max_budget:
            return BudgetAnalysis(
                max_budget=max_budget,
                estimated_cost=estimated_cost,
                status="WITHIN_BUDGET",
                exceeded_amount=0.0,
                recommendation="Trip is within budget"
            )

        exceeded = round(estimated_cost - max_budget, 2)

        return BudgetAnalysis(
            max_budget=max_budget,
            estimated_cost=estimated_cost,
            status="BUDGET_EXCEEDED",
            exceeded_amount=exceeded,
            recommendation="Reduce distance or choose cheaper transport"
        )