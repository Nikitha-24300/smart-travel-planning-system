"""
==================================================
Smart Travel Planning System
Author: Nikki
Description:
Application Entry Point
==================================================
"""

from config.logging_config import configure_logging
from exceptions.custom_exceptions import ValidationError
from models.trip_request import TripRequest
from services.application_controller import ApplicationController


def main():
    """
    Entry point of the application.
    """

    configure_logging()

    controller = ApplicationController()

    request = TripRequest(
        source="Hyderabad",
        destination="Chennai",
        preference="fastest"
    )

    try:

        response = controller.plan_trip(request)

        print("\n===================================")
        print(" SMART TRAVEL PLANNING SYSTEM")
        print("===================================\n")

        print("Shortest Route")
        print("--------------")
        print(" -> ".join(response.shortest_path))

        print(f"\nDistance : {response.total_distance} km")

        print("\nAlternative Routes")
        print("------------------")

        for index, route in enumerate(
            response.alternative_routes,
            start=1
        ):
            print(f"{index}. {' -> '.join(route)}")

    except ValidationError as error:

        print("\nValidation Error")
        print("----------------")
        print(error)

    except Exception as error:

        print("\nUnexpected Error")
        print("----------------")
        print(error)


if __name__ == "__main__":
    main()