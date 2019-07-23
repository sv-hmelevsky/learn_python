# Mmm yummy
pizzas = ["chicken and cheese", "pepperoni and bacon", "philadelphia"]

# Get all pizzas in list
for pizza in pizzas:
    print("Oh! I like \"" + pizza.title() + "\" pizza!")
print("I want them all! :)".upper())

# The range function!
range_list = list(range(1, 5))
print(range_list)

# List of squares of whole numbers from 1 to 10
squares_range = list(range(1, 11))
square_result = []
for value in squares_range:
    square_result.append(value ** 2)
print(square_result)

# Minimum
print(min(square_result))

# Maximum
print(max(square_result))

# Sum
print(sum(square_result))

# Range short notation
square_short = [value ** 2 for value in range(1, 16)]
print(square_short)
