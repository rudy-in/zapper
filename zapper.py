import click
from scraper import scrape_website, extract_sensitive_data
from subdomain_enum import find_subdomains
from port_scan import advanced_port_scan
from dir_enum import directory_enum
from vuln_scan import simple_vuln_scan
from utils import save_results
import logging

# Setup logging
logging.basicConfig(
    filename='recon_tool.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

@click.group()
def cli():
    """Recon Tool CLI - A multi-purpose reconnaissance tool for ethical use."""
    pass

@cli.command()
@click.option('--url', prompt='Target URL', help='The target website URL to scrape.')
@click.option('--output', default='scrape_results.csv', help='Output file to save the results.')
def scrape(url, output):
    """Scrape a website for emails, credentials, and sensitive information."""
    logging.info(f"Starting scraping for {url}")
    content = scrape_website(url)
    emails, creds, passwords = extract_sensitive_data(content)
    results = {
        'url': url,
        'emails': emails,
        'credentials': creds,
        'password_fields': len(passwords)
    }
    save_results(results, output)
    logging.info(f"Scraping completed. Results saved to {output}")
    print(f"Scraping completed. Results saved to {output}")

@cli.command()
@click.option('--domain', prompt='Target Domain', help='The target domain for subdomain enumeration.')
@click.option('--output', default='subdomains.txt', help='Output file to save the subdomains.')
def subdomain(domain, output):
    """Enumerate subdomains of a given domain."""
    logging.info(f"Starting subdomain enumeration for {domain}")
    subdomains = find_subdomains(domain)
    save_results(subdomains, output, is_list=True)
    logging.info(f"Subdomain enumeration completed. Results saved to {output}")
    print(f"Subdomain enumeration completed. Results saved to {output}")

@cli.command()
@click.option('--target', prompt='Target IP or Domain', help='The target IP address or domain to scan.')
@click.option('--ports', default='20,21,22,23,25,53,80,443', help='Comma-separated list of ports to scan.')
@click.option('--output', default='port_scan_results.txt', help='Output file to save the port scan results.')
def scan(target, ports, output):
    """Scan open ports on the target."""
    ports_list = list(map(int, ports.split(',')))
    logging.info(f"Starting advanced port scan for {target} on ports {ports}")
    open_ports = advanced_port_scan(target, ports_list)
    save_results(open_ports, output)
    logging.info(f"Port scanning completed. Results saved to {output}")
    print(f"Port scanning completed. Results saved to {output}")

@cli.command()
@click.option('--url', prompt='Target URL', help='The target website URL for directory enumeration.')
@click.option('--output', default='directories.txt', help='Output file to save found directories.')
def dir_enum(url, output):
    """Enumerate directories on the target URL."""
    logging.info(f"Starting directory enumeration for {url}")
    directories = directory_enum(url)
    save_results(directories, output, is_list=True)
    logging.info(f"Directory enumeration completed. Results saved to {output}")
    print(f"Directory enumeration completed. Results saved to {output}")

@cli.command()
@click.option('--url', prompt='Target URL', help='The target website URL for vulnerability scanning.')
@click.option('--output', default='vulnerabilities.txt', help='Output file for vulnerability results.')
def vuln_scan(url, output):
    """Perform a simple vulnerability scan on the target."""
    logging.info(f"Starting vulnerability scan for {url}")
    vulnerabilities = simple_vuln_scan(url)
    save_results(vulnerabilities, output, is_list=True)
    logging.info(f"Vulnerability scanning completed. Results saved to {output}")
    print(f"Vulnerability scanning completed. Results saved to {output}")

@cli.command()
@click.option('--url', prompt='Target URL', help='The target website URL for comprehensive recon.')
@click.option('--output', default='full_recon_report.json', help='Output file for the full recon report.')
def full(url, output):
    """Perform a full reconnaissance including scraping, subdomain enumeration, port scanning, and directory enumeration."""
    logging.info(f"Starting full recon for {url}")

    # Scraping
    content = scrape_website(url)
    emails, creds, passwords = extract_sensitive_data(content)

    # Subdomain Enumeration
    domain = url.split('//')[-1].split('/')[0]
    subdomains = find_subdomains(domain)

    # Port Scanning
    open_ports = advanced_port_scan(domain, [80, 443])

    # Directory Enumeration
    directories = directory_enum(url)

    # Vulnerability Scan
    vulnerabilities = simple_vuln_scan(url)

    # Compile Results
    results = {
        'url': url,
        'emails': emails,
        'credentials': creds,
        'password_fields': len(passwords),
        'subdomains': subdomains,
        'open_ports': open_ports,
        'directories': directories,
        'vulnerabilities': vulnerabilities
    }

    save_results(results, output)
    logging.info(f"Full recon completed. Results saved to {output}")
    print(f"Full recon completed. Results saved to {output}")

if __name__ == '__main__':
    cli()
