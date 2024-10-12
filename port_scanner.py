import socket
import threading
from scapy.all import IP,TCP,sr1,UDP,ICMP

HOST = input("Enter IP Address: ")

print("The Port Scanner performs several types of scans")
print("Choose from these Options:")
print("1) TCP Scan")
print("2) SYN Scan")
print("3) UDP Scan")
OPTION = input("Enter Scan Option: ")

OPTIONS = ['1', '2', '3']

if OPTION not in OPTIONS:
    exit()


def tcp_scan(PORT):
    SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCKET.settimeout(5)
    if SOCKET.connect_ex((HOST, PORT)) == 0:
        print(f"The Port {PORT} is Open")
        SOCKET.settimeout(5)
        try:
            data = SOCKET.recv(1024)
            print(f"Data Received from PORT {PORT}:\n ", data)
        except socket.timeout:
            print(f"No Data Received from PORT {PORT}")
        finally:
            SOCKET.close()


def syn_scan(PORT):
    ip_packet = IP(dst=HOST)
    tcp_packet = TCP(dport=PORT, flags="S")
    
    response = sr1(ip_packet/tcp_packet, timeout=2, verbose=0)
    
    if response is None:
        print(f"The Port {PORT} is Filtered")
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:
            print(f"The Port {PORT} is Open.")
            reset_packet = ip_packet/TCP(dport=PORT, flags="R")
            sr1(reset_packet, timeout=1, verbose=0)


def udp_scan(PORT):
    ip_packet = IP(dst=HOST)
    udp_packet = UDP(dport=PORT)

    response = sr1(ip_packet/udp_packet, timeout=2, verbose=0)
    
    if response is None:
        print(f"The Port {PORT} is Filtered")
    elif response.haslayer(UDP):
        print(f"The Port {PORT} is Open")
    elif response.haslayer(ICMP):
        icmp_type = response.getlayer(ICMP).type
        icmp_code = response.getlayer(ICMP).code

        if icmp_type == 3 and icmp_code in [1, 2, 9, 10, 13]:
            print(f"The Port {PORT} is Filtered") 


def port_Scanner():
    threads = []
    for PORT in range(0,1024):
        if OPTION == '1':
            thread = threading.Thread(target=tcp_scan, args=(PORT,))
        elif OPTION == '2':
            thread = threading.Thread(target=syn_scan, args=(PORT,))
        elif OPTION == '3':
            thread = threading.Thread(target=udp_scan, args=(PORT,))

        threads.append(thread)
        thread.start() 

    for thread in threads:
        thread.join()

port_Scanner()