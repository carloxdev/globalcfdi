# -*- coding: utf-8 -*-

# Django's Libraries
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic.base import View

# Own's Libraries
from .models import Empresa
from .forms import EmpresaCreateForm
from .forms import EmpresaEditForm
from .tasks import test_Credentials


@method_decorator(login_required, name='dispatch')
class EmpresaListView(View):

    def __init__(self):
        self.template_name = 'empresa/empresa_lista.html'
        self.mensaje = ''

    def get(self, request):

        return render(request, self.template_name, {})


@method_decorator(login_required, name='dispatch')
class EmpresaCreateView(View):

    def __init__(self):
        self.template_name = 'empresa/empresa_nuevo.html'

    def get(self, request):

        # Obtenemos el usuario
        formulario = EmpresaCreateForm(username=request.user)

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)

    def post(self, request):

        formulario = EmpresaCreateForm(
            request.POST,
            request.FILES,
            username=request.user
        )

        if formulario.is_valid():

            datos_formulario = formulario.cleaned_data
            empresa = Empresa()
            empresa.clave = datos_formulario.get('clave')
            empresa.razon_social = datos_formulario.get('razon_social')
            empresa.rfc = datos_formulario.get('rfc')
            empresa.ciec = datos_formulario.get('ciec')
            empresa.activa = datos_formulario.get('activa')
            empresa.email = datos_formulario.get('email')
            empresa.logo = datos_formulario.get('logo')
            empresa.certificado = datos_formulario.get('certificado')
            empresa.llave = datos_formulario.get('llave')
            empresa.contrasena = datos_formulario.get('contrasena')

            if request.user.is_staff:
                empresa.usuario = datos_formulario.get('usuario')
            else:
                empresa.usuario = request.user

            empresa.save()

            return redirect(reverse('configuracion:empresa_lista'))

        else:
            contexto = {
                'form': formulario
            }
            return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
class EmpresaUpdateView(View):

    def __init__(self):
        self.template_name = 'empresa/empresa_editar.html'

    def get(self, request, pk):

        empresa = get_object_or_404(Empresa, pk=pk)

        formulario = EmpresaEditForm(
            username=request.user,
            instance=empresa
        )

        contexto = {
            'form': formulario,
            'empresa': empresa
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):

        empresa = get_object_or_404(Empresa, pk=pk)
        self.clave = empresa.clave

        formulario = EmpresaEditForm(
            request.POST,
            request.FILES,
            username=request.user,
            instance=empresa
        )

        if formulario.is_valid():

            # datos_formulario = formulario.cleaned_data
            # empresa.razon_social = datos_formulario.get('razon_social')
            # empresa.rfc = datos_formulario.get('rfc')
            # empresa.ciec = datos_formulario.get('ciec')
            # empresa.activa = datos_formulario.get('activa')
            # empresa.email = datos_formulario.get('email')
            # empresa.logo = datos_formulario.get('logo')
            # empresa.certificado = datos_formulario.get('certificado')
            # empresa.llave = datos_formulario.get('llave')
            # empresa.contrasena = datos_formulario.get('contrasena')
            empresa = formulario.save(commit=False)

            # if request.user.username == 'root':
            #     empresa.usuario = datos_formulario.get('usuario')

            empresa.save()

            return redirect(
                reverse('configuracion:empresa_lista')
            )

        contexto = {
            'form': formulario,
            'clave': self.clave
        }
        return render(request, self.template_name, contexto)


@method_decorator(login_required, name='dispatch')
class EmpresaTestCredentials(View):

    def __init__(self):
        self.template_name = "empresa/empresa_verificacion.html"

    def get(self, request, pk):
        test_Credentials.delay(pk)
        return render(request, self.template_name, {})
