import random

# Generate a random number between 1 and 20 and store it in magic_number
magic_number = random.randint(1, 20)

# Number of guesses the player is allowed
guesses_left = 5

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 20.")




# Loop continues as long as the player still has guesses left
while guesses_left > 0:

    # Ask the user for their guess
    user_guess = input("Enter your guess: ")

    # Check if the user typed a valid number (digits only)
    # If not, we DO NOT reduce guesses_left
    if not user_guess.isdigit():
        print("That is not a number. Your guess was NOT counted. Try again.")
        continue  # Restart the loop and ask again

    # Convert the guess string into an integer
    user_guess = int(user_guess)

    # Check if the guess is correct
    if user_guess == magic_number:
        print("Correct! You guessed the magic number!")
        break  # Exit the loop because the user won
    else:
        # Since the guess was valid but wrong, remove 1 guess
        guesses_left -= 1

        # Give a hint based on the guess
        if user_guess < magic_number:
            print("Go HIGHER!")  # The guess was too low
        else:
            print("Go LOWER!")   # The guess was too high

        # Tell the user how many guesses they have left
        print(f"You have {guesses_left} guesses left.")

# -----------------------
# END OF GAME
# -----------------------
# If guesses_left is 0, the player has lost
if guesses_left == 0:
    print("You've run out of guesses!")
    print(f"The magic number was: {magic_number}")