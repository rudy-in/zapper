import requests
import re
from bs4 import BeautifulSoup
import logging

def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        logging.info(f"Successfully fetched {url}")
        return response.content
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

def extract_sensitive_data(content):
    if not content:
        return [], [], []

    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()

    # Extract emails
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

    # Extract potential credentials (e.g., email:password)
    potential_creds = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+:\S+)", text)

    # Find password input fields
    password_fields = soup.find_all('input', {'type': 'password'})

    logging.info(f"Extracted {len(emails)} emails, {len(potential_creds)} credentials, and {len(password_fields)} password fields")

    return emails, potential_creds, password_fields
