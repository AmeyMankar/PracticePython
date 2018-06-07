# Now we are given several pairs of values and we want to calculate sum for each pair.

# Input data will contain the total count of pairs to process in the first line.
# The following lines will contain pairs themselves - one pair at each line.
# Answer should contain the results separated by spaces.

#http://www.codeabbey.com/index/task_view/sums-in-loop

choice = 1
user_input = []
total_sum = 0

while choice != 2:
	user_input.append(input("Please enter a pair of values, seperated by a comma:\t").split(","))
	choice = int(input("Do you want to add another pair? 1)Yes 2)No:\t"))

for pair in user_input:
	print(pair)
	for item in pair:
		total_sum += int(item)
	print("Total sum: \t"+str(total_sum))
	total_sum = 0
