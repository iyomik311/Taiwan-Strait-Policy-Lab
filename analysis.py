"""
analysis.py

Taiwan Strait Policy Lab
Version 2

AI Policy Analysis
"""


def generate_analysis(
    risk,
    shield,
    economic,
):
    """
    AI Policy Brief 생성

    Parameters
    ----------
    risk : float
    shield : float
    economic : float

    Returns
    -------
    str
    """

    report = []

    report.append("# Taiwan Strait Policy Assessment\n")

    # ------------------------
    # Military Assessment
    # ------------------------

    report.append("## Military Assessment")

    if risk >= 80:
        report.append(
            "- Military confrontation is highly likely."
        )
        report.append(
            "- Crisis management should be the highest priority."
        )

    elif risk >= 60:
        report.append(
            "- Regional tensions are elevated."
        )
        report.append(
            "- Deterrence remains important."
        )

    elif risk >= 40:
        report.append(
            "- The security environment is unstable."
        )
        report.append(
            "- Diplomatic engagement is recommended."
        )

    else:
        report.append(
            "- Military escalation risk is relatively low."
        )

    # ------------------------
    # Silicon Shield
    # ------------------------

    report.append("\n## Silicon Shield Assessment")

    if shield >= 80:
        report.append(
            "- Taiwan's semiconductor industry provides a strong deterrent."
        )

    elif shield >= 60:
        report.append(
            "- Semiconductor interdependence contributes to regional stability."
        )

    elif shield >= 40:
        report.append(
            "- The Silicon Shield effect exists but is limited."
        )

    else:
        report.append(
            "- The deterrent effect of the semiconductor industry is weak."
        )

    # ------------------------
    # Economic Assessment
    # ------------------------

    report.append("\n## Economic Assessment")

    if economic >= 80:
        report.append(
            "- A conflict would severely disrupt global trade and supply chains."
        )

    elif economic >= 60:
        report.append(
            "- Significant economic losses are expected."
        )

    elif economic >= 40:
        report.append(
            "- Moderate economic disruption is possible."
        )

    else:
        report.append(
            "- Economic impacts are expected to remain manageable."
        )

    # ------------------------
    # Strategic Outlook
    # ------------------------

    report.append("\n## Strategic Outlook")

    if risk > shield:
        report.append(
            "- Escalation pressures currently outweigh deterrence."
        )
    else:
        report.append(
            "- Deterrence mechanisms remain stronger than escalation pressures."
        )

    # ------------------------
    # Policy Recommendation
    # ------------------------

    report.append("\n## Policy Recommendation")

    if risk >= 70:
        report.append(
            "1. Strengthen diplomatic communication."
        )
        report.append(
            "2. Prevent military miscalculation."
        )
        report.append(
            "3. Coordinate with allies and international organizations."
        )

    elif economic >= 70:
        report.append(
            "1. Diversify supply chains."
        )
        report.append(
            "2. Enhance economic resilience."
        )
        report.append(
            "3. Prepare emergency trade measures."
        )

    else:
        report.append(
            "1. Maintain strategic deterrence."
        )
        report.append(
            "2. Expand economic cooperation."
        )
        report.append(
            "3. Continue diplomatic dialogue."
        )

    return "\n".join(report)
