# test-client.py
import socket
import sys
import time 

# СоздаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

time_error = 0

# Подключаем сокет к порту, через который прослушивается сервер
server_address = ('localhost', 10000)
while True:
    print('Попытка подключиться к {} по порту {}'.format(*server_address))
    try:
        sock.connect(server_address)
        print('\nПодключено к {} порт {}'.format(*server_address))
        log_server = open('C:/Users/levfe/OneDrive/Рабочий стол/log_server.txt', 'a+')
        time_error = 0
        break
    except:
        print('Нет ответа, ожидание...')                
        log_server = open('C:/Users/levfe/OneDrive/Рабочий стол/log_server.txt', 'a+')
        log_server.write('{} {} \n'.format('offline serw', time.asctime()))
        log_server.close()
        time.sleep(5)
        time_error+=1
    if time_error>3:
        log_server = open('C:/Users/levfe/OneDrive/Рабочий стол/log_server.txt', 'a+')
        log_server.write('{} {} \n'.format('server down ', time.asctime()))
        log_server.close()
        print('\nСервер не отвечает более 20 секунд')
        sys.exit(1)

while True:
    time.sleep(2)
    try:
        mess = '1'
        sock.send(mess.encode())
        log_server.write('{} {} \n'.format(sock.recv(16).decode(), time.asctime()))
        time_error = 0
    except:
        print('\nНет ответа от сервера')
        log_server.close()
        sock.close()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            print('Попытка подключиться к {} по порту {}'.format(*server_address))
            try:
                sock.connect(server_address)
                print('\nПодключено к {} порт {}'.format(*server_address))
                log_server = open('C:/Users/levfe/OneDrive/Рабочий стол/log_server.txt', 'a+')
                time_error = 0
                break
            except:
                print('Нет ответа, ожидание...')                
                log_server = open('C:/Users/levfe/OneDrive/Рабочий стол/log_server.txt', 'a+')
                log_server.write('{} {} \n'.format('offline serw', time.asctime()))
                log_server.close()
                time.sleep(5)
                time_error+=1
            if time_error>3:
                log_server = open('C:/Users/levfe/OneDrive/Рабочий стол/log_server.txt', 'a+')
                log_server.write('{} {} \n'.format('server down ', time.asctime()))
                log_server.close()
                print('\nСервер не отвечает более 20 секунд')
                sys.exit(1)