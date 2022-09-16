import socket
from threading import Thread

def send(client):
    while True :
        msg = input("->")
        msg  = msg.encode('utf-8')
        client.send(msg)
   

def reception(client):

    while True :
        requete_client = client.recv(500)
        requete_client = requete_client.decode('utf-8')
        print(requete_client)
        if not requete_client :
            print("close")
            break
    
        
    
host = "192.168.56.1"
port = 9000

socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((host,port))
socket.listen(1)
print("le serveur est en marche ")



#creation de la boucle while pour que le serveur reste tjrs allumer tant que le client est connecte

client, ip = socket.accept()
print("le client d'ip ",ip ,"s'est connecte")


envoi = Thread(target=send,args=[client])
recep = Thread(target=reception,args=[client])

envoi.start()
recep.start()

recep.join()
 
client.close()
socket.close()
    





   

