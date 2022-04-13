from copy import *
# nums = [1, 2, 3]
# print(nums)
# print(type(nums))
#
# nums2 = list("some words")
# print(nums2)
# print(type(nums2))
#
# pows_of_two = [2 ** i for i in range(11)]
# print(pows_of_two)
#
# num_list = [7 * i + 1 for i in range(20) if i % 4 == 3]
# print(num_list)
#
# print(num_list[1])
#
# print(len(nums2))
#
# nums[1] = -10
# print(nums)
#
# print(nums2[2:6])
#
# m = [1, 5, 10, 15, 20, 25]
# print(m[5:1:-2])
# print(m[5:-1:-1])
# print(m[-5:-1:-1])
# print(m[-1:-5:-1])
# print(m[::-1])
# print(m[:-10:-1])
# print(m[10:-10:-1])
# print(m[10:0:-1])
#
# s = [10, 20, 30]
# s.append(100)
# s.append([1, 2])
# print(s)
#
# s.extend([40, 50])
# print(s)
#
# s.insert(1, -5)
# print(s)
#
# s.insert(1, [3, 4])
# print(s)
#
# s[2:2] = [5, 6]
# print(s)
#
# s[2:3] = [200, 300]
# print(s)
#
# k = [1, 2, 3] + [4, 5]
# print(k)

# s = [i * (10 - i) for i in range(11)]
# print(s)
# print('Deleted element from list', s.pop(5))
# print(s)
#
# s.remove(21)
# print(s)
#
# del s[3]
# print(s)
#
# s[2:5] = []
# print(s)
#
# s[1:3] = [-1, -2, -3, -4, -5]
# print(s)


# k = 2 in [1, 2, 3]
# print(k)

# p = [1, 2, 3, 4, 5, 6, 4, 3, 2, 1].index(2)
# print(p)
#
# p = [1, 2, 3, 4, 5, 6, 4, 3, 2, 1].index(2, 3)
# print(p)
#
# c = [1, 2, 3, 4, 5, 6, 4, 3, 2, 1, 4, 3, 2].count(2)
# print(c)
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a.reverse()
# print(a)
#
# b = reversed(a)
# print(list(b))
#
# c = [1, 2, 3, 4, 5, 6, 4, 3, 2, 1, 4, 3, 2]
# c.sort()
# print(c)
#
# c = [1, 2, 3, 4, 5, 6, 4, 3, 2, 1, 4, 3, 2]
# c.sort(reverse=True)
# print(c)
#
# c = [1, 2, 3, 4, 5, 6, 4, 3, 2, 1, 4, 3, 2, 8, 3, 0, 45, 3]
# d = sorted(c)
# print(d)
#
# c = [1, 2, 3, 4, 5, 6, 4, 3, 2, 1, 4, 3, 2, 8, 3, 0, 45, 3]
# d = sorted(c, reverse=True)
# print(d)
#
# print(min(d))
# print(max(d))
# print(sum(d))


# a = [10, 20, 30]
# b = a
# print(f'a = {a}')
# print(f'b = {b}')
# # b[1] = 0
# # print(a)
#
# b = a[:]
#
# print(b)
#
# b[1] = 0
#
# print(a)
# print(b)
#
# d = a.copy()
# print(a)
# print(d)
#
# d[0] = 100
# print(d)
# print(a)

x = [10, 20, [100, 200], 30, [300, 400]]

y = x[:]
z = x.copy()
d = deepcopy(x)

x[2][1] = 0
x[4] = 0

print(x)
print(y)
print(z)
print(d)