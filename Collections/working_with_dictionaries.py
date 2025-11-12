student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set up"]
}

# A dictionary in Python saves data in key–value pairs
# each piece of data (the value) is associated with a unique key that acts like a label or name for that value.
# Each key must be unique, and each key is paired with a value.
# You can access any value by referring to its key, not by position (like in a list).

#  key       value
# "name"	"susan"
# "stream"	"tech"
# "completed_lessons"	4

# A dictionary stores data as key: value pairs.
# Each value must be accompanied by a key that describes what the value represents.
# This makes data easy to look up, update, or reference by name instead of position.

print(student_1)

# Print its data type to the screen
print(type(student_1))

# Print the value for the key "stream"
print(student_1["stream"])

# Print the value for 'completed_lesson_names' (the list)
print(student_1["completed_lesson_names"])

# Print the data type for the value of 'completed_lesson_names'
print(type(student_1["completed_lesson_names"]))

# Print the first item in the list of 'completed_lesson_names'
print(student_1["completed_lesson_names"][0])

# Change the value of "completed_lessons" to 3
student_1["completed_lessons"] = 3
print(student_1['completed_lessons'])


# Print the dictionary to check the change
print(student_1)

# 10. Delete "data_types" from the list under the key 'completed_lesson_names'
student_1["completed_lesson_names"].remove("data_types")

# Print dictionary again to confirm removal
print(student_1)

# 11. Use the keys() method to list all keys in the dictionary
print(student_1.keys())