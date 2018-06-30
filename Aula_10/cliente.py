import socket
import threading
import sys


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def listen(self):
        print("Conectado a {0}".format(str(self.host)))
        threading.Thread(target=self.send, args=[]).start()
        threading.Thread(target=self.receive, args=[]).start()

    def send(self):
        while True:
            saida = (input()).encode('utf-8')
            self.client.send(saida)

    def receive(self):
        while True:
            entrada = self.client.recv(4096)
            if entrada:
                print(entrada.decode('utf-8'))

if __name__ == "__main__":
    while True:
        PORT = input("Porta? ")
        try:
            PORT = int(PORT)
            break
        except ValueError:
            pass

    Client('localhost', PORT).listen()