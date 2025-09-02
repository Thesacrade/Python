"""
Write a Python program that does the following:

Takes two numbers as input from the user
Performs addition, subtraction, multiplication, and division on those numbers.
Prints the results of these operations.
Additionally, ask the user for their name and greet them with a message.
"""

num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))
summation = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:
    quotient = num1 / num2
else :
    quotient = "Undefined (Can't divide by zero)"

print("Result of addition is: ", summation)
print("Result of subtraction is: ", difference )
print("Result of multiplication is: ", product)
print("Result of division is: ", quotient, "\n")
name = input("Enter your name\n")
print (f"Hello {name} thanks for participation")





