def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)


num = 10
saying = 'hello'
numbers = [42, 256, 16]

double(num)
print(num)
double(saying)
print(saying)
double(numbers)
print(numbers)
print()
change(numbers)
print(numbers)
