import re

hand = open('mbox.txt')
regex = input('Enter a regular expression: ')
countRegex = 0
for line in hand:
    line = line.rstrip()
    if re.search(regex, line):
        countRegex += 1
print('mbox.txt had', countRegex, 'lines that matched', regex)
