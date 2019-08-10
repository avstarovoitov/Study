# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


###

from sys import argv

file_name = argv[1]

with open(file_name, 'r') as config:
    for line in config.readlines():
        if not line.startswith('!') and (ignore[0] not in line) and (ignore[1] not in line) and (ignore[2] not in line):
            print(line.rstrip())
