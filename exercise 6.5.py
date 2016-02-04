str = 'X-DSPAM-Confidence: 0.8475'
colpos = str.find(':')
number = float(str[colpos+1:])
print(number)


