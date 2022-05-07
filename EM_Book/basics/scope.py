# pi = 'outer pi variable'
#
#
# def print_pi():
#     pi = 'inner pi variable'
#     print(pi)
#
#
# print_pi()
# print(pi)


pi = 'global pi variable'

def outer():
    pi = 'outer pi variable'
    def inner():
        # pi = 'inner variable'
        nonlocal pi
        print(pi)
    inner()

outer()
print(pi)