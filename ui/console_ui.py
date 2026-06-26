"""
==================================================
Smart Travel Planning System
Module : Console UI
Author : Nikki
==================================================
"""

from models.trip_request import TripRequest
from ui.menu import Menu


class ConsoleUI:
    """
    Handles all console interactions.
    """

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

        print("\nTrip Details")
        print("------------------------")

        source = input("Enter Source City : ").strip()

        destination = input("Enter Destination City : ").strip()

        Menu.display_preference_menu()

        preference_choice = input(
            "\nChoose Preference : "
        ).strip()

        preference = self.get_preference(
            preference_choice
        )

        Menu.display_transport_menu()

        transport_choice = input(
            "\nChoose Transport : "
        ).strip()

        transport = self.get_transport_mode(
            transport_choice
        )

        return TripRequest(

            source=source,

            destination=destination,

            preference=preference,

            transport_mode=transport

        )

    @staticmethod
    def get_preference(choice):

        mapping = {

            "1": "fastest",

            "2": "shortest"

        }

        return mapping.get(

            choice,

            "fastest"

        )

    @staticmethod
    def get_transport_mode(choice):

        mapping = {

            "1": "any",

            "2": "bus",

            "3": "train",

            "4": "flight"

        }

        return mapping.get(

            choice,

            "any"

        )