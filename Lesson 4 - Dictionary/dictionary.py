# Abstract dictionary of dictionary ^_^
persones_list = {
    1: {
        "first_name": "Vasya",
        "last_name": "Vasin",
        "age": 21,
        "city": "Samara",
        "favorite_numbers": [5, 10, 15],
    },
    2: {
        "first_name": "Sveta",
        "last_name": "Vasina",
        "age": 23,
        "city": "Samara",
        "favorite_numbers": [1, 69, 100],
    }
}

favorite_languages = {
    "Vasya": "Python",
    "Sveta": "Assembler"
}

# Tuple list
persone_list = ("Vasya", "Sveta")

# Bruteforce dict like this
for key, persones in persones_list.items():
    for key, persone in persones.items():
        if persone in sorted(persone_list):
            print(key + ":", persone)
            print("favorite_language: " + favorite_languages[persone])
        else:
            print(key + ":", persone)

    print("\n")