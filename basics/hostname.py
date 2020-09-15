import socket
import os

def line():
    print('='*100)

hostName = (socket.gethostname())
hostIp = (socket.gethostbyname(hostName))

print(f'Hostname = {hostName}')
print(f'IP-Adresse = {hostIp}')
line()

if os.system(f'ping -c 1 {hostIp}') == 0:
    line()
    print(f'Der Hostname {hostName} ist erreichbar')
line()
line()



hostname = input('Hostname: ')
ip = socket.gethostbyname(hostname)
print(f'Der {hostname} hat folgende IP-Adresse {ip}')
line()


