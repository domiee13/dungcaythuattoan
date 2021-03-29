import socket
host = "localhost"
port = 8000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
while(True):
    client,addr = s.accept()
    try:
        print("Connected by",addr)
        while True:
            data = client.recv(1024)
            str_data = data.decode("utf8")
            if str_data=="exit":
                break
            print("Client: "+str_data)
            # msg = input("Server: ")
            # client.send(bytes(msg.upper(),"utf8"))
            client.send(bytes(str_data.upper(),"utf8"))
    finally:
        client.close()