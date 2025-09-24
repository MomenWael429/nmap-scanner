# nmap_scanner

Small Python script that uses `python-nmap` to scan an IP range and print hosts, their state, and open TCP ports.

**Warning:** Only scan networks you own or have permission to test.

## Requirements
- Python 3.6+
- `nmap` installed on your system
- Python package: `python-nmap` (`pip install python-nmap`)

## Usage
```bash
sudo python3 nmap_scanner.py <IP_RANGE>
a venv will be needed and if it doesn't work do the following while in the venv:
1. which python
2. sudo <path given by the which python command> nmap_scanner.py <ip_range>
