import imghdr


class FileSignature:

    @staticmethod
    def detect(uploaded_file):

        uploaded_file.seek(0)

        image_type = imghdr.what(uploaded_file)

        uploaded_file.seek(0)

        if image_type:
            return image_type.upper()

        header = uploaded_file.read(8)

        uploaded_file.seek(0)

        if header.startswith(b"%PDF"):
            return "PDF"

        if header.startswith(b"PK"):
            return "DOCX / ZIP"

        return "Unknown"