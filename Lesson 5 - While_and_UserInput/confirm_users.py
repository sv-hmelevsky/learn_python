# Simple user verification
unconfirmed_users = ['alice', 'jhon', 'zic']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users hav been confirmed:")
for confirmed_user in confirmed_users:
    print("\t- " + confirmed_user.title())
