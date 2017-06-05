
# Third's Libraries
from rest_framework import routers

# Own's Libraries
from facturas.views_rest import FacturaProveedorExByPageAPI
from facturas.views_rest import FacturaProveedorByPageAPI
from facturas.views_rest import FacturaProveedorAPI
from facturas.views_rest import FacturaClienteByPageAPI
from facturas.views_rest import FacturaClienteAPI
from facturas.views_rest import ComprobanteEmpleadoByPageAPI
from facturas.views_rest import ComprobanteEmpleadoAPI
from facturas.views_rest import LogByPageAPI
from facturas.views_rest import ResumenByPageAPI


router_facturas = routers.DefaultRouter()

router_facturas.register(
    r'facturaproveedor_bypage',
    FacturaProveedorByPageAPI,
    'facturaproveedor_bypage'
)
router_facturas.register(
    r'facturaproveedorex_bypage',
    FacturaProveedorExByPageAPI,
    'facturaproveedorex_bypage'
)
router_facturas.register(
    r'facturaproveedor',
    FacturaProveedorAPI,
    'facturaproveedor'
)
router_facturas.register(
    r'facturacliente_bypage',
    FacturaClienteByPageAPI,
    'facturacliente_bypage'
)
router_facturas.register(
    r'facturacliente',
    FacturaClienteAPI,
    'facturacliente'
)
router_facturas.register(
    r'comprobanteempleado_bypage',
    ComprobanteEmpleadoByPageAPI,
    'comprobanteempleado_bypage'
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
