import pandas as pd
import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/history"


def show_history():

    st.title("📜 Trip History")
    st.caption("View all previously planned trips.")

    try:

        response = requests.get(API_URL, timeout=10)

        if response.status_code != 200:
            st.error("Unable to fetch trip history.")
            return

        trips = response.json()

        if not trips:
            st.info("No trips planned yet.")
            return

        df = pd.DataFrame(trips)

        if "route" in df.columns:
            df["route"] = df["route"].apply(
                lambda x: " ➜ ".join(x) if isinstance(x, list) else x
            )

        st.metric("Total Trips", len(df))

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            status_filter = st.selectbox(
                "Filter by Status",
                ["All"] + sorted(df["status"].unique().tolist())
            )

        with col2:
            preference_filter = st.selectbox(
                "Filter by Preference",
                ["All"] + sorted(df["preference"].unique().tolist())
            )

        filtered_df = df.copy()

        if status_filter != "All":
            filtered_df = filtered_df[
                filtered_df["status"] == status_filter
            ]

        if preference_filter != "All":
            filtered_df = filtered_df[
                filtered_df["preference"] == preference_filter
            ]

        st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

        st.download_button(
            label="📥 Download History (CSV)",
            data=filtered_df.to_csv(index=False),
            file_name="trip_history.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"API Error : {e}")