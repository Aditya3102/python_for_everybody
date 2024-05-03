import re


fname = input("Enter the name of the file you would like to open: ")
fhand = open(fname)
reg_ex = input("Enter a regular expression: ")
lines = 0
for line in fhand:
    x = re.findall(reg_ex, line)
    lines += 1
print(f"{fname} had {lines} lines that matched {reg_ex}")