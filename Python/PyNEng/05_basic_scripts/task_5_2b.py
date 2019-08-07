# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

###

from sys import argv

network, mask = argv[1].split('/')
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

