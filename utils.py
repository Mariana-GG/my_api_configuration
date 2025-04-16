import secrets


def create_secret_key():
    """Helps you create secret key"""
    return f"django-secure-{secrets.token_urlsafe(50)}"
