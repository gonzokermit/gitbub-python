import socket
import time
import os
import sys
import threading
import datetime
#from datetime import datetime

def double_line():
	print("="*100)

def one_line():
	print("-"*100)

def clear_screen():
	os.system("clear")

def get_version(sock):
	return sock.recv(1024)

def scan_port(target,port):
	try:
		sock = socket.socket()
		sock.settimeout(0.7)
		sock.connect((target,port))
		try:
			version = get_version(sock)
			print("[+] Port {} is open ==> {}.".format(port,version.decode().strip()))
		except:
			print("[++] Port {} is open.".format(port))
	except:
		#print("[-] Port {} is closed.".format(port))
		pass

clear_screen()

try:
	ports = (21,22,23,25,53,80,139,143,443,445,992,993)

	double_line()
	target = input("Enter Target to Scan: ")
	target_ip = socket.gethostbyname(target)
	print("Start Scan from {} ==> {} ... Please Wait!".format(target_ip,target))
	one_line()
	#start_time = datetime.now()
	start_time = datetime.datetime.now()

	#for port in range(1,1025):
	for port in ports:
		#scan_port(target,port)
		thread = threading.Thread(target=scan_port, args=(target,port))
		thread.start()
		thread.join(1)

except socket.gaierror:
	print("This is not a valid Hostname or IP-Address")
	sys.exit()
except KeyboardInterrupt:
	print("\rCRTL+c detected ... finish Program!")
	sys.exit()

end_time = datetime.datetime.now()
total_time = end_time - start_time

one_line()
print("Scan from {} ==> {} is finished in {}!".format(target,target_ip,total_time))
#print("Scan from {} ==> {} is finished in {}!".format(target,target_ip,total_time.datetime.strftime("%H-%M-%S")))
double_line()
#print(total_time.timedelta().strftime("%H:%M:%S"))
