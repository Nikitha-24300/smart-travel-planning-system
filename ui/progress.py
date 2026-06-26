"""
==================================================
Smart Travel Planning System
Module : Progress Animation
Author : Nikki
==================================================
"""

import time


class Progress:

    @staticmethod
    def loading():

        print("\nSearching best routes", end="")

        for _ in range(5):
            time.sleep(0.4)
            print(".", end="", flush=True)

        print("\n")