import requests


def get_ip_information(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        
        response = requests.get(url)
        data = response.json()

        if data["status"] == "success":
            return {
                "country": data.get("country", "N/A"),
                "city": data.get("city", "N/A"),
                "region": data.get("regionName", "N/A"),
                "isp": data.get("isp", "N/A"),
                "asn": data.get("as", "N/A"),
                "organization": data.get("org", "N/A")
            }

        else:
            return {
                "error": data.get("message", "Unable to fetch IP information")
            }

    except Exception as e:
        return {
            "error": str(e)
        }