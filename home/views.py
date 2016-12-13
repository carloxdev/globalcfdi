# -*- coding: utf-8 -*-

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


class Index(View):

    def __init__(self):
        self.template_name = 'home/index.html'

    def get(self, request):

        if request.user.is_authenticated():
            return redirect(reverse('home.dashboard'))

        else:
            return render(request, self.template_name, {})

        return render(request, self.template_name, {})

    def post(self, request):
        return render(request, self.template_name, {})


@method_decorator(login_required, name='dispatch')
class Dashboard(View):

    def __init__(self):
        self.template_name = 'home/dashboard.html'

    def get(self, request):

        if request.user.is_staff:
            # Si es administrador se mostraran todas
            empresas = Empresa.objects.all()
        else:
            # Si no solo se mostraran las empresas activas
            empresas = Empresa.objects.filter(
                usuario=request.user,
                activa=True
            )

        lista = []

        for empresa in empresas:

            resumen_empresa = EmpresaResumen(empresa)

            resumen_empresa.get_Nomina_Resumen()
            resumen_empresa.get_Clientes_Resumen()
            resumen_empresa.get_Proveedores_Resumen()

            lista.append(resumen_empresa)

        contexto = {
            'empresas_resumen': lista
        }

        return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
class DashboardDetalle(View):

    def __init__(self):
        self.template_name = 'home/dashboard_detalle.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        return render(request, self.template_name, {})


class Servicios(View):

    def __init__(self):
        self.template_name = 'home/servicios.html'

    def get(self, request):
        return render(request, self.template_name, {})


class Contactanos(View):

    def __init__(self):
        self.template_name = 'home/contactanos.html'

    def get(self, request):
        return render(request, self.template_name, {})


class QuienesSomos(View):

    def __init__(self):
        self.template_name = 'home/quienes_somos.html'

    def get(self, request):
        return render(request, self.template_name, {})


# class Ejemplo(View):

#     def __init__(self):
#         self.template_name = 'ejemplo.html'

#     def get(self, request):
#         return render(request, self.template_name, {})

#     def post(self, request):
#         return render(request, self.template_name, {})
