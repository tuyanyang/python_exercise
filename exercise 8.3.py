fhand = open('mbox-short_1.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug: ', words)
    if len(words) > 2 and words[0] == 'From' :
       print(words[2])