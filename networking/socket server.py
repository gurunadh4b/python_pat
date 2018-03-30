import socket
s=socket.socket()
s.bind((localhost,2000))
s.listen(5)
print('starting server')
print('waiting for client connection')
(con,client)=s.accept()
print('connected with client :',client)
while True:
    client_msg=con.recv(1024)
    print(client_msg)
    if client_msg=='bye':
        con.send('bye')
        con.close()
        break
    msg=eval(input('enter your message to client :'))
    con.send(msg)
