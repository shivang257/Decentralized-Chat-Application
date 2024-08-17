import threading
import socket

host = 'localhost'
port =  59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port)) 

server.listen() # listens incoming connections

clients = [] # names
aliases = [] # nicknames   


def broadcast(message):
    """
    This function sends a msg from the  
    server to all the connected clients.
    """
    # simply iterate through all the clients in list 
    for client in clients:

        # and send each client a message
        client.send(message)



def handle_client(client):
    """
    This function handles client connections, 
    When client A connects to the server and 
    sends a msg to client B, B should get msg
    """
    while True:
        try:
            # Storing received message
            MSG_SIZE = 1024
            message = client.recv(MSG_SIZE) # 1024 is the max. bytes, a server receives from client 
            broadcast(message)
            # If a message receives, invoke broadcast

        except:
            index = clients.index(client) # Gives index of failure client
            broadcast(f'{alias} has left the server!'.encode('utf-8'))
            clients.remove(client) # Removes client from clients list
            client.close()
        
            # Removing alias of failure client from the aliases list
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8')) # Need to send them in bytes
            aliases.remove(alias)
            break

# Main function to receive the clients connection
def receive():
    while True:
        print('Aptcha is running and listening ...')
        client, address = server.accept() # returns new socket and address of the client

        print(f'Connection is established with {str(address)}')

        # Now we are sending this client to know its alias
        client.send('alias?'.encode('utf-8'))

        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)

        # Broadcast that alias has connected to the chat room
        broadcast(f"{alias} has connected to the chat room".encode('utf-8'))

        client.send('\n you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target = handle_client, args = (client,))
        thread.start()

if __name__ == "__main__":
    receive()