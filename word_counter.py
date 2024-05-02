import string


counts = dict()
fname = input("Which file do you want to open? ")

try:
    with open(fname) as filehandle:
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
        
    sort = input("Would you like me to sort this list for you in alphabetical order? ")
    if sort == "YES":
        sorted_list = list(counts.keys())
        sorted_list.sort()
        sorted_counts = dict()
        for key in sorted_list:
            sorted_counts[key] = counts[key]
        print(sorted_counts)
    
    elif sort == "NO": 
        print(counts)
    
except FileNotFoundError:
    print("The file you were looking for was not found.")
    exit()
