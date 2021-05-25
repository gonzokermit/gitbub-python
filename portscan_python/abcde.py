import socket
import os
import sys
import time
import threading
from datetime import datetime

def clear_screen():
	os.system("clear")

def double_line():
	print("=" *100)

def one_line():
	print("-" *100)

def get_version(sock):
	return sock.recv(1024)

def scan_port(target,port):
	try:
		sock = socket.socket()
		sock.settimeout(0.5)
		sock.connect((target,port))
		try:
			version = get_version(sock)
			print("[++] Port {} is open --> {}".format(port,version.decode().strip()))
		except:
			print("[-] Port {} is open".format(port))
	except:
		#print("[-] Port {} is closed".format(port))
		pass

clear_screen()
double_line()

try:
	target = input("Enter target to Scan: ")
	target_ip = socket.gethostbyname(target)
	print("Start Scan {} with IP {} ... Please wait!".format(target,target_ip))
	one_line()
	start_time = datetime.now()

	ports = (21,22,23,25,53,80,139,443,455,992,993)
	for port in ports:
	#for port in range(1,101):
		#scan_port(target,port)
		thread = threading.Thread(target=scan_port, args=(target,port))
		thread.start()
		thread.join(0.7)

	end_time = datetime.now()
	total_time = end_time - start_time
except socket.gaierror:
	print("This is not a valid Hostname or IP-Address!")

except KeyboardInterrupt:
	time.sleep(1)
	print("\rDetected CRTL+c ... finished Program")
	sys.exit()

one_line()
print("Scan from {} with IP {} finished in {}".format(target,target_ip,total_time))
double_line()


