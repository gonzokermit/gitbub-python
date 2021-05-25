import socket
import os
import sys
import threading
import time
from datetime import datetime

def get_version(sock):
	return sock.recv(1024)

def scan_port(target,port):
	try:
		sock = socket.socket()
		sock.settimeout(0.7)
		sock.connect((target,port))
		try:
			version = get_version(sock)
			print("[++] Port {} is open ==> {}.".format(port,version.decode().strip()))
		except:
			print("[+] Port {} is open.".format(port))
	except:
		#print("[-] Port {} is closed.".format(port))
		pass

try:
	target = input("Enter Target to Scan: ")
	target_ip = socket.gethostbyname(target)
	print("Start Scan Ports from {} with IP-Address {}...".format(target,target_ip))
	start_time = datetime.now()

	for port in range(1,90):
		#scan_port(target,port)
		thread = threading.Thread(target=scan_port, args=(target,port))
		thread.start()
		thread.join(1)

except socket.gaierror:
	print("Not a valid Hostname or IP-Address!")
	sys.exit()
except KeyboardInterrupt:
	print("\rDetected CRTL+c ... finish Programm!")
	sys.exit()

end_time = datetime.now()
total_time = end_time - start_time

print("Scan {} ==> {} finished in {}".format(target,target_ip,total_time))
