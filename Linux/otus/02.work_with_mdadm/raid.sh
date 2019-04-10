#!/bin/bash

echo "Будем собираем RAID-10 из 4 дисков sd{b,c,d,e}"

echo "Очищаем суперблоки:"
mdadm --zero-superblock  --force /dev/sd{b,c,d,e}

echo "собираем RAID-10"
mdadm --create --verbose /dev/md0 -l 10 -n 4 /dev/sd{b,c,d,e}
echo "RAID собран"

echo "Проверяем RAID"
cat /proc/mdstat

echo "Прописываем конфигурацию в автозагрузку"
echo "DEVICE partitions" > /etc/mdadm.conf
mdadm --detail --scan --verbose | awk '/ARRAY/ {print}' >> /etc/mdadm.conf
echo "Готово!"

