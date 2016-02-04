fname = input('Enter a file name: ')
fhand = open(fname)
countday = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        #print(words)
        countday[words[2]] = countday.get(words[2],0) + 1
print(countday)
