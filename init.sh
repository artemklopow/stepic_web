sudo ln -s ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default.conf;
sudo nginx -t;
sudo /etc/init.d/nginx restart;
