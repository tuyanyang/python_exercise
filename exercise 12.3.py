import urllib.request

URL = input('Enter URL: ')
try:
    fhand = urllib.request.urlopen(URL)
except:
    print('Bad URL: ', URL)
    exit()

data = b''
num = 0
is_print = True
for line in fhand:
    num += len(line)
    data += line
    if is_print:
        if num > 3000:
            print(line[:(num-3000)].decode().strip())
            is_print = False
        else:
            print(line.decode().strip())

print('Number of characters: ', num)




