"""
==================================================
Smart Travel Planning System
Author : Nikki
Main Entry Point
==================================================
"""

from config.logging_config import configure_logging
from exceptions.custom_exceptions import ValidationError
from services.application_controller import ApplicationController
from ui.console_ui import ConsoleUI


def display_trip_result(response):
    """
    Displays the planned trip in a professional format.
    """

    print("\n")
    print("=" * 70)
    print("                 SMART TRAVEL PLANNING SYSTEM")
    print("=" * 70)

    print("\nTRIP SUMMARY")
    print("-" * 70)

    print("\nBest Route")
    print("   " + " -> ".join(response.shortest_path))

    print(f"\nTotal Distance : {response.total_distance:.2f} km")

    if response.metrics:

        print("\nTRAVEL METRICS")
        print("-" * 70)

        print(
            f"Estimated Time      : "
            f"{response.metrics.estimated_time:.2f} Hours"
        )

        print(
            f"Estimated Cost      : "
            f"₹{response.metrics.estimated_cost:.2f}"
        )

        print(
            f"Carbon Emission     : "
            f"{response.metrics.carbon_emission:.2f} kg CO₂"
        )

        print(
            f"Route Score         : "
            f"{response.metrics.route_score:.2f}/100"
        )

    print("\nALTERNATIVE ROUTES")
    print("-" * 70)

    if response.alternative_routes:

        for index, route in enumerate(
            response.alternative_routes,
            start=1
        ):
            print(f"{index}. {' -> '.join(route)}")

    else:

        print("No alternative routes found.")

    print("\nSTATUS")
    print("-" * 70)
    print(response.status)

    if response.message:
        print(response.message)

    print("=" * 70)


def main():

    configure_logging()

    controller = ApplicationController()

    ui = ConsoleUI()

    while True:

        request = ui.show_main_menu()

        if request is None:
            print("\nGoodbye! Thank you for using Smart Travel Planning System.")
            break

        try:

            response = controller.plan_trip(request)

            display_trip_result(response)

        except ValidationError as error:

            print("\nValidation Error")
            print("-" * 70)
            print(error)

        except Exception as error:

            print("\nUnexpected Error")
            print("-" * 70)
            print(error)


if __name__ == "__main__":
    main()