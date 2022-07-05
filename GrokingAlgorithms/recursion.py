# PSEUDOCODE

# search for a key in box inside other inside other.... by while cycle

# def look_for_key(main_box):
#     pile = main_box.make_a_pile_to_look_trough()
#     while pile is not empty:
#         box = pile.grab_a_box()
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print("found the key!")


# recursion

# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item)
#         elif item.is_a_key():
#             print("found the key!")


# countdown

def countdown(i):
    print(i)
    if i <= 0:
        return i
    else:
        countdown(i - 1)


n = 10
countdown(n)
