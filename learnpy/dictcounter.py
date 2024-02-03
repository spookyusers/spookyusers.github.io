#dictcounter


counts = dict()
names = ['csev', 'cwen', 'csev', 'zquian', 'cwen']

# prints count of all keys in dictionary
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# find count for key
x = counts.get('csev', 0) 
print(x)

# counts names in dictionary, simplified
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)