import streamlit as st
import requests

HISTORY_API = "http://127.0.0.1:8000/history"


def show_dashboard():

    st.title("📊 Smart Travel Dashboard")

    try:
        res = requests.get(HISTORY_API, timeout=10)
        data = res.json()

        if not data:
            st.info("No trip data available yet.")
            return

        total_trips = len(data)

        # KPIs
        st.markdown("## Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Trips", total_trips)

        budgets = [t for t in data if t["status"] == "BUDGET_EXCEEDED"]
        col2.metric("Budget Exceeded Trips", len(budgets))

        within = total_trips - len(budgets)
        col3.metric("Within Budget", within)

        # Popular routes
        st.markdown("## 🔥 Recent Trips")

        for i, trip in enumerate(data[:5], 1):
            st.write(
                f"{i}. {trip['source']} → {trip['destination']} | {trip['status']}"
            )

    except Exception as e:
        st.error(f"Error loading dashboard: {str(e)}")