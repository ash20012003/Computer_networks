import socket

ip = '127.0.0.1'
port = 42069

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    file = open("./data.txt", 'r')
    data = file.read()

    client.send('./data.txt'.encode("utf-8"))
    msg = client.recv(1024).decode("utf-8")
    print(f"[SERVER] {msg}")

    client.send(data.encode("utf-8"))

    msg = client.recv(1024).decode("utf-8")
    print(f"[SERVER] {msg}")

    file.close()
    client.close()
    print("[CLOSED]")

if __name__ == "__main__":
    main()