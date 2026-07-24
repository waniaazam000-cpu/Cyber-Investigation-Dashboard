"""
risk_engine.py
---------------------------------------
Cyber Investigation Dashboard

Risk Assessment Engine
"""

from collections import Counter


class RiskEngine:

    def __init__(self):

        self.findings = []

    def add_finding(
        self,
        severity,
        title,
        recommendation
    ):

        self.findings.append(
            {
                "Severity": severity.lower(),
                "Title": title,
                "Recommendation": recommendation
            }
        )

    def summary(self):

        counter = Counter()

        for finding in self.findings:

            counter[finding["Severity"]] += 1

        if counter["high"] > 0:

            overall = "High"

        elif counter["medium"] > 0:

            overall = "Medium"

        elif counter["low"] > 0:

            overall = "Low"

        else:

            overall = "Safe"

        return {

            "Overall Risk": overall,

            "High Findings": counter["high"],

            "Medium Findings": counter["medium"],

            "Low Findings": counter["low"],

            "Findings": self.findings

        }
    