# Remove all repeated animals
animals = ["cat", "dog", "rabbit", "cat", "raven", "rat", "cat"]

while "cat" in animals:
    animals.remove("cat")
print(animals)