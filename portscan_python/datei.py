print("Kurswerte")

try:
	while True:
		print("Bitte erst das Datum und dann mit einem Leerzeichen den Kurswert eintragen!")
		date = input("Eingabe:  ")

		file = open("boerse.txt", "a") 
		file.write("\r{}\n".format(date))
		file.close()
		file = open("boerse.txt", "r")
		for line in file:
			word = line.strip()
			print(word)
		file.close()
		while True:
			again = input("Nochmal, Bitte y or n eingeben: ")
			if again in ["y","n"]:
				break
			else:
				print("Falsche Eingabe, Bitte y oder n eingeben!")
		if again == "n":
			break
	print("Program finished!")
except KeyboardInterrupt:
		print("\rDetected CRTL+c ... Finished Program!")
