import socket
#from IPy import IP
import ipaddress
import time

def scan_port(target,port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((target,port))
        print("Port {} is open".format(port))
    except:
        print("Port {} is closed".format(port))

while True:
    try:
        target = input("Enter Target to Scan : ")
        ipaddress.ip_address(target)
        print("IP-Address is ok!")
        for port in range(77,88):
            scan_port(target,port)
        break
    except ValueError:
        print("This is not a valid IP-Address!!!!!")
    
print("Program is finished")
