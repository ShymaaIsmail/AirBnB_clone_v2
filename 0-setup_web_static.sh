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
ln -s -f /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

NGINX_CONF="/etc/nginx/sites-available/default"
search_text="location \/"
line_number=$(( $(sed -n "/$search_text/=" $NGINX_CONF | head -n 1) - 1 ))
sudo sed -i "${line_number}s/.*/\\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t\ttry_files \$uri \$uri\/ =404;\n\t}/" $NGINX_CONF
service nginx restart
