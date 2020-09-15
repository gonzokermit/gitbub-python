import socket
from IPy import IP

def scan_port(ip_address,port):
    try:
        sock = socket.socket()
        sock.connect((ip_address,port))
        print("[+] Port {} is open.".format(port))
    except:
        print("[+] Port {} is closed.".format(port))

ip_address = input("Enter Target to Scan : ")
port = int(input("Enter Port to Scan : "))

scan_port(ip_address,port)


