# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

###

ipaddr = input('Введите IP-адрес в формате 10.0.1.1: ')
ipaddr_check = ipaddr.split('.')
ipaddr_is_correct = False

while not ipaddr_is_correct:
    if (len(ipaddr_check) != 4):
        print('Неправильный IP-адрес')
        ipaddr = input('Введите IP-адрес ещё раз: ')
        ipaddr_check = ipaddr.split('.')
        continue
    else:
        counter = 0
        for octet in ipaddr_check:
            try:
                if not 0 <= int(octet) <= 255:
                    print('Неправильный IP-адрес')
                    ipaddr = input('Введите IP-адрес ещё раз: ')
                    ipaddr_check = ipaddr.split('.')
                    continue
                else:
                    counter += 1
            except ValueError:
                print('Неправильный IP-адрес')
                ipaddr = input('Введите IP-адрес ещё раз: ')
                ipaddr_check = ipaddr.split('.')
                continue
        if counter == 4:
            ipaddr_is_correct = True
        else:
            continue

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

