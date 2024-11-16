x = 1
while x <= 5:
    print(x)
    x += 1

print('')

while True:
    user_say = input('Say something: ')
    if user_say == 'Bye':
        print('Bye')
        break
    else:
        print(f"You are {user_say}")