import json
from pathlib import Path

import requests
import streamlit as st

API_URL = "https://smart-travel-api-nupf.onrender.com/plan-trip"


def load_cities():

    project_root = Path(__file__).resolve().parents[2]
    routes_file = project_root / "data" / "routes.json"

    with open(routes_file, "r", encoding="utf-8") as file:
        routes = json.load(file)

    cities = set()

    for route in routes:
        cities.add(route["source"])
        cities.add(route["destination"])

    return sorted(cities)


def show_plan_trip():

    cities = load_cities()

    st.title("🚆 Smart Travel Planner")
    st.caption("Plan optimized routes using Graph Algorithms and AI.")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        source = st.selectbox(
            "Source City",
            cities
        )

    with col2:

        destinations = [c for c in cities if c != source]

        destination = st.selectbox(
            "Destination City",
            destinations
        )

    col3, col4 = st.columns(2)

    with col3:
        preference = st.selectbox(
            "Optimization",
            [
                "fastest",
                "cheapest",
                "eco",
                "balanced"
            ]
        )

    with col4:
        transport = st.selectbox(
            "Transport Mode",
            [
                "any",
                "bus",
                "train",
                "flight"
            ]
        )

    budget = st.number_input(
        "Maximum Budget (₹)",
        min_value=0.0,
        value=0.0,
        step=100.0
    )

    st.markdown("---")

    if st.button("🚀 Plan Trip"):

        payload = {
            "source": source,
            "destination": destination,
            "preference": preference,
            "transport_mode": transport,
            "max_budget": budget if budget > 0 else None
        }

        try:

            response = requests.post(
                API_URL,
                json=payload,
                timeout=30
            )

            if response.status_code != 200:
                st.error(response.text)
                return

            data = response.json()

            st.success("Trip planned successfully!")

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Distance",
                f"{data['distance']} km"
            )

            c2.metric(
                "Status",
                data["status"]
            )

            c3.metric(
                "Alternative Routes",
                len(data["alternative_routes"])
            )

            st.markdown("---")

            st.subheader("Best Route")

            st.success(
                " ➜ ".join(data["route"])
            )

            metrics = data.get("metrics")

            if isinstance(metrics, dict):

                st.markdown("---")
                st.subheader("Travel Metrics")

                m1, m2, m3, m4 = st.columns(4)

                m1.metric(
                    "Time",
                    f"{metrics['estimated_time']} hrs"
                )

                m2.metric(
                    "Cost",
                    f"₹{metrics['estimated_cost']}"
                )

                m3.metric(
                    "CO₂",
                    f"{metrics['carbon_emission']} kg"
                )

                m4.metric(
                    "Score",
                    metrics["route_score"]
                )

                st.info(
                    f"🌦 Weather : {metrics['weather']} ({metrics['temperature']} °C)"
                )

                st.warning(
                    f"🚦 Traffic : {metrics['traffic_status']}"
                )

                st.info(
                    metrics["recommendation"]
                )

            budget_data = data.get("budget")

            if isinstance(budget_data, dict):

                st.markdown("---")
                st.subheader("Budget Analysis")

                if budget_data["status"] == "WITHIN_BUDGET":
                    st.success("✅ Within Budget")

                elif budget_data["status"] == "NO_BUDGET":
                    st.info("No Budget Specified")

                else:
                    st.error("⚠ Budget Exceeded")

                st.write(
                    f"Estimated Cost : ₹{budget_data['estimated_cost']}"
                )

                st.write(
                    budget_data["recommendation"]
                )

            st.markdown("---")

            st.subheader("Alternative Routes")

            for i, route in enumerate(
                data["alternative_routes"],
                start=1
            ):
                st.write(
                    f"{i}. {' ➜ '.join(route)}"
                )

        except Exception as e:

            st.error(f"API Error : {e}")