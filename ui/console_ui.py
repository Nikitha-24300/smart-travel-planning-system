"""
==================================================
Smart Travel Planning System
Module : Console UI
Author : Nikki
==================================================
"""

from models.trip_request import TripRequest
from ui.menu import Menu
from ui.progress import Progress


class ConsoleUI:

    def show_main_menu(self):

        Menu.display_welcome()

        while True:

            Menu.display_main_menu()

            choice = input("\nEnter choice : ").strip()

            if choice == "1":

                return self.collect_trip_details()

            elif choice == "2":

                print("\nThank you for using Smart Travel Planning System.")

                return None

            else:

                print("\nInvalid choice.")

    def collect_trip_details(self):

        print("\nEnter Trip Details")

        source = input("Source City : ").strip()
        destination = input("Destination City : ").strip()

        # -----------------------------
        # Preference Menu
        # -----------------------------
        Menu.display_preference_menu()

        preference = self.get_preference(
            input("\nChoice : ").strip()
        )

        # -----------------------------
        # Transport Menu
        # -----------------------------
        Menu.display_transport_menu()

        transport = self.get_transport_mode(
            input("\nChoice : ").strip()
        )

        # -----------------------------
        # NEW: Budget Input (Milestone 6)
        # -----------------------------
        budget_input = input(
            "\nEnter Maximum Budget (press Enter to skip): "
        ).strip()

        if budget_input == "":
            max_budget = None
        else:
            try:
                max_budget = float(budget_input)
            except ValueError:
                print("Invalid budget input. Setting budget to None.")
                max_budget = None

        Progress.loading()

        return TripRequest(
            source=source,
            destination=destination,
            preference=preference,
            transport_mode=transport,
            max_budget=max_budget
        )

    @staticmethod
    def get_preference(choice):

        mapping = {
            "1": "fastest",
            "2": "shortest"
        }

        return mapping.get(choice, "fastest")

    @staticmethod
    def get_transport_mode(choice):

        mapping = {
            "1": "any",
            "2": "bus",
            "3": "train",
            "4": "flight"
        }

        return mapping.get(choice, "any")