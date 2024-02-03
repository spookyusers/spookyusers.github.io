# parse out email addresses from file

fname = input("Enter file name: ")

if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
emails = list()
unique = None

for line in fh:
    if ('From ') in line:
        line = line.rstrip()
        words = line.split()
        email = words[1]
        print(email)
        emails.append(email)
        count = count + 1
    
    

print("There were", count, "lines in the file with From as the first word")

