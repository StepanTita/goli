release: python manage.py makemigrations && python manage.py migrate
web: gunicorn goli.wsgi:application