import socket
import encrypt
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

inp = input("Input message: ")

# Connect with server
s.connect(('localhost', 3030))

# Encrypt method call
inp = encrypt.encrypt(inp)

s.sendall(inp.encode('utf-8'))
data = s.recv(1024)
s.close()