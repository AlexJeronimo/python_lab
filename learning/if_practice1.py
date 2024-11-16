age = int(input("PLease enter your age: "))

def graduate(age):
    if  1 < age < 7:
        return("You are should go in the kidgarden")
    elif 7 < age < 16:
        return("You are should go in middle school")
    elif 16 < age < 24:
        return("You are should go to the high school or institute")
    else:
        return("Work till death!!!")
    

print(graduate())