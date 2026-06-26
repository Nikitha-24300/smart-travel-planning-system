"""
Custom exceptions used throughout the Smart Travel Planning System.
"""


class TravelPlannerException(Exception):
    """
    Base exception for the application.
    """
    pass


class ValidationError(TravelPlannerException):
    """
    Raised when user input is invalid.
    """
    pass


class CityNotFoundError(ValidationError):
    """
    Raised when a city does not exist in the graph.
    """
    pass


class SameCityError(ValidationError):
    """
    Raised when source and destination are identical.
    """
    pass


class EmptyFieldError(ValidationError):
    """
    Raised when required fields are empty.
    """
    pass