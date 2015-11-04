# -*- coding: utf-8 -*-
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["127.0.0.1:8000"]  # must specify domain for production

SECRET_KEY = 'LKasdnj1nJN81NDbf891nJANBgfkb>Ghvahv24'

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DB_NAME',
            'USER': 'DB_USER',
            'PASSWORD': 'DB_PASSWORD',
            'HOST': 'RDS_HOST',
            'PORT': '3306',
        }
    }

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

WEB_SOCKET_ADDRESS = 'http://127.0.0.1:8888/sockets'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

