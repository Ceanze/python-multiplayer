from socket import *
import time
import threading

SERVER_RUNNING = True

# create UDP socket and bind to specified port
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

threads = []
connectedUsers = []

def removeUser(IP):
    i = 0
    for adress in connectedUsers:
        if adress[0] == IP:
            connectedUsers.remove(adress)
            serverSocket.sendto(str("user removed").encode(), adress)
        i += 1

def sendToAllUsers(msg, exceptionIP = "0"):
    for adress in connectedUsers:
        if adress[0] != exceptionIP:
            serverSocket.sendto(msg.encode(), adress)

def sendToOneUser(msg, directiveIP):
    for adress in connectedUsers:
        if adress[0] == directiveIP:
            serverSocket.sendto(msg.encode(), adress)


def serverThread():
    global SERVER_RUNNING
    global decodeMsg
    print("Server Thread running!")
    while SERVER_RUNNING:
        msg, clientAddress = serverSocket.recvfrom(2048)
        decodeMsg = msg.decode()

        if decodeMsg.find("NEW") != -1:
            exists = False
            
            for adress in connectedUsers:
                if adress[0] == clientAddress[0]:
                    exists = True
            
            if exists == False:
                print("User connected:", clientAddress)
                connectedUsers.append(clientAddress)

                userStr = "connected;" + clientAddress[0]
                sendToAllUsers(userStr,  clientAddress[0])

                #Update connecting users about current users on server
                allUsers = "ALL;"
                #Check if only one person
                if len(connectedUsers) != 1:
                    for ip in connectedUsers:
                        if ip[0] != clientAddress[0]:
                            allUsers += ip[0] + ";"    
                    allUsers = allUsers[:-1]

                if allUsers != "ALL;":
                    sendToOneUser(allUsers, clientAddress[0])
        elif decodeMsg.find("QUIT") != -1:
            print("User disconnected:", clientAddress)
            removeUser(clientAddress[0])
            userStr = "disconnected;" + clientAddress[0]
            sendToAllUsers(userStr, clientAddress[0])
            sendToOneUser("QUIT", clientAddress[0])
        elif decodeMsg.find("P;") != -1:
            modifiedMessage = "P;" + clientAddress[0] + ";"  + decodeMsg[2:] 
            sendToAllUsers(modifiedMessage, clientAddress[0])
            
           
    return

helpMessage = '''All commands:
                    quit - turn server off
                    list - gives a list of all connected users
                    '''

if __name__ == '__main__':
    print ("The UDP server is ready to recieve")

    t = threading.Thread(target=serverThread)
    threads.append(t)
    t.start()

    
    print("Input Thread Running!")
    while SERVER_RUNNING:
        msg = input("Input:")
        if msg == "quit":
            sendToAllUsers("QUIT")
            SERVER_RUNNING = False
            print("Shutting down...")
            serverSocket.sendto(str("TURN OFF").encode(), ('127.0.0.1', 8080))
        elif msg == "list":
            print(connectedUsers)
        elif msg == "help":
            print(helpMessage)
        

    t.join()

    serverSocket.close()
    print("Shutdown complete!")