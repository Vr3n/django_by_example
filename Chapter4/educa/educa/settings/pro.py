from .base import *

DEBUG = False

ADMINS = (
    ('Viren Patel', 'vickyspatel@gmail.com'),
)

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'django@123',
        'HOST': 'localhost'
    }
}
