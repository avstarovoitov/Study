#!/bin/bash

# Download source code for nmap
yumdownloader --source mc

# Unpack rpm
rpm -i /home/vagrant/mc*

# Change configuration
sed -i -e s/--enable-vfs-smb/--disable-vfs-smb/g /root/rpmbuild/SPECS/mc.spec
sed -i -e s/--enable-vfs-sftp/--disable-vfs-sftp/g /root/rpmbuild/SPECS/mc.spec
sed -i -e s/--enable-vfs-mcfs/--disable-vfs-mcfs/g /root/rpmbuild/SPECS/mc.spec

# Install dependencies
yum-builddep -y /root/rpmbuild/SPECS/mc.spec
yum -y install  gcc gcc-c++

# Create RPM
rpmbuild -bb /root/rpmbuild/SPECS/mc.spec

# Install web server
yum -y install httpd
rm -f /etc/httpd/conf.d/welcome.conf

# Create repo
mkdir /var/www/html/repo
cp /root/rpmbuild/RPMS/x86_64/mc* /var/www/html/repo/
createrepo /var/www/html/repo/

# Start web-server
systemctl start httpd
systemctl enable httpd

# Create repo file
cat >> /etc/yum.repos.d/otus.repo << EOF
[otus]
name=otus-linux
baseurl=http://localhost/repo
gpgcheck=0
enabled=1
EOF

# Install mc
yum --disablerepo=* --enablerepo=otus install -y  mc
