===============
django-maintain
===============

Installation
============

::

    pip install django-maintain


Usage
=====

::

    # Django-Maintain Settings
    DJANGO_SITE_MAINTAIN = False  # Default ``False``, Modify ``True`` when maintain
    DJANGO_SITE_MAINTAIN_NOTICE_URL = ''


Settings.py
===========

::

    # Use `MIDDLEWARE_CLASSES` prior to Django 1.10
    MIDDLEWARE = [
        ...
        # 'competion.middleware.SiteMaintainMiddleware',  # hasattr(request, 'user') == False
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'competion.middleware.SiteMaintainMiddleware',  # hasattr(request, 'user') == True
        ...
    ]

