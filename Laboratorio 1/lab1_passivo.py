#Matheus Henrique Panno Guimaraes

import socket

HOST = ''    
PORT = 2020

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1) 

newSock, end = sock.accept()
print ('Conectado com: ', end)

while True:
	msg = newSock.recv(1024)
	if not msg: break 
	else: print("Recebi do ativo a msg: " + str(msg,  encoding='utf-8'))
	newSock.send(msg) 


newSock.close() 
sock.close() 
