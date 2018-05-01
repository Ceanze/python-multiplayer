import socket
import threading
from player import *

msg = ""
players = []
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
threadRunning = True

def listen():
    global msg
    global server
    global threadRunning

    while threadRunning:
        msg = server.recv(1024).decode()
        if msg.find("disconnected") != -1:
            fill, ip = msg.split(";")
            for p in players:
                if p[0] == ip:
                    players.remove(p)
        elif msg.find("connected") != -1:
            print("Found connected")
            fill, ip = msg.split(";")
            p = Player([320, 300])
            players.append([ip, p])
        elif msg.find("ALL") != -1:
            print("Found exisiting players")
            ips = msg[4:].split(";")
            for clients in ips:
                p = Player([320, 300])
                players.append([clients, p])     
        elif msg.find("P;") != -1:
            ip, position = msg[2:].split(";")
            pos = position.split("/")
            for p in players:
                if p[0] == ip:
                    p[1].setPosition([int(pos[0]), int(pos[1])])
                    

    return


class Client:

    def __init__(self, serverIP, port):
        self.serverIP = serverIP
        self.port = port      
        self.lastMsg = ""



    def update(self, position):
        # Update the server with the players position
        msg = "P;" + str(position[0]) + "/" + str(position[1])
        if self.lastMsg != msg:
            server.sendto(msg.encode(), (self.serverIP, self.port))
        self.lastMsg = msg

    def connect(self):
        # Connect to the server by sending a NEW message to it.
        server.sendto("NEW".encode(), (self.serverIP, self.port))
        self.t = threading.Thread(target=listen)
        self.t.start()
        print("Started thread\n")

    def quit(self):
        server.sendto("QUIT".encode(), (self.serverIP, self.port))
        server.close()
        threadRunning = False
        self.t.join()

    def recv(self):
        return server.recv(1024)

    def getPlayers(self):
        return players