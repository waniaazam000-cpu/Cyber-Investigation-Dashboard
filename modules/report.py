"""
report.py
---------------------------------------
Cyber Investigation Dashboard

Investigation Report Generator

Supports:
- JSON Report
- PDF Report
"""

import json
import os
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer


class ReportGenerator:

    def __init__(self):

        self.report_directory = "reports"

        os.makedirs(self.report_directory, exist_ok=True)

    def generate_json(self, data):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"Investigation_Report_{timestamp}.json"

        filepath = os.path.join(
            self.report_directory,
            filename
        )

        with open(filepath, "w", encoding="utf-8") as report:

            json.dump(
                data,
                report,
                indent=4,
                default=str
            )

        return filepath

    def generate_pdf(self, data):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"Investigation_Report_{timestamp}.pdf"

        filepath = os.path.join(
            self.report_directory,
            filename
        )

        document = SimpleDocTemplate(filepath)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>Cyber Investigation Dashboard</b>",
                styles["Title"]
            )
        )

        story.append(
            Paragraph(
                f"Generated: {datetime.now()}",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 20))

        for section, values in data.items():

            story.append(
                Paragraph(
                    f"<b>{section}</b>",
                    styles["Heading2"]
                )
            )

            if isinstance(values, dict):

                for key, value in values.items():

                    story.append(
                        Paragraph(
                            f"{key}: {value}",
                            styles["Normal"]
                        )
                    )

            else:

                story.append(
                    Paragraph(
                        str(values),
                        styles["Normal"]
                    )
                )

            story.append(Spacer(1, 12))

        document.build(story)

        return filepath

    def summary(
        self,
        metadata,
        footprint,
        dns,
        security,
        threat,
        risk
    ):

        report = {

            "Scan Time": datetime.now(),

            "Metadata": metadata,

            "Digital Footprint": footprint,

            "DNS Analysis": dns,

            "Security Analysis": security,

            "Threat Intelligence": threat,

            "Risk Assessment": risk

        }

        return report