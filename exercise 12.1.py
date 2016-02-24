import socket

URL = input("Enter URL: ")
l = URL.split("/")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((l[2], 80))
    request = ('GET ' + URL + ' HTTP/1.0\n\n')
    mysock.send(request.encode('utf-8'))
except:
    print('Bad URL: ', URL)
    exit()

data = b''
while True:
    curdata = mysock.recv(512)
    if len(curdata) < 1:
        break
    data += curdata

mysock.close()
mydata = data.decode()
print(mydata)
