# We need to sum two numbers and tell the result. 
#http://www.codeabbey.com/index/task_view/sum-of-two

def sum(number1,number2):
	return number1+number2

number_1 = int(input("Enter first number: \t"))
number_2 = int(input("Enter second number: \t"))

print("The sum of the two entered numbers is: " + str(sum(number_1,number_2)))
