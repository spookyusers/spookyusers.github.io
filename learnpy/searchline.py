# search a file's lines and print lines that include the search parameter.

file = open('')
for line in file:
    line = line.rstrip()
    if not line.startswith(''):
        continue
    print(line)
    