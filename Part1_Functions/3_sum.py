# https://www.w3schools.com/python/python_casting.asp / https://www.w3schools.com/python/python_scope.asp
# Write a function add(a, b) that returns the sum of the two numbers.
# Ask the user for two numbers (as input), convert them to integers, call the function, and print the result.
    
# Write your code here:

n1 = int(input("Please type in the first number: "))
n2 = int(input("Please type in the second number: "))

def add(a, b):
    return a + b

def feedback():
    print("The sum of ", n1, " and ", n2, " is ", add(n1, n2))

feedback()
