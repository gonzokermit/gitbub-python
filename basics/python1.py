#Einfache Beispiele

def line():
    print('=' * 80)
line()

#Start-------------------------
line()
firstName = 'John'
lastName = 'Miller'

print(f'{firstName} {lastName}')
line()
#Ende--------------------------

#Start-------------------------
vorname = input('Vorname: ')
nachname = input('Nachname: ')
alter = int(input('Alter: '))

print(f'Dein Name ist {vorname} {nachname} und du bist {alter} Jahre alt.')
line()
#Ende---------------------------

#Start--------------------------
vorname1 = input('Vorname: ')
nachname1 = input('Nachname: ')
alter1 = int(input('Alter: '))

if alter <= 40:
    print(f'Dein Name ist {vorname1} {nachname1} und du bist {alter1} Jahre jung.')
else:
    print(f'Dein Name ist {vorname1} {nachname1} und du bist {alter1} Jahre alt.')
line()
#Ende----------------------------

#Start--------------------------
for i in range(1,5):
    print(i)
line()

for ip in range(50,53):
    print('192.168.2.' + str(ip))
line()

for ip1 in range(22,24):
    print(f'192.168.55.{ip1}')
line()

ipaddress = input('IP-Address eingeben z.B. 192.168.0.  --- : ')
for last_oktet in range(66,70):
    print(f'{ipaddress}{last_oktet}')
line()
#Ende-----------------------------

#Start-----------------------------
x = 0
while x < 5:
    x+=1
    print(x)

while True:
    nochmal = input('Nochmal j oder n : ')
    if nochmal == 'j':
        print('Und Nochmal!')
    else:
        break
print('ENDE')
line()
#ENDE

#START
sum = 0
zahl = float(input('Erste Zahl: '))
while zahl > 0:
    sum = sum - zahl
    zahl = float(input('Noch eine Zahl: '))
print(f'Das Ergebnis ist {sum}')
#ENDE


