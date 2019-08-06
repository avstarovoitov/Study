# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
network, mask = input('Enter network and mask like 10.1.1.0/24: ').split('/')
mask_bin = (int(mask) * '1') + ((32 - int(mask)) * '0')
mask_dec = [int(mask_bin[:8], 2), int(mask_bin[8:16], 2), int(mask_bin[16:24], 2), int(mask_bin[24:32], 2)]
network = network.split('.')

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
print(template.format(int(a), int(b), int(c), int(d), e, f, g, h, '/' + mask))