# -*- coding: utf-8 -*-

# Librerias Django:
from django.shortcuts import render
from django.http import HttpResponse

# Django Login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Django Generic Views
from django.views.generic.base import View

# Librerias Python:
import json

# API Rest:
from rest_framework import viewsets
from rest_framework import filters

# Serializadores:
from .serializers import FacturaProveedorSerializer
from .serializers import FacturaClienteSerializer
from .serializers import ComprobanteEmpleadoSerializer
from .serializers import LogSerializer
from .serializers import ResumenSerializer

# Paginadores:
from .pagination import GenericPagination

# Filtros:
from .filters import LogFilter
from .filters import FacturaProveedorFilter
from .filters import FacturaClienteFilter
from .filters import ComprobanteEmpleadoFilter
from .filters import ResumenFilter

# Modelos
from .models import FacturaProveedor
from .models import FacturaCliente
from .models import ComprobanteEmpleado
from .models import Log
from .models import Resumen

# Formularios:
from .forms import FacturaProveedorFormFiltros
from .forms import ObtenerForm
from .forms import LogFormFiltros
from .forms import ResumenFormFiltros

# Django Paginacion:
# from django.core.paginator import Paginator
# from django.core.paginator import EmptyPage
# from django.core.paginator import PageNotAnInteger

# Tasks
from .tasks import obtener_facturas
from core.sat import WebServiceSAT


class ValidarFactura(View):

    def get(self, request, type, uuid):

        satweb = WebServiceSAT()

        estado = ""
        mensaje = ""

        try:

            if type == "proveedor":
                documento = FacturaProveedor.objects.get(uuid=uuid)

            elif type == "cliente":
                documento = FacturaCliente.objects.get(uuid=uuid)

            elif type == "empleado":
                documento = ComprobanteEmpleado.objects.get(uuid=uuid)

            else:
                documento = None

            if documento is not None:

                estado = satweb.get_Estado(
                    documento.emisor_rfc,
                    documento.receptor_rfc,
                    documento.total,
                    documento.uuid
                )

                if estado != documento.estadoSat:
                    documento.estadoSat = estado
                    documento.save()
                    mensaje = "Estado actualizado a:"
                else:
                    mensaje = "El estado no a cambiado en la BD"

            else:
                mensaje = "Favor de especificar un tipo"

        except Exception, error:
            mensaje = "Error: {} ".format(str(error))

        msg = {
            "estado": estado,
            "mensaje": mensaje
        }

        data = json.dumps(msg)

        return HttpResponse(data, content_type='application/json')


class MarcarPago(View):

    def get(self, request, type, uuid, value):

        mensaje = ""

        try:

            if type == "proveedor":
                documento = FacturaProveedor.objects.get(uuid=uuid)

            elif type == "cliente":
                documento = FacturaCliente.objects.get(uuid=uuid)

            elif type == "empleado":
                documento = ComprobanteEmpleado.objects.get(uuid=uuid)

            else:
                documento = None

            if documento is not None:

                documento.pago = value
                documento.save()
                mensaje = "Se actualizo el registro"

            else:
                mensaje = "Favor de especificar un tipo"

        except Exception, error:
            mensaje = "Error: {} ".format(str(error))

        msg = {
            "mensaje": mensaje
        }

        data = json.dumps(msg)

        return HttpResponse(data, content_type='application/json')


class ReconocerFactura(View):

    def get(self, request, type, uuid, value):

        mensaje = ""

        try:

            if type == "proveedor":
                documento = FacturaProveedor.objects.get(uuid=uuid)

            elif type == "cliente":
                documento = FacturaCliente.objects.get(uuid=uuid)

            elif type == "empleado":
                documento = ComprobanteEmpleado.objects.get(uuid=uuid)

            else:
                documento = None

            if documento is not None:

                documento.comprobacion = value
                documento.save()
                mensaje = "Se actualizo el registro"

            else:
                mensaje = "Favor de especificar un tipo"

        except Exception, error:
            mensaje = "Error: {} ".format(str(error))

        msg = {
            "mensaje": mensaje
        }

        data = json.dumps(msg)

        return HttpResponse(data, content_type='application/json')


# ----------------- FACTURA PROVEEDOR ----------------- #


@method_decorator(login_required, name='dispatch')
class FacturaProveedorList(View):

    def __init__(self):
        self.template_name = 'factura_proveedor/fac_proveedor_lista.html'

    def get(self, request):

        formulario = FacturaProveedorFormFiltros(request.user)

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


class FacturaProveedorAPI(viewsets.ModelViewSet):
    serializer_class = FacturaProveedorSerializer
    pagination_class = GenericPagination

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FacturaProveedorFilter

    def get_queryset(self):

        if self.request.user.is_staff:
            facturas = FacturaProveedor.objects.all()
        else:
            empresas = self.request.user.empresa_set.all()
            facturas = FacturaProveedor.objects.filter(empresa__in=empresas)

        return facturas


