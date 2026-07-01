"""
==================================================
Smart Travel Planning System
Module: Budget Analysis Model (FIXED)
==================================================
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class BudgetAnalysis:
    max_budget: Optional[float]
    estimated_cost: float
    status: str
    exceeded_amount: float
    recommendation: str