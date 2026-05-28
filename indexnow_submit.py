#!/usr/bin/env python3
"""
IndexNow submission script for Bcom IT Solutions (www.bcomservices.com)
Run this script after publishing new pages or making significant updates.
Bing will crawl the submitted URLs within minutes.

The API_KEY value must match the contents of the .txt file at the repo
root (e.g. {API_KEY}.txt) — Bing fetches that file to verify ownership.

Usage:
    python3 indexnow_submit.py
"""
import json
import urllib.request
import urllib.error

API_KEY = "3d4626b5bf37fa409c81a8349d0e17fe931ceded5724d2591957fd93c7508dbb"
HOST = "www.bcomservices.com"
BASE_URL = "https://www.bcomservices.com"

URLS = [
    f"{BASE_URL}/",
    f"{BASE_URL}/business.html",
    f"{BASE_URL}/home-users.html",
    f"{BASE_URL}/industries.html",
    f"{BASE_URL}/about.html",
    f"{BASE_URL}/contact.html",
    f"{BASE_URL}/support.html",
    f"{BASE_URL}/privacy-policy.html",
    f"{BASE_URL}/terms-and-conditions.html",
    f"{BASE_URL}/it-support-and-services-gold-coast.html",
    f"{BASE_URL}/managed-it-services-for-small-businesses-gold-coast.html",
    f"{BASE_URL}/on-site-technical-support-gold-coast.html",
    f"{BASE_URL}/remote-it-support-gold-coast.html",
    f"{BASE_URL}/it-consulting-strategy-gold-coast.html",
    f"{BASE_URL}/it-needs-assessment-gold-coast.html",
    f"{BASE_URL}/computer-consultant-gold-coast.html",
    f"{BASE_URL}/artificial-intelligence-service-gold-coast.html",
    f"{BASE_URL}/ai-chatbot-gold-coast.html",
    f"{BASE_URL}/ai-voice-agent-gold-coast.html",
    f"{BASE_URL}/microsoft-copilot-gold-coast.html",
    f"{BASE_URL}/microsoft-365-setup-gold-coast.html",
    f"{BASE_URL}/cloud-computing-service-gold-coast.html",
    f"{BASE_URL}/cybersecurity-services-gold-coast.html",
    f"{BASE_URL}/asic-cybersecurity-compliance-gold-coast.html",
    f"{BASE_URL}/iso-42001-ai-governance-gold-coast.html",
    f"{BASE_URL}/hardware-procurement-setup-gold-coast.html",
    f"{BASE_URL}/hardware-software-troubleshooting-gold-coast.html",
    f"{BASE_URL}/software-installation-configuration-gold-coast.html",
    f"{BASE_URL}/software-recommendations-gold-coast.html",
    f"{BASE_URL}/technology-procurement-advice-gold-coast.html",
    f"{BASE_URL}/data-backup-recovery-gold-coast.html",
    f"{BASE_URL}/cybersecurity-health-check-for-small-business-gold-coast.html",
    f"{BASE_URL}/network-security-and-firewall-configuration-gold-coast.html",
    f"{BASE_URL}/virus-and-malware-removal-services-gold-coast.html",
    f"{BASE_URL}/business-wifi-gold-coast.html",
    f"{BASE_URL}/network-cabling-for-offices-gold-coast.html",
    f"{BASE_URL}/phone-line-installation-cabling-gold-coast.html",
    f"{BASE_URL}/telecommunications-contractor-gold-coast.html",
    f"{BASE_URL}/business-phone-systems-gold-coast.html",
    f"{BASE_URL}/voip-phone-system-installation-and-support-gold-coast.html",
    f"{BASE_URL}/pabx-phone-systems-gold-coast.html",
    f"{BASE_URL}/panasonic-pbx-gold-coast.html",
    f"{BASE_URL}/lg-ericsson-pbx-gold-coast.html",
    f"{BASE_URL}/alcatel-lucent-pbx-gold-coast.html",
    f"{BASE_URL}/nec-pbx-gold-coast.html",
    f"{BASE_URL}/nbn-internet-support-gold-coast.html",
    f"{BASE_URL}/network-troubleshooting-diagnostics-gold-coast.html",
    f"{BASE_URL}/it-support-hospitality-gold-coast.html",
    f"{BASE_URL}/it-support-healthcare-gold-coast.html",
    f"{BASE_URL}/it-support-real-estate-gold-coast.html",
    f"{BASE_URL}/it-support-restaurants-gold-coast.html",
    f"{BASE_URL}/it-support-retail-gold-coast.html",
    f"{BASE_URL}/it-support-trades-gold-coast.html",
    f"{BASE_URL}/it-support-small-business-gold-coast.html",
    f"{BASE_URL}/computer-repairs-gold-coast.html",
    f"{BASE_URL}/on-site-computer-repair-gold-coast.html",
    f"{BASE_URL}/os-troubleshooting-repair-gold-coast.html",
    f"{BASE_URL}/performance-optimisation-gold-coast.html",
    f"{BASE_URL}/computer-networking-service-gold-coast.html",
    f"{BASE_URL}/home-wifi-setup-and-troubleshooting-gold-coast.html",
    f"{BASE_URL}/mesh-network-setup-gold-coast.html",
    f"{BASE_URL}/wifi-range-extension-gold-coast.html",
    f"{BASE_URL}/router-and-modem-configuration-gold-coast.html",
    f"{BASE_URL}/ubiquiti-unifi-wifi-gold-coast.html",
    f"{BASE_URL}/tp-link-wifi-gold-coast.html",
    f"{BASE_URL}/netgear-wifi-gold-coast.html",
    f"{BASE_URL}/asus-wifi-gold-coast.html",
    f"{BASE_URL}/synology-wifi-gold-coast.html",
    f"{BASE_URL}/linksys-wifi-gold-coast.html",
    f"{BASE_URL}/d-link-wifi-gold-coast.html",
    f"{BASE_URL}/eero-wifi-gold-coast.html",
    f"{BASE_URL}/google-nest-wifi-gold-coast.html",
    f"{BASE_URL}/grandstream-wifi-gold-coast.html",
    f"{BASE_URL}/aruba-instant-on-wifi-gold-coast.html",
]

def submit():
    payload = {
        "host": HOST,
        "key": API_KEY,
        "keyLocation": f"{BASE_URL}/{API_KEY}.txt",
        "urlList": URLS
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        "https://api.indexnow.org/indexnow",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "IndexNow-Submit/1.0"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            status = response.status
            print(f"Submitted {len(URLS)} URLs to Bing IndexNow")
            print(f"HTTP Status: {status}")
            if status == 200:
                print("Result: URLs accepted immediately")
            elif status == 202:
                print("Result: URLs accepted — crawl scheduled")
            else:
                print(f"Result: Unexpected status {status}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}")
        body = e.read().decode('utf-8', errors='ignore')
        if body:
            print(f"Response: {body}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print(f"IndexNow Submission — bcom ICT")
    print(f"Host: {HOST}")
    print(f"API Key: {API_KEY}")
    print(f"URLs to submit: {len(URLS)}")
    print("-" * 50)
    submit()
