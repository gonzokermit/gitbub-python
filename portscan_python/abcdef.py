import socket
import time
import sys
import os
import threading
from datetime import datetime

def double_line():
	print("=" * 100)

def one_line():
	print("-" * 100)

def clear_screen():
	os.system("clear")

def scan_port(target,port):
	try:
		sock = socket.socket()
		sock.settimeout(0.5)
		sock.connect((target,port))
		try:
			version = get_version(sock)
			print("[++] Port {} is open --> {}".format(port,version.decode().strip()))
		except:
			print("[+] Port {} is open".format(port))
	except:
		#print("[-] Port {} is closed".format(port))
		pass

def get_version(sock):
	return sock.recv(1024)

clear_screen()
double_line()

try:
	target = input("Enter target to scan: ")
	target_ip = socket.gethostbyname(target)
	print("Start scan {} with IP {} ... Please wait!".format(target,target_ip))
	one_line()
	start_time = datetime.now()

	for port in range(20,81):
		#scan_port(target,port)
		thread = threading.Thread(target=scan_port, args=(target,port))
		thread.start()
		thread.join(0.7)

	end_time = datetime.now()
	total_time = end_time - start_time

except socket.gaierror:
	print("Not a valid hostname or IP-Address")
except KeyboardInterrupt:
	print("\rDetected CRTL+c ... finish Program!")

one_line()
print("Scan from {} with IP {} is finished in {}".format(target,target_ip,total_time))
