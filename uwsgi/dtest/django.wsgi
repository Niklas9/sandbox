import os
import sys

import django.core.handlers.wsgi as wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'dtest.settings'
application = wsgi.WSGIHandler()

path = '/app/sandbox/uwsgi'
if path not in sys.path:  sys.path.append(path)
