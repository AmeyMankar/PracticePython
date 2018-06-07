# To have more practice with conditional statements we are going to write a program which uses complex condition. I.e. one if ... else statement could be (and should be) nested inside other to solve this problem.

# Several triplets of numbers are given to you. Your task is to select minimum among each of triplets.

# Input data will contain in the first line the number of triplets to follow.
# Next lines will contain one triplet each.
# Answer should contain selected minimums of triplets, separated by spaces.

# Example:

# data:
# 3
# 7 3 5
# 15 20 40
# 300 550 137

# answer:
# 3 15 137

#http://www.codeabbey.com/index/task_view/min-of-three

number_of_lists = int(input("How many lists you want?\t"))
number_of_items = int(input("How many numbers you want to add into your lists?\t"))
user_input = []
list_of_lists = []
min_list = []
loop1 = 0
loop2 = 0
i = 0


while loop1 < number_of_lists:
	print("List"+str(loop1+1))
	while loop2 < number_of_items:
		user_input.append(int(input("Enter any number:\t")))
		loop2 += 1
	loop2 = 0
	list_of_lists.append(user_input)
	user_input = []
	loop1 += 1

print("Entered list:\t")
print(list_of_lists)

for list in list_of_lists:
	min_num = list[i]
	for i in range(len(list)):
		if min_num > list[i]:
			min_num = list[i]
		i += 1
	min_list.append(min_num)
	i = 0

print("Minimum list: \t")
print(min_list)
