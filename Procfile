release: python manage.py migrate
web: gunicorn sort_proj.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput