sudo ln -sf home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo nginx -t
sudo /etc/init.d/nginx restart
