import socket
import sys

server_ip = input("Server IP-Adresse: ")
server_port = int(input("Server-Port: "))

server_socket = socket.socket()

server_socket.bind((server_ip,server_port))
server_socket.listen(1)
print("{} horcht an Port {} nach eingehenden Verbindungen...".format(server_ip,server_port))
client_socket,client_address = server_socket.accept()
print("{} hat an Port {} eine Verbindung hergestellt.".format(client_address[0],client_address[1]))

print("Shell>> ",end="")
while True:
	command = input()
	if command == "exit":
		client_socket.close()
		server_socket.close()
		sys.exit()
	if len(command) > 0:
		client_socket.send(command.encode())
		data = client_socket.recv(8192)
		print(data.decode("utf-8"),end="")

