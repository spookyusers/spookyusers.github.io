# search proponderance of words in a file and print largest and smallest and their counts.

#Get File
name = input('Enter file name: ')
handle = open(name)

counts = dict() # create dictionary

for line in handle:
    words = line.split() #creates list from first line
    for word in words:
        counts[word] = counts.get(word,0) + 1 #adds word to dictionary or counts it if it's already there

bigcount = None
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print('Most repeated word:',bigword,bigcount)

