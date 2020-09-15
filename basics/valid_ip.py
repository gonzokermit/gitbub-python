import ipaddress

try:
    target = input("IP: ")
    ipaddress.ip_address(target)
    print("IP is ok")
except ValueError:
    print("IP is not valid")