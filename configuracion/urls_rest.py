# Third's Libraries
from rest_framework import routers

# Own's Librares
from configuracion.views_rest import EmpresaByPageAPI
router_configuracion = routers.DefaultRouter()

router_configuracion.register(
    r'empresa_bypage',
    EmpresaByPageAPI,
    'empresa_bypage'
)
