# When program deals with numbers which have fraction part we sometimes want to round such values to whole integer. We'll need this for programming some later problems (to make answers simpler, for example),
# so let us have the following dedicated exercise to learn this trick.

# There are several pairs of numbers. For each pair you are to divide first by second and return the result, rounded to the nearest integer.

# In cases, when result contains exactly 0.5 as a fraction part, value should be rounded up (i.e. by adding another 0.5). Note that for negative values "greater" means "closer to zero". Refer to the Wikipedia
 # page on Rounding for more thorough explanations.

# In any further problems, when rounding is mentioned - just the same rounding algorithm is supposed (unless other is explicitly specified).

# Input data will give a number of test-cases in the first line.
# Next lines will contain one test-case (i.e. the pair of numbers) each.
# Answer should contain division-and-rounding results for each pair, separated with spaces

# Example:

# input data:
# 3
# 12 8
# 11 -3
# 400 5

# answer:
# 2 -4 80

#http://www.codeabbey.com/index/task_view/rounding

list_of_lists = []
user_input = []
i = 0

num_of_lists = int(input("How many lists would you like to have?\t"))
num_of_items = 2
answer = []

for list in range(num_of_lists):
	print("List ",str(list+1))
	for i in range(num_of_items):
		user_input.append(int(input("Please enter a number:\t")))
		i += 1
	list_of_lists.append(user_input)
	list += 1
	i = 0
	user_input = []

print("You entered:\n")
print(list_of_lists)

for list in list_of_lists:
	if (list[0] % list[1]) == 0.5:
		answer.append(str(list[0] / list[1]))
	if(list[0] % list[1]) < 0.5:
		answer.append(str((list[0] / list[1])-0.5))
	if(list[0] % list[1]) > 0.5:
		answer.append(str((list[0] / list[1])+0.5))
	else:
		answer.append(str(list[0] / list[1]))

print("Solution:\n")
print(answer)