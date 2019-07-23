# List functions
countries = ["Germany", "Canada", "Netherlands", "USA", "Jamaica"]

# First element of list as UPPERCASE :)
print(countries[0].upper())

# Last element of list as lowercase
print(countries[-1].lower())

# Count list element
print(len(countries))

# Count list element for cycle
print(len(countries)-1)

# Add new element to list
countries.append("Russia")
print(countries)

# Add new element to current position
countries.insert(1, "China")
print(countries)

# Forever delete element from the list
del(countries[-1])
# Remove firs entry of element
countries.remove('China')
print(countries)

# Take and delete last element of list
poppeed_countrie = countries.pop()
second_poppeed_countrie = countries.pop(2)
print(poppeed_countrie, second_poppeed_countrie, countries)