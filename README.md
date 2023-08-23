# django-shop

## program purpose

An online store website written with django

## how to work

you can create a admin user with execute this command Where the manage.py is:

python manage.py createsuperuser

and with this super user you can login in admin panel in 127.0.0.1:80/admin

in admin panel you can add product and category to show in your website

and you must build a celery worker with this command :

celery -A DjangoShop worker -l INFO

and for celery beat:

celery -A DjangoShop worker --beat --scheduler django --loglevel=info

and you must set arvan access key or remove storage app from setting.py
