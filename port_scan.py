import socket
import concurrent.futures
import logging

def advanced_port_scan(target, ports):
    open_ports = {}

    def check_port(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    service = get_service_name(port)
                    open_ports[port] = service
                    logging.info(f"Port {port} is open on {target} (Service: {service})")
                except Exception as e:
                    logging.error(f"Error getting service name for port {port}: {e}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(check_port, ports)

    return open_ports

def get_service_name(port):
    # Basic service mapping based on common ports
    service_map = {
        21: 'FTP',
        22: 'SSH',
        23: 'Telnet',
        25: 'SMTP',
        53: 'DNS',
        80: 'HTTP',
        443: 'HTTPS',
        110: 'POP3',
        143: 'IMAP'
    }
    return service_map.get(port, 'Unknown')
