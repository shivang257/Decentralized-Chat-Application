import threading
import socket

alias = input('Choose an alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Needs tuple inside tuple
client.connect(('127.0.0.1', 59000)) 

def client_receive():
    """
    Function to handle receiving messages from the server.
    Runs in a separate thread to continuously listen for incoming messages.
    """
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            # If server asks for alias, send the alias
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            # If any error, print error message & close connection
            print('Error!')
            client.close()
            break

def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target = client_receive)
receive_thread.start()

send_thread = threading.Thread(target = client_send)
send_thread.start()