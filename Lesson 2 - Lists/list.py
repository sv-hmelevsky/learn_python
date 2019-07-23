# List sort example
countries = ["Germany", "Canada", "Netherlands", "USA", "Jamaica"]

print(countries)

# Sorted ASC without change the list
print(sorted(countries))
print(countries)

# Sorted DSC without change the list
print(sorted(countries, reverse = True))
print(countries)

# DSC sort the list with change the base
countries.reverse()
print(countries)

# Back to base sort
countries.reverse()
print(countries)

# ASC sort with change base list
countries.sort()
print(countries)

# DSC sort with change base list
countries.sort(reverse = True)
print(countries)