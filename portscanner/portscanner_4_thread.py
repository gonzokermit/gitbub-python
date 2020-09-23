import socket
import time
import threading
import os

def doubleline():
    print("="*100)

def get_banner(sock):
    return sock.recv(1024)

def scan_port(target,port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((target,port))
        try:
            banner = get_banner(sock)
            print("[+] Port {} is open on {} {} ==> {}".format(port,target_ip,target,banner.decode().strip()))
        except:
            print("[+] Port {} is open on {} {}.".format(port,target_ip,target))
        
        open_ports.append(port)
    except:
        #print("[+] Port {} is closed.".format(port))
        pass

open_ports = []

os.system("clear")

target = input("Enter Target to Scan: ")
target_ip = socket.gethostbyname(target)
print("")
print("Hostname {} with IP-Address {} scan Ports 1-1024 ...".format(target,target_ip))
print("")

for port in range(1,1025):
    #scan_port(target,port)
    thread = threading.Thread(target=scan_port,args=(target,port))
    thread.start()
    thread.join(0.2)

doubleline()
print("Scan done : {}".format(target_ip))
print("Summary of open Ports ==> {} ".format(open_ports))