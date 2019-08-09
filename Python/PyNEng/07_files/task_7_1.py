# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

###

with open('ospf.txt', 'r') as ospf:
    ospf_conf = ospf.readlines()

template = '''Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}'''

for line in ospf_conf:
    line = line.replace(',', '').replace('[','').replace(']','').replace('O', 'OSPF').split()
    print(template.format(line[0], line[1], line[2], line[4], line[5], line[6]))
    print(6 * '=')
