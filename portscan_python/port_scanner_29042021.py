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

def get_version(sock):
	return sock.recv(1024)

def scan_again():
	while True:
		again = input("Scan again? // Please enter y or n: ")
		if again in ["y","n"]:
			break
		else:
			print("Not a valid letter // Enter y or n!")
	if again == "n":
		print("--- Program finished ---")
		sys.exit()

def scan_port(target,port):
	try:
		sock = socket.socket()
		sock.settimeout(1.5)
		sock.connect((target,port))
		try:
			version = get_version(sock)
			print("[++] Port {} is open --> {}".format(port,version.decode().strip()))
		except:
			print("[++] Port {} is open".format(port))
	except:
		#print("[--] Port {} is close".format(port))
		pass
while True:
	try:
		clear_screen()
		double_line()
		target = input("Enter the target to scan: ")
		target_ip = socket.gethostbyname(target)
		start_time = datetime.now()
		one_line()

		#for port in range(1,5000):
			#scan_port(target,port)
		ports = (21,22,23,25,53,80,110,111,139,143,443,445,993,995,1723,3389,5900,8080)
		for port in ports:
			thread = threading.Thread(target=scan_port, args=(target,port))
			thread.start()
			thread.join(2.9)

		end_time = datetime.now()
		total_time = end_time - start_time
		one_line()
		print("Scan from {} with IP {} is finished in {}".format(target,target_ip,total_time))
		double_line()

		scan_again()

	except socket.gaierror:
		print("This is not a valid hostname or IP-Address!")
		sys.exit()
	except KeyboardInterrupt:
		print("\rDetected Crtl+c ... finished Program!")
		sys.exit()


