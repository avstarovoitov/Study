# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

###

ipaddr = input('Введите IP-адрес в формате 10.0.1.1: ')
ipaddr_check = ipaddr.split('.')

if len(ipaddr_check) != 4:
    print('Неправильный IP-адрес')
else:
    for octet in ipaddr_check:
        if not 0 <= int(octet) <= 255:
            print('Неправильный IP-адрес')
            break
    else:
        if 1 <= int(ipaddr.split('.')[0]) <= 223:
            print('unicast')
        elif 224 <= int(ipaddr.split('.')[0]) <= 239:
            print('multicast')
        elif ipaddr == '255.255.255.255':
            print('local broadcast')
        elif ipaddr == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
