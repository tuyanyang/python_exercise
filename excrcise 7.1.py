fname = input('Enter the file name: ')
fhand = open(fname)
for line in fhand:
    print(line.upper())
