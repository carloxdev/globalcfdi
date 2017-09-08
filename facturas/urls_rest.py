
# Third's Libraries
from rest_framework import routers

# Own's Libraries
from facturas.views_rest import ComprobanteProveedorExByPageAPI
from facturas.views_rest import ComprobanteProveedorByPageAPI
from facturas.views_rest import ComprobanteProveedorAPI
from facturas.views_rest import ComprobanteClienteByPageAPI
from facturas.views_rest import ComprobanteClienteAPI
from facturas.views_rest import ComprobanteEmpleadoExByPageAPI
from facturas.views_rest import ComprobanteEmpleadoByPageAPI
from facturas.views_rest import ComprobanteEmpleadoAPI
from facturas.views_rest import LogByPageAPI
from facturas.views_rest import ResumenByPageAPI


router_facturas = routers.DefaultRouter()

router_facturas.register(
    r'comprobanteproveedor_bypage',
    ComprobanteProveedorByPageAPI,
    'comprobanteproveedor_bypage'
)
router_facturas.register(
    r'comprobanteproveedorex_bypage',
    ComprobanteProveedorExByPageAPI,
    'comprobanteproveedorex_bypage'
)
router_facturas.register(
    r'comprobanteproveedor',
    ComprobanteProveedorAPI,
    'comprobanteproveedor'
)
router_facturas.register(
    r'comprobantecliente_bypage',
    ComprobanteClienteByPageAPI,
    'comprobantecliente_bypage'
)
router_facturas.register(
    r'comprobantecliente',
    ComprobanteClienteAPI,
    'comprobantecliente'
)
router_facturas.register(
    r'comprobanteempleado_bypage',
    ComprobanteEmpleadoByPageAPI,
    'comprobanteempleado_bypage'
)
router_facturas.register(
    r'comprobanteempleadoex_bypage',
    ComprobanteEmpleadoExByPageAPI,
    'comprobanteempleadoex_bypage'
)
router_facturas.register(
    r'comprobanteempleado',
    ComprobanteEmpleadoAPI,
    'comprobanteempleado'
)
router_facturas.register(
    r'log_bypage',
    LogByPageAPI,
    'log_bypage'
)
router_facturas.register(
    r'resumen_bypage',
    ResumenByPageAPI,
    'resumen_bypage'
)
