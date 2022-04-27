import os
import csv

file = open("D:\WORK\RVTools_export_all_2022-04-25_04.01.53\RVTools_tabvCPU.csv")

csvreader = csv.reader(file)
header = next(csvreader)
#print(header)
rows = []
for row in csvreader:
    rows.append(row)
# print(rows)
count = []
for line in rows:
    count.append(line[4])
    # print(line)
file.close()
cores = 0
for i in count:
    cores += int(i)
print(cores)
