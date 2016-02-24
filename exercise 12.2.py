import socket

URL = input("Enter URL: ")
l = URL.split("/")
#print(l[2])
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((l[2], 80))
    request = 'GET ' + URL + ' HTTP/1.0\n\n'
    mysock.send(request.encode('utf-8'))
except:
    print('Bad URL: ', URL)
    exit()

data = b''
num = 0
is_print = True
while True:
    curdata = mysock.recv(512)
    if len(curdata) < 1:
        break
    num += len(curdata)
    data += curdata
    if is_print:
        if num > 3000:
            print(curdata[:(num-3000)].decode())
            is_print = False
        else:
            print(curdata.decode())

mysock.close()
print('Number of characters: ', num)
