fname = input('Enter a file name: ')
fhand = open(fname)
countdomain = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        address = words[1].split('@')
        countdomain[address[1]] = countdomain.get(address[1],0) + 1
print(countdomain)
