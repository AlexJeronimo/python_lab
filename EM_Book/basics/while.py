# while True:
#     city = input()
#
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")


# unconfirmed_users = ['Alice', 'Bob', 'Candace']
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f"Verifying user : {current_user.title()}")
#     confirmed_users.append(current_user)
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users[::-1]:
#     print(confirmed_user.title())


# pets = ['dog', 'cat', 'parrot', 'goldfish', 'cat', 'dog', 'rabbit']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# responses = {}
#
# polling_active = True
#
# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountainn would you like to climb someday? ")
#
#     responses[name] = response
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#
#     if repeat == 'no':
#         polling_active = False
#
# print("\n--- Poll Results ---")
# for name , response in responses.items():
#     print(f"{name} would like to climb {response}.")

x = 2
while x >= 1:
    print(x)
    x -= 1
