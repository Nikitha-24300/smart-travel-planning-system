"""
==================================================
Smart Travel Planning System
Budget Planner Service
Version : 3.0
Author  : Nikki
==================================================
"""

from models.budget_analysis import BudgetAnalysis


class BudgetPlanner:
    """
    Performs budget analysis and generates
    recommendations for the user.
    """

    def analyze(
        self,
        max_budget: float | None,
        estimated_cost: float,
        transport_mode: str = "any"
    ) -> BudgetAnalysis:

        analysis = BudgetAnalysis()

        analysis.max_budget = max_budget
        analysis.estimated_cost = round(estimated_cost, 2)

        # =================================================
        # No Budget Provided
        # =================================================

        if max_budget is None or max_budget <= 0:

            analysis.status = "NO_BUDGET"

            analysis.recommendation = (
                "No budget provided. Cost estimation only."
            )

            analysis.savings_suggestion = (
                "Enter a budget to receive personalized suggestions."
            )

            return analysis

        # =================================================
        # Budget Utilization
        # =================================================

        utilization = (estimated_cost / max_budget) * 100

        analysis.budget_utilization = round(utilization, 2)

        # =================================================
        # Within Budget
        # =================================================

        if estimated_cost <= max_budget:

            analysis.status = "WITHIN_BUDGET"

            analysis.remaining_budget = round(
                max_budget - estimated_cost,
                2
            )

            analysis.recommendation = (
                "Your trip is within budget."
            )

            if analysis.remaining_budget > max_budget * 0.30:

                analysis.savings_suggestion = (
                    "You still have a healthy budget remaining."
                )

            elif analysis.remaining_budget > max_budget * 0.10:

                analysis.savings_suggestion = (
                    "Budget usage is good."
                )

            else:

                analysis.savings_suggestion = (
                    "You are close to your budget limit."
                )

            return analysis

        # =================================================
        # Budget Exceeded
        # =================================================

        analysis.status = "BUDGET_EXCEEDED"

        analysis.exceeded_amount = round(
            estimated_cost - max_budget,
            2
        )

        analysis.remaining_budget = 0.0

        # Transport Recommendation

        if transport_mode == "flight":

            suggestion = (
                "Consider switching to train or bus."
            )

        elif transport_mode == "train":

            suggestion = (
                "Consider sleeper class or cheaper trains."
            )

        elif transport_mode == "bus":

            suggestion = (
                "Consider economy bus options."
            )

        else:

            suggestion = (
                "Try a cheaper transport option."
            )

        analysis.recommendation = suggestion

        analysis.savings_suggestion = (
            f"Reduce your trip cost by "
            f"₹{analysis.exceeded_amount:.2f} "
            f"to stay within budget."
        )

        return analysis