migrate:
	python manage.py makemigrations
	python manage.py migrate

collect-static:
	python manage.py collectstatic --no-input

run:
	python manage.py runserver
