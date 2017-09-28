import socket

host = "localhost"
port = 8000
message = "Welcome to the Jungle"

print("UDP target host:", host)
print("UDP target port:", port)
print("message:", message)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(bytes(message, "utf-8"), (host,port))
