shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

print(shopping_list)

print(type(shopping_list))

print(shopping_list[0])

print(shopping_list[-1])

shopping_list[1] = "rice"

print(shopping_list[1])

# add one item to end
shopping_list.append("carrots")

print(len(shopping_list))

# add multiple items
shopping_list.extend(["toffee", "coffee"])

print(shopping_list)

# remove bananas
shopping_list.remove("bananas")

print(shopping_list)

# remove last item
shopping_list.pop()

print(shopping_list)