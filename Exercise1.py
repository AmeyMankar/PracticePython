# Exercise1

# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

import datetime

name = input("Enter your name: ")
age = input("Enter your age: ")
looping = input("How many times you want to repeat the output?")
i = 1

if(name.isalpha()):
	if(age.isdigit()):
		if(looping.isdigit()):
			while i <= int(looping):
				print("You will be 100 years old in "+str(100-int(age))+" years i.e. in "+ str(datetime.datetime.now().year+(100-int(age))))
				i += 1
else:
	print("Incorrect input. Please try again")




