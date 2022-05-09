# Special (magic) methods __method_name__

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def __len__(self):
        return self.age

    def __add__(self, other):
        return self.age + other.age

    def __del__(self):
        print("Person object with name " + self.first_name + " is deleted from memory")


jack = Person('Jack', 'White', 45)
jane = Person('Jane', 'Eyre', 23)

print(jack + jane)
# print(len([1, 2, 3, 4, 5]))
# print(len(jack))
#
# print([1, 2, 3, 4, 5])
# print(jack)
#
# del (jack)
# print(jack)
