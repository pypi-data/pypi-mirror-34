VHOST_PATH="/etc/apache2/sites-available/{site}.conf"
cat > $VHOST_PATH  <<EOL
<VirtualHost *:80>
    ServerName {site}

    DocumentRoot /var/www/{site}/{path}

    <Directory /var/www/{site}/{path}>
        AllowOverride All
    </Directory>

    ErrorLog  /var/www/{site}/error.log"
    CustomLog /var/www/{site}/access.log combined"

</VirtualHost>
EOL