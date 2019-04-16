# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

IP = '192.168.3.1'
IP = IP.split('.')
a, b, c, d = [int(i) for i in IP]
template = '''
{a:<10}{b:<10}{c:<10}{d:<10}
{a:08b}  {b:08b}  {c:08b}  {d:08b}
'''
print(template.format(a = a, b = b, c = c, d = d))