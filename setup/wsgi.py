"""
WSGI config for setup project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
from whitenoise import WhiteNoise

from setup import MyWSGIApp

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings', 'site_sintonize.settings')

#application = get_wsgi_application()

application = MyWSGIApp()
application = WhiteNoise(application, root= "site_sintonize/static")