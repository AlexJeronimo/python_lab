# print('ax = b')
# try:
#     a = float(input('enter a: '))
#     b = float(input('enter b: '))
#     x = b / a
#     print(f'x = {x}')
# except:
#     print('you entered wrong data')
# print('work finished')


print('ax = b')
try:
    a = float(input('enter a: '))
    b = float(input('enter b: '))
    x = b / a
    print(f'x = {x}')
except ValueError:
    print('you should be enter a number')
except ZeroDivisionError:
    print("you can't divide by zero")
print('work finished')
