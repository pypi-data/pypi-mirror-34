mkdir /var/www/{site}
chown -R {owner}:www-data /var/www/{site}
chmod g+s /var/www/{site}
chmod o-rwx /var/www/{site}

touch /var/www/{site}/access-{site}.log
touch /var/www/{site}/error-{site}.log