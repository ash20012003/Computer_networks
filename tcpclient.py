import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1',12345))
payload = 'Hey Server'
while True:
    client.send(payload.encode('utf-8'))
    server_data = client.recv(1024)
    print(str(server_data))
    more = input("continue??")
    if more.lower()=='y':
        payload = input("Enter payload")
    else:
        break
client.close()
