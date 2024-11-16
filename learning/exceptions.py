import random

def cut_cake(people):
    try:
        parts = 1 / people
        print(f"Each person can get {parts} of cake")
    #except ArithmeticError:
    #   print("Can't divide by zero!")
    #except TypeError:
    #    print("Programm allows only numbers!")
    except (ZeroDivisionError, TypeError):
        print("Something went wrong! Can't divide!")

#cut_cake("Hello")


while True:
    people = random.randint(1, 10)
    cut_cake(people)