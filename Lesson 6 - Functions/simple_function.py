# Simple print user name
def display_name(user_name):
    if str(user_name) != "":
        print("Hello " + user_name.title() + "!" + " Nice to meet you!")
    else:
        print("The name can't be empty!")

display_name(input("Enter your name!\n"))