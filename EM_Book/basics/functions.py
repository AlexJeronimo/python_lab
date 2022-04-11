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



