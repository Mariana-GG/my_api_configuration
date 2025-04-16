from .base import *
import environ


env = environ.Env()
environ.Env.read_env(str(HOME_DIR / ".env"))
SECRET_KEY = env.str("SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
