import socket
from IPy import IP
import os
import sys
import threading
from datetime import datetime

def double_line():
    print("="*100)

def one_line():
    print("-"*100)

def get_version(sock):
    return sock.recv(1024)

def scan_port(target,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((target,port))
        try:
            version = get_version(sock)
            print("[+] Port {} is open ==> {}".format(port,version.decode().strip()))
        except:
            print("[+] Port {} is open!".format(port))
    except:
        #print("[+] Port {} is closed".format(port))
        pass

try:
    os.system("clear")
    double_line()
    target = input("Enter Target to Scan: ")
    target_ip = socket.gethostbyname(target)
    one_line()
    print("Start scan Ports 1-1024 from IP-Adress {} ==> Hostname {} ...".format(target_ip,target))
    start_time = datetime.now()
    one_line()
    #end_time = datetime.now()

    for port in range(1,1025):
        #scan_port(target,port)
        thread = threading.Thread(target=scan_port,args=(target,port))
        thread.start()
        thread.join(0.1)

except KeyboardInterrupt:
    print("\rDetected CRTL + c ....  ==> Program finished!")
    sys.exit(0)
except socket.gaierror:
    print("Not valid Hostname!")
    sys.exit(0)

end_time = datetime.now()
total_time = end_time - start_time
one_line()
print("Scan of IP-Address {} ==> Hostname {} finished in {} !".format(target,target_ip,total_time))
double_line()