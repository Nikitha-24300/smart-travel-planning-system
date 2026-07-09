import pandas as pd
import plotly.express as px
import requests
import streamlit as st

API_URL = "https://smart-travel-api-nupf.onrender.com/history"


def show_analytics():

    st.title("📊 Travel Analytics")
    st.caption("Insights from your planned trips.")

    try:

        response = requests.get(API_URL, timeout=10)

        if response.status_code != 200:
            st.error("Unable to fetch analytics.")
            return

        trips = response.json()

        if not trips:
            st.info("No trip data available.")
            return

        df = pd.DataFrame(trips)

        if "route" in df.columns:
            df["route"] = df["route"].apply(
                lambda x: " ➜ ".join(x) if isinstance(x, list) else x
            )

        # ================= KPIs =================

        total_trips = len(df)
        avg_distance = round(df["distance"].mean(), 2)
        max_distance = round(df["distance"].max(), 2)
        min_distance = round(df["distance"].min(), 2)

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Trips", total_trips)
        c2.metric("Average Distance", f"{avg_distance} km")
        c3.metric("Longest Trip", f"{max_distance} km")
        c4.metric("Shortest Trip", f"{min_distance} km")

        st.markdown("---")

        # ================= Status =================

        st.subheader("Trip Status")

        status_df = (
            df["status"]
            .value_counts()
            .reset_index()
        )

        status_df.columns = ["Status", "Trips"]

        fig1 = px.pie(
            status_df,
            names="Status",
            values="Trips",
            hole=0.45,
            title="Trip Status Distribution"
        )

        st.plotly_chart(fig1, use_container_width=True)

        # ================= Preference =================

        st.subheader("Preference Distribution")

        pref_df = (
            df["preference"]
            .value_counts()
            .reset_index()
        )

        pref_df.columns = ["Preference", "Trips"]

        fig2 = px.bar(
            pref_df,
            x="Preference",
            y="Trips",
            text="Trips",
            title="Preferred Route Type"
        )

        st.plotly_chart(fig2, use_container_width=True)
        # ================= Distance =================

        st.subheader("Distance of Every Trip")

        trip_df = df.copy()

        trip_df["Trip"] = (
            trip_df["source"]
            + " → "
            + trip_df["destination"]
        )

        fig3 = px.bar(
            trip_df,
            x="Trip",
            y="distance",
            text="distance",
            title="Trip Distance"
        )

        st.plotly_chart(fig3, use_container_width=True)

        # ================= Routes =================

        st.subheader("Most Used Routes")

        route_df = (
            trip_df["Trip"]
            .value_counts()
            .reset_index()
        )

        route_df.columns = ["Route", "Count"]

        fig4 = px.bar(
            route_df,
            x="Count",
            y="Route",
            orientation="h",
            text="Count",
            title="Route Frequency"
        )

        st.plotly_chart(fig4, use_container_width=True)

        st.markdown("---")

        st.subheader("Summary")

        st.success(
            f"""
• Total Trips : {total_trips}

• Average Distance : {avg_distance} km

• Most Frequent Preference : {df['preference'].mode()[0]}

• Most Frequent Status : {df['status'].mode()[0]}
"""
        )

    except Exception as e:
        st.error(f"Analytics Error : {e}")