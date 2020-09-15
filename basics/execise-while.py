def line():
    print('-'*100)

zaehler = 0
people = []

while zaehler <= 3:
        name = input('Write a Name to the list : ')
        people.append(name)
        zaehler = zaehler + 1

line()
print('In the list are: ')
print(', ' .join(people))
line()
print(*people, sep = ', ')



line()

result = 0
zahlen = []

print('Bei Eingabe der Zahl 0 wird das Ergebnis berechnet.')
zahl = int(input('Erste Zahl: '))
zahlen.append(zahl)

while zahl > 0:
    result = result + zahl
    zahl = int(input('Naechste Zahl: '))
    zahlen.append(zahl)

print('---Einfache Ausgabe---')
print(zahlen)
print(result)

print('---Formatierte Ausgabe---')
print(str(zahlen)[1:-1])
print(f'Ergebnis = {result}')

print('---Formatierte Ausgabe---')
print('Das Ergebnis von ' ,(str(zahlen)[1:-2]), 'ist' ,result)
