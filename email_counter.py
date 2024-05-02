fname = input("Enter a file name: ")

counts = dict()
try:
    fhand = open(fname)
    for line in fhand:
        words = line.split()
        for word in words:
            if "@" in word:
                if word not in counts:
                    counts[word] = 1
                else: counts[word] += 1
    l = []
    for key, value in counts.items():
        l.append((value, key))
    l.sort(reverse=True)
    print(l[0][1].translate(line.maketrans(" "," ", "<>;")), l[0][0])

except FileNotFoundError:
    print("The file you were lookinf for hhas not been found or cannot be opened.")
    exit()