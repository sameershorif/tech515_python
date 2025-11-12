print("Hello!")

# List of menu items
starters = ["Soup", "Salad", "Garlic Bread"]
mains = ["Steak", "Pasta", "Burger"]
desserts = ["Ice Cream", "Brownie", "Cheesecake"]

# Print and take input for starter
print("\nStarters:", starters)
starter_choice = input("Please choose a starter: ")

# Print and take input for main
print("\nMains:", mains)
main_choice = input("Please choose a main course: ")

# Print and take input for dessert
print("\nDesserts:", desserts)
dessert_choice = input("Please choose a dessert: ")

# Level 2

# Store customer’s choices in a list
customer_order_list = [starter_choice, main_choice, dessert_choice]

# Use an f-string to confirm the order
print(f"\nThank you for your order! You chose {starter_choice}, {main_choice}, and {dessert_choice}.")

# Level 3

# Dictionary with prices
menu_prices = {
    "Soup": 4.50,
    "Salad": 4.00,
    "Garlic Bread": 3.50,
    "Steak": 12.00,
    "Pasta": 9.50,
    "Burger": 10.00,
    "Ice Cream": 3.50,
    "Brownie": 4.00,
    "Cheesecake": 4.50
}

# Calculate total bill
total = sum(menu_prices[item] for item in customer_order_list)

print(f"\nTotal bill: £{total}")
