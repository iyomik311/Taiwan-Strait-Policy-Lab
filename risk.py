"""
risk.py

Taiwan Strait Policy Lab
Version 2
"""


def calculate_risk(
    us_support,
    china_pressure,
    taiwan_position,
    sanctions,
    semiconductor,
):
    """
    Escalation Risk Index (0~100)

    국제정치학 이론 기반

    ↑ 중국 압박
    ↑ 대만 독립 성향

    ↓ 미국 억지력
    ↓ 국제 제재
    ↓ Silicon Shield
    """

    # 기본 위험
    risk = 40

    # 중국 군사 압박
    risk += china_pressure * 5

    # 대만 독립 성향
    risk += taiwan_position * 3

    # 미국 억지력
    risk -= us_support * 3

    # 국제 제재
    risk -= sanctions * 0.15

    # Silicon Shield
    risk -= semiconductor * 0.12

    # 범위 제한
    risk = max(0, min(100, risk))

    return round(risk, 1)


def risk_level(score):

    if score < 20:
        return "🟢 Very Low"

    elif score < 40:
        return "🟢 Low"

    elif score < 60:
        return "🟡 Moderate"

    elif score < 80:
        return "🟠 High"

    else:
        return "🔴 Critical"


def deterrence_index(
    us_support,
    sanctions,
):
    """
    억지력(0~100)

    미국 군사 지원과 국제 제재가
    억지력을 높인다고 가정
    """

    score = (
        us_support * 8
        + sanctions * 0.4
    )

    return round(
        max(0, min(100, score)),
        1
    )


def security_dilemma(
    us_support,
    china_pressure,
):
    """
    안보딜레마 지수

    양국의 군사적 행동이
    동시에 커질수록 긴장 상승
    """

    score = (
        us_support
        * china_pressure
    )

    score *= 1.2

    return round(
        max(0, min(100, score)),
        1
    )
