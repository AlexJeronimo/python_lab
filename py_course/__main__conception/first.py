# print(1)
# print('string')
# # __name__ = '__main__'
# print(__name__)
#
#
# def func_one():
#     pass
#
# class One:
#     def __init(self):
#         pass
#
#
# if __name__ == '__main__':
#     func_one()
#     One

def function_1():
    print('function_1 from first.py')


print('top level in first.py')

if __name__ == '__main__':
    print('first.py is being run directly')
else:
    print('first.py has been imported')
