"""
==================================================
Smart Travel Planning System
Main Entry Point (FIXED)
==================================================
"""

from config.logging_config import configure_logging
from exceptions.custom_exceptions import ValidationError
from services.application_controller import ApplicationController
from ui.console_ui import ConsoleUI


def display_trip_result(response):

    print("\n" + "=" * 70)
    print("SMART TRAVEL PLANNING SYSTEM")
    print("=" * 70)

    print("\nTRIP SUMMARY")
    print("-" * 70)

    print("\nBest Route")
    print("   " + " -> ".join(response.shortest_path))

    # DISTANCE
    print("\nDISTANCE")
    print("-" * 70)

    print(f"Graph Distance      : {response.total_distance:.2f} km")

    if response.metrics:
        print(f"Road Distance       : {response.metrics.real_distance:.2f} km")

    # METRICS
    if response.metrics:

        print("\nTRAVEL METRICS")
        print("-" * 70)

        print(f"Estimated Time      : {response.metrics.estimated_time:.2f} Hours")
        print(f"Real Drive Time     : {response.metrics.real_duration:.2f} Hours")
        print(f"Estimated Cost      : ₹{response.metrics.estimated_cost:.2f}")
        print(f"Carbon Emission     : {response.metrics.carbon_emission:.2f} kg CO₂")
        print(f"Route Score         : {response.metrics.route_score:.2f}/100")

        print("\nWEATHER")
        print("-" * 70)

        print(f"Weather             : {response.metrics.weather}")
        print(f"Temperature         : {response.metrics.temperature:.1f} °C")

        print("\nTRAFFIC")
        print("-" * 70)

        print(f"Traffic Status      : {response.metrics.traffic_status}")
        print(f"Traffic Factor      : {response.metrics.traffic_factor:.2f}")

    # BUDGET (SAFE FIX)
    if getattr(response, "budget", None):

        print("\nBUDGET ANALYSIS")
        print("-" * 70)

        print(f"Budget              : ₹{response.budget.max_budget}")
        print(f"Estimated Cost      : ₹{response.budget.estimated_cost}")
        print(f"Status              : {response.budget.status}")
        print(f"Exceeded By         : ₹{response.budget.exceeded_amount}")

        print("\nRecommendation")
        print(response.budget.recommendation)

    # ALTERNATIVES
    print("\nALTERNATIVE ROUTES")
    print("-" * 70)

    for i, route in enumerate(response.alternative_routes, 1):
        print(f"{i}. {' -> '.join(route)}")

    # STATUS
    print("\nSTATUS")
    print("-" * 70)

    print(response.status)
    print(response.message)


def main():

    configure_logging()

    controller = ApplicationController()
    ui = ConsoleUI()

    while True:

        request = ui.show_main_menu()

        if request is None:
            print("\nGoodbye!")
            break

        try:
            response = controller.plan_trip(request)
            display_trip_result(response)

        except ValidationError as e:
            print("\nValidation Error:", e)

        except Exception as e:
            print("\nUnexpected Error:", e)


if __name__ == "__main__":
    main()