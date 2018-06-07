# You will be again given triplets of numbers, but now the middle of them should be chosen - i.e. not the largest and not the smallest one. Such number is called the Median (of the set, array etc).

# Be sure, this problem is not simply "another stupid exercise" - it is used as a part in powerful QuickSort algorithm, for example.

# Input data will contain in the first line the number of triplets to follow.
# Next lines will contain one triplet each.
# Answer should contain selected medians of triplets, separated by spaces.

# Example:

# data:
# 3
# 7 3 5
# 15 20 40
# 300 550 137

# answer:
# 5 20 300
# #http://www.codeabbey.com/index/task_view/median-of-three


list_of_lists = []
user_input = []
solution = []
i = 0
j = 0
num_of_lists = 0
num_of_items = 0
median = 0

num_of_lists = int(input("How many lists do you need?:\t"))
num_of_items = int(input("How many items do you need?:\t"))

for i in range(num_of_lists):
	print("List ",i+1)
	for j in range(num_of_items):
		user_input.append(input("Please enter a number:\t"))
		j += 1
	i += 1
	j = 0
	list_of_lists.append(user_input)
	user_input = []

print(list_of_lists)

for list in list_of_lists:
	list.sort()
	if (len(list) % 2) != 0:
		median = list[int(len(list) / 2)]
	else:
		median = (int(list[int(len(list) / 2)]) + int(list[int(len(list) / 2)-1]))/2
	solution.append(median)
	# print(list[(int(len(list) / 2))-1])


print(solution)

