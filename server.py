import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 3030))
s.listen(1)
conn, addr = s.accept() # Метод который принимает входящее соединение.

while True:
	data = conn.recv(1024) # Получаем данные из сокета.r
	if not data:
		break
	conn.sendall(data) # Отправляем данные в сокет.
	print(data.decode('utf-8'))
conn.close()