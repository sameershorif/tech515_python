# x needs to be initialised, otherwise the loop doesn't know what x is
x = 0
while x < 10:
    print(f"x -> {x}")
    # If we don't increment x, the while condition will always be true → infinite loop
    x = x + 1


x = 0
while x < 10:
    print(f"x -> {x}")

    if x == 4:
        break  # stop the loop when x reaches 4

    x = x + 1