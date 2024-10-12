import whois
import logging

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        result = {
            'Domain Name': w.domain_name,
            'Registrar': w.registrar,
            'Whois Server': w.whois_server,
            'Creation Date': w.creation_date,
            'Expiration Date': w.expiration_date,
            'Updated Date': w.updated_date,
            'Name Servers': w.name_servers,
            'Email': w.emails,
        }
        logging.info(f"Whois lookup successful for {domain}")
        return result
    except Exception as e:
        logging.error(f"Whois lookup failed for {domain}: {e}")
        return {}
