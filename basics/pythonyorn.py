while True:
    firstName = input("Vorname: ")
    lastName = input("Nachname: ")
    while True:
        try:
            age = int(input("Alter: "))
            if age <= 40:
                print("Dein Name ist {} {} und du bist {} Jahre jung.".format(firstName, lastName, age))
            else:
                print("Dein Name ist {} {} und du bist {} Jahre alt.".format(firstName, lastName, age))
            break
        except ValueError:
            print("Bitte ein Zahl eingeben!!!")
    while True:
        again = input("Nochmal ... Bitte y or n eingeben: ")
        if again in ["y","n"]:
            break
        else:
            print("Falsche Eingaben ... Bitte y or n :")
    if again == "n":
        break
print("Programm ist beendet!")