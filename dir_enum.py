import requests
import logging

def directory_enum(url):
    common_dirs = ['/admin', '/login', '/uploads', '/api', '/dashboard']
    found_dirs = []

    for dir in common_dirs:
        full_url = url.rstrip('/') + dir
        response = requests.get(full_url, timeout=5)
        if response.status_code == 200:
            found_dirs.append(full_url)
            logging.info(f"Found directory: {full_url}")
        else:
            logging.info(f"Directory not found: {full_url}")

    return found_dirs
