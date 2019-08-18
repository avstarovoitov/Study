# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

### def not allowed by rule ^

def cut_line(string):
    return int(string[1:5])
lines = []
with open('CAM_table.txt') as cam:
    for line in cam:
        try:
            if line[1].isdigit():
                lines.append(line)
        except IndexError:
            pass
lines = sorted(lines, key = cut_line)
for line in lines:
    line = line.rstrip().split()
    print(' {:<8} {:<16} {}'.format(line[0], line[1], line[3]))
