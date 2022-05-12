"""
WSGI config for A2SL project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('wordnet')
nltk.download('wordnet')
nltk.download('omw-1.4')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A2SL.settings')

application = get_wsgi_application()
