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
count = 0
while True:
    curdata = mysock.recv(5120)
    if len(curdata) < 1:
        break
    count += len(curdata)
    print(len(curdata), count)
    data += curdata

mysock.close()

pos = data.decode().find('\r\n\r\n')
#print('Header length: ', pos)
#print(data[:pos].decode())
mydata = data[pos+4:]
print(mydata.decode())
