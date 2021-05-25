import socket
import os
import sys
import time
import threading
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
			print("[++] Port {} is open. ==> {}".format(port,version.decode().strip()))
		except:
			print("[+] Port {} is open.".format(port))
	except:
		#print("[-] Port {} is closed.".format(port))
		pass
try:
	#ports = (21,22,25,53,80,143,139,443,445,992,993)

	target = input("Enter Target to Scan: ")
	target_ip = socket.gethostbyname(target)
	print("Start Scan Ports from {} ==> {} Please Wait ...!".format(target,target_ip))

	start_time = datetime.now()

	for port in range(1,1025):
	#for port in ports:
		#scan_port(target,port)
		thread = threading.Thread(target=scan_port, args=(target,port))
		thread.start()
		thread.join(1)

	end_time = datetime.now()
	total_time = end_time - start_time

except socket.gaierror:
	print("Not a valid Hostname or IP-Address!")
	sys.exit()
except KeyboardInterrupt:
	print("\rDetected CRTL+c ... finish Programm!")
	sys.exit()

print("Scanning Ports from {} ==> {} is finished in {}!".format(target,target_ip,total_time))
