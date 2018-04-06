sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
cp /home/box/web/etc/hello.py /home/box/etc/hello.py
gunicorn -c etc/hello.py web/hello:application
