# -*- coding: utf-8 -*-

# Librerias Django
from django.forms import ModelForm
from django.forms import TextInput
from django.forms import Select
from django.forms import PasswordInput

# Modelos:
from .models import Empresa


class EmpresaCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('username')
        super(EmpresaCreateForm, self).__init__(*args, **kwargs)

        if self.usuario.is_superuser is False:
            del self.fields['usuario']

    class Meta:
        model = Empresa
        fields = '__all__'
        exclude = [
            'verificada',
            'certificado',
            'llave',
        ]
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control'}),
            'razon_social': TextInput(attrs={'class': 'form-control'}),
            'rfc': TextInput(attrs={'class': 'form-control'}),
            'ciec': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'usuario': Select(attrs={'class': 'form-control'}),
            'contrasena': PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'ciec': "Clave CIEC",
        }


class EmpresaEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('username')
        super(EmpresaEditForm, self).__init__(*args, **kwargs)

        if self.usuario.is_superuser is False:
            del self.fields['usuario']

    class Meta:
        model = Empresa
        fields = '__all__'
        exclude = [
            'clave',
            'verificada',
            'certificado',
            'llave',
        ]
        widgets = {
            'razon_social': TextInput(attrs={'class': 'form-control'}),
            'rfc': TextInput(attrs={'class': 'form-control'}),
            'ciec': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'usuario': Select(attrs={'class': 'form-control'}),
            'contrasena': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'ciec': "Clave CIEC",
        }
