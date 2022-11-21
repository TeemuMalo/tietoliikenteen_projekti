# echo-client.py

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('172.20.241.9', 20000))
s.sendall(b'82\n')

chunks = []
while True:
    data = s.recv(1024)
    if len(data) == 0:
        break
    chunks.append(data.decode('utf-8'))





with open('C:/Koulu (Tietotekniikka)/anturidataa/dataa3.txt', 'w') as f: 
    for i in chunks:
        print(i, end = '')

        f.write(i)



s.close()

