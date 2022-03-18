# while True:
#     city = input()
#
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")


unconfirmed_users = ['Alice', 'Bob', 'Candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user : {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
