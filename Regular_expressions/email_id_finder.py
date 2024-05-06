import re


fhand = open("mbox.txt")
for line in fhand:
    line = line.rstrip()
    x = re.findall("^From (.*@\S*[a-zA-Z])", line)
    if len(x) > 0:
        print(x)