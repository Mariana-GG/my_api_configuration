import os
from django.core.asgi import get_asgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_api_configuration.settings.dev")
application = get_asgi_application()

