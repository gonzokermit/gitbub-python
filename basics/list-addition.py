friends = ["Kevin", "Karen", "Jim", "2", "Oskar"]
print(friends)
print(friends[0], [4])

names = ["Karsten", "Bob", "Hans"]
for name in names:
    print(name)


def line():
    print("-"*30)
while True:
    result = 0
    zahlen = []
    zahl = float(input("Erste Zahl: "))
    zahlen.append(zahl)
    while zahl > 0:
        result = result + zahl
        zahl = float(input("Naechste Zahl: "))
        line()
        zahlen.append(zahl)
        for x in zahlen:
            print(x)
    line()
    print(f"Das Ergebnis ist {result}")
    while True:
        nochmal = input("Nochmal y oder n : ")
        if nochmal in ["y","n"]:
            break
        else:
            print("Falsche Eingabe, Bitte y oder n : ")
    if nochmal == "n":
        break
print("Das Wars")

