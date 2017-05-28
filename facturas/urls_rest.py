
# Third's Libraries
from rest_framework import routers

# Own's Libraries
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
    r'facturasproveedor_bypage',
    FacturaProveedorByPageAPI,
    'facturasproveedor_bypage'
)
router_facturas.register(
    r'facturasproveedor',
    FacturaProveedorAPI,
    'facturasproveedor'
)
router_facturas.register(
    r'facturascliente_bypage',
    FacturaClienteByPageAPI,
    'facturascliente_bypage'
)
router_facturas.register(
    r'facturas_cliente',
    FacturaClienteAPI,
    'facturas_cliente'
)
router_facturas.register(
    r'comprobantes_empleado',
    ComprobanteEmpleadoByPageAPI,
    'comprobantes_empleado'
)
router_facturas.register(
    r'comprobantes_empleado',
    ComprobanteEmpleadoAPI,
    'comprobantes_empleado'
)
router_facturas.register(
    r'logs',
    LogByPageAPI,
    'logs'
)
router_facturas.register(
    r'resumenes',
    ResumenByPageAPI,
    'resumenes'
)
