import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/history"


def show_history():

    st.title("📜 Trip History")

    try:
        res = requests.get(API_URL, timeout=10)

        if res.status_code != 200:
            st.error("Failed to fetch history")
            return

        data = res.json()

        if not data:
            st.info("No trips found yet.")
            return

        st.success(f"Total Trips: {len(data)}")

        for i, trip in enumerate(data, 1):

            with st.container():

                st.markdown("---")

                st.subheader(f"Trip {i}")

                col1, col2, col3 = st.columns(3)

                col1.metric("Source", trip.get("source"))
                col2.metric("Destination", trip.get("destination"))
                col3.metric("Status", trip.get("status"))

                st.write("**Route:**", " → ".join(trip.get("route", [])))
                st.write(f"Distance: {trip.get('distance')} km")
                st.write(f"Preference: {trip.get('preference')}")

    except Exception as e:
        st.error(f"API Error: {str(e)}")