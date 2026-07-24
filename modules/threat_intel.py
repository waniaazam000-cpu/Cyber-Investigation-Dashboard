"""
threat_intel.py
---------------------------------------
Cyber Investigation Dashboard

Module:
Threat Intelligence Analysis

Features:
- Suspicious file indicator checking
- Hash reputation preparation
- URL/domain analysis support
- Threat status generation
"""


import hashlib
from pathlib import Path


class ThreatIntelAnalyzer:
    """
    Basic Threat Intelligence Analyzer.
    
    This module prepares files for threat intelligence checks.
    """


    def __init__(self, uploaded_file):
        self.file = uploaded_file
        self.filename = uploaded_file.name
        self.extension = Path(self.filename).suffix.lower()



    def calculate_sha256(self):
        """
        Generate SHA-256 hash for threat intelligence lookup.
        """

        self.file.seek(0)

        sha256 = hashlib.sha256()

        while True:
            data = self.file.read(4096)

            if not data:
                break

            sha256.update(data)

        self.file.seek(0)

        return sha256.hexdigest()



    def check_file_type(self):
        """
        Basic file type risk check.
        """

        suspicious_extensions = [
            ".exe",
            ".bat",
            ".cmd",
            ".ps1",
            ".vbs",
            ".scr"
        ]


        if self.extension in suspicious_extensions:

            return {
                "Status": "Suspicious",
                "Reason": "Executable or script file detected"
            }


        return {
            "Status": "Normal",
            "Reason": "No suspicious extension detected"
        }



    def analyze_hash(self):
        """
        Prepare hash information for reputation checking.
        """

        file_hash = self.calculate_sha256()

        return {
            "SHA-256": file_hash,
            "Threat Lookup": "Ready for external intelligence check"
        }



    def generate_report(self):
        """
        Generate threat intelligence result.
        """

        file_check = self.check_file_type()

        return {

            "File Name": self.filename,

            "File Type Analysis": file_check,

            "Hash Reputation": self.analyze_hash(),

            "Overall Status": file_check["Status"]

        }