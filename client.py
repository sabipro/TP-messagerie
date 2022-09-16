import socket
from threading import Thread


def send(socket):
    while True :
        msg = input("->")
        msg = msg.encode('utf-8')
        socket.send(msg)
   
def reception(socket):
    while True :
        requete_server = socket.recv(500)
        requete_server = requete_server.decode('utf-8')
        print(requete_server)



host = "192.168.56.1"
port = 9000

socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.connect((host,port))


envoi = Thread(target=send,args=[socket])
recep = Thread(target=reception,args=[socket])

envoi.start()
recep.start()

    


