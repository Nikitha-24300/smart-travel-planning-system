import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/plan-trip"


def show_plan_trip():

    # ---------------- HEADER ----------------
    st.markdown(
        """
        <h1 style='text-align:center; color:#1f77b4;'>
        🚆 Smart Travel Planner
        </h1>
        <p style='text-align:center; color:gray;'>
        Plan optimized routes with AI intelligence
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # ---------------- INPUT CARD ----------------
    with st.container():

        st.subheader("📍 Trip Details")

        col1, col2 = st.columns(2)

        with col1:
            source = st.text_input("Source City", "Hyderabad")

        with col2:
            destination = st.text_input("Destination City", "Chennai")

        col3, col4 = st.columns(2)

        with col3:
            preference = st.selectbox(
                "Preference",
                ["fastest", "cheapest", "eco", "balanced"]
            )

        with col4:
            transport = st.selectbox(
                "Transport Mode",
                ["any", "bus", "train", "flight"]
            )

        budget = st.number_input(
            "Max Budget (optional)",
            min_value=0.0,
            value=0.0
        )

    st.markdown("---")

    # ---------------- BUTTON ----------------
    if st.button("🚀 Plan My Trip", use_container_width=True):

        payload = {
            "source": source,
            "destination": destination,
            "preference": preference,
            "transport_mode": transport,
            "max_budget": budget if budget > 0 else None
        }

        try:
            res = requests.post(API_URL, json=payload, timeout=30)

            if res.status_code != 200:
                st.error(f"API Error: {res.text}")
                return

            data = res.json()

            st.success("Trip Planned Successfully!")

            # ================= KPI CARDS =================
            st.markdown("## 📊 Trip Overview")

            k1, k2, k3 = st.columns(3)

            k1.metric("Distance (km)", data.get("total_distance"))
            k2.metric("Status", data.get("status"))
            k3.metric("Routes Found", len(data.get("alternative_routes", [])))

            st.markdown("---")

            # ================= BEST ROUTE =================
            st.markdown("## 🏆 Best Route")

            st.markdown(
                f"""
                <div style="
                    padding:15px;
                    border-radius:10px;
                    background-color:#f0f2f6;
                    font-size:18px;
                    font-weight:bold;
                    text-align:center;">
                    {' → '.join(data.get("route", []))}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("---")

            # ================= METRICS =================
            metrics = data.get("metrics") or {}

            if metrics:

                st.markdown("## 📈 Travel Analytics")

                c1, c2, c3, c4 = st.columns(4)

                c1.metric("Time (hrs)", metrics.get("estimated_time"))
                c2.metric("Cost (₹)", metrics.get("estimated_cost"))
                c3.metric("CO₂ (kg)", metrics.get("carbon_emission"))
                c4.metric("Score", metrics.get("route_score"))

                c5, c6 = st.columns(2)

                c5.metric("Road Distance", metrics.get("real_distance"))
                c6.metric("Drive Time", metrics.get("real_duration"))

                st.markdown("### 🌦 Weather Conditions")
                st.info(f"{metrics.get('weather')} | {metrics.get('temperature')}°C")

                st.markdown("### 🚦 Traffic Status")
                st.warning(
                    f"{metrics.get('traffic_status')} (Factor: {metrics.get('traffic_factor')})"
                )

            # ================= BUDGET =================
            budget_data = data.get("budget") or {}

            if budget_data:

                st.markdown("## 💰 Budget Analysis")

                if budget_data.get("status") == "WITHIN_BUDGET":
                    st.success("✅ Within Budget")
                else:
                    st.error("⚠️ Budget Exceeded")

                b1, b2, b3 = st.columns(3)

                b1.metric("Budget", f"₹{budget_data.get('max_budget')}")
                b2.metric("Cost", f"₹{budget_data.get('estimated_cost')}")
                b3.metric("Exceeded", f"₹{budget_data.get('exceeded_amount')}")

                st.info(f"💡 {budget_data.get('recommendation')}")

            # ================= ALTERNATIVES =================
            st.markdown("## 🔀 Alternative Routes")

            for i, route in enumerate(data.get("alternative_routes", []), 1):
                st.write(f"**{i}.** {' → '.join(route)}")

            st.markdown("---")
            st.success("🎯 Trip planning completed successfully!")

        except Exception as e:
            st.error(f"API Connection Error: {str(e)}")