# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

# API Rest
from rest_framework import routers

# Mis API Views:
from facturas.views import FacturaProveedorAPI
from facturas.views import FacturaClienteAPI
from facturas.views import ComprobanteEmpleadoAPI
from facturas.views import LogAPI
from facturas.views import ResumenAPI

from configuracion.views import EmpresaAPI

router = routers.DefaultRouter()
router.register(
    r'facturas_proveedor',
    FacturaProveedorAPI,
    'facturas_proveedor'
)
router.register(
    r'facturas_cliente',
    FacturaClienteAPI,
    'facturas_cliente'
)
router.register(
    r'comprobantes_empleado',
    ComprobanteEmpleadoAPI,
    'comprobantes_empleado'
)
router.register(
    r'logs',
    LogAPI,
    'logs'
)
router.register(
    r'resumenes',
    ResumenAPI,
    'resumenes'
)
router.register(
    r'empresas',
    EmpresaAPI,
    'empresas'
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^', include('home.urls')),
    url(r'^', include('seguridad.urls')),
    url(r'^', include('configuracion.urls')),
    url(r'^', include('facturas.urls')),
]


if settings.DEBUG:

    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
