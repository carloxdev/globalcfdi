# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import ComprobanteProveedorList
from .views import ComprobanteClienteList
from .views import ComprobanteEmpleadoList
from .views import ResumenList
from .views import LogList
from .views import ObtenerFacturas
from .views import ValidarFactura
from .views import MarcarPago
from .views import ReconocerFactura

apps_name = "facturas"

urlpatterns = [
    url(
        r'^comprobantes/proveedores/(?P<empresa>.*?)/(?P<anio>.*?)/(?P<mes>.*?)/$',
        ComprobanteProveedorList.as_view(),
        name='proveedor_lista'
    ),
    url(
        r'^comprobantes/clientes/(?P<empresa>.*?)/(?P<anio>.*?)/(?P<mes>.*?)/$',
        ComprobanteClienteList.as_view(),
        name='cliente_lista'
    ),
    url(
        r'^comprobantes/empleados/(?P<empresa>.*?)/(?P<anio>.*?)/(?P<mes>.*?)/$',
        ComprobanteEmpleadoList.as_view(),
        name='empleado_lista'
    ),
    url(
        r'^comprobantes/resumen/$',
        ResumenList.as_view(),
        name='resumen_lista'
    ),
    url(
        r'^comprobantes/logs/$',
        LogList.as_view(),
        name='log_lista'
    ),
    url(
        r'^comprobantes/obtener/$',
        ObtenerFacturas.as_view(),
        name='obtener_facturas'
    ),
    url(
        r'^comprobantes/validar_factura/(?P<type>.*)/(?P<uuid>.+)/$',
        ValidarFactura.as_view(),
        name='validar_factura'
    ),
    url(
        r'^comprobantes/marcar_pago/(?P<type>.*)/(?P<uuid>.+)/(?P<value>.+)/$',
        MarcarPago.as_view(),
        name='marcar_pago'
    ),
    url(
        r'^comprobantes/reconocer_factura/(?P<type>.*)/(?P<uuid>.+)/(?P<value>.+)/$',
        ReconocerFactura.as_view(),
        name='reconocer_factura'
    ),
]
