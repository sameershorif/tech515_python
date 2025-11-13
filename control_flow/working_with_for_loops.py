# Starting code to put at the top:

example_string = "test"
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

for character in example_string:
    print(character)


for num in list_data:
    print(num * 2)

for data in embedded_lists:
    print(data)
    for item in data:
        print(item)



for data_dict in dict_data:
    print(data_dict)

for data_dict in dict_data.values():
    print(data_dict)

for data_dict in dict_data.values():
    for value in data_dict.values():
        print(value)

# for data_dict in dict_data.values():
#     for key, value in data_dict.items():
#         if key == "money":
#             print(value)

for data_dict in dict_data.values():
    print(data_dict["money"])

for num in list_data:
    if num < 3:
        print("less than 3")
    elif num == 3:
        print("I found three")
    else:
        print("greater than 3")




