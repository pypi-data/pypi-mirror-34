encryptedPass=`openssl passwd -crypt "${username}_unix_password"`
useradd {username} -M -p $encryptedPass
