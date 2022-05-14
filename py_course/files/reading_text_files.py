# text = open(r'E:\Projects\python_lab\tsukimichi moonlight special ending song.txt')
# for line in text:
#     print(line, end='')
# text.close()


# text = open(r'E:\Projects\python_lab\tsukimichi moonlight special ending song.txt')
# for line in text:
#     if 'is' in line.lower():
#         print(line, end='')
# text.close()


# with open(r'E:\Projects\python_lab\tsukimichi moonlight special ending song.txt') as tsukimichi:
#     # for line in tsukimichi:
#     #     if 'is' in line:
#     #         print(line, end='')
#
#     line = tsukimichi.readline()
#     while line:
#         print(line, end='')
#         line = tsukimichi.readline()

# with open(r'E:\Projects\python_lab\tsukimichi moonlight special ending song.txt') as tsukimichi:
#     lines = tsukimichi.readlines()
# # print(lines)
# for line in lines[::-1]:
#     print(line, end='')


with open(r'E:\Projects\python_lab\tsukimichi moonlight special ending song.txt', 'r') as tsukimichi:
    text = tsukimichi.read()
print(text)
