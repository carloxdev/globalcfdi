
# Third's Libraries
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Own's Libraries
from .models import ComprobanteProveedor
from .models import ComprobanteCliente
from .models import ComprobanteEmpleado
from .models import Log
from .models import Resumen

from .serializers import ComprobanteProveedorSerializer
from .serializers import ComprobanteClienteSerializer
from .serializers import ComprobanteEmpleadoSerializer
from .serializers import LogSerializer
from .serializers import ResumenSerializer

from .pagination import GenericPagination

from .filters import LogFilter
from .filters import ComprobanteProveedorFilter
from .filters import ComprobanteClienteFilter
from .filters import ComprobanteEmpleadoFilter
from .filters import ResumenFilter


class ComprobanteProveedorExByPageAPI(viewsets.ModelViewSet):
    queryset = ComprobanteProveedor.objects.all()
    serializer_class = ComprobanteProveedorSerializer
    pagination_class = GenericPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ComprobanteProveedorFilter
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class ComprobanteProveedorByPageAPI(viewsets.ModelViewSet):
    serializer_class = ComprobanteProveedorSerializer
    pagination_class = GenericPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ComprobanteProveedorFilter
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        if self.request.user.is_staff:
            facturas = ComprobanteProveedor.objects.all()
        else:
            empresas = self.request.user.empresa_set.all()
            facturas = ComprobanteProveedor.objects.filter(empresa__in=empresas)

        return facturas


class ComprobanteProveedorAPI(viewsets.ModelViewSet):
    serializer_class = ComprobanteProveedorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ComprobanteProveedorFilter
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        if self.request.user.is_staff:
            facturas = ComprobanteProveedor.objects.all()
        else:
            empresas = self.request.user.empresa_set.all()
            facturas = ComprobanteProveedor.objects.filter(empresa__in=empresas)

        return facturas


class ComprobanteClienteByPageAPI(viewsets.ModelViewSet):
    serializer_class = ComprobanteClienteSerializer
    pagination_class = GenericPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ComprobanteClienteFilter
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            facturas = ComprobanteCliente.objects.all()
        else:
            empresas = self.request.user.empresa_set.all()
            facturas = ComprobanteCliente.objects.filter(empresa__in=empresas)

        return facturas


class ComprobanteClienteAPI(viewsets.ModelViewSet):
    serializer_class = ComprobanteClienteSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ComprobanteClienteFilter
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            facturas = ComprobanteCliente.objects.all()
        else:
            empresas = self.request.user.empresa_set.all()
            facturas = ComprobanteCliente.objects.filter(empresa__in=empresas)

        return facturas

class ComprobanteEmpleadoExByPageAPI(viewsets.ModelViewSet):
    queryset = ComprobanteEmpleado.objects.all()
    serializer_class = ComprobanteClienteSerializer
    pagination_class = GenericPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ComprobanteEmpleadoFilter
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

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
