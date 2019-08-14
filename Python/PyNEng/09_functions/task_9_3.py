# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

###

config_filename = 'config_sw1.txt'

def get_int_vlan_map (config_filename):
    access_vlan_map = {}
    trunk_vlan_map = {}
    with open(config_filename) as config:
        for line in config:
            if line.startswith('interface'):
                interface = line.split()[-1]
            try:
                if 'switchport access vlan' in line:
                    access_vlan_map.update({interface: int(line.split()[-1])})
                elif 'switchport trunk allowed' in line:
                    trunk_vlan_map.update({interface: [int(vlan) for vlan in line.split()[-1].split(',')]})
            except ValueError:
                pass
    return access_vlan_map, trunk_vlan_map

print(get_int_vlan_map (config_filename))
