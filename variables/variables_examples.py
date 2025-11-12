
# What is a variable?
# A variable in Python is a named storage location used to hold a value that can be accessed and changed during a program’s execution.

# Why is it called a variable?
# It’s called a variable because the value it stores can vary or change while the program runs.

# age = 21
# pi = 3.141592653589793
# first_name = "Sam"


# = is used to assign a value to a variable, while
# == is used to compare two values to check if they are equal.

# print(age == 21)  # compares age to 21 , returns True
# print(age == 27)  # compares age to 21 , returns False

# print(age,type(age))
# print(pi, type(pi))
# print(first_name, type(first_name))

# Python is strongly typed which means a variable’s type matters, you cannot automatically mix incompatible types
# without explicitly converting them.
# Example:

# print(name + age)
# This will cause an error because you can't add a string and an integer directly

# Correct way: convert 'age' to string
# print(first_name + " is " + str(age))

#Javascript

# let age = 21;
# let name = "Sam";
# console.log(name + age); automatically converts number to string

# In weakly typed languages, types are often implicitly converted,
# which can lead to unexpected results.
# In Python, you must convert manually so it prevents hidden bugs.


# Python is dynamically typed meaning you don’t have to declare variable types, the interpreter
# determines the type at runtime.

#Python
# x = 10          x is an int
# x = "Hello"     now x is a str
# print(x)

# Output:
# Hello

#Java
# int x = 10;
# x = "Hello";  Compile-time error: incompatible types

# In statically typed languages variable types are fixed at compile time, so you must define them in advance.

# In Python, types can change at runtime, giving flexibility

# print('Before Overwrite:')
# print(age, id(age))
#
# age = 28
# print('After Overwrite:')
# print(age, id(age))

# In Python, integers (and all immutable types) cannot be changed once created.
# When you overwrite the variable with a new number, Python creates a new object
# in memory and makes the variable point to that new object, giving it a different id.

# x = 10
# y = x
#
# print(id(x), id(y))

# When you do y = x, both x and y point to the same object in memory so they share the same id.
# if you later do x = 20, Python creates a new integer object (20) and makes x point to that new object.
# The variable y still points to the original value (10), so its id stays the same.

name = input("What is your name? ")
age = input("What is your age?  ")
month = input("What month were you born?  ")
year = input("What year were you born?  ")

age = int(age)

# concatenation
print("Hi " + name + ", " + str(age))

# f-string
print(f"You were born in {month} of the year {year}.")



#dob = input("Enter your date of birth: ")

# print('Your name is ' + name + " and you are " + age + " and you were born on " + dob)





