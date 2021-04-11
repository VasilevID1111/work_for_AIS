# test-server.py
import socket
import sys

# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту
server_address = ('localhost', 10112)
print('Старт сервера на {} порт {}'.format(*server_address))
sock.bind(server_address)

# Слушаем входящие подключения
sock.listen(1)

while True:
    # ждем соединения
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    print('Подключено к:', client_address)
    data1 = connection.recv(16)
    data1 = data1.decode()
    print(f'Получено: {data1}')
    connection.close()