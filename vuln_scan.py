import requests
import logging

def simple_vuln_scan(url):
    vulnerabilities = []

    # Example checks
    checks = [
        {'path': '/.env', 'desc': 'Check for .env file'},
        {'path': '/backup.zip', 'desc': 'Check for backup zip file'}
    ]

    for check in checks:
        full_url = url.rstrip('/') + check['path']
        response = requests.get(full_url, timeout=5)
        if response.status_code == 200:
            vulnerabilities.append(full_url)
            logging.info(f"Vulnerability found: {check['desc']} at {full_url}")
        else:
            logging.info(f"No vulnerability found for: {check['desc']} at {full_url}")

    return vulnerabilities
