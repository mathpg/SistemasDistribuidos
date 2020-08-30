#Matheus Henrique Panno Guimares

import socket

HOST = 'localhost'
PORT = 2020     

sock = socket.socket() 

sock.connect((HOST, PORT)) 

#chave utilizada para finalizar a comunicacao
senha="fim" 

print("Para finalizar a comunicacão digite a msg: " + senha) 
while True:
    msg=input("Digite uma msg: ")
    if(msg==senha):
        print("Fim da comunicação")
        break

    sock.send(msg.encode())

    msg = sock.recv(1024)

    print("Recebi do passivo a msg: " + str(msg,  encoding='utf-8'))

sock.close() 
