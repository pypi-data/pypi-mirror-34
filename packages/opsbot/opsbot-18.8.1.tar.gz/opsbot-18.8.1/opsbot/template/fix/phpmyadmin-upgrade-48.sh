mv /usr/share/phpmyadmin /usr/share/phpmyadmin_old
wget  https://files.phpmyadmin.net/phpMyAdmin/4.8.2/phpMyAdmin-4.8.2-english.tar.gz
tar -xvzf phpMyAdmin-4.8.2-english.tar.gz
mv phpMyAdmin-4.8.2-english /usr/share/phpmyadmin
rm phpMyAdmin-4.8.2-english.tar.gz
cp /etc/phpmyadmin/config.inc.php  /usr/share/phpmyadmin
mkdir /usr/share/phpmyadmin/tmp
chown www-data:www-data /usr/share/phpmyadmin/tmp
rm -rf /usr/share/phpmyadmin_old