# extract avg values
tot = 0

fname = input('Filename: ')
fh = open(fname)
spamval = None

for line in fh:
    if line.startswith('X-DSPAM-Confidence'):
        tot = tot + 1
        pos = line.find('0')
        val = float(line[pos :])
        if spamval is None:
            spamval = val
        else:
            spamval = spamval + val

avgspamval = spamval / tot
        
print('Average spam confidence:',avgspamval)
    
