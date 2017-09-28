import socket

host = "localhost"
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))
client.send(bytes("GET / HTTP/1.1\r\nHost: localhost\r\n\r\n", "utf-8"))

response = client.recv(4096)
print(response)
