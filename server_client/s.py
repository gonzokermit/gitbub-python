import socket

server_ip = "192.168.0.105"
server_port = 55555

#Verbindungs-socket wird erstellt
s = socket.socket()

#Methode bind = binden des socket an eine Adresse
s.bind((server_ip,server_port))

#Methode listen = nach Verbindungsanfragen horchen
s.listen(1)
print("Server {} wartet auf Port {} auf Verbindungen...".format(server_ip,server_port))

#Methode accept = wartet auf eingehende Verbindungsnachfrage und akzeptiert diese
#Tupel = erstes Element = Kommunikationssocket wird für die Kommunikation mit dem verbundenen Client verwendet
#Tupel = zweites Element = Adressobjekt des Clients
comm_socket, address = s.accept()
print("Client {} hat eine Verbindung hergestellt.".format(address))

#Nachricht vom Verbindungspartner wird erwartet und ausgegeben
#Methode recv = Nachricht vom Kommunikationssocket(Client) wird empfangen
"""
nachricht = comm_socket.recv(1024)
print("Nachricht vom Client :: {}".format(nachricht.decode()))

antwort = "Hallo, und ich bin der Server"
comm_socket.send(antwort.encode())
"""

while True:
    empfange_nachricht = comm_socket.recv(1024)
    if empfange_nachricht == "exit":
        comm_socket.close()
        s.close()
        break
    else:
        print("Nachricht vom Client: {}".format(empfange_nachricht.decode()))
        sende_nachricht = input("Versende eine Nachricht: ")
        comm_socket.send(sende_nachricht.encode())
