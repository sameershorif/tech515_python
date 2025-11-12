age = input("What is your age?  ")
name = input("What is your name?  ")
this_year = 2025

age = int(age)
name = str(name)

print(f'OMG {name}, you are {age} years old so you were born in', this_year - age )

print('you have lived for' , age * 8760 , 'hours')