import socket
import time
import sys
import os
import threading
from datetime import datetime

def clear_screen():
	os.system("clear")

def double_line():
	print("=" * 100)

def one_line():
	print("-" * 100)

def get_version(sock):
	return sock.recv(1024)

def scan_port(target,port):
	try:
		sock = socket.socket()
		sock.settimeout(0.7)
		sock.connect((target,port))
		try:
			version = get_version(sock)
			print("[++] Port {} is open ==> {}".format(port,version.decode().strip()))
		except:
			print("[+] Port {} is open".format(port))
	except:
		#print("[-] Port {} is closed".format(port))
		pass

try:
	double_line()
	target = input("Enter Target to Scan: ")
	target_ip = socket.gethostbyname(target)
	print("Start scanning {} ==> {} ... Please Wait!".format(target,target_ip))
	one_line()
	start_time = datetime.now()

	ports = (21,22,23,25,53,80,139,443,445,992,993)
	for port in ports:
		#scan_port(target,port)
		thread = threading.Thread(target=scan_port, args=(target,port))
		thread.start()
		thread.join(1)

	end_time = datetime.now()
	total_time = end_time - start_time

except socket.gaierror:
	print("Not a valid Hostname or IP-Address")
	sys.exit()
except KeyboardInterrupt:
	print("\rDetected CRTL+c ... finished Program!")
	sys.exit()

one_line()
print("Scan from {} ==> {} finished in {}!".format(target,target_ip,total_time))
double_line()
