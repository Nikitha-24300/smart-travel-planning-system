"""
Central dependency container (Singleton-style)
Prevents multiple controller/service instances
"""

from services.application_controller import ApplicationController

_controller = None


def get_controller():
    global _controller

    if _controller is None:
        _controller = ApplicationController()

    return _controller