"""
==================================================
Smart Travel Planning System
Module : Formatter
Author : Nikki
==================================================
"""


class Formatter:

    @staticmethod
    def banner():

        print("\n")
        print("=" * 70)
        print("          SMART TRAVEL PLANNING SYSTEM")
        print("=" * 70)

    @staticmethod
    def heading(title):

        print("\n")
        print("-" * 70)
        print(title.upper())
        print("-" * 70)

    @staticmethod
    def success(message):

        print(f"\n[SUCCESS] {message}")

    @staticmethod
    def error(message):

        print(f"\n[ERROR] {message}")

    @staticmethod
    def line():

        print("-" * 70)