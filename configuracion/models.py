# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Models Django:
from django.contrib.auth.models import User

# Utilidades
from .utilities import get_FilePath


class Empresa(models.Model):

    clave = models.CharField(max_length=144, null=True)
    razon_social = models.CharField(max_length=144)
    logo = models.ImageField(
        upload_to='empresas/imagenes',
        blank=True,
        null=True
    )
    rfc = models.CharField(max_length=144, null=True, blank=True)
    ciec = models.CharField(max_length=144, null=True, blank=True)
    certificado = models.FileField(
        upload_to=get_FilePath,
        blank=True,
        null=True
    )
    llave = models.FileField(
        upload_to=get_FilePath,
        blank=True,
        null=True
    )
    contrasena = models.CharField(max_length=144, null=True, blank=True)
    activa = models.BooleanField(default=False)
    usuario = models.ForeignKey(User)
    email = models.EmailField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clave.encode("utf-8")
