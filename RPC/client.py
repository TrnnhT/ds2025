import xmlrpc.client

def request_file():
    server_url = "http://127.0.0.1:7090"
    print("Connecting to RPC server...")
    client = xmlrpc.client.ServerProxy(server_url)

    print("Requesting file content from the server...")
    file_data = client.get_file_content()

    if isinstance(file_data, str):
        if file_data == "File not found":
            print("Error")
    else:
        outputt = "received_file.txt"
        with open(outputt, "wb") as file:
            file.write(file_data)
        print(f"Successful")

if __name__ == "__main__":
    request_file()
