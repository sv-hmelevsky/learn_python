# Condition exit from loop with flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True

while active:
    message = input(prompt)
    if message != 'quit':
        print(message)
    else:
        active = False