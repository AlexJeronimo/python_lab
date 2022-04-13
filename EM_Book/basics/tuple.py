a = tuple([10, 20])
b = (10, 20)
c = (100,)
d = 30, 40, 50
f = ()

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(a)
print(b)
print(c)
print(d)

print(a[1])

print(a[:])
print(b[::-1])

f = b + (10, 20, [30, 40], 50)

print(f)
print(f[2:5])
print(len(f))
