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
import calendar
from datetime import date
# from datetime import datetime


# Modelos
from .models import ComprobanteProveedor
from .models import ComprobanteCliente
from .models import ComprobanteEmpleado

# Formularios:
from .forms import FacturaRecibidaFormFiltros
from .forms import FacturaEmitidaFormFiltros
from .forms import ObtenerForm
from .forms import LogFormFiltros
from .forms import ResumenFormFiltros

# Librerias Propias:
# from core.tools.datos import Chronos

# Django Paginacion:
# from django.core.paginator import Paginator
# from django.core.paginator import EmptyPage
# from django.core.paginator import PageNotAnInteger

# Tasks
# from .tasks import obtener_Facturas
# from core.sat import WebServiceSAT


@method_decorator(login_required, name='dispatch')
class ValidarFactura(View):

    def get(self, request, type, uuid):

        # satweb = WebServiceSAT()

        # estado = ""
        # mensaje = ""

        # try:

        #     if type == "proveedor":
        #         documento = ComprobanteProveedor.objects.get(uuid=uuid)

        #     elif type == "cliente":
        #         documento = ComprobanteCliente.objects.get(uuid=uuid)

        #     elif type == "empleado":
        #         documento = ComprobanteEmpleado.objects.get(uuid=uuid)

        #     else:
        #         documento = None

        #     if documento is not None:

        #         estado = satweb.get_Estado(
        #             documento.emisor_rfc,
        #             documento.receptor_rfc,
        #             documento.total,
        #             documento.uuid
        #         )

        #         if estado != documento.estadoSat:
        #             documento.estadoSat = estado
        #             documento.save()
        #             mensaje = "Estado actualizado a:"
        #         else:
        #             mensaje = "El estado no a cambiado en la BD"

        #     else:
        #         mensaje = "Favor de especificar un tipo"

        # except Exception, error:
        #     mensaje = "Error: {} ".format(str(error))

        # msg = {
        #     "estado": estado,
        #     "mensaje": mensaje
        # }

        # data = json.dumps(msg)

        data = {}

        return HttpResponse(data, content_type='application/json')


@method_decorator(login_required, name='dispatch')
class MarcarPago(View):

    def get(self, request, type, uuid, value):

        mensaje = ""

        try:

            if type == "proveedor":
                documento = ComprobanteProveedor.objects.get(uuid=uuid)

            elif type == "cliente":
                documento = ComprobanteCliente.objects.get(uuid=uuid)

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


@method_decorator(login_required, name='dispatch')
class ReconocerFactura(View):

    def get(self, request, type, uuid, value):

        mensaje = ""

        try:

            if type == "proveedor":
                documento = ComprobanteProveedor.objects.get(uuid=uuid)

            elif type == "cliente":
                documento = ComprobanteCliente.objects.get(uuid=uuid)

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


@method_decorator(login_required, name='dispatch')
class ComprobanteProveedorList(View):

    def __init__(self):
        self.template_name = 'comprobante_proveedor/com_proveedor_lista.html'

    def get(self, request, empresa, anio, mes):

        formulario = FacturaRecibidaFormFiltros(request.user)

        initial = {}

        if empresa != 0:
            initial['empresa'] = empresa

        if anio == '0' and mes == '0':

            hoy = date.today()

            days = calendar.monthrange(hoy.year, hoy.month)[1]

            initial['fecha_inicio'] = "{}-{:02d}-{}".format(
                str(hoy.year),
                hoy.month,
                "01"
            )
            initial['fecha_final'] = "{}-{:02d}-{:02d}".format(
                str(hoy.year),
                hoy.month,
                days
            )

        elif anio != '0' and mes == '0':
            initial['fecha_inicio'] = str(anio) + "-01-01"
            initial['fecha_final'] = str(anio) + "-12-31"

        formulario.initial = initial

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
class ComprobanteProveedorView(View):

    template_name = 'comprobante_proveedor/com_proveedor_view.html'

    def get(self, request, uuid):
        return render(request, self.template_name, {})


