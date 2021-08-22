import socket

server_ip = "192.168.0.105"
server_port = 55555

#Verbindungs-socket erstellen
s = socket.socket()

#Methode connect verbindet den Client mit dem Server
#Die Methode connect verschickt genau die Verbindungsanfrage, die beim Server durch accept akzeptiert werden kann
s.connect((server_ip,server_port))

"""
nachricht = "Hallo ich bin der Client"
s.send(nachricht.encode())

antwort = s.recv(1024)
print("Antwort vom Server:: {} ".format(antwort.decode()))
"""

while True:
    sende_nachricht = input("Versende eine Nachricht: ")
    s.send(sende_nachricht.encode())

    empfange_nachricht = s.recv(1024)
    print("Nachricht vom Server: {}".format(empfange_nachricht.decode()))