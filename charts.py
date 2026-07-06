"""
charts.py

Taiwan Strait Policy Lab
Version 2
"""

import plotly.graph_objects as go
import plotly.express as px


def gauge_chart(value, title):
    """게이지 차트"""

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": title},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "darkblue"},
                "steps": [
                    {"range": [0, 20], "color": "#2ecc71"},
                    {"range": [20, 40], "color": "#a3e635"},
                    {"range": [40, 60], "color": "#f1c40f"},
                    {"range": [60, 80], "color": "#e67e22"},
                    {"range": [80, 100], "color": "#e74c3c"},
                ],
            },
        )
    )

    fig.update_layout(height=320)

    return fig


def radar_chart(result):
    """레이더 차트"""

    labels = [
        "Risk",
        "Shield",
        "Economy",
        "Deterrence",
        "Resilience",
    ]

    values = [
        result["Risk"],
        result["Silicon Shield"],
        result["Economic Cost"],
        result["Deterrence Index"],
        result["Global Resilience"],
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=labels,
            fill="toself",
            name="Simulation",
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
            )
        ),
        showlegend=False,
        height=450,
    )

    return fig


def comparison_chart(result):
    """막대그래프"""

    labels = [
        "Risk",
        "Shield",
        "Economy",
        "Deterrence",
        "Trade",
    ]

    values = [
        result["Risk"],
        result["Silicon Shield"],
        result["Economic Cost"],
        result["Deterrence Index"],
        result["Trade Disruption"],
    ]

    fig = px.bar(
        x=labels,
        y=values,
        text=values,
    )

    fig.update_layout(
        height=420,
        xaxis_title="Indicator",
        yaxis_title="Score",
    )

    return fig


def payoff_history(history):
    """누적 보상 그래프"""

    rounds = []
    us = []
    china = []

    us_total = 0
    china_total = 0

    for i, row in enumerate(history):

        us_total += row["US Payoff"]
        china_total += row["China Payoff"]

        rounds.append(i + 1)
        us.append(us_total)
        china.append(china_total)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=rounds,
            y=us,
            mode="lines",
            name="US",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=rounds,
            y=china,
            mode="lines",
            name="China",
        )
    )

    fig.update_layout(
        title="Accumulated Payoff",
        xaxis_title="Round",
        yaxis_title="Total Payoff",
        height=450,
    )

    return fig
