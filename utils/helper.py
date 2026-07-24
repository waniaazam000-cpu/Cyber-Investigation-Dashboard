"""
helper.py
-------------------------
Common helper functions used across the project.
"""

from datetime import datetime


def format_file_size(size_bytes):
    """
    Convert file size into a readable format.
    """

    if size_bytes < 1024:
        return f"{size_bytes} Bytes"

    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"

    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB"

    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"


def current_scan_time():
    """
    Return current scan date and time.
    """

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def get_risk_level(score):
    """
    Convert numerical score into a risk level.
    """

    if score <= 20:
        return "🟢 Low"

    elif score <= 50:
        return "🟡 Medium"

    elif score <= 80:
        return "🟠 High"

    return "🔴 Critical"


def yes_no(value):
    """
    Convert Boolean values to Yes/No.
    """

    return "Yes" if value else "No"


def safe_value(value):
    """
    Replace empty values with 'Not Available'.
    """

    if value is None:
        return "Not Available"

    if str(value).strip() == "":
        return "Not Available"

    return str(value)


def investigation_note(field):
    """
    Explain why a metadata field matters.
    """

    notes = {

        "GPS": "May reveal where the file was created.",

        "Camera Model": "May identify the device used.",

        "Author": "May reveal document ownership.",

        "Creation Date": "Useful during forensic investigations.",

        "Modified Date": "Helps build an investigation timeline.",

        "Software": "Shows which application created or edited the file.",

        "SHA256": "Unique fingerprint used to verify file integrity."
    }

    return notes.get(field, "No investigation note available.")