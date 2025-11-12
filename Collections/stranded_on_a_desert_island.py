# 1. How are tuples similar to lists?
# Both tuples and lists can store multiple items in a single variable.
# They can contain different data types (e.g. strings, numbers, booleans).
# Both are ordered, meaning the items keep their position and can be accessed by index (e.g. my_tuple[0]).

# Are tuples immutable and what does this mean?
# Yes, tuples are immutable.
# This means you cannot change, add, or remove items after the tuple is created.

# 3. What other data types are immutable?
# int (integers)
# float (decimal numbers)
# str (strings)
# boolean (True/False)
# All of these cannot be changed in place, modifying them creates a new object in memory.

# What are good use cases for tuples instead of lists?
# Tuples are great when:
# You want to store data that shouldn’t change, like fixed settings or coordinates.
# You need faster access (tuples are slightly faster than lists).
# You want to use them as dictionary keys (only immutable types can be keys).

#prints tuple and counts how many breads there are
# essentials = ("bread", "eggs", "milk")
#
# print(essentials)
# print(essentials.count("bread"))

# Starting code:
# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")
# save the items as a tuple
essentials_tuple = (essential_item1, essential_item2, essential_item3)  # YOUR CODE GOES HERE INSTEAD OF 'None'
# print the tuple
print("Here are your items as a tuple:", essentials_tuple)
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")
# try to add the 4th item to the tuple
# if you can't add the 4th item, work out how to save the 4th item to the tuple
# create a new tuple that includes the old items + the new one
essentials_tuple = essentials_tuple + (essential_item4,)

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)
