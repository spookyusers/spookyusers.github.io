# read a file and capitalize the words

# Use words.txt as the file name

fname = input("Enter file name: ")
fh = open('words.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())