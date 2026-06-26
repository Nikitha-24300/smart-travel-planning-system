from models.trip_request import TripRequest
from services.application_controller import ApplicationController


def main():
    controller = ApplicationController()

    request = TripRequest(
        source="Hyderabad",
        destination="Chennai",
        preference="fastest"
    )

    response = controller.plan_trip(request)

    print("\n===== SMART TRAVEL PLANNING SYSTEM =====")

    print("\nShortest Route")
    print(" -> ".join(response.shortest_path))

    print(f"\nDistance : {response.total_distance} km")

    print("\nAlternative Routes")

    for route in response.alternative_routes:
        print(" -> ".join(route))


if __name__ == "__main__":
    main()