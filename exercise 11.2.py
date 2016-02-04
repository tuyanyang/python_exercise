import re

fname = input("Enter file: ")
fhand = open(fname)
numlist = list()
for line in fhand:
    line = line.rstrip()
    numStr = re.findall('^New Revision: ([0-9]+)', line)
    if len(numStr) == 1:
        num = float(numStr[0])
        numlist.append(num)
print(sum(numlist)/len(numlist))
