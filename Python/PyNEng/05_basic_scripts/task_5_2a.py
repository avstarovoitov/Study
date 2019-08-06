# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

###

network, mask = input('Enter network and mask like 10.1.1.0/24: ').split('/')
mask_bin = (int(mask) * '1') + ((32 - int(mask)) * '0')
mask_bit = 32 - int(mask)
mask_dec = [int(mask_bin[:8], 2), int(mask_bin[8:16], 2), int(mask_bin[16:24], 2), int(mask_bin[24:32], 2)]
network = network.split('.')
network_in_dec = '{:08b}'.format(int(network[0])) + '{:08b}'.format(int(network[1])) + '{:08b}'.format(int(network[2])) + '{:08b}'.format(int(network[3]))
network_in_dec = network_in_dec[:int(mask)] + ('0' * mask_bit)
network = [int(network_in_dec[:8], 2), int(network_in_dec[8:16], 2), int(network_in_dec[16:24], 2), int(network_in_dec[24:32], 2)]

template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

Mask:
{8:}
{4:<8} {5:<8} {6:<8} {7:<8}
{4:08b} {5:08b} {6:08b} {7:08b}
'''
a, b, c, d = network
e, f, g, h = mask_dec
print(template.format(a, b, c, d, e, f, g, h, '/' + mask))

