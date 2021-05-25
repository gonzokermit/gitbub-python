try:
	while True:
		first_name = input("Enter your firstname: ")
		last_name = input("Enter your lastname: ")

		while True:
			try:
				age = int(input("Enter your age: "))

				if age <= 40:
					print("Your name is {} {} and you are {} years young.".format(first_name,last_name,age))
				else:
					print("Your name is {} {} and you are {} years old.".format(first_name,last_name,age))
				break

			except ValueError:
				print("This is not a number!!!!")

		while True:
			again = input("Again, please enter y or n : ")
			if again in ["y","n"]:
				break
			else:
				print("Please enter y or n!!!!!")
		if again == "n":
			break

except KeyboardInterrupt:
	print("\rCRTL+c detected ... finish Program!")

print("Program is finished!")