@method_decorator(login_required, name='dispatch')
class ComprobanteClienteList(View):

    def __init__(self):
        self.template_name = 'comprobante_cliente/com_cliente_lista.html'

    def get(self, request, empresa, anio, mes):

        formulario = FacturaEmitidaFormFiltros(request.user)

        initial = {}

        if empresa != 0:
            initial['empresa'] = empresa

        if anio == '0' and mes == '0':

            hoy = date.today()

            days = calendar.monthrange(hoy.year, hoy.month)[1]

            initial['fecha_inicio'] = "{}-{:02d}-{}".format(
                str(hoy.year),
                hoy.month,
                "01"
            )
            initial['fecha_final'] = "{}-{:02d}-{:02d}".format(
                str(hoy.year),
                hoy.month,
                days
            )

        elif anio != '0' and mes == '0':
            initial['fecha_inicio'] = str(anio) + "-01-01"
            initial['fecha_final'] = str(anio) + "-12-31"

        formulario.initial = initial

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
class ComprobanteEmpleadoList(View):

    def __init__(self):
        self.template_name = 'comprobante_empleado/com_empleado_lista.html'

    def get(self, request, empresa, anio, mes):

        formulario = FacturaEmitidaFormFiltros(request.user)

        initial = {}

        if empresa != 0:
            initial['empresa'] = empresa

        if anio == '0' and mes == '0':

            hoy = date.today()

            days = calendar.monthrange(hoy.year, hoy.month)[1]

            initial['fecha_inicio'] = "{}-{:02d}-{}".format(
                str(hoy.year),
                hoy.month,
                "01"
            )
            initial['fecha_final'] = "{}-{:02d}-{:02d}".format(
                str(hoy.year),
                hoy.month,
                days
            )

        elif anio != '0' and mes == '0':
            initial['fecha_inicio'] = str(anio) + "-01-01"
            initial['fecha_final'] = str(anio) + "-12-31"

        formulario.initial = initial

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
class LogList(View):

    def __init__(self):
        self.template_name = 'log/log_lista.html'

    def get(self, request):

        formulario = LogFormFiltros(request.user)

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


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
        self.bandera = ''
        self.mensaje = ''

    def get(self, request):
        formulario = ObtenerForm(username=request.user)

        contexto = {
            'form': formulario,
            'bandera': self.bandera,
        }

        return render(request, self.template_name, contexto)

    def post(self, request):

        # formulario = ObtenerForm(request.POST, username=request.user)

        # if formulario.is_valid():
        #     datos_formulario = formulario.cleaned_data

        #     empresa_clave = datos_formulario.get('empresa')
        #     fecha_inicio = str(datos_formulario.get('fecha_inicio'))
        #     fecha_fin = str(datos_formulario.get('fecha_final'))
        #     tipo_comprobante = datos_formulario.get('tipo_comprobante')

        #     print "Empresa: {}".format(empresa_clave)
        #     print "Fecha Inicio: {}".format(fecha_inicio)
        #     print "Fecha Final: {}".format(fecha_fin)
        #     print "Tipo Comprobante: {}".format(tipo_comprobante)

        #     try:
        #         f_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        #         f_final = datetime.strptime(fecha_fin, "%Y-%m-%d")

        #         fechas = Chronos.getDays_FromRange(f_inicio, f_final)

        #         # Descargar Emitidas y Recibidas por cada fecha
        #         for fecha in fechas:

        #             obtener_Facturas.delay(
        #                 empresa_clave,
        #                 str(fecha),
        #                 tipo_comprobante
        #             )

        #         self.bandera = "INICIO_PROCESO"
        #         self.mensaje = "En la siguiente tabla se " \
        #             "mostrara el resultado de la descargar por Dia:"""

        #     except Exception as e:
        #         self.bandera = "ERROR"
        #         self.mensaje = "Ocurio un error al llamar la tarea: {}".format(
        #             str(e)
        #         )

        # contexto = {
        #     'form': formulario,
        #     'mensaje': self.mensaje,
        #     'bandera': self.bandera,
        # }
        return render(request, self.template_name, {})
