import socket

host = "localhost"
port = 8080
message = b"Welcome to the Jungle"

print("UDP target host:", host)
print("UDP target port:", port)
print("message:", message)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(message, (host,port))
