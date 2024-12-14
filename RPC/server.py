from xmlrpc.server import SimpleXMLRPCServer
import os

def get_file_content():
    file_path = r"E:\distrbuted system\task1\host\file.txt"
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            print(f"File is sending.")
            return file.read()
    else:
        print("Error")
        return "Error"

if __name__ == "__main__":
    host_ip = "127.0.0.1"
    port_number = 7090
    server = SimpleXMLRPCServer((host_ip, port_number))
    print(f"The RPC Server is running")
    server.register_function(get_file_content, "get_file_content")
    server.serve_forever()
