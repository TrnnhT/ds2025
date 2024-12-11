import socket
import os

def host_program():

    ip_host = '127.0.0.1'  
    port = 1001
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip_host, port))
    server_socket.listen(1)
    print(f"The server is listening on {ip_host}:{port}")
    
    connect, address = server_socket.accept()
    print(f"Connection from {address} has been established.")

    filename = r'E:\distrbuted system\task1\host\file.txt' 
    
    if os.path.exists(filename):
        try:
            with open(filename, 'rb') as file:
                print(f"Sending file: {filename}")

                while True:
                    data = file.read(1024)
                    if not data:
                        break  
                    connect.send(data)  
                    
            print(f"File {filename} sent successfully!")
            
        except Exception as e:
            print(f"Error sending file: {e}")
            connect.send(b"Error sending file!")
    else:
        print(f"File {filename} not found!")
        connect.send(b"File not found!") 
    
    connect.close()
    server_socket.close()  

if __name__ == '__main__':
    host_program()
