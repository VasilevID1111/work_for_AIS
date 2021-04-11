# test-client.py
import socket
import sys
import time 
import random

# СоздаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаем сокет к порту, через который прослушивается сервер
server_address = ('localhost', 10001)

while True:
            try:
                sock.connect(server_address)
                print('Подключено к {} порт {}'.format(*server_address))
                break
            except:
                print('Нет ответа, ожидание...')
                time.sleep(5)

while True:
    time.sleep(2)
    try:
        # Отправка данных
        p_data = 740 + random.gauss(0, 15)
        mess = str(int(p_data))
        sock.sendall(mess.encode())
    
        # Смотрим ответ
        sock.recv(1)
    except:
        print('\nСервер не ответил, попытка переподключения...')
        sock.close()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                sock.connect(server_address)
                print('Подключено к {} порт {}'.format(*server_address))
                break
            except:
                print('Нет ответа, ожидание...')
                time.sleep(5)
        pass