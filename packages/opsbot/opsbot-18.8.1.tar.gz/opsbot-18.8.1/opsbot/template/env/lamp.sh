#will set password later
debconf-set-selections <<< "mysql-server mysql-server/root_password password $root_mysql_password"
debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $root_mysql_password"
apt install -y lamp-server^
#enable mod rewrite
a2enmod rewrite

#
service apache2 start
service mysql start
debconf-set-selections <<< "phpmyadmin phpmyadmin/dbconfig-install boolean true"
debconf-set-selections <<< "phpmyadmin phpmyadmin/app-password-confirm password $root_mysql_password"
debconf-set-selections <<< "phpmyadmin phpmyadmin/mysql/admin-pass password $root_mysql_password"
debconf-set-selections <<< "phpmyadmin phpmyadmin/mysql/app-pass password $phpmyadmin_mysql_password"
debconf-set-selections <<< "phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2"
apt install -y phpmyadmin