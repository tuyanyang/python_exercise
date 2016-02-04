import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

data = b''
while True:
    curdata = mysock.recv(512)
    if len(curdata) < 1:
        break
    data = data + curdata
mysock.close()
mydata=data.decode()
print(mydata)



