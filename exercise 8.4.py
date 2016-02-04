fname = input('Enter file: ')
fhand = open(fname)
wordlist = list()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in wordlist:
            wordlist.append(word)
wordlist.sort()
print(wordlist)
