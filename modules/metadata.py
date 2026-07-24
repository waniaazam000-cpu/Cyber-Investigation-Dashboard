"""
metadata.py
---------------------------------------
Cyber Investigation Dashboard

Module:
Metadata Analysis

Supported Files:
- Images (JPG, JPEG, PNG)
- PDF
- DOCX
"""

import os
from pathlib import Path

from utils.file_signature import FileSignature

import exifread
from PIL import Image
from docx import Document
from pypdf import PdfReader

from utils.hashing import generate_all_hashes
from utils.helper import format_file_size, safe_value


class MetadataAnalyzer:
    """
    Metadata Analyzer
    Extracts metadata from supported file types.
    """

    def __init__(self, uploaded_file):
        self.file = uploaded_file
        self.filename = uploaded_file.name
        self.extension = Path(self.filename).suffix.lower()

    def basic_information(self):
        """Return basic information about the uploaded file."""

        self.file.seek(0, os.SEEK_END)
        file_size = self.file.tell()
        self.file.seek(0)

        return {
            "File Name": self.filename,
            "Extension": self.extension,
            "Detected File Type": FileSignature.detect(self.file),
            "File Size": format_file_size(file_size),
            "Hashes": generate_all_hashes(self.file)
        }

    def extract_image_metadata(self):
        """Extract metadata from image files."""

        self.file.seek(0)

        image = Image.open(self.file)

        metadata = {
            "Width": image.width,
            "Height": image.height,
            "Image Format": image.format,
            "Image Mode": image.mode
        }

        self.file.seek(0)

        tags = exifread.process_file(self.file)

        field_mapping = {
            "Image Make": "Camera Brand",
            "Image Model": "Camera Model",
            "EXIF DateTimeOriginal": "Date Taken",
            "Image Software": "Software",
            "GPS GPSLatitude": "GPS Latitude",
            "GPS GPSLongitude": "GPS Longitude",
            "GPS GPSLatitudeRef": "Latitude Reference",
            "GPS GPSLongitudeRef": "Longitude Reference",
            "EXIF LensModel": "Lens Model",
            "EXIF ISOSpeedRatings": "ISO",
            "EXIF ExposureTime": "Exposure Time",
            "EXIF FNumber": "Aperture",
            "EXIF FocalLength": "Focal Length"
        }

        for exif_key, output_key in field_mapping.items():
            metadata[output_key] = safe_value(tags.get(exif_key))

        return metadata

    def extract_pdf_metadata(self):
        """Extract metadata from PDF files."""

        self.file.seek(0)

        reader = PdfReader(self.file)
        info = reader.metadata

        metadata = {
            "Pages": len(reader.pages)
        }

        if info:
            metadata.update({
                "Author": safe_value(info.author),
                "Creator": safe_value(info.creator),
                "Producer": safe_value(info.producer),
                "Title": safe_value(info.title),
                "Subject": safe_value(info.subject),
                "Creation Date": safe_value(info.creation_date),
                "Modified Date": safe_value(info.modification_date)
            })

        return metadata

    def extract_docx_metadata(self):
        """Extract metadata from DOCX files."""

        self.file.seek(0)

        document = Document(self.file)
        props = document.core_properties

        return {
            "Author": safe_value(props.author),
            "Title": safe_value(props.title),
            "Subject": safe_value(props.subject),
            "Category": safe_value(props.category),
            "Comments": safe_value(props.comments),
            "Created": safe_value(props.created),
            "Modified": safe_value(props.modified),
            "Last Modified By": safe_value(props.last_modified_by),
            "Revision": safe_value(props.revision)
        }

    def analyze(self):
        """Detect file type and extract metadata."""

        result = {
            "Basic Information": self.basic_information()
        }

        if self.extension in [".jpg", ".jpeg", ".png"]:
            result["Metadata"] = self.extract_image_metadata()

        elif self.extension == ".pdf":
            result["Metadata"] = self.extract_pdf_metadata()

        elif self.extension == ".docx":
            result["Metadata"] = self.extract_docx_metadata()

        else:
            result["Metadata"] = {
                "Error": "Unsupported file type."
            }

        return result