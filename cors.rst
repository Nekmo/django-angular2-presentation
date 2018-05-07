


.. code-block:: console

    $ pip install django-cors-headers



.. code-block:: python

    # project/settings/dev.py
    from .defaults import *

    INSTALLED_APPS.append('corsheaders')
    MIDDLEWARE.append('django.middleware.common.CommonMiddleware')

    # CELERY_TASK_ALWAYS_EAGER = True
    CORS_ORIGIN_ALLOW_ALL = True
    ALLOWED_HOSTS = ['*']

