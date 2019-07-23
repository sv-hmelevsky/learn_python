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
result_result = []
for square_number in squares_range:
    result_result.append(square_number ** 2)
print(result_result)
