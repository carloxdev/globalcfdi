
# Third's Libraries
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Own's Libraries
from .models import FacturaProveedor
from .models import FacturaCliente
from .models import ComprobanteEmpleado
from .models import Log
from .models import Resumen

from .serializers import FacturaProveedorSerializer
from .serializers import FacturaClienteSerializer
from .serializers import ComprobanteEmpleadoSerializer
from .serializers import LogSerializer
from .serializers import ResumenSerializer

from .pagination import GenericPagination

from .filters import LogFilter
from .filters import FacturaProveedorFilter
from .filters import FacturaClienteFilter
from .filters import ComprobanteEmpleadoFilter
from .filters import ResumenFilter


class FacturaProveedorExByPageAPI(viewsets.ModelViewSet):
    queryset = FacturaProveedor.objects.all()
    serializer_class = FacturaProveedorSerializer
    pagination_class = GenericPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FacturaProveedorFilter
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class FacturaProveedorByPageAPI(viewsets.ModelViewSet):
    serializer_class = FacturaProveedorSerializer
    pagination_class = GenericPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FacturaProveedorFilter
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        if self.request.user.is_staff:
            facturas = FacturaProveedor.objects.all()
        else:
            empresas = self.request.user.empresa_set.all()
            facturas = FacturaProveedor.objects.filter(empresa__in=empresas)

        return facturas


class FacturaProveedorAPI(viewsets.ModelViewSet):
    serializer_class = FacturaProveedorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FacturaProveedorFilter
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        if self.request.user.is_staff:
            facturas = FacturaProveedor.objects.all()
        else:
            empresas = self.request.user.empresa_set.all()
            facturas = FacturaProveedor.objects.filter(empresa__in=empresas)

        return facturas


class FacturaClienteByPageAPI(viewsets.ModelViewSet):
    serializer_class = FacturaClienteSerializer
    pagination_class = GenericPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FacturaClienteFilter
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            facturas = FacturaCliente.objects.all()
        else:
            empresas = self.request.user.empresa_set.all()
            facturas = FacturaCliente.objects.filter(empresa__in=empresas)

        return facturas


class FacturaClienteAPI(viewsets.ModelViewSet):
    serializer_class = FacturaClienteSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FacturaClienteFilter
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            facturas = FacturaCliente.objects.all()
        else:
            empresas = self.request.user.empresa_set.all()
            facturas = FacturaCliente.objects.filter(empresa__in=empresas)

        return facturas


class ComprobanteEmpleadoByPageAPI(viewsets.ModelViewSet):
    serializer_class = ComprobanteEmpleadoSerializer
    pagination_class = GenericPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ComprobanteEmpleadoFilter
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            facturas = ComprobanteEmpleado.objects.all()
        else:
            empresas = self.request.user.empresa_set.all()
            facturas = ComprobanteEmpleado.objects.filter(empresa__in=empresas)

        return facturas


class ComprobanteEmpleadoAPI(viewsets.ModelViewSet):
    serializer_class = ComprobanteEmpleadoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ComprobanteEmpleadoFilter
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            facturas = ComprobanteEmpleado.objects.all()
        else:
            empresas = self.request.user.empresa_set.all()
            facturas = ComprobanteEmpleado.objects.filter(empresa__in=empresas)

        return facturas


class LogByPageAPI(viewsets.ModelViewSet):
    queryset = Log.objects.all().order_by('-created_date',)
    serializer_class = LogSerializer
    pagination_class = GenericPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = LogFilter
    permission_classes = (IsAuthenticated,)


class ResumenByPageAPI(viewsets.ModelViewSet):
    queryset = Resumen.objects.all().order_by('fecha',)
    serializer_class = ResumenSerializer
    pagination_class = GenericPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ResumenFilter
    permission_classes = (IsAuthenticated,)
