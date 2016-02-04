fname = input('Enter a file name: ')
fhand = open(fname)
countAddr = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        #print(words)
        countAddr[words[1]] = countAddr.get(words[1],0) + 1
largest = None
for key in countAddr:
    if largest is None or countAddr[key] > largest:
        largest = countAddr[key]
        largestAddr = key
print(largestAddr,largest)