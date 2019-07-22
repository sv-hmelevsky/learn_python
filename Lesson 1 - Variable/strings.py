name = "ada loveRCase"

# Uppercase first letter in any word in var
print(name.title())

# Uppercasing any letter of word in var
print(name.upper())

# Lowercasing any letter of word in var
print(name.lower())


# Concatination
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)
print("Hello, \n\t" + full_name.title() + "!")
print("Language: \n\t- Python \n\t- PHP \n\t- JavaScript")

# Remove whitespace from begin and end of the var
favorite_lang = " Python and PHP "
print("With whitespace: " + favorite_lang
    + "\nClear left: " + favorite_lang.lstrip()
    + "\nClear right: " + favorite_lang.rstrip()
    + "\nClear any: " + favorite_lang.strip())