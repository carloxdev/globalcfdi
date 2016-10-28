# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import FacturaProveedorList
from .views import FacturaClienteList
from .views import ComprobanteEmpleadoList
from .views import ResumenList
from .views import logsList


# ----------------- FACTURAS PROVEEDORES ----------------- #
urlpatterns = [
    url(
        r'^comprobantes/proveedores/$',
        FacturaProveedorList.as_view(),
        name='facturas.comprobantes_proveedores'
    ),
    url(
        r'^comprobantes/clientes/$',
        FacturaClienteList.as_view(),
        name='facturas.comprobantes_clientes'
    ),
    url(
        r'^comprobantes/empleados/$',
        ComprobanteEmpleadoList.as_view(),
        name='facturas.comprobantes_empleados'
    ),
    url(
        r'^resumen/$',
        ResumenList.as_view(),
        name='facturas.resumen'
    ),
    url(
        r'^logs/$',
        logsList.as_view(),
        name='facturas.logs'
    ),
]
