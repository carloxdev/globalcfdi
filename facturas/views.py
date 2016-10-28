# -*- coding: utf-8 -*-

# Librerias Django:
from django.shortcuts import render

# Django Login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Django Generic Views
from django.views.generic.base import View

# API Rest:
from rest_framework import viewsets

# Serializadores:
from .serializers import FacturaProveedorSerializer
from .serializers import FacturaClienteSerializer
from .serializers import ComprobanteEmpleadoSerializer
from .serializers import LogSerializer

# Paginadores:
from .pagination import FacturaProveedorPaginacion
from .pagination import FacturaClientePaginacion
from .pagination import ComprobanteEmpleadoPaginacion
from .pagination import LogPaginacion

# Modelos
from .models import FacturaProveedor
from .models import FacturaCliente
from .models import ComprobanteEmpleado
from .models import Log
from .models import Resumen

# Django Paginacion:
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


# ----------------- COMPROBANTES PROVEEDORES ----------------- #


@method_decorator(login_required, name='dispatch')
class FacturaProveedorList(View):

    def __init__(self):
        self.template_name = 'ComprobantesProveedores/facproveedor_lista.html'

    def get(self, request):
        return render(request, self.template_name, {})


@method_decorator(login_required, name='dispatch')
class FacturaClienteList(View):

    def __init__(self):
        self.template_name = 'ComprobantesClientes/faccliente_lista.html'

    def get(self, request):
        return render(request, self.template_name, {})


@method_decorator(login_required, name='dispatch')
class ComprobanteEmpleadoList(View):

    def __init__(self):
        self.template_name = 'ComprobantesEmpleados/comempleado_lista.html'

    def get(self, request):
        return render(request, self.template_name, {})


@method_decorator(login_required, name='dispatch')
class logsList(View):

    def __init__(self):
        self.template_name = 'Logs/log_lista.html'

    def get(self, request):
        return render(request, self.template_name, {})


@method_decorator(login_required, name='dispatch')
class ResumenList(View):

    def __init__(self):
        self.template_name = 'Resumenes/resumen_lista.html'

    def get(self, request):
        # Buscar Empresavb

        resumenes_list = Resumen.objects.all()

        paginador = Paginator(resumenes_list, 15)

        pagina = request.GET.get('page')

        try:
            resumenes = paginador.page(pagina)

        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            resumenes = paginador.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of
            # results.
            resumenes = paginador.page(paginador.num_pages)

        contexto = {
            'resumenes': resumenes
        }
        return render(request, self.template_name, contexto)


# ----------------- API REST ----------------- #

class FacturaProveedorAPI(viewsets.ModelViewSet):
    queryset = FacturaProveedor.objects.all()
    serializer_class = FacturaProveedorSerializer
    pagination_class = FacturaProveedorPaginacion

    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = FacturaRecibidaFilter


class FacturaClienteAPI(viewsets.ModelViewSet):
    queryset = FacturaCliente.objects.all()
    serializer_class = FacturaClienteSerializer
    pagination_class = FacturaClientePaginacion


class ComprobanteEmpleadoAPI(viewsets.ModelViewSet):
    queryset = ComprobanteEmpleado.objects.all()
    serializer_class = ComprobanteEmpleadoSerializer
    pagination_class = ComprobanteEmpleadoPaginacion


class LogAPI(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    pagination_class = LogPaginacion
