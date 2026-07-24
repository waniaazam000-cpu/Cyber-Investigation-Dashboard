"""
hashing.py
-------------------------
Generate cryptographic hashes for uploaded files.

Supported Hashes:
- MD5
- SHA1
- SHA256
"""

import hashlib


CHUNK_SIZE = 8192


def calculate_hash(file, algorithm):
    """
    Calculate hash for an uploaded file.

    Parameters:
        file: Uploaded file object
        algorithm: hashlib algorithm

    Returns:
        Hexadecimal hash string
    """

    hash_object = algorithm()

    file.seek(0)

    while True:
        chunk = file.read(CHUNK_SIZE)

        if not chunk:
            break

        hash_object.update(chunk)

    file.seek(0)

    return hash_object.hexdigest()


def get_md5(file):
    """
    Return MD5 hash.
    """
    return calculate_hash(file, hashlib.md5)


def get_sha1(file):
    """
    Return SHA1 hash.
    """
    return calculate_hash(file, hashlib.sha1)


def get_sha256(file):
    """
    Return SHA256 hash.
    """
    return calculate_hash(file, hashlib.sha256)


def generate_all_hashes(file):
    """
    Generate all supported hashes.

    Returns:
        Dictionary containing:
        - MD5
        - SHA1
        - SHA256
    """

    return {
        "MD5": get_md5(file),
        "SHA1": get_sha1(file),
        "SHA256": get_sha256(file)
    }