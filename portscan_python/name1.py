import os
import sys

def double_line():
	print("="*100)

def one_line():
	print("-"*100)

def clear_screen():
	os.system("clear")

clear_screen()

try:

	while True:
		double_line()
		firstName = input("Please enter your first name: ")
		lastName = input("Please enter your last name: ")

		while True:

			try:
				age = int(input("Please enter your age: "))
				one_line()

				if age <= 40:
					print("Your name is {} {} and you are {} years young.".format(firstName,lastName,age))
					double_line()
				else:
					print("Your name is {} {} and you are {} years old.".format(firstName,lastName,age))
					double_line()
				break

			except ValueError:
				print("Please give a number!")

		while True:

			again = input("Again, Please enter y or n : ")

			if again in ["y","n"]:
				break
			else:
				print("Not a valid string!")

		if again == "n":
			break

except KeyboardInterrupt:
	print("\rDetected CRTL+c ... finished Program!")
	sys.exit()

print("The Program is finished!")
double_line()

