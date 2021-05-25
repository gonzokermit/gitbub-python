en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow" : "gelb"}
print(en_de)

colour = input("Farbe ? ")

if colour in en_de:
	print("Die Farbe {} ist ein Schlüssel".format(colour))
	print("Der deutsche Wert für {} ist {}".format(colour,en_de[colour]))
else:
	print("Die Farbe {} ist kein Schlüssel".format(colour))
	print("Der deutsche Wert für {} ist ?".format(colour))
	en_de[colour] = "brown" : "braun"
	print("Nun kennen wir auch die Farbe {}".format(colour))
	print(en_de)


