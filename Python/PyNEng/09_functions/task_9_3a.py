# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

###

def get_int_vlan_map (config_filename):
    access_vlan_map = {}
    trunk_vlan_map = {}
    default_vlan = 1
    with open(config_filename) as config:
        for line in config:
            if line.startswith('interface FastEthernet'):
                interface = line.split()[-1]
                access_vlan_map.update({interface: default_vlan})
            if 'switchport access vlan' in line:
                access_vlan_map[interface] = int(line.split()[-1])
            elif 'switchport trunk allowed' in line:
                del access_vlan_map[interface]
                trunk_vlan_map.update({interface: [int(vlan) for vlan in line.split()[-1].split(',')]})
    return access_vlan_map, trunk_vlan_map

print(get_int_vlan_map('config_sw2.txt'))
