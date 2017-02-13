# -*- coding: utf-8 -*-

# Librerias django
from django.contrib import admin

# Modelos:
from .models import Empresa


@admin.register(Empresa)
class AdminEmpresa(admin.ModelAdmin):
    list_display = (
        'clave',
        'razon_social',
        'rfc',
        'ciec',
        'certificado',
        'llave',
        'contrasena',
        'activa',
        'usuario',
        'email',
        'logo',
        'created_date',
        'updated_date',
    )
