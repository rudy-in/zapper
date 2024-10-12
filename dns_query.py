import dns.resolver
import logging

def dns_query(domain):
    results = {}

    try:
        # A records
        a_records = dns.resolver.resolve(domain, 'A')
        results['A Records'] = [str(record) for record in a_records]

        # MX records
        mx_records = dns.resolver.resolve(domain, 'MX')
        results['MX Records'] = [str(record) for record in mx_records]

        # NS records
        ns_records = dns.resolver.resolve(domain, 'NS')
        results['NS Records'] = [str(record) for record in ns_records]

        logging.info(f"DNS query successful for {domain}")
    except Exception as e:
        logging.error(f"DNS query failed for {domain}: {e}")
        return {}

    return results
