# open and read file with links per line
with open(r"D:\kayak info links.txt", 'r') as kayak_links:
    lines = kayak_links.readlines()

# delete double links in list
li = []
[li.append(i) for i in lines if i not in li]
# print lines from the list
# for line in li[::-1]:
#     print(line, end='')
# count lines in original and changed lists
# print(len(lines))
# print(len(li))

# write changes to a new file with stripping "\n" command to delete empty rows
with open(r'D:\kayak_info_links_without_doubles.txt', 'w') as kayak_links_form:
    for line in li[::-1]:
        print(line.strip('\n'), file=kayak_links_form)
