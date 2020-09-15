#Portscan with Threading

import socket
from IPy import IP
import time
import threading

def scan_port(ip_address,port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip_address,port))
        print("[+] Port {} is open.".format(port))
    except:
        #print("[+] Port {} is closed.".format(port))
        pass

ip_address = input("Enter Target to Scan : ")

for port in range(1,1025):
    thread = threading.Thread(target = scan_port, args = (ip_address,port))
    thread.start()

time.sleep(2)

print("Programm is finished!")

