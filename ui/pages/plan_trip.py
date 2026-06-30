import streamlit as st

from models.trip_request import TripRequest
from services.application_controller import ApplicationController

controller = ApplicationController()


def show_plan_trip():

    st.header("🗺️ Plan Your Trip")

    col1, col2 = st.columns(2)

    with col1:
        source = st.text_input("Source City", "Hyderabad")

    with col2:
        destination = st.text_input("Destination City", "Chennai")

    preference = st.selectbox(
        "Preference",
        ["fastest", "cheapest", "eco", "balanced"]
    )

    transport = st.selectbox(
        "Transport Mode",
        ["any", "bus", "train", "flight"]
    )

    if st.button("Plan Trip"):

        request = TripRequest(
            source=source,
            destination=destination,
            preference=preference,
            transport_mode=transport
        )

        response = controller.plan_trip(request)

        st.success("Trip Planned Successfully!")

        # -------------------------
        # KPI DASHBOARD CARDS
        # -------------------------
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Distance (km)", response.total_distance)

        with col2:
            st.metric("Status", response.status)

        with col3:
            st.metric("Routes Found", len(response.alternative_routes))

        # -------------------------
        # BEST ROUTE
        # -------------------------
        st.subheader("🏆 Best Route")

        st.markdown(
            f"<h3 style='color:#00C853'>{' → '.join(response.shortest_path)}</h3>",
            unsafe_allow_html=True
        )

        # -------------------------
        # ALTERNATIVE ROUTES
        # -------------------------
        st.subheader("🔀 Alternative Routes")

        for i, route in enumerate(response.alternative_routes, 1):
            st.write(f"**{i}.** {' → '.join(route)}")

        # -------------------------
        # STATUS
        # -------------------------
        st.subheader("📌 System Status")

        if response.status == "SUCCESS":
            st.success(response.message)
        else:
            st.error(response.message)