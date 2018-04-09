sudo pip3 install --upgrade django
sudo ln -sf python3 /usr/bin/python
sudo cp /home/box/web/etc/gunicorn-debian /usr/sbin/gunicorn-debian
sudo cp /home/box/web/etc/gunicorn /usr/bin/gunicorn
sudo cp /home/box/web/etc/gunicorn_django /usr/bin/gunicorn_django
sudo cp /home/box/web/etc/gunicorn_paster /usr/bin/gunicorn_paster



sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
sudo gunicorn -c /etc/gunicorn.d/hello.py hello:application
