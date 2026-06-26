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


def main():

    configure_logging()

    controller = ApplicationController()

    ui = ConsoleUI()

    while True:

        request = ui.show_main_menu()

        if request is None:

            break

        try:

            response = controller.plan_trip(

                request

            )

            print("\n")

            print("=" * 60)

            print("TRIP RESULT")

            print("=" * 60)

            print("\nShortest Route")

            print("------------------------")

            print(

                " -> ".join(

                    response.shortest_path

                )

            )

            print(

                f"\nDistance : {response.total_distance} km"

            )

            print("\nAlternative Routes")

            print("------------------------")

            for i, route in enumerate(

                    response.alternative_routes,

                    start=1

            ):

                print(

                    f"{i}. {' -> '.join(route)}"

                )

        except ValidationError as error:

            print("\nValidation Error")

            print("------------------------")

            print(error)

        except Exception as error:

            print("\nUnexpected Error")

            print("------------------------")

            print(error)


if __name__ == "__main__":

    main()