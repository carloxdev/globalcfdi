# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import FacturaProveedorList
from .views import FacturaClienteList
from .views import ComprobanteEmpleadoList
from .views import ResumenList
from .views import LogsList
from .views import ObtenerFacturas
from .views import ValidarFactura
from .views import MarcarPago
from .views import ReconocerFactura

# ----------------- FACTURAS PROVEEDORES ----------------- #
urlpatterns = [
    url(
        r'^comprobantes/proveedores/$',
        FacturaProveedorList.as_view(),
        name='facturas.factura_proveedor_lista'
    ),
    url(
        r'^comprobantes/clientes/$',
        FacturaClienteList.as_view(),
        name='facturas.factura_cliente_lista'
    ),
    url(
        r'^comprobantes/empleados/$',
        ComprobanteEmpleadoList.as_view(),
        name='facturas.comprobante_empleado_lista'
    ),
    url(
        r'^comprobantes/resumen/$',
        ResumenList.as_view(),
        name='facturas.resumen_lista'
    ),
    url(
        r'^comprobantes/logs/$',
        LogsList.as_view(),
        name='facturas.log_lista'
    ),
    url(
        r'^comprobantes/obtener/$',
        ObtenerFacturas.as_view(),
        name='facturas.obtener_facturas'
    ),
    url(
        r'^comprobantes/validar_factura/(?P<type>.*)/(?P<uuid>.+)/$',
        ValidarFactura.as_view(),
        name='facturas.validar_factura'
    ),
    url(
        r'^comprobantes/marcar_pago/(?P<type>.*)/(?P<uuid>.+)/(?P<value>.+)/$',
        MarcarPago.as_view(),
        name='facturas.marcar_pago'
    ),
    url(
        r'^comprobantes/reconocer_factura/(?P<type>.*)/(?P<uuid>.+)/(?P<value>.+)/$',
        ReconocerFactura.as_view(),
        name='facturas.reconocer_factura'
    ),
]
