#Erstes Python Programm

result = 0
zahl = int(input('Erste Zahl: '))
while zahl > 0:
    result = result + zahl
    zahl = int(input('Zahl: '))
print(f'Ergebnis = {result}')

for i in range(6):
    print(i)

for x in range(1, 20, 4):
    print(x)

for nummer in range(10,15):
    print(f'Nr. {nummer}')

for host in range(109, 112):
    print(f'Host Nr. 192.168.55.{host}')

ipstart = int(input('Start IP-Adresse eingeben: '))
ipend = int(input('End IP-Adresse eingeben: '))
for ip in range(ipstart, ipend):
    print(f'192.168.55.{ip}')



    

        


