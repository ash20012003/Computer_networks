import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
''' we can also use scket.socket(socket.AF_INET, socket.SOCK_STREAM)'''
server.bind(('127.0.0.1',12345))
server.listen(5)

while True:
    print("Server waiting for connection...")
    conn,addr = server.accept()
    print("client connceted from",addr)
    while True:
        receive_data = conn.recv(1024)
        if not receive_data:
            break
        print("CLIENT -> ",receive_data.decode())
        conn.send(bytes("SERVER -> ",'utf-8'))
        print("Exited by user")
    conn.close()
server.close()