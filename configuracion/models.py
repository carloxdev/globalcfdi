# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Models Django:
from django.contrib.auth.models import User

# Librerias Propias
from .utilities import get_FilePath
from .utilities import get_ImagePath

from .validators import validate_cert
from .validators import validate_key
from .validators import validate_size
from .validators import validate_clave


class Empresa(models.Model):

    VERIFICACION_ESTADO = (
        ('VER', 'Verificada'),
        ('PEN', 'Sin Verificar'),
        ('PRO', 'Verificando'),
        ('ERR', 'Error en verificacion'),
    )

    clave = models.CharField(
        max_length=144,
        null=True,
        validators=[validate_clave],
        unique=True
    )
    razon_social = models.CharField(max_length=144)
    logo = models.ImageField(
        upload_to=get_ImagePath,
        blank=True,
        null=True
    )
    rfc = models.CharField(
        max_length=144,
        null=True,
        blank=True,
        validators=[validate_clave]
    )
    ciec = models.CharField(
        max_length=144,
        null=True,
        blank=True,
        validators=[validate_clave]
    )
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
    contrasena = models.CharField(
        max_length=144,
        null=True,
        blank=True,
        validators=[validate_clave]
    )
    verificada = models.CharField(
        max_length=4,
        choices=VERIFICACION_ESTADO,
        default="PEN"
    )
    activa = models.BooleanField(default=False)
    usuario = models.ForeignKey(User)
    email = models.EmailField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clave.encode("utf-8")


class EmailAccount(models.Model):
    clave = models.CharField(max_length=255, null=True, blank=True)
    account = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    smtp_server = models.CharField(max_length=255, null=True, blank=True)
    people = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.clave.encode("utf-8")
