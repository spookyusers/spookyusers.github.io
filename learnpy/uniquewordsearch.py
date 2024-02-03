# make a list of all unique words in the romeo file and sort them.

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
wval = 0

for line in fh:
    words = line.split()
    for newwords in words:
        if newwords not in lst:
            lst.append(newwords)
lst.sort()
print(lst)