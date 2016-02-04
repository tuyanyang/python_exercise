fname = input('Enter a file name: ')
fhand = open(fname)
countHr = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time = words[5].split(':')
        countHr[time[0]] = countHr.get(time[0], 0) + 1
l = list(countHr.items())
l.sort()
for key, val in l:
    print(key, val)


