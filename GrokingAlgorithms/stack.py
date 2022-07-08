# stack

# def greet(name):
#     print("Hello " + name + "!")
#     greet2(name)
#     print("getting ready to say bye...")
#     bye()
#
#
# def greet2(name):
#     print("how are you, " + name + "?")
#
#
# def bye():
#     print("ok bye!")
#
#
# greet("Alex")


# stack with recursion
# factorial - factorial(3) = 3*2*1
# factorial(3) - 3!

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(3))

