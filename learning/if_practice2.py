#string1 = input("Enter string1: ")
#string2 = input("Enter string2: ")

def strings(string1, string2):
    if not isinstance(string1, str) and isinstance(string2, str):
        return("0")
    elif string1 == string2:
        return("1")
    elif string1 != string2 and len(string1) > len(string2):
        return("2")
    elif string1 != string2 and string2 == "learn":
        return(3)


print(strings('mother', 'love'))
print(strings('love', 'love'))
print(strings(3, 'love'))
print(strings('world', 'learn'))