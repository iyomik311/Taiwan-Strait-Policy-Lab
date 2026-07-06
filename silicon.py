"""
silicon.py

Taiwan Strait Policy Lab
Version 2

Silicon Shield Model
"""


def silicon_shield_score(
    semiconductor,
    interdependence,
    sanctions,
):
    """
    Silicon Shield Index (0~100)

    높을수록 전쟁 억제 효과가 큼

    반도체 의존도 ↑
    경제 상호의존 ↑
    국제 공조(제재 가능성) ↑
    """

    score = 0

    # 글로벌 반도체 의존도
    score += semiconductor * 0.50

    # 경제 상호의존
    score += interdependence * 0.35

    # 국제사회의 대응 가능성
    score += sanctions * 0.15

    score = max(0, min(100, score))

    return round(score, 1)


def shield_level(score):

    if score < 20:
        return "🔴 Very Weak"

    elif score < 40:
        return "🟠 Weak"

    elif score < 60:
        return "🟡 Moderate"

    elif score < 80:
        return "🟢 Strong"

    else:
        return "🟢 Very Strong"


def deterrence_effect(shield_score):
    """
    Silicon Shield가 군사적 억지력에
    기여하는 정도 (0~100)
    """

    effect = shield_score * 0.90

    return round(effect, 1)


def semiconductor_dependency(semiconductor):
    """
    세계 경제의 대만 반도체 의존도
    """

    dependency = semiconductor

    return round(
        max(0, min(100, dependency)),
        1
    )


def global_resilience(
    semiconductor,
    interdependence,
):
    """
    글로벌 공급망 회복력

    공급망 다변화가 부족할수록
    회복력은 낮아짐
    """

    resilience = (
        semiconductor * 0.40
        + interdependence * 0.60
    )

    return round(
        max(0, min(100, resilience)),
        1
    )
