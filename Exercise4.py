# Of two numbers, please, select one with minimum value. Here are several pairs of numbers for thorough testing.

# Input data will contain number of test-cases in the first line.
# Following lines will contain a pair of numbers to compare each.
# For Answer please enter the same amount of minimums separated by space, for example:

#http://www.codeabbey.com/index/task_view/min-of-two

user_input1 = []
user_input2 = []
answer = []

# user_input1.append(input("Enter your first list of numbers, seperated by a comma \t").split(","))
# user_input2.append(input("Enter your first list of numbers, seperated by a comma \t").split(","))

choice1 = 1
choice2 = 1

while choice1 != 2:
	user_input1.append(int(input("Enter your number for the first list: \t")))
	choice1	= int(input("Do you want to add another number? 1)Yes 2)No:\t"))


while choice2 != 2:
	user_input2.append(int(input("Enter your number for the second list: \t")))
	choice2	= int(input("Do you want to add another number? 1)Yes 2)No:\t"))

print(user_input1)
print(user_input2)

for i in range(len(user_input1)):
	if user_input1[i] <= user_input2[i]:
		answer.append(user_input1[i])
	else:
		answer.append(user_input2[i])
print("Lower numbers are:\n")
print(answer)