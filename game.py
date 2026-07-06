from dataclasses import dataclass


@dataclass
class Strategy:

    name: str
    us_payoff: int
    china_payoff: int


class TaiwanGame:
    """
    Taiwan Strait Policy Lab
    Version 2

    3 × 3 Strategic Game
    """

    US_STRATEGIES = [
        "Strong Deterrence",
        "Strategic Ambiguity",
        "Limited Support"
    ]

    CHINA_STRATEGIES = [
        "Status Quo",
        "Military Pressure",
        "Escalation"
    ]

    def __init__(
        self,
        us_support,
        china_pressure,
        taiwan_position
    ):

        self.us_support = us_support
        self.china_pressure = china_pressure
        self.taiwan_position = taiwan_position

    def payoff_matrix(self):

        us = [
            [8, 6, 2],
            [7, 5, 3],
            [4, 2, 0]
        ]

        china = [
            [5, 6, 9],
            [4, 5, 8],
            [2, 3, 6]
        ]

        # 미국 지원이 높을수록 미국 보상 증가
        bonus = self.us_support * 0.3

        for i in range(3):
            for j in range(3):
                us[i][j] += bonus

        # 중국 압박이 높을수록 중국 보상 증가
        bonus = self.china_pressure * 0.3

        for i in range(3):
            for j in range(3):
                china[i][j] += bonus

        # 대만 독립 성향이 높을수록
        # Status Quo 보상 감소
        penalty = self.taiwan_position * 0.2

        china[0][0] -= penalty
        china[1][0] -= penalty
        china[2][0] -= penalty

        return us, china

    def strategy_names(self):

        return {
            "US": self.US_STRATEGIES,
            "China": self.CHINA_STRATEGIES
        }

    def recommend_strategy(self):

        if self.us_support >= 7:
            us = "Strong Deterrence"

        elif self.us_support >= 4:
            us = "Strategic Ambiguity"

        else:
            us = "Limited Support"

        if self.china_pressure >= 7:
            china = "Escalation"

        elif self.china_pressure >= 4:
            china = "Military Pressure"

        else:
            china = "Status Quo"

        return {

            "US Strategy": us,

            "China Strategy": china

        }from dataclasses import dataclass


@dataclass
class Strategy:

    name: str
    us_payoff: int
    china_payoff: int


class TaiwanGame:
    """
    Taiwan Strait Policy Lab
    Version 2

    3 × 3 Strategic Game
    """

    US_STRATEGIES = [
        "Strong Deterrence",
        "Strategic Ambiguity",
        "Limited Support"
    ]

    CHINA_STRATEGIES = [
        "Status Quo",
        "Military Pressure",
        "Escalation"
    ]

    def __init__(
        self,
        us_support,
        china_pressure,
        taiwan_position
    ):

        self.us_support = us_support
        self.china_pressure = china_pressure
        self.taiwan_position = taiwan_position

    def payoff_matrix(self):

        us = [
            [8, 6, 2],
            [7, 5, 3],
            [4, 2, 0]
        ]

        china = [
            [5, 6, 9],
            [4, 5, 8],
            [2, 3, 6]
        ]

        # 미국 지원이 높을수록 미국 보상 증가
        bonus = self.us_support * 0.3

        for i in range(3):
            for j in range(3):
                us[i][j] += bonus

        # 중국 압박이 높을수록 중국 보상 증가
        bonus = self.china_pressure * 0.3

        for i in range(3):
            for j in range(3):
                china[i][j] += bonus

        # 대만 독립 성향이 높을수록
        # Status Quo 보상 감소
        penalty = self.taiwan_position * 0.2

        china[0][0] -= penalty
        china[1][0] -= penalty
        china[2][0] -= penalty

        return us, china

    def strategy_names(self):

        return {
            "US": self.US_STRATEGIES,
            "China": self.CHINA_STRATEGIES
        }

    def recommend_strategy(self):

        if self.us_support >= 7:
            us = "Strong Deterrence"

        elif self.us_support >= 4:
            us = "Strategic Ambiguity"

        else:
            us = "Limited Support"

        if self.china_pressure >= 7:
            china = "Escalation"

        elif self.china_pressure >= 4:
            china = "Military Pressure"

        else:
            china = "Status Quo"

        return {

            "US Strategy": us,

            "China Strategy": china

        }
