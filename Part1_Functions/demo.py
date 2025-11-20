# functions = block and reusable code
# () - after the function name
# def - defining a new function 


# def first_function(name, age):
#     print(f"Hello {name}")
#     print(f"You are {age} years old")

# first_function("Ion", 30)
# first_function("Dina", 40)

first_name = "Alex"
last_name = "Ionascu"

def full_name(first_name, second_name):
    return first_name + second_name

name = full_name(first_name, last_name)

othername = full_name("Dina", "Patraru")

print(name, othername)