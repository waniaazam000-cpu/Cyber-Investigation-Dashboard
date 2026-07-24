"""
validators.py
-------------------------
Validation functions for uploaded files.
This module helps protect the application by checking:
- File extension
- File size
- Safe filename
"""

import os
from pathlib import Path

# Allowed file extensions
ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".pdf",
    ".docx"
}

# Maximum file size (20 MB)
MAX_FILE_SIZE = 20 * 1024 * 1024


def is_allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    """
    extension = Path(filename).suffix.lower()
    return extension in ALLOWED_EXTENSIONS


def is_file_size_valid(file):
    """
    Check whether uploaded file size is within the allowed limit.
    """
    current_position = file.tell()
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(current_position)

    return size <= MAX_FILE_SIZE


def get_file_extension(filename):
    """
    Return the file extension.
    """
    return Path(filename).suffix.lower()


def sanitize_filename(filename):
    """
    Remove potentially dangerous characters from filenames.
    """
    safe_name = Path(filename).name
    safe_name = safe_name.replace(" ", "_")
    return safe_name


def validate_file(file):
    """
    Perform complete validation.
    Returns:
        (True, "File is valid")
        or
        (False, "Reason")
    """

    filename = sanitize_filename(file.name)

    if not is_allowed_file(filename):
        return False, "Unsupported file type."

    if not is_file_size_valid(file):
        return False, "File exceeds the maximum size (20 MB)."

    return True, "File is valid."