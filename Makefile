dev-start-nosettings:
	python manage.py runserver

dev-makemigrations-nosettings:
	python manage.py makemigrations

dev-migrate-nosettings:
	python manage.py migrate

dev-check-nosettings:
	python manage.py check

dev-start:
	python manage.py runserver --settings=my_api_configuration.settings.dev

dev-collect-static:
	python manage.py collectstatic --settings=my_api_configuration.settings.dev

dev-create-admin:
	python manage.py createsuperuser  --settings=my_api_configuration.settings.dev

dev-install:
	pip install -r requirements/dev.txt

dev-showmigrations:
	python manage.py showmigrations --settings=my_api_configuration.settings.dev

dev-makemigrations:
	python manage.py makemigrations --settings=my_api_configuration.settings.dev

dev-makemigrations-app:
	python manage.py makemigrations $(app) --settings=my_api_configuration.settings.dev

dev-migrate:
	python manage.py migrate  --settings=my_api_configuration.settings.dev

dev-migrate2:
	python manage.py migrate $(app) $(m) --settings=my_api_configuration.settings.dev

dev-sqlmigrate:
	python manage.py sqlmigrate $(app) $(m) --settings=my_api_configuration.settings.dev

dev-shell:
	python manage.py shell --settings=my_api_configuration.settings.dev
    
dev-test:
	python manage.py test $(route) --settings=my_api_configuration.settings.dev

dev-custom-command:
	python manage.py get_current_date --settings=my_api_configuration.settings.dev

dev-somebooks:
	python manage.py get_some_books --settings=my_api_configuration.settings.dev

dev-sendemail:
	python manage.py send_email $(email) --settings=my_api_configuration.settings.dev