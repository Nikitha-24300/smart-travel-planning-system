import streamlit as st

st.set_page_config(
    page_title="Smart Travel System",
    layout="wide"
)

st.title("🚆 Smart Travel Planning System")

menu = st.sidebar.selectbox(
    "Navigation",
    ["Plan Trip", "Trip History"]
)

if menu == "Plan Trip":
    from ui.pages.plan_trip import show_plan_trip
    show_plan_trip()

elif menu == "Trip History":
    from ui.pages.history import show_history
    show_history()