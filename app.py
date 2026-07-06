import streamlit as st
import pandas as pd

from simulator import TaiwanSimulator
from charts import (
    gauge_chart,
    radar_chart,
    comparison_chart,
    payoff_history,
)

st.set_page_config(
    page_title="Taiwan Strait Policy Lab",
    page_icon="🌏",
    layout="wide",
)

st.title("🌏 Taiwan Strait Policy Lab")
st.caption("Game Theory & International Relations Policy Simulator")

st.divider()

# ==========================
# Sidebar
# ==========================

st.sidebar.header("Policy Settings")

us_support = st.sidebar.slider(
    "🇺🇸 US Military Support",
    0, 10, 5
)

china_pressure = st.sidebar.slider(
    "🇨🇳 China Military Pressure",
    0, 10, 5
)

taiwan_position = st.sidebar.slider(
    "🇹🇼 Taiwan Independence Position",
    0, 10, 5
)

semiconductor = st.sidebar.slider(
    "🌐 Semiconductor Dependence",
    0, 100, 70
)

interdependence = st.sidebar.slider(
    "💰 Economic Interdependence",
    0, 100, 70
)

sanctions = st.sidebar.slider(
    "🌍 International Sanctions",
    0, 100, 50
)

rounds = st.sidebar.slider(
    "Simulation Rounds",
    10,
    500,
    100
)

run = st.sidebar.button("▶ Run Simulation")

# ==========================
# Run
# ==========================

if run:

    simulator = TaiwanSimulator(
        us_support,
        china_pressure,
        taiwan_position,
        semiconductor,
        interdependence,
        sanctions,
    )

    result = simulator.run(rounds)

    # --------------------
    # KPI
    # --------------------

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "📈 Escalation Risk",
        result["Risk"],
        result["Risk Level"]
    )

    c2.metric(
        "🛡 Silicon Shield",
        result["Silicon Shield"],
        result["Shield Level"]
    )

    c3.metric(
        "💸 Economic Cost",
        result["Economic Cost"],
        result["Economic Level"]
    )

    st.divider()

    # --------------------
    # Nash
    # --------------------

    st.subheader("🎲 Nash Equilibrium")

    for eq in result["Nash"]:

        if isinstance(eq, str):
            st.info(eq)

        else:
            st.success(
                f'US : {eq["US Strategy"]}\n\n'
                f'China : {eq["China Strategy"]}'
            )

    # --------------------
    # Analysis
    # --------------------

    st.divider()

    st.subheader("🤖 AI Policy Assessment")

    st.markdown(result["Analysis"])

    # --------------------
    # Gauges
    # --------------------

    st.divider()

    st.subheader("📈 Policy Indicators")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.plotly_chart(
            gauge_chart(
                result["Risk"],
                "Escalation Risk"
            ),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            gauge_chart(
                result["Silicon Shield"],
                "Silicon Shield"
            ),
            use_container_width=True
        )

    with col3:
        st.plotly_chart(
            gauge_chart(
                result["Economic Cost"],
                "Economic Cost"
            ),
            use_container_width=True
        )

    # --------------------
    # Radar
    # --------------------

    st.subheader("Strategic Profile")

    st.plotly_chart(
        radar_chart(result),
        use_container_width=True
    )

    # --------------------
    # Comparison
    # --------------------

    st.subheader("Strategic Indicators")

    st.plotly_chart(
        comparison_chart(result),
        use_container_width=True
    )

    # --------------------
    # History
    # --------------------

    st.subheader("Simulation History")

    st.plotly_chart(
        payoff_history(
            result["History"]
        ),
        use_container_width=True
    )

    df = pd.DataFrame(result["History"])

    st.dataframe(df)

    st.download_button(
        "⬇ Download CSV",
        data=df.to_csv(index=False),
        file_name="taiwan_policy_lab.csv",
        mime="text/csv",
    )

else:

    st.info("Select policy settings and press **Run Simulation**.")
