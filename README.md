# Port Scanner

## Overview
The Port Scanner is a Python-based network scanning tool that allows users to perform various types of port scans on a specified IP address. It supports TCP scans, SYN scans, and UDP scans, helping users to identify open ports and determine the status of the services running on a target machine.

## Features
- **TCP Scan**: Identifies open TCP ports on the target machine.
- **SYN Scan**: Performs a stealthy SYN scan to determine the state of TCP ports.
- **UDP Scan**: Scans for open UDP ports and checks their status.

## Technologies Used
- Python
- Scapy (for packet crafting and sending)
- Socket (for TCP connection attempts)
- Threading (to perform concurrent scans)

## Getting Started

### Prerequisites
To run this project, ensure you have the following installed:
- Python 3.x
- Scapy library (can be installed via pip)
- Basic networking knowledge

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/pola-k/port-scanner.git
   ```
   
2. Change into the project directory:
   ```bash
   cd port-scanner
   ```

3. Install the required dependencies:
   ```bash
   pip install scapy
   ```

### Usage
1. Run the script:
   ```bash
   python port_scanner.py
   ```

2. When prompted, enter the IP address of the target machine you want to scan.

3. Choose the type of scan you want to perform:
   - **1** for TCP Scan
   - **2** for SYN Scan
   - **3** for UDP Scan

4. The results of the scan will be displayed in the terminal, indicating which ports are open, filtered, or unresponsive.

### Example
```bash
Enter IP Address: 192.168.1.1
The Port Scanner performs several types of scans
Choose from these Options:
1) TCP Scan
2) SYN Scan
3) UDP Scan
Enter Scan Option: 1
The Port 80 is Open
Data Received from PORT 80: <data>
```

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and commit them with a descriptive message.
4. Push your branch and open a pull request.

## Disclaimer
**Use this tool responsibly and only on networks you have permission to scan. Unauthorized scanning can be considered illegal and unethical.**

---
