class FileSignature:

    @staticmethod
    def detect(uploaded_file):

        uploaded_file.seek(0)

        header = uploaded_file.read(32)

        uploaded_file.seek(0)

        image_type = FileSignature._detect_image_type(header)

        if image_type:
            return image_type.upper()

        if header.startswith(b"%PDF"):
            return "PDF"

        if header.startswith(b"PK"):
            return "DOCX / ZIP"

        return "Unknown"

    @staticmethod
    def _detect_image_type(header):

        if header.startswith(b"\xff\xd8\xff"):
            return "jpeg"

        if header.startswith(b"\x89PNG\r\n\x1a\n"):
            return "png"

        if header.startswith(b"GIF87a") or header.startswith(b"GIF89a"):
            return "gif"

        if header[:4] == b"RIFF" and header[8:12] == b"WEBP":
            return "webp"

        if header.startswith(b"BM"):
            return "bmp"

        if header.startswith(b"II*\x00") or header.startswith(b"MM\x00*"):
            return "tiff"

        return None