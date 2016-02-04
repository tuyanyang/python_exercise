import re

fname = input("Enter file: ")
fhand = open(fname)
numlist = list()
for line in fhand:
    line = line.rstrip()
    numStr = re.findall('^New Revision: ([0-9]+)', line)
    if len(numStr) > 0:
        numlist.extend(numStr)
#print(numlist)
num = [float(n) for n in numlist]
print(sum(num)/len(num))
