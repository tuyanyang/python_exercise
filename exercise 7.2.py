fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        total += float(line[19:])
print('Average spam confidence: ',total/count)

