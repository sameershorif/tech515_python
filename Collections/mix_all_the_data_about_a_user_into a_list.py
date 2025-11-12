name = input("What is your name? ")
age = input("What is your age?  ")
month = input("What month were you born?  ")
year = input("What year were you born?  ")

age = int(age)

user_details_list = [name, age, month, year]

print(user_details_list)

print(type(user_details_list[1]))

height = input("What is your height in cm? ")

height = float(height)
user_details_list.append(height)

print(user_details_list[-1])

# # concatenation
# print("Hi " + name + ", " + str(age))
#
# # f-string
# print(f"You were born in {month} of the year {year}.")