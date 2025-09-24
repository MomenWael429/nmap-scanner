#!/usr/bin/env python3

import nmap
import sys

def scan_network(ip_range):
    print(f"[+] Starting Nmap scan on {ip_range}...\n")

    scanner = nmap.PortScanner()

    try:
        scanner.scan(hosts=ip_range, arguments='-T4 -F')  # Fast scan (-F), normal timing (-T4)

        for host in scanner.all_hosts():
            print(f"Host: {host} ({scanner[host].hostname()})")
            print(f"  State: {scanner[host].state()}")

            if 'tcp' in scanner[host]:
                print("  Open Ports:")
                for port in scanner[host]['tcp']:
                    print(f"    Port {port}: {scanner[host]['tcp'][port]['name']} ({scanner[host]['tcp'][port]['state']})")
            print("-" * 40)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sudo python3 nmap_scanner.py <IP_RANGE>")
        print("Example: sudo python3 nmap_scanner.py 192.168.1.0/24")
        sys.exit(1)

    ip_range = sys.argv[1]
    scan_network(ip_range)
