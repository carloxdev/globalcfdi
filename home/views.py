# -*- coding: utf-8 -*-

# Librerias django

# Django Atajos
from django.shortcuts import render

# Django Login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Django Generic Views
from django.views.generic.base import View

# Otros Models:
from configuracion.models import Empresa
from facturas.models import Resumen

# negocio.py
from .negocio import EmpresaResumen


class Index(View):

    def __init__(self):
        self.template_name = 'home/index.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        return render(request, self.template_name, {})


@method_decorator(login_required, name='dispatch')
class Dashboard(View):

    def __init__(self):
        self.template_name = 'home/dashboard.html'

    def get(self, request):

        empresas = Empresa.objects.filter(
            usuario=request.user,
            activa=True
        )

        lista = []
        cantidad_nomina = 0
        total_nomina = 0

        cantidad_clientes = 0
        total_clientes = 0

        cantidad_proveedores = 0
        total_proveedores = 0

        for empresa in empresas:

            # Comprobante Empleados
            resumen_nomina = Resumen.objects.filter(
                empresa=empresa,
                tipo="EMPLEADOS"
            )
            for resumen in resumen_nomina:
                cantidad_nomina += resumen.cantidad_guardadas
                total_nomina += resumen.total

            # Factura de Clientes
            resumen_cliente = Resumen.objects.filter(
                empresa=empresa,
                tipo="CLIENTES"
            )
            for resumen in resumen_cliente:
                cantidad_clientes += resumen.cantidad_guardadas
                total_clientes += resumen.total

            # Factura de Proveedores
            resumen_proveedor = Resumen.objects.filter(
                empresa=empresa,
                tipo="PROVEEDORES"
            )
            for resumen in resumen_proveedor:
                cantidad_proveedores += resumen.cantidad_guardadas
                total_proveedores += resumen.total

            resumen_empresa = EmpresaResumen(
                empresa,
                cantidad_nomina,
                total_nomina,
                cantidad_clientes,
                total_clientes,
                cantidad_proveedores,
                total_proveedores,
            )

            lista.append(resumen_empresa)

        contexto = {
            'lista_empresas_resumen': lista
        }

        return render(request, self.template_name, contexto)


class Servicios(View):

    def __init__(self):
        self.template_name = 'home/servicios.html'

    def get(self, request):
        return render(request, self.template_name, {})
