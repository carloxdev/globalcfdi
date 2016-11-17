# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import FacturaProveedorList
from .views import FacturaClienteList
from .views import ComprobanteEmpleadoList
from .views import ResumenList
from .views import LogsList
from .views import Obtener


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
        r'^comprobantes/resumen/$',
        ResumenList.as_view(),
        name='facturas.resumen'
    ),
    url(
        r'^comprobantes/logs/$',
        LogsList.as_view(),
        name='facturas.logs'
    ),
    url(
        r'^comprobantes/obtener/$',
        Obtener.as_view(),
        name='facturas.obtener'
    ),
]
