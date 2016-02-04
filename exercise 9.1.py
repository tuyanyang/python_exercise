fhand = open('words.txt')
wordic = dict()
n = 1
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in wordic:
            wordic[word] = n
            n += 1
print(wordic)
print(len(wordic))
print('everyone' in wordic)
