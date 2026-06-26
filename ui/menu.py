"""
==================================================
Smart Travel Planning System
Module : Console Menu
Author : Nikki
==================================================
"""

from ui.formatter import Formatter


class Menu:

    @staticmethod
    def display_welcome():

        Formatter.banner()

    @staticmethod
    def display_main_menu():

        Formatter.heading("Main Menu")

        print("1. Plan Trip")
        print("2. Exit")

    @staticmethod
    def display_preference_menu():

        Formatter.heading("Route Preference")

        print("1. Fastest")
        print("2. Shortest Distance")

    @staticmethod
    def display_transport_menu():

        Formatter.heading("Transport Mode")

        print("1. Any")
        print("2. Bus")
        print("3. Train")
        print("4. Flight")