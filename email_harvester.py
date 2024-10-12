import requests
import re
import logging

def harvest_emails(url):
    emails = []
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        text = response.text
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
        logging.info(f"Harvested {len(emails)} emails from {url}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error harvesting emails from {url}: {e}")
    return emails
