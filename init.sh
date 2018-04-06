mkdir etc
cp /home/box/web/etc/hello.py /home/box/etc/hello.py
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicort restart
gunicorn -c etc/hello.py hello:application &
