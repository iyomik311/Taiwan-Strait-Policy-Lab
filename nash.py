"""
nash.py

Taiwan Strait Policy Lab
Version 2
"""

from typing import List, Tuple


def calculate_nash(us_matrix, china_matrix):
    """
    Pure Strategy Nash Equilibrium 계산

    Parameters
    ----------
    us_matrix : list[list]
    china_matrix : list[list]

    Returns
    -------
    list
        [(us_strategy, china_strategy), ...]
    """

    rows = len(us_matrix)
    cols = len(us_matrix[0])

    equilibria = []

    for us in range(rows):

        for china in range(cols):

            us_payoff = us_matrix[us][china]
            china_payoff = china_matrix[us][china]

            # 미국 최적 반응
            us_best = True

            for alt_us in range(rows):

                if us_matrix[alt_us][china] > us_payoff:
                    us_best = False
                    break

            # 중국 최적 반응
            china_best = True

            for alt_china in range(cols):

                if china_matrix[us][alt_china] > china_payoff:
                    china_best = False
                    break

            if us_best and china_best:
                equilibria.append((us, china))

    return equilibria


def format_equilibria(equilibria):

    us_names = [
        "Strong Deterrence",
        "Strategic Ambiguity",
        "Limited Support"
    ]

    china_names = [
        "Status Quo",
        "Military Pressure",
        "Escalation"
    ]

    if len(equilibria) == 0:
        return [
            "No Pure Strategy Nash Equilibrium"
        ]

    result = []

    for us, china in equilibria:

        result.append({
            "US Strategy": us_names[us],
            "China Strategy": china_names[china]
        })

    return result


def print_equilibrium(equilibria):

    formatted = format_equilibria(equilibria)

    print("\n===== Nash Equilibrium =====")

    for eq in formatted:

        if isinstance(eq, str):
            print(eq)

        else:
            print(
                f'US : {eq["US Strategy"]}'
            )
            print(
                f'China : {eq["China Strategy"]}'
            )
            print()
