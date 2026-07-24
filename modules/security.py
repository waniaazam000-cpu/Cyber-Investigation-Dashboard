import ssl
import socket
import requests
from urllib.parse import urlparse


class SecurityAnalyzer:

    def __init__(self, url):
        self.url = url

        parsed = urlparse(url)

        if parsed.netloc:
            self.domain = parsed.netloc
        else:
            self.domain = parsed.path

    def https_enabled(self):

        return self.url.startswith("https://")

    def security_headers(self):

        try:

            response = requests.get(
                self.url,
                timeout=10,
                allow_redirects=True
            )

            headers = response.headers

            return {

                "HSTS": headers.get(
                    "Strict-Transport-Security",
                    "Missing"
                ),

                "Content Security Policy": headers.get(
                    "Content-Security-Policy",
                    "Missing"
                ),

                "X-Frame-Options": headers.get(
                    "X-Frame-Options",
                    "Missing"
                ),

                "X-Content-Type-Options": headers.get(
                    "X-Content-Type-Options",
                    "Missing"
                ),

                "Referrer Policy": headers.get(
                    "Referrer-Policy",
                    "Missing"
                ),

                "Server": headers.get(
                    "Server",
                    "Unknown"
                )

            }

        except Exception:

            return {
                "Error": "Unable to retrieve headers."
            }

    def ssl_certificate(self):

        try:

            context = ssl.create_default_context()

            with context.wrap_socket(
                socket.socket(),
                server_hostname=self.domain
            ) as s:

                s.settimeout(10)

                s.connect((self.domain, 443))

                certificate = s.getpeercert()

                return {

                    "Issuer": certificate.get("issuer"),

                    "Subject": certificate.get("subject"),

                    "Version": certificate.get("version"),

                    "Valid From": certificate.get("notBefore"),

                    "Valid Until": certificate.get("notAfter")

                }

        except Exception:

            return {

                "Issuer": "Unavailable",

                "Subject": "Unavailable",

                "Version": "Unavailable",

                "Valid From": "Unavailable",

                "Valid Until": "Unavailable"

            }

    def analyze(self):

        return {

            "HTTPS Enabled": self.https_enabled(),

            "Security Headers": self.security_headers(),

            "SSL Certificate": self.ssl_certificate()

        }