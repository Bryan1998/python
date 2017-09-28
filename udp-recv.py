import socket

# variables
host = "localhost"
port = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.bind((host,port))

while True:
	data, addr = client.recvfrom(4096)
	print("received message:", data)
