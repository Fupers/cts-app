run:
	python3 manage.py runserver 0.0.0.0:5050

celery:
	celery -A backend worker --loglevel=info

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

createsuperuser:
	python3 manage.py createsuperuser