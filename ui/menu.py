"""
==================================================
Smart Travel Planning System
Module : Console Menu
Author : Nikki
==================================================
"""


class Menu:
    """
    Displays menus used in the console application.
    """

    @staticmethod
    def display_welcome():

        print("\n" + "=" * 60)
        print("      SMART TRAVEL PLANNING SYSTEM")
        print("=" * 60)

    @staticmethod
    def display_main_menu():

        print("\nSelect an option")
        print("------------------------")
        print("1. Plan a Trip")
        print("2. Exit")

    @staticmethod
    def display_preference_menu():

        print("\nRoute Preference")
        print("------------------------")
        print("1. Fastest")
        print("2. Shortest Distance")

    @staticmethod
    def display_transport_menu():

        print("\nTransport Mode")
        print("------------------------")
        print("1. Any")
        print("2. Bus")
        print("3. Train")
        print("4. Flight")