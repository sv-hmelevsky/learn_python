# Exercises with list slice
numbers_range = list(range(1, 11))

# First three elements
print(numbers_range[:3])

# Three elements from the middle
middle_border = round((len(numbers_range)-1) / 2)
print(numbers_range[middle_border:middle_border+3])

# Last three elements
print(numbers_range[-3:])