class FacturaProveedorTodosAPI(viewsets.ModelViewSet):
    serializer_class = FacturaProveedorSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FacturaProveedorFilter

    def get_queryset(self):

        if self.request.user.is_staff:
            facturas = FacturaProveedor.objects.all()
        else:
            empresas = self.request.user.empresa_set.all()
            facturas = FacturaProveedor.objects.filter(empresa__in=empresas)

        return facturas

# ----------------- FACTURA CLIENTE ----------------- #


@method_decorator(login_required, name='dispatch')
class FacturaClienteList(View):

    def __init__(self):
        self.template_name = 'factura_cliente/fac_cliente_lista.html'

    def get(self, request):
        formulario = FacturaProveedorFormFiltros(request.user)

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


class FacturaClienteAPI(viewsets.ModelViewSet):
    serializer_class = FacturaClienteSerializer
    pagination_class = GenericPagination

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FacturaClienteFilter

    def get_queryset(self):
        empresas = self.request.user.empresa_set.all()
        return FacturaCliente.objects.filter(empresa__in=empresas)


class FacturaClienteTodosAPI(viewsets.ModelViewSet):
    serializer_class = FacturaClienteSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FacturaClienteFilter

    def get_queryset(self):
        empresas = self.request.user.empresa_set.all()
        return FacturaCliente.objects.filter(empresa__in=empresas)

# ----------------- COMPROBANTE EMPLEADO ----------------- #


@method_decorator(login_required, name='dispatch')
class ComprobanteEmpleadoList(View):

    def __init__(self):
        self.template_name = 'comprobante_empleado/com_empleado_lista.html'

    def get(self, request):
        formulario = FacturaProveedorFormFiltros(request.user)

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


class ComprobanteEmpleadoAPI(viewsets.ModelViewSet):
    serializer_class = ComprobanteEmpleadoSerializer
    pagination_class = GenericPagination

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ComprobanteEmpleadoFilter

    def get_queryset(self):
        empresas = self.request.user.empresa_set.all()
        return ComprobanteEmpleado.objects.filter(empresa__in=empresas)


class ComprobanteEmpleadoTodosAPI(viewsets.ModelViewSet):
    serializer_class = ComprobanteEmpleadoSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ComprobanteEmpleadoFilter

    def get_queryset(self):
        empresas = self.request.user.empresa_set.all()
        return ComprobanteEmpleado.objects.filter(empresa__in=empresas)

# ----------------- LOG ----------------- #


@method_decorator(login_required, name='dispatch')
class LogsList(View):

    def __init__(self):
        self.template_name = 'log/log_lista.html'

    def get(self, request):

        formulario = LogFormFiltros(request.user)

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


class LogAPI(viewsets.ModelViewSet):
    queryset = Log.objects.all().order_by('-created_date',)
    serializer_class = LogSerializer
    pagination_class = GenericPagination

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = LogFilter


# ----------------- RESUMEN ----------------- #

@method_decorator(login_required, name='dispatch')
class ResumenList(View):

    def __init__(self):
        self.template_name = 'resumen/resumen_lista.html'

    def get(self, request):
        # Buscar Empresavb

        # resumenes_list = Resumen.objects.all()

        # paginador = Paginator(resumenes_list, 15)

        # pagina = request.GET.get('page')

        # try:
        #     resumenes = paginador.page(pagina)

        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page.
        #     resumenes = paginador.page(1)
        # except EmptyPage:
        #     # If page is out of range (e.g. 9999), deliver last page of
        #     # results.
        #     resumenes = paginador.page(paginador.num_pages)

        # contexto = {
        #     'resumenes': resumenes
        # }

        formulario = ResumenFormFiltros(request.user)

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
class ObtenerFacturas(View):

    def __init__(self):
        self.template_name = 'resumen/obtener_facturas.html'
        self.mensaje = ''

    def get(self, request):
        formulario = ObtenerForm(username=request.user)

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)

    def post(self, request):

        formulario = ObtenerForm(request.POST, username=request.user)

        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data

            empresa = datos_formulario.get('empresa')
            fecha_inicio = str(datos_formulario.get('fecha_inicio'))
            fecha_fin = str(datos_formulario.get('fecha_final'))

            print fecha_inicio
            print fecha_fin

            try:
                obtener_facturas.delay(
                    empresa,
                    fecha_inicio,
                    fecha_fin
                )
            except Exception as e:
                self.mensaje = str(e)

        contexto = {
            'form': formulario,
            'mensaje': self.mensaje
        }
        return render(request, self.template_name, contexto)


class ResumenAPI(viewsets.ModelViewSet):
    queryset = Resumen.objects.all().order_by('fecha',)
    serializer_class = ResumenSerializer
    pagination_class = GenericPagination

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ResumenFilter
