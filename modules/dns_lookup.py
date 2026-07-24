import dns.resolver


class DNSLookup:

    def __init__(self, domain):
        self.domain = domain

    def lookup(self, record_type):

        try:

            answers = dns.resolver.resolve(
                self.domain,
                record_type
            )

            return [str(answer) for answer in answers]

        except Exception:

            return []

    def analyze(self):

        return {

            "A Records": self.lookup("A"),

            "AAAA Records": self.lookup("AAAA"),

            "MX Records": self.lookup("MX"),

            "NS Records": self.lookup("NS"),

            "TXT Records": self.lookup("TXT"),

            "CNAME Records": self.lookup("CNAME")

        }