# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Models Django:
from django.contrib.auth.models import User


class Empresa(models.Model):

    clave = models.CharField(max_length=144, null=True)
    razon_social = models.CharField(max_length=144)
    logo = models.ImageField(upload_to='empresas', blank=True, null=True)
    rfc = models.CharField(max_length=144)
    ciec = models.CharField(max_length=144)
    activa = models.BooleanField(default=False)
    usuario = models.ForeignKey(User)
    email = models.EmailField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.razon_social


# class Responsable(models.Model):
#     nombre = models.CharField(max_length=144)
#     correo = models.EmailField()
#     empresa = models.ForeignKey(Empresa)

#     def __str__(self):
#         return "{} - {}".format(self.nombre, self.empresa)
