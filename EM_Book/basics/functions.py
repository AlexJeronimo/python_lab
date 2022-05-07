# def greet_user(user):
#     print(f"Hello, {user.title()}!")
#
#
# greet_user("Alex")

# def describe_pet(animal_type, pet_name):
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet('cat', 'stupid')

# def build_person(first_name, last_name, age=None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# def print_greeting():
#     '''
#     Print 'Hello' text
#     :return: None
#     '''
#     print('Hello')
#
#
# print_greeting()


# def print_greeting_with_name(name='Unknown User'):
#     '''
#     :param name
#     :return: None
#     '''
#     print(f'Hello {name}!')
#
#
# print_greeting_with_name()
# help(print_greeting_with_name)


# def sum_of_two_numbers(a=0, b=0):
#     '''
#
#     :param a: The first addend
#     :param b: The second addend
#     :return: Sum of a and b
#     '''
#     return a + b
#
#
# x = sum_of_two_numbers(1, 3)
# print(x)
#
# help(sum_of_two_numbers)


# def is_string_in_text(text, string):
#     if string.lower() in text.islower():
#         return True
#     else:
#         return False
#
#
# a = 'abcd'
# b = 'acjgfuihriabcdpeojbetiononr abdc'
#
# x = is_string_in_text(b, a)
# print(x)


# def is_string_in_text(string, text):
#     return string.lower() in text.lower()
#
#
# print(is_string_in_text('hey', 'hey dude'))


# def te_percent_of_product(x, y):
#     return (x * y) * 0.1
#
#
# print(te_percent_of_product(10, 20))


# def ten_percent_of_product_with_args(*args):
#     product = 1
#     for number in args:
#         product *= number
#     return product * 0.1
#
#
# print(ten_percent_of_product_with_args(10, 20, 7, 2))


# def percent_of_product_with_args(percent, *args):
#     product = 1
#     for number in args:
#         product *= number
#     return product / 100 * percent
#
#
# print(percent_of_product_with_args(3, 20, 7, 2, 45, 325))

# def func_with_kwargs(**kwargs):
#     print(kwargs)
#
#
# func_with_kwargs(first=1, second=2, third=3)
#
#
# def func_with_args(*args):
#     print(args)
#
#
# func_with_args(1, 2, 3)

# def hello_with_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print(f"Hello! Nice to meet you, {kwargs['name']}")
#     else:
#         print("Hello! What is your name?")
#
#
# hello_with_kwargs(gender='male', age=34, name='Alex')
# hello_with_kwargs(gender='male', age=34)


# def hello_with_greeting_and_kwargs(greeting, **kwargs):
#     if 'name' in kwargs:
#         print(f"{greeting}! Nice to meet you, {kwargs['name']}")
#     else:
#         print(f"{greeting}! What is your name?")
#
#
# hello_with_greeting_and_kwargs('Hi', gender='male', age=34, name='Alex')
# hello_with_greeting_and_kwargs('Hello', gender='male', age=34)



def func_with_args_and_kwargs(*args, **kwargs):
    # print(args)
    # print(kwargs)
    print(f"I would like {args[1]} {kwargs['food']}")


func_with_args_and_kwargs(45, 'one', drink='coffee', food='sandwich')
