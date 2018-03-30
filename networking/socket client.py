import socket
s=socket.socket()
print('starting client...')
print('connection to the server')
s.connect((localhost,2000))
while True:
    msg=eval(input('enter your message to server :'))
    s.send(msg)
    res=s.recv(1025)
    print(res)
    if res=='bye':
        s.send('Thank you')
        break
s.close()
