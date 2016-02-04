import re
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()
countLett = dict()
total = 0
for line in fhand:
    line = re.sub('[^a-zA-Z]', '', line).lower()
    total += len(line)
    for char in line:
        countLett[char] = countLett.get(char, 0) + 1
#print(countLett)
l = list()
for key, val in countLett.items():
    l.append((val/total, key))
l.sort(reverse=True)
sum = 0
for key, val in l:
    print(val, key)
    sum += key
print(sum)