# -*- coding: utf-8 -*-

# Librerias django
from django.contrib import admin

# Modelos:
from .models import Ambiente


@admin.register(Ambiente)
class AdminAmbiente(admin.ModelAdmin):
    list_display = (
        'clave',
        'account_email',
        'password_email',
        'smtp_server',
    )
