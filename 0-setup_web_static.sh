#!/usr/bin/env bash
# scripts that can Prepare the  web servers

# install nginx
apt-get update -y
apt-get install nginx -y

# create directorys and files...
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "My Web Static Server" > /data/web_static/releases/test/index.html

# my symbolic link for file
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -hR ubuntu:ubuntu /data/

hbnb_static=$"\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"

sed -i '/^}$/i \ '"$hbnb_static" /etc/nginx/sites-available/default

apt install ufw -y
ufw allow 'NGINX HTTP'
service nginx restart
