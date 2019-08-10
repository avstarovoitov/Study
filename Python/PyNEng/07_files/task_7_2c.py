# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

###

from sys import argv

file_name_src = argv[1]
file_name_dst = argv[2]

with open(file_name_src, 'r') as src, open(file_name_dst, 'w') as dst:
    for line in src.readlines():
        if (ignore[0] not in line) and (ignore[1] not in line) and (ignore[2] not in line):
            dst.write(line)
