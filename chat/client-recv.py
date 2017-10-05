import socket
import sys

# variables
host = "localhost"
port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.bind((host,port))

while True:
	data, addr = client.recvfrom(4096)
	print(data.decode('utf-8'))
