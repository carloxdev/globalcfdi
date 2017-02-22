# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Models Django:
from django.contrib.auth.models import User

# Librerias Propias
from .utilities import get_FilePath
from .validators import validate_cert
from .validators import validate_key
from .validators import validate_size


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
        null=True,
        validators=[
            validate_cert,
            validate_size
        ]
    )
    llave = models.FileField(
        upload_to=get_FilePath,
        blank=True,
        null=True,
        validators=[
            validate_key,
            validate_size
        ]
    )
    contrasena = models.CharField(max_length=144, null=True, blank=True)
    activa = models.BooleanField(default=False)
    usuario = models.ForeignKey(User)
    email = models.EmailField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clave.encode("utf-8")
