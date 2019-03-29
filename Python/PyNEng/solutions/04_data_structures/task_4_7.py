# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'

MAC = MAC.split(':')
a, b, c = MAC
print(str(bin(int(a, 16))).replace('0b', ''), str(bin(int(b, 16))).replace('0b', ''), str(bin(int(c, 16))).replace('0b', ''))
