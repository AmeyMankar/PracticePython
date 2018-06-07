# You are to write program to convert degrees of Fahrenheit to Celsius.

# Input data contains N+1 values, first of them is N itself (Note that you should not try to convert it).
# Answer should contain exactly N results, rounded to nearest integer and separated by spaces.

# Example:

# data:
# 5 495 353 168 -39 22
# answer:
# 257 178 76 -39 -6

# #http://www.codeabbey.com/index/task_view/fahrenheit-celsius


user_input = []
solution = []
num_of_items = 0
i = 0
choice = 0

choice = int(input("Do you want to convert 1) Farenhite to Celcius 2) Celsius to Farenhite?\t"))
num_of_items = int(input("How many temperatures would you like to convert?:\t"))

for i in range(num_of_items):
	user_input.append(int(input("Please enter a temperature:\t")))
	i += 1

i = 0

for i in range(len(user_input)):
	if choice == 1:
		solution.append(int(((user_input[i]-32)*5)/9))
	else:
		solution.append(int((user_input[i]*9)/5)+32)
	i += 1

print("Solution:\n")
print(solution)