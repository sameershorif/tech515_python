#1
import numbers


def print_something():
    print("this is my function")

print_something()

#2
def print_something_better(string):
    print(string)

# Call the function to test it
print_something_better("Hello World!")

#3, 7
def greet(name: str):
    print("Hello, my name is " + name + ".")

# greet("Susan")
# greet(24601)

#4
# def addition(int1, int2):
#     return int1 + int2
#
# # print(addition(2, 2))

# Functions need return if you want them to give back a value.
# Without return, the result is discarded and the function outputs None.
# Printing is different from returning.
# print() only shows something on the screen.
# return gives the value back to the caller so it can be used later.
# A function should only print when the requirement says so.

#5
def addition(int1=2, int2=2):
    return int1 + int2

print(addition(4, 4))

# Default values are only used when no arguments are provided.
# When you call addition(4, 4), you override the default values.
# So instead of using 2 + 2, it uses 4 + 4.

#6
def print_every_numbers(*numbs):
    print(type(numbs))
    for num in numbs:
        print(num)

example_tuple = (1, 2, 2, 3, 3, 4, 5, 5)

print_every_numbers(*example_tuple)

# The asterisk *
# *numbers collects all positional arguments into a tuple
# This allows the function to accept 0, 1, or 100 arguments without changing the function definition

#8
def division(int1: int = 2, int2: int = 5) -> float:
    result: float = int1 / int2
    return result


# b. Define variables with type hints BEFORE calling the function
a: int = 4
b: int = 6

# c. Call the function with variables
print(division(a, b))     # This should print: 0.6666666666666666

# d. Call the function using default values
print(division())         # This should print: 0.4

# Type hints for arguments:
# int1: int
# int2: int
# This tells Python and your IDE that both parameters should be integers.
# Default values:
# int1: int = 2
# int2: int = 5
# If no arguments are passed, Python uses these defaults → 2 ÷ 5 = 0.4
# Return type hint:
# -> float
# This warns you if the function returns something that isn't a float.

#9
# Use meaningful names
# Keep functions short and focused
# Use arguments instead of hard-coding values
# Return values instead of printing inside the function
# Use default argument values when appropriate
# Add docstrings (optional but good practice) """."""
# Don’t repeat yourself (DRY principle)