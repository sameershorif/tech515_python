#Starting code:

mixture = [1, 2, 3,"one", "two", "three"]

print(mixture)

print(mixture[1:3])

# Returns every second item in the list
print(mixture[0::2])  # starts at index 0, takes every 2nd item → [1, 3, 'two']

# Start at the last item, stop at the 3rd last item, step in reverse order
print(mixture[-1:-3:-1])    # starts from the last item ('three'), moves backwards, and stops before index -3 ('one') , returns ['three', 'two']

# list[start:stop:step]
# start → where to begin
# stop → where to end (but not including this index)
# step → how to move (positive = forward, negative = backward)