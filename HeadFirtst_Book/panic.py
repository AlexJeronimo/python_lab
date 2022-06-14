phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)



# num = "1234"
# pnum = list(num)
# print(num)
# print(pnum)
# pnum.extend([pnum.pop(), pnum.pop(), pnum.pop()])
# print(pnum)

