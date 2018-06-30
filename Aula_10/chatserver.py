#Exercicio feito com base no exemplo de servidor multithread dado em sala de aula

import socket
import threading

class ChatThreadedServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.client_list = []

    def listen(self):
        self.server.listen(5)
        print("Chat iniciado na porta: {0}".format(self.port))
        while True:
            client, address = self.server.accept()
            #client.settimeout(60)
            self.client_list.append(client)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def broadcast(self, message, client):
        for clt in self.client_list:
            if clt != client:
                try:
                    clt.send(message.encode('utf-8'))
                except:
                    clt.close()
                    # if the link is broken, we remove the client
                    self.client_list.remove(clt)

    def listenToClient(self, client, address):
        print ("Cliente {0} conectado".format(str(address[1])))
        size = 4096
        while True:
            try:
                msg = client.recv(size)
                if msg:
                    # Set the response to echo back the recieved data
                    strdata = msg.decode('utf-8')
                    msgToSend = "<{0}>".format(address[1])+ strdata
                    print(msgToSend)
                    self.broadcast(msgToSend, client)
                else:
                    raise print('Client disconnected')
            except:
                client.close()
                print("Cliente {0} desconectado".format(address[1]))
                return False


if __name__ == "__main__":
    while True:
        port_num = input("Porta? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ChatThreadedServer('', port_num).listen()