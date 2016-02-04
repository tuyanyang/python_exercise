import socket

URL = input("Enter URL: ")
l = URL.split("/")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((l[2], 80))
except:
    print('Bad URL: ', URL)
    exit()

quest = ('GET ' + URL + ' HTTP/1.0\n\n')
mysock.send(quest.encode('utf-8'))

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data)

mysock.close()
