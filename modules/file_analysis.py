"""
file_analysis.py
---------------------------------------
Cyber Investigation Dashboard

Module:
File Security Analysis

Features:
- File signature detection
- Hash generation
- Extension verification
- Basic risk assessment
"""

from pathlib import Path

from utils.file_signature import FileSignature
from utils.hashing import generate_all_hashes


class FileAnalyzer:
    """
    Performs basic file security analysis.
    """

    def __init__(self, uploaded_file):
        self.file = uploaded_file
        self.filename = uploaded_file.name
        self.extension = Path(self.filename).suffix.lower()


    def check_file_signature(self):
        """
        Detect actual file type from file signature.
        """

        self.file.seek(0)

        detected_type = FileSignature.detect(self.file)

        return {
            "File Extension": self.extension,
            "Detected Type": detected_type
        }


    def generate_hashes(self):
        """
        Generate cryptographic hashes.
        """

        self.file.seek(0)

        return generate_all_hashes(self.file)


    def check_integrity(self):
        """
        Basic integrity check.
        """

        signature = self.check_file_signature()

        extension = signature["File Extension"]
        detected = str(signature["Detected Type"]).lower()


        mismatch = False


        if extension in [".jpg", ".jpeg"] and "jpeg" not in detected:
            mismatch = True

        elif extension == ".png" and "png" not in detected:
            mismatch = True

        elif extension == ".pdf" and "pdf" not in detected:
            mismatch = True

        elif extension == ".docx" and "document" not in detected:
            mismatch = True


        if mismatch:
            return "⚠️ File extension does not match actual file type"

        return "✅ File integrity looks normal"


    def calculate_risk(self):
        """
        Basic risk classification.
        """

        integrity = self.check_integrity()


        if "⚠️" in integrity:
            return "High Risk"

        return "Low Risk"


    def analyze(self):
        """
        Return complete file analysis report.
        """

        return {
            "File Signature": self.check_file_signature(),
            "Hashes": self.generate_hashes(),
            "Integrity Check": self.check_integrity(),
            "Risk Level": self.calculate_risk()
        }