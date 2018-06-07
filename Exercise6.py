# This problem introduces popular algorithm of the "linear search", which should be learnt thoroughly as it is often used in programming more complex tasks (sorting etc.)

# Very common operation on sequence of values, or arrays is to find its extremal value - maximum or minimum. To achieve this one need to store current maximum (or minimum respectively) in a separate variable,
# and then run through array, comparing each of its elements to this variable. Whenever next value is greater than this temporary variable, this value should be copied into it (as a new maximum).

# At the end of the pass this temporary variable will hold the extremum value.

# Input data will give you exactly 300 numbers in a single line.
# Answer should contain maximum and minimum of these values, separated by space.

# Example:

# input data:
# 1 3 5 7 9 11 ... 295 297 299 300 298 296 ... 12 10 8 6 4 2

# answer:
# 300 1

#http://www.codeabbey.com/index/task_view/maximum-of-array

total_items = 0
user_input = []
i = 0
min_value = 0
max_value = 0

total_items = int(input("How many numbers would you like to add to the list?\t"))

for i in range(total_items):
	user_input.append(input("Enter a number:\t"))
	i += 1

print("You entered:\n")
print(user_input)

min_value = user_input[0]
max_value = user_input[0]

for i in range(total_items):
	if user_input[i] < min_value:
		min_value = user_input[i]
	if user_input[i] > max_value:
		max_value = user_input[i]
	i += 1

print("Minimum value:\t", min_value)
print("Maximum value:\t", max_value)