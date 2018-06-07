# Let us find the sum of several numbers (more than two). It will be useful to do this in a loop.
#http://www.codeabbey.com/index/task_view/sum-in-loop


user_input = []
sum_of_numbers = 0
choice=1

while choice != 2:
	user_input.append(int(input("Please enter your number: \t")))
	choice = int(input("Do you want to add more numbers: 1) Yes 2) No: \t"))

for item in user_input:
	sum_of_numbers += item

print("Total sum of numbers is:\t"+str(sum_of_numbers))

