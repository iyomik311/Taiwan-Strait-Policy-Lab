"""
economy.py

Taiwan Strait Policy Lab
Version 2
"""


def calculate_economic_cost(
    risk,
    semiconductor,
    interdependence,
):
    """
    Economic Cost Index (0~100)

    위험도 ↑  -> 경제 피해 증가

    반도체 의존 ↑ -> 전쟁 시 피해 증가

    경제 상호의존 ↑ -> 전쟁 가능성은 감소하지만
                      실제 충돌 시 피해는 매우 큼
    """

    cost = 0

    # 군사적 긴장
    cost += risk * 0.60

    # 글로벌 반도체 공급망
    cost += semiconductor * 0.25

    # 경제 상호의존
    cost += interdependence * 0.30

    return round(max(0, min(100, cost)), 1)


def economic_level(score):

    if score < 20:
        return "🟢 Minimal"

    elif score < 40:
        return "🟢 Low"

    elif score < 60:
        return "🟡 Moderate"

    elif score < 80:
        return "🟠 Severe"

    else:
        return "🔴 Extreme"


def supply_chain_impact(
    semiconductor,
    risk,
):
    """
    반도체 공급망 충격
    """

    impact = (
        semiconductor * 0.70
        + risk * 0.30
    )

    return round(
        max(0, min(100, impact)),
        1
    )


def global_trade_disruption(
    interdependence,
    risk,
):
    """
    세계 무역 교란 지수
    """

    disruption = (
        interdependence * 0.50
        + risk * 0.50
    )

    return round(
        max(0, min(100, disruption)),
        1
    )


def investment_confidence(
    risk,
    sanctions,
):
    """
    투자 신뢰도 (0~100)

    높을수록 투자환경이 양호
    """

    confidence = 100

    confidence -= risk * 0.60
    confidence -= sanctions * 0.20

    return round(
        max(0, min(100, confidence)),
        1
    )
