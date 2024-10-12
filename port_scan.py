import nmap
import logging

def port_scan(target, ports):
    nm = nmap.PortScanner()
    open_ports = []

    try:
        nm.scan(target, arguments='-sS -T4 -p ' + ','.join(map(str, ports)))
        for port in ports:
            if nm[target]['tcp'][port]['state'] == 'open':
                open_ports.append(port)
                logging.info(f"Port {port} is open on {target}")
    except Exception as e:
        logging.error(f"Nmap scan failed for {target}: {e}")

    return open_ports
