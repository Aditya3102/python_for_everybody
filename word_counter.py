import string


counts = dict()

try:
    with open("story.txt") as filehandle:
        for line in filehandle:
            line = line.rstrip()
            line = line.translate(line.maketrans(" "," ", string.punctuation))
            line = line.lower()
            words = line.split()
            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
    print(counts)

except FileNotFoundError:
    print("The file you were looking for was not found.")
