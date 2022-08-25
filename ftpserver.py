import socket

ip = '127.0.0.1'
port = 42069

def main():
    print("[STARTING] server is starting.\n")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()
    print('[LISTENING] server is listening.\n')

    while True:
        conn, addr = server.accept()
        print(f"[NEW CONN] {addr} connected.")

        filename = conn.recv(1024).decode("utf-8")
        print("[RECEIVED].")
        file = open(filename,'w')
        conn.send("Filename received".encode("utf-8"))

        data = conn.recv(1024).decode("utf-8")
        print(f"[RECV] data received")
        file.write(data)
        conn.send("File data received".encode("utf-8"))

        file.close()
        conn.close()
        print("[DISCONNECTED]")

if __name__=='__main__':
    main()