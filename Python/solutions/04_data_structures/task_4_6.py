# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

template = '''
{:30}{}
{:30}{}
{:30}{}
{:30}{}
{:30}{}
{:30}{}
'''
ospf_route = ospf_route.replace('O', 'OSPF').replace('[', '').replace(']', '').replace(',', '').replace('via', '').split()
a, b, c, d, e, f = ospf_route
print(template.format('Protocol:', a, 'Prefix:', b, 'AD/Metric:', c, 'Next-Hop:', d, 'Last update:', e, 'Outbound Interface:', f))
