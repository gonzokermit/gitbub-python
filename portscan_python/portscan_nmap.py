import socket
import os
import sys

def doubleline():
	print("=" * 100)

def host_discovery(network):
	os.system("sudo nmap -sn {}".format(network))

def stealth_scan(target):
	os.system("sudo nmap -sS {}".format(target))

def version_scan(target):
	os.system("sudo nmap -sV {}".format(target))

while True:
	os.system("clear")

	print("----- Portscanner Choise -----")
	print("")
	print("Host Discovery         ==>        1")
	print("TCP Syn Stealth Scan   ==>        2")
	print("Version Scan           ==>        3")
	print("")
	print("END                    ==>        0")
	print("")

	try:
		choise = int(input("What do you want scan ? "))
		print("-" * 100)
		if choise == 1:
			network = input("Enter Network to Scan: ")
			host_discovery(network)
		elif choise == 2:
			target = input("Enter Target to Scan: ")
			stealth_scan(target)
		elif choise == 3:
			target = input("Enter Target to Scan: ")
			version_scan(target)
		elif choise == 0:
			break
		else:
			print("Please enter Number !!!!")
	except ValueError:
		print("This is not a valid Number!")
	except KeyboardInterrupt:
		print("\r CRTL detected ... FINISH\n")
		break

	while True:
		doubleline()
		again = input("You want run this Program again -- Please enter y or n : ")
		if again in ["y","n"]:
			break
		else:
			print("Please Enter y or n !!!!")
	if again == "n":
		break

print("Program is finished")

