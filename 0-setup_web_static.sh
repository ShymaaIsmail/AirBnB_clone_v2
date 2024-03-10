#!/usr/bin/env bash
# SETUP WEB STATIC
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
        <head>
        </head>
        <body>
            Holberton School
        </body>
    </html>" > "/data/web_static/releases/test/index.html"
ln -s -f  /data/web_static/releases/test/ /data/web_static/current
chown  -R ubuntu:ubuntu /data/
NGINX_CONF="/etc/nginx/sites-available/default"
NEW_LOCATION="
 location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
}"
if grep -q "location /hbnb_static" "$NGINX_CONF"; then
    echo "Location block already exists. Skipping."
else
    if grep -q "location / {" "$NGINX_CONF"; then
        sed -i "/location \/ {/a $(echo $NEW_LOCATION | sed 's/\//\\\//g')" "$NGINX_CONF"
    else
        sed -i "/server {/a $(echo $NEW_LOCATION | sed 's/\//\\\//g')" "$NGINX_CONF"
    fi
    echo "New location block added successfully."
fi
service nginx restart
