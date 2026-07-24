Cyber Investigation Dashboard

Project Overview

Cyber Investigation Dashboard is a Python-based cybersecurity investigation platform developed using Streamlit. It combines digital forensics, metadata analysis, OSINT, threat intelligence, DNS investigation, and risk assessment into a single interactive dashboard.

The project helps investigators analyze uploaded files and websites, generate investigation reports, and identify potential security risks.
link (https://waniaazam000-cpu-ewxa3hrxvqxae3l4ocgmbm.streamlit.app/)

Features

* Metadata Analysis
* File Signature Detection
* MD5, SHA1 & SHA256 Hash Generation
* File Integrity Verification
* Threat Intelligence Analysis
* Risk Assessment Engine
* Digital Footprint Investigation
* WHOIS Lookup
* DNS Record Analysis
* Investigation Report Generation (JSON & PDF)

⸻

Technologies Used

* Python
* Streamlit
* Pillow
* ExifRead
* PyPDF
* python-docx
* python-whois
* dnspython
* Requests
* ReportLab
project structure
Cyber Investigation Dashboard
│
├── app.py
├── modules
│   ├── metadata.py
│   ├── file_analysis.py
│   ├── footprints.py
│   ├── dns_lookup.py
│   ├── threat_intel.py
│   ├── risk_engine.py
│   └── report.py
│
├── utils
│   ├── hashing.py
│   ├── validators.py
│   ├── helper.py
│   └── file_signature.py
│
├── reports
├── README.md
└── requirements.txt


installation
git clone <repository-url>

cd cyber-investigation-dashboard

pip install -r requirements.txt

streamlit run app.py
Supported File Types

* JPG
* JPEG
* PNG
* PDF
* DOCX

⸻

Modules

Metadata Analysis

Extracts metadata from images, PDF files, and Microsoft Word documents.

File Security Analysis

* File signature verification
* Hash generation
* Integrity checking

Digital Footprint

* Domain extraction
* IP lookup
* WHOIS information
* Reverse DNS

DNS Analysis

* A Record
* AAAA Record
* MX Record
* NS Record
* TXT Record
* CNAME Record

Threat Intelligence

Performs basic file reputation preparation and suspicious file detection.

Risk Assessment

Calculates a security risk score and provides recommendations based on findings.

Report Generation

Creates investigation reports in JSON and PDF formats.

⸻

Future Improvements

* VirusTotal API Integration
* Malware Hash Reputation
* SSL Certificate Analysis
* Security Headers Analysis
* Geolocation Mapping
* Machine Learning Risk Prediction

⸻

Author

Wania Azam

BS Cyber Security & Digital Forensics
