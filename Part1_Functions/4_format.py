# https://www.w3schools.com/python/python_strings_format.asp
# Write a function greet_person(name) that returns the message “Hello, NAME!”.
# Ask the user for their name and print the returned message.
    
# Write your code here:

n = input("Please type in your name: ")

def greet_person(name):
    return f"Hello, {n}!"

def feedback():
    print(greet_person(n))

feedback()

