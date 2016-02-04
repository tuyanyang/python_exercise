fname = input('Enter a file name: ')
fhand = open(fname)
countAddr = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        countAddr[words[1]] = countAddr.get(words[1], 0) + 1
l = list()
for key, val in countAddr.items():
    l.append((val, key))
l.sort(reverse=True)
print(l[0][1],l[0][0])
