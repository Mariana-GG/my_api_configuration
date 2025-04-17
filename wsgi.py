import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_api_configuration.settings.dev")
application = get_wsgi_application()

