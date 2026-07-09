import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Smart Travel Planning System",
    page_icon="🚆",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown(
    """
    <style>

    .main-title{
        text-align:center;
        font-size:42px;
        font-weight:bold;
        color:#1f77b4;
    }

    .sub-title{
        text-align:center;
        color:gray;
        margin-bottom:20px;
    }

    section[data-testid="stSidebar"]{
        background-color:#f7f9fc;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# HEADER
# ==========================================

st.markdown(
    "<div class='main-title'>🚆 Smart Travel Planning System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Intelligent Route Optimization using Graph Algorithms, Real-Time APIs, and Multi-Criteria Decision Making</div>",
    unsafe_allow_html=True
)

st.markdown("---")

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "🏠 Plan Trip",
        "📜 Trip History",
        "📊 Analytics"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("System Status : Online")

st.sidebar.info(
    """
Features

• AI Route Planning

• Budget Analysis

• Live Weather

• Live Maps

• Traffic Analysis

• Travel Analytics
"""
)

# ==========================================
# ROUTING
# ==========================================

if page == "🏠 Plan Trip":

    from pages.plan_trip import show_plan_trip

    show_plan_trip()

elif page == "📜 Trip History":

    from pages.history import show_history

    show_history()

elif page == "📊 Analytics":

    from pages.analytics import show_analytics

    show_analytics()