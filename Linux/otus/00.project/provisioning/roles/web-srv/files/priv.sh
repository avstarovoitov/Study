#!/bin/bash

sudo chown apache:apache -R /var/www/html/
sudo chcon -t httpd_sys_content_t /var/www/html/ -R

cd /var/www/html/
find . -type f -exec chmod 0644 {} \;
find . -type d -exec chmod 0755 {} \;

sudo chcon -t httpd_sys_rw_content_t app/admin/import-export/upload/ -R
sudo chcon -t httpd_sys_rw_content_t app/subnets/import-subnet/upload/ -R
