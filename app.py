import streamlit as st

from modules.metadata import MetadataAnalyzer
from modules.file_analysis import FileAnalyzer
from modules.footprints import FootprintAnalyzer
from modules.dns_lookup import DNSLookup
from modules.threat_intel import ThreatIntelAnalyzer
from modules.risk_engine import RiskEngine
from modules.report import ReportGenerator
from utils.ip_lookup import get_ip_information

from utils.validators import validate_file


# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="Cyber Investigation Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Cyber Investigation Dashboard")
st.write(
    "Digital Forensics | Metadata Analysis | Threat Intelligence | OSINT"
)

st.divider()

# ==========================================
# WEBSITE INVESTIGATION
# ==========================================

st.header("🌐 Website Investigation (OSINT)")

url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)

footprint_result = {}
dns_result = {}

if url:

    footprint = FootprintAnalyzer(url)

    footprint_result = footprint.analyze()

    st.subheader("Digital Footprint")

    st.write(footprint_result)

    dns = DNSLookup(
        footprint.domain
    )

    dns_result = dns.analyze()

    st.subheader("DNS Analysis")

    st.write(dns_result)

st.divider()

# ==========================================
# FILE INVESTIGATION
# ==========================================

st.header("📁 File Investigation")

uploaded_file = st.file_uploader(
    "Upload File For Investigation",
    type=[
        "jpg",
        "jpeg",
        "png",
        "pdf",
        "docx"
    ]
)

if uploaded_file:

    if validate_file(uploaded_file):

        # ---------------------------------
        # Metadata Analysis
        # ---------------------------------

        st.divider()

        st.header("📄 Metadata Analysis")

        metadata_analyzer = MetadataAnalyzer(
            uploaded_file
        )

        metadata_result = metadata_analyzer.analyze()

        st.subheader("Basic Information")

        for key, value in metadata_result["Basic Information"].items():

            if key == "Hashes":

                st.write("### 🔐 Hash Values")

                for hash_name, hash_value in value.items():

                    st.write(
                        f"**{hash_name}:** {hash_value}"
                    )

            else:

                st.write(
                    f"**{key}:** {value}"
                )

        st.subheader("Extracted Metadata")

        for key, value in metadata_result["Metadata"].items():

            st.write(
                f"**{key}:** {value}"
            )

        # ---------------------------------
        # File Security Analysis
        # ---------------------------------

        st.divider()

        st.header("🛡️ File Security Analysis")

        file_analyzer = FileAnalyzer(
            uploaded_file
        )

        file_result = file_analyzer.analyze()

        for key, value in file_result.items():

            st.write(
                f"**{key}:** {value}"
            )

        # ---------------------------------
        # Threat Intelligence
        # ---------------------------------

        st.divider()

        st.header("🚨 Threat Intelligence")

        threat_analyzer = ThreatIntelAnalyzer(
            uploaded_file
        )

        threat_result = threat_analyzer.generate_report()

        for key, value in threat_result.items():

            st.write(
                f"**{key}:** {value}"
            )

        # ---------------------------------
        # Risk Assessment
        # ---------------------------------

        st.divider()

        st.header("⚠️ Risk Assessment")

        risk = RiskEngine()

        if threat_result["Overall Status"] == "Suspicious":

            risk.add_finding(
                "high",
                "Suspicious File Detected",
                "Perform further malware analysis."
            )

        risk_result = risk.summary()

        for key, value in risk_result.items():

            st.write(
                f"**{key}:** {value}"
            )

        # ---------------------------------
        # Investigation Report
        # ---------------------------------
        st.divider()

        st.header("📑 Investigation Report")

        if st.button("Generate Investigation Report"):

            report = ReportGenerator()

            report_data = report.summary(
                metadata_result,
                footprint_result,
                dns_result,
                file_result,
                threat_result,
                risk_result
            )

            # Generate JSON Report
            json_path = report.generate_json(
                report_data
            )

            # Generate PDF Report
            pdf_path = report.generate_pdf(
                report_data
            )

            st.success(
                "✅ Investigation Report Generated Successfully!"
            )

            st.write("### 📄 JSON Report")
            st.success(json_path)

            st.write("### 📕 PDF Report")
            st.success(pdf_path)

    else:

        st.error(
            "❌ Unsupported or Invalid File."
        )