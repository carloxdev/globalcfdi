import os, sys
sys.path.append('E:\\Proyectos\\SmartCFDI\\Sitio')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SmartCFDI.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()