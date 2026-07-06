"""
simulator.py

Taiwan Strait Policy Lab
Version 2
"""

import random

from game import TaiwanGame
from nash import calculate_nash, format_equilibria
from risk import (
    calculate_risk,
    risk_level,
    deterrence_index,
    security_dilemma,
)
from economy import (
    calculate_economic_cost,
    economic_level,
    supply_chain_impact,
    global_trade_disruption,
    investment_confidence,
)
from silicon import (
    silicon_shield_score,
    shield_level,
    deterrence_effect,
    global_resilience,
)
from analysis import generate_analysis


class TaiwanSimulator:

    def __init__(
        self,
        us_support,
        china_pressure,
        taiwan_position,
        semiconductor,
        interdependence,
        sanctions,
    ):

        self.us_support = us_support
        self.china_pressure = china_pressure
        self.taiwan_position = taiwan_position
        self.semiconductor = semiconductor
        self.interdependence = interdependence
        self.sanctions = sanctions

        self.game = TaiwanGame(
            us_support,
            china_pressure,
            taiwan_position,
        )

    def run(self, rounds=100):

        us_matrix, china_matrix = self.game.payoff_matrix()

        us_total = 0
        china_total = 0

        history = []

        for _ in range(rounds):

            us = random.randint(0, 2)
            china = random.randint(0, 2)

            us_score = us_matrix[us][china]
            china_score = china_matrix[us][china]

            us_total += us_score
            china_total += china_score

            history.append(
                {
                    "Round": len(history) + 1,
                    "US Strategy": self.game.US_STRATEGIES[us],
                    "China Strategy": self.game.CHINA_STRATEGIES[china],
                    "US Payoff": us_score,
                    "China Payoff": china_score,
                }
            )

        # ------------------------
        # Strategic Indicators
        # ------------------------

        risk = calculate_risk(
            self.us_support,
            self.china_pressure,
            self.taiwan_position,
            self.sanctions,
            self.semiconductor,
        )

        shield = silicon_shield_score(
            self.semiconductor,
            self.interdependence,
            self.sanctions,
        )

        economy = calculate_economic_cost(
            risk,
            self.semiconductor,
            self.interdependence,
        )

        deterrence = deterrence_index(
            self.us_support,
            self.sanctions,
        )

        dilemma = security_dilemma(
            self.us_support,
            self.china_pressure,
        )

        supply = supply_chain_impact(
            self.semiconductor,
            risk,
        )

        trade = global_trade_disruption(
            self.interdependence,
            risk,
        )

        confidence = investment_confidence(
            risk,
            self.sanctions,
        )

        resilience = global_resilience(
            self.semiconductor,
            self.interdependence,
        )

        shield_effect = deterrence_effect(
            shield
        )

        # ------------------------
        # Nash Equilibrium
        # ------------------------

        equilibria = calculate_nash(
            us_matrix,
            china_matrix,
        )

        # ------------------------
        # AI Analysis
        # ------------------------

        analysis = generate_analysis(
            risk,
            shield,
            economy,
        )

        return {

            "US Total": round(us_total, 2),
            "China Total": round(china_total, 2),

            "US Average": round(us_total / rounds, 2),
            "China Average": round(china_total / rounds, 2),

            "Risk": risk,
            "Risk Level": risk_level(risk),

            "Silicon Shield": shield,
            "Shield Level": shield_level(shield),

            "Economic Cost": economy,
            "Economic Level": economic_level(economy),

            "Deterrence Index": deterrence,
            "Security Dilemma": dilemma,

            "Supply Chain Impact": supply,
            "Trade Disruption": trade,

            "Investment Confidence": confidence,
            "Global Resilience": resilience,

            "Shield Effect": shield_effect,

            "Nash": format_equilibria(equilibria),

            "Analysis": analysis,

            "History": history,
        }
