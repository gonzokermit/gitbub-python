import socket
import sys
import os
import time
import threading
from datetime import datetime

def again():
	while True:
		again = input("Please enter y or n : ")
		if again in ["y","n"]:
			break
		else:
			print("Not a valid letter! Please enter y or n!!!!!")
	if again == "n":
		sys.exit()
		print("The Program is Finished")

def doubleline():
	print("="*100)

def oneline():
	print("-"*100)

def clearscreen():
	os.system("clear")

def get_version(sock):
	return sock.recv(1024)

def scan_port(target,port):
	try:
		sock = socket.socket()
		sock.settimeout(0.2)
		sock.connect((target,port))
		try:
			version = get_version(sock)
			print("[+] Port {} is open --> {}".format(port,version.decode().strip()))
		except:
			print("[+] Port {} is open".format(port))
	except:
		#print("[-] Port {} is closed".format(port))
		pass

clearscreen()
doubleline()

while True:
	try:
		target = input("Enter target to scan: ")
		target_ip = socket.gethostbyname(target)
		oneline()
		print("Start scan {} with IP {} ....Please wait!".format(target,target_ip))
		oneline()
		starttime = datetime.now()

		for port in range(10,81):
			#scan_port(target,port)
			thread = threading.Thread(target=scan_port, args=(target,port))
			thread.start()
			thread.join(0.5)

		endtime = datetime.now()
		totaltime = endtime - starttime

		oneline()
		print("Scan from {} with IP {} finished in {}".format(target,target_ip,totaltime))
		doubleline()
		again()

	except socket.gaierror:
		print("Not a valid hostname or IP-Address")
		again()
	except KeyboardInterrupt:
		print("\rDetected Crtl+c ... finished Program!")
		sys.exit()












