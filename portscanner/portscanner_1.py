import socket
from IPy import IP
import time

ip_address = input("Enter Target to Scan : ")
port = 80

try:
    sock = socket.socket()
    sock.connect((ip_address,port))
    print("Port {} is open".format(port))
except:
    print("Port {} is closed".format(port))

