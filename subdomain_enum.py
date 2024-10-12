import socket
import logging

def find_subdomains(domain):
    subdomains = []
    wordlist = ['www', 'mail', 'ftp', 'test', 'dev', 'api', 'blog', 'webmail']
    for sub in wordlist:
        full_domain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full_domain)
            subdomains.append(full_domain)
            logging.info(f"Found subdomain: {full_domain} with IP {ip}")
        except socket.gaierror:
            continue
    return subdomains
