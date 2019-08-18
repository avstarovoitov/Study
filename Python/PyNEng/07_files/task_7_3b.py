# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

###

with open('CAM_table.txt') as cam:
    lines = []
    for line in cam:
        try:
            if line[1].isdigit():
                lines.append(line)
        except IndexError:
            pass
vlans = sorted({int(vlan[1:5]) for vlan in lines})
input_vlan = int(input('Enter vlan number from ' + str(vlans) + ' : '))
output_dict = dict.fromkeys(vlans)

for line in lines:
    if not output_dict[int(line[1:5])]:
        output_dict[int(line[1:5])] = [line.rstrip()]
    else:
        temp_value = output_dict[int(line[1:5])]
        temp_value.append(line)
        output_dict[int(line[1:5])] = temp_value

for line in output_dict[input_vlan]:
    print(' {:<8} {:<16} {}'.format(line.split()[0], line.split()[1], line.split()[3]))
