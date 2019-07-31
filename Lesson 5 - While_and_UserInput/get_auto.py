# Example car rental
auto_list = ["BMW", "Audi", "Subaru", "BA3-2114"]

# Long welcome text
welcome_text = "Greetings to car rental! \n"
welcome_text += "We have are good deal for you friend! \n"
welcome_text += "What car you like at!? \n"
welcome_text += "Here the list: "

print(welcome_text)

# Show all car in list
for car_id, car_name in enumerate(auto_list):
    print("\t" + str(car_id) + " :", car_name)

print("Enter the car number: ")
car_number = input()

if int(car_number) < len(auto_list):
    print("Ok! The " + auto_list[int(car_number)] + " is yours now! Congratulation!")
else:
    print("Sorry! But we don't have car with this ID")