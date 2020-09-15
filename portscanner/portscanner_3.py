import socket
from IPy import IP
import time

def scan_port(ip_address,port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip_address,port))
        print("[+] Port {} is open.".format(port))
    except:
        print("[+] Port {} is closed.".format(port))

ip_address = input("Enter Target to Scan : ")

for port in range(1,1025):
    scan_port(ip_address,port)
    
print("Programm ist beendet")
