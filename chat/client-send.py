import socket

host = "localhost"
port = 8080

name = input("Name: ")
text = input("Text: ")

message = name,text

str_message = ': '.join(message)
b_message = str.encode(str_message)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b_message, (host,port))
