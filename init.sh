sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo gunicorn -c hello.py hello:app

sudo /etc/init.d/mysql start

sudo gunicorn -c /home/box/web/etc/django-gunicorn.conf ask.wsgi:application
sudo /etc/init.d/gunicorn restart

