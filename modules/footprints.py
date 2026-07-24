"""
footprints.py
---------------------------------------
Cyber Investigation Dashboard

Module:
Digital Footprint Analysis

Features:
- Domain extraction
- IP lookup
- WHOIS information
- IP geolocation
- Cloud provider detection
- Reverse DNS
"""

import socket
import whois
import requests

from urllib.parse import urlparse


class FootprintAnalyzer:

    def __init__(self, url):
        self.url = url
        self.domain = self.extract_domain()

    def extract_domain(self):

        parsed = urlparse(self.url)

        if parsed.netloc:
            domain = parsed.netloc
        else:
            domain = parsed.path

        domain = domain.replace("www.", "")

        return domain

    def get_ip(self):

        try:
            return socket.gethostbyname(self.domain)

        except Exception:
            return "Not Available"

    def get_whois(self):

        try:

            data = whois.whois(self.domain)

            return {

                "Registrar": data.registrar,

                "Creation Date": str(data.creation_date),

                "Expiration Date": str(data.expiration_date),

                "Updated Date": str(data.updated_date),

                "Name Servers": data.name_servers

            }

        except Exception:

            return {

                "Registrar": "Not Available",

                "Creation Date": "Not Available",

                "Expiration Date": "Not Available",

                "Updated Date": "Not Available",

                "Name Servers": "Not Available"

            }

    def get_ip_information(self):

        ip = self.get_ip()

        if ip == "Not Available":

            return {

                "IP Address": "Not Available"

            }

        try:

            response = requests.get(
                f"https://ipinfo.io/{ip}/json",
                timeout=5
            )

            info = response.json()

            org = info.get("org", "Unknown")

            cloud = "No"

            providers = [

                "Amazon",
                "AWS",
                "Google",
                "Azure",
                "Microsoft",
                "Cloudflare",
                "Oracle",
                "Alibaba",
                "DigitalOcean",
                "Linode",
                "OVH",
                "Vultr"

            ]

            for provider in providers:

                if provider.lower() in org.lower():

                    cloud = provider

                    break

            return {

                "IP Address": ip,

                "Hostname": info.get("hostname", "Unknown"),

                "City": info.get("city", "Unknown"),

                "Region": info.get("region", "Unknown"),

                "Country": info.get("country", "Unknown"),

                "Postal Code": info.get("postal", "Unknown"),

                "Location": info.get("loc", "Unknown"),

                "Timezone": info.get("timezone", "Unknown"),

                "Organization": org,

                "ASN": org,

                "Cloud Provider": cloud,

                "VPN / Proxy": "Unknown",

                "Abuse Contact": "Not Available"

            }

        except Exception as e:

            return {

                "IP Address": ip,

                "Error": str(e)

            }

    def reverse_dns(self):

        try:

            ip = self.get_ip()

            return socket.gethostbyaddr(ip)[0]

        except Exception:

            return "Not Available"

    def analyze(self):

        return {

            "Target Domain": self.domain,

            "Resolved IP": self.get_ip(),

            "WHOIS Information": self.get_whois(),

            "IP Information": self.get_ip_information(),

            "Reverse DNS": self.reverse_dns()

        }