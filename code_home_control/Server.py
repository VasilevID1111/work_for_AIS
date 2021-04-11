# test-server.py
import socket
import sys

# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту
server_address112 = ('localhost', 10112)
server_address = ('localhost', 10000)
server_address1 = ('localhost', 10001)
server_address2 = ('localhost', 10002)
server_address3 = ('localhost', 10003)
server_address4 = ('localhost', 10004)
server_address5 = ('localhost', 10005)
print('Старт сервера на {} порт {}'.format(*server_address))
print('Старт сервера на {} порт {}'.format(*server_address1))
print('Старт сервера на {} порт {}'.format(*server_address2))
print('Старт сервера на {} порт {}'.format(*server_address3))
print('Старт сервера на {} порт {}'.format(*server_address4))
sock.bind(server_address)
sock1.bind(server_address1)
sock2.bind(server_address2)
sock3.bind(server_address3)
sock4.bind(server_address4)

# Слушаем входящие подключения
sock.listen(1)
sock1.listen(1)
sock2.listen(1)
sock3.listen(1)
sock4.listen(1)

while True:
    # ждем соединения
    print('Ожидание соединения...')
    connection, server_sensor = sock.accept()
    connection_p, p_sensor = sock1.accept()
    connection_t, t_sensor = sock2.accept()
    connection_gm, gm_sensor = sock3.accept()
    connection_ga, ga_sensor = sock4.accept()
    # попытка обработки данных датчиков
    try:
        print('Подключено к датчику температуры:', p_sensor)
        print('Подключено к датчику давления:', t_sensor)
        print('Подключено к датчику GPSM:', gm_sensor)
        print('Подключено к датчику GPSA:', ga_sensor)
        print('Подключено к датчику сервера:', server_sensor)
        # Принимаем данные порциями и отправляем ответ о соединении
        while True:
           # обмен данными с датчиком давления
            try:
                data_p = connection_p.recv(16)  
                data_p = int(data_p.decode())
                data = '1'
                print('Обработка данных датчика давления')
                # проверка давления
                if data_p < 710:
                    sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock0.connect(server_address112)
                    mess = 'sos break-in'
                    print('\nОтправляем экстренное сообщение о взломе\n')
                    sock0.sendall(mess.encode())
                    sock0.close()
                print(f'Получено: {data_p}')
                print('Отправка датчику температуры пакетов.\n')
                connection_p.sendall(data.encode())
           # отправка ошибки датчику сервера
            except:
                try:
                    data_s = connection.recv(16)
                    data = 'offline pres'
                    if data:
                        print('Датчик сервера онлайн')
                        print('Ответ датчику сервера\n')
                        connection.send(data.encode())
                except:
                    print('\nПотеряно соединение датчик сервера, разрыв соединений...')
                connection.close()
                connection_p.close()
                connection_t.close()
                connection_gm.close()
                connection_ga.close()
                print('Потеряно соединение давления, разрыв соединений...\n')
                break
           # обмен данными с датчиком температуры
            try:
                data_t = connection_t.recv(8)
                data_t = float(data_t.decode())
                data = '1'
                print('Обработка данных датчика температуры')
                print(f'Получено: {data_t}')
                # проверка температуры
                if data_t > 35.0:
                    sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock0.connect(server_address112)
                    print('\nОтправляем экстренное сообщение о пожаре\n')
                    mess = 'sos fire'
                    sock0.sendall(mess.encode())
                    sock0.close()
                print('Отправка датчику давления пакетов.\n')
                connection_t.sendall(data.encode())
           # отправка ошибки датчику сервера
            except:
                # отправка ошибки датчику сервера
                try:
                    data_s = connection.recv(8)
                    data = 'offline temp'
                    if data:
                        print('Датчик сервера онлайн')
                        print('Ответ датчику сервера\n')
                        connection.send(data.encode())
                except:
                    print('\nПотеряно соединение датчик сервера')
                connection.close()
                connection_p.close()
                connection_t.close()
                connection_gm.close()
                connection_ga.close()
                print('Потеряно соединение с датчиком температуры, разрыв соединений...\n')
                break
            # обмен данными с датчиком GPSM
            try:
                data_gm = connection_gm.recv(8)
                data_gm= data_gm.decode()
                data = '1'
                print('Обработка данных датчика GPSM')
                sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock0.connect(server_address5)
                if data_gm == '0':
                    mess = 'open_door'
                else:
                    mess = 'close_door'
                sock0.sendall(mess.encode())
                sock0.close()
                print(f'Получено: {data_gm}')
                print('Отправка датчику давления пакетов.\n')
                connection_gm.sendall(data.encode())
           # отправка ошибки датчику сервера
            except:
                # отправка ошибки датчику сервера
                try:
                    data_s = connection.recv(8)
                    data = 'offline GPSM'
                    if data:
                        print('Датчик сервера онлайн')
                        print('Ответ датчику сервера\n')
                        connection.send(data.encode())
                except:
                    print('\nПотеряно соединение датчик сервера')
                connection.close()
                connection_p.close()
                connection_t.close()
                connection_gm.close()
                connection_ga.close()
                print('Потеряно соединение с датчиком GPS1, разрыв соединений...\n')
                break 
            # обмен данными с датчиком GPSA
            try:
                data_ga = connection_ga.recv(8)
                data_ga = data_ga.decode()
                data = '1'
                print('Обработка данных датчика GPSA')
                sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock0.connect(server_address5)
                if data_ga == '0':
                    mess = 'open_door_ga'
                else:
                    mess = 'close_door_ga'
                sock0.sendall(mess.encode())
                sock0.close()
                print(f'Получено: {data_ga}')
                print('Отправка датчику давления пакетов.\n')
                connection_ga.sendall(data.encode())
           # отправка ошибки датчику сервера
            except:
                # отправка ошибки датчику сервера
                try:
                    data_s = connection.recv(8)
                    data = 'offline GPSM'
                    if data:
                        print('Датчик сервера онлайн')
                        print('Ответ датчику сервера\n')
                        connection.send(data.encode())
                except:
                    print('\nПотеряно соединение датчик сервера')
                connection.close()
                connection_p.close()
                connection_t.close()
                connection_gm.close()
                connection_ga.close()
                print('Потеряно соединение с датчиком GPS2, разрыв соединений...\n')
                break
           # обмен данными с датчиком сервера
            try:
                data_s = connection.recv(1)
                data = 'online all s'
                if data:
                    print('Датчик сервера онлайн')
                    print('Ответ датчику сервера\n')
                    connection.send(data.encode())
           # ошибка датчика сервера
            except:
                print('\nПотеряно соединение датчик сервера, разрыв соединений...')
                connection.close()
                connection_p.close()
                connection_t.close()
                connection_gm.close()
                connection_ga.close()
                break
    # Ошибка обработки данных, переподключение к датчикам
    except:
        connection.close()
        connection_p.close()
        connection_t.close()
        connection_gm.close()
        connection_ga.close()
        print('Ошибка обработки данных, переподключение к датчикам...\n')