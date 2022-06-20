# from DBcm import UseDatabase
#
# config = {'host': '127.0.0.1',
#           'user': 'vsearch',
#           'password': 'vsearchpasswd',
#           'database': 'vsearchlogDB', }
#
# with UseDatabase(config) as cursor:
#     _SQL = """show tables"""
#     cursor.execute(_SQL)
#     data = cursor.fetchall()
#
# print(data)


# def outer():
#     def inner():
#         print('This is inner.')
#
#     print('This is outer, invoking inner.')
#     inner()


# def outer():
#     def inner():
#         print('This is inner.')
#
#     print('This is outer, invoking inner.')
#     return inner
#
#
# # outer()
#
# i = outer()
# print(i)
# print(type(i))
# i()

# def myfunc(*args):
#     for a in args:
#         print(a, end=' ')
#     if args:
#         print()
#
#
# myfunc(10)
# myfunc()
# myfunc(10, 20, 30, 40, 50, 60, 70)
#
# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# myfunc(values)
# myfunc(*values)
# print(*values)
#
#
# def myfunc2(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v, sep='->', end=' ')
#     if kwargs:
#         print()
#
#
# myfunc2(a=10, b=20)
# myfunc2()
# myfunc2(a=10, b=20, c=30, d=10, e=50, f=60, t='hello')
# values2 = {'a': 10, 'b': 20, 'c': 30, 'd': 'hello'}
# myfunc2(**values2)


# def myfunc3(*args, **kwargs):
#     if args:
#         for a in args:
#             print(a, end=' ')
#         print()
#     if kwargs:
#         for k, v in kwargs.items():
#             print(k, v, sep='->', end=' ')
#         print()
#
#
# myfunc3()
# myfunc3(1, 2, 3)
# myfunc3(a=10, b=20, c=30)
# myfunc3(1, 2, 3, a=10, b=20, c=30)

# try:
#     with open('myfile.txt') as fh:
#         file_data = fh.read()
#     print(file_data)
# except FileNotFoundError:
#     print('Tha data file is missing.')
# except PermissionError:
#     print('This is not allowed.')
# except:
#     print('Some other error occurred.')

# import sys
# try:
#     1/0
# except:
#     err = sys.exc_info()
#     for e in err:
#         print(e)


# try:
#     with open('myfile.txt') as fh:
#         file_data = fh.read()
#     print(file_data)
# # except FileNotFoundError:
# #     print('Tha data file is missing.')
# except PermissionError:
#     print('This is not allowed.')
# except Exception as err:
#     print('Some other error occurred: ', str(err))

class ConErr(Exception):
    pass


# raise ConErr('Cannot connect .... is it the panic?')


try:
    raise ConErr('Whoops!')
except ConErr as err:
    print('Got:', str(err))

