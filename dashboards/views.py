# -*- coding: utf-8 -*-

# Librerias Python
from datetime import date

# Librerias Django
from django.core.urlresolvers import reverse

# Django Atajos
from django.shortcuts import render
from django.shortcuts import redirect

# Django Login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Django Generic Views
from django.views.generic.base import View

# Otros Models:
from configuracion.models import Empresa

# negocio.py
from .negocio import EmpresaResumen

# Formularios
from .forms import DasboardFormFiltros


@method_decorator(login_required, name='dispatch')
class ResumenAllByYear(View):

    def __init__(self):
        self.template_name = 'all_by_year.html'

    def get_ResumenEmpresas(self, _usuario, _anio):

        if _usuario.is_staff:
            # Si es administrador se mostraran todas
            empresas = Empresa.objects.all()
        else:
            # Si no solo se mostraran las empresas de dicho usuario
            empresas = Empresa.objects.filter(
                usuario=_usuario
            )

        lista = []

        fecha_inicial = str(_anio) + "-01-01"
        fecha_final = str(_anio) + "-12-31"

        for empresa in empresas:

            resumen_empresa = EmpresaResumen(empresa)

            resumen_empresa.get_Nomina_Resumen(fecha_inicial, fecha_final)
            resumen_empresa.get_Clientes_Resumen(fecha_inicial, fecha_final)
            resumen_empresa.get_Proveedores_Resumen(fecha_inicial, fecha_final)

            lista.append(resumen_empresa)

        return lista

    def get(self, request):

        anio_actual = date.today().year

        empresas_resumen = self.get_ResumenEmpresas(
            request.user,
            anio_actual
        )

        formulario = DasboardFormFiltros(
            initial={
                'anio': anio_actual
            }
        )

        contexto = {
            'empresas_resumen': empresas_resumen,
            'form': formulario,
            'anio': anio_actual
        }

        return render(request, self.template_name, contexto)

    def post(self, request):

        anio_selected = request.POST.get('anio')

        empresas_resumen = self.get_ResumenEmpresas(
            request.user,
            anio_selected
        )

        formulario = DasboardFormFiltros(
            initial={
                'anio': anio_selected
            }
        )

        contexto = {
            'empresas_resumen': empresas_resumen,
            'form': formulario,
            'anio': anio_selected
        }

        return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
class ResumenOneByMonth(View):

    def __init__(self):
        self.template_name = 'one_by_month.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        return render(request, self.template_name, {})
