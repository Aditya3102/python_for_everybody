import re


total_of_num = 0
total_num_of_num = 0

fhand = open("mbox.txt")
for line in fhand:
    x = re.findall("^[A-Za-z]+ [A-Za-z]+: (\d*)", line)
    if len(x) > 0:
        total_of_num += int(x[0])
        total_num_of_num += 1

print(int(total_of_num/total_num_of_num))
