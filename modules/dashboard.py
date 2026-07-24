"""
dashboard.py
---------------------------------------
Cyber Investigation Dashboard
Dashboard Module
"""

import streamlit as st


class Dashboard:

    def __init__(self):
        pass

    def show_header(self):

        st.title("🛡️ Cyber Investigation Dashboard")

        st.caption(
            "Metadata Analysis | Digital Footprint | Threat Intelligence | DFIR"
        )

        st.divider()

    def show_scan_information(self):

        st.subheader("📌 Investigation Overview")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Metadata", "Completed")

        with col2:
            st.metric("Security", "Completed")

        with col3:
            st.metric("Threat Intelligence", "Completed")

    def show_metadata(self, metadata):

        st.subheader("📂 Metadata Analysis")

        if not metadata:
            st.info("No metadata available.")
            return

        st.json(metadata)

    def show_footprint(self, footprint):

        st.subheader("🌐 Digital Footprint")

        if not footprint:
            st.info("No digital footprint available.")
            return

        st.json(footprint)

    def show_dns(self, dns):

        st.subheader("🌍 DNS Lookup")

        if not dns:
            st.info("No DNS records found.")
            return

        st.json(dns)

    def show_security(self, security):

        st.subheader("🔒 Website Security")

        if not security:
            st.info("No security analysis available.")
            return

        st.json(security)

    def show_threat(self, threat):

        st.subheader("🚨 Threat Intelligence")

        if not threat:
            st.info("No threat intelligence available.")
            return

        st.json(threat)

    def show_risk(self, risk):

        st.subheader("⚠️ Risk Assessment")

        if not risk:
            st.info("No risk assessment available.")
            return

        st.json(risk)

    def show_recommendations(self, recommendations):

        st.subheader("💡 Recommendations")

        if not recommendations:
            st.success("No recommendations available.")
            return

        for recommendation in recommendations:
            st.write(f"• {recommendation}")

    def show_footer(self):

        st.divider()

        st.caption(
            "Cyber Investigation Dashboard | Developed for SOC, DFIR & Cybersecurity Investigations"
        )