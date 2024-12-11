import socket

def client_program():
   
    ip_host = '127.0.0.1'  
    port = 7090

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_host, port))
    
    filename = 'file.txt'  
    with open(filename, 'wb') as transfer_file:
        print("Receiving file from the server...")
        while True:
            content = client_socket.recv(1024)
            if not content:
                print("Error")
                break  
            transfer_file.write(content)  
    print("Received file successfully")
    client_socket.close()

if __name__ == '__main__':
    client_program()
