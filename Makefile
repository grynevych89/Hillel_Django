manage_py := python manage.py

run:
	$(manage_py) runserver

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

createsuperuser:
	$(manage_py) createsuperuser

shell:
	$(manage_py) shell_plus --print-sql

worker:
	celery -A root worker -l info --autoscale=0,10

beat:
	celery -A root beat -l info

pytest:
	pytest ./apps/tests --cov=app --cov-report html && coverage report --fail-under=80.0
