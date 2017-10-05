import socket
host = "localhost"
port = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))
client.send("GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
response = client.recv(4096)
print(response)
