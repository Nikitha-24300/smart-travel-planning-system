import streamlit as st

st.set_page_config(
    page_title="Smart Travel Planner",
    page_icon="🚆",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🚆 Smart Travel System")
menu = st.sidebar.radio(
    "Navigation",
    ["Plan Trip", "Trip History"]
)

st.sidebar.markdown("---")
st.sidebar.info("AI-powered route optimization system")

# ---------------- ROUTING ----------------
if menu == "Plan Trip":
    from ui.pages.plan_trip import show_plan_trip
    show_plan_trip()

elif menu == "Trip History":
    from ui.pages.history import show_history
    show_history()