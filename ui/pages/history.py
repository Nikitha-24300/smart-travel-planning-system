import streamlit as st
import sqlite3
import pandas as pd


def show_history():

    st.header("📊 Trip History")

    conn = sqlite3.connect("travel.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT source, destination, route, total_distance, preference, status
        FROM trips
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        st.warning("No trips found.")
        return

    df = pd.DataFrame(
        rows,
        columns=[
            "Source",
            "Destination",
            "Route",
            "Distance",
            "Preference",
            "Status"
        ]
    )

    st.dataframe(df, width="stretch", hide_index=True)