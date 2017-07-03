# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models
from django.conf import settings


class F0101(models.Model):

    clave = models.IntegerField(db_column='ABAN8', primary_key=True)
    nombre = models.CharField(max_length=40, db_column='ABALPH')
    tipo = models.CharField(max_length=3, db_column='ABAT1')
    rfc = models.CharField(max_length=20, db_column='ABTAX')

    class Meta:
        managed = False
        if settings.DEBUG:
            db_table = u'"CRPDTA"."F0101"'
        else:
            db_table = u'"PRODDTA"."F0101"'

    def __str__(self):
        return "{} - {}".format(self.clave, self.nombre)


class F5903000(models.Model):
    # UUID
    ftgenkey = models.CharField(max_length=40, primary_key=True)

    # RFC EMISOR
    fttax = models.CharField(max_length=20, null=True, blank=True)
    # RFC RECEPTOR
    fttaxs = models.CharField(max_length=20, null=True, blank=True)
    # Tipo (CXC, CXP)
    ftbrtpo = models.CharField(max_length=3)
    fttxr1 = models.IntegerField(default=0)
    fttxr2 = models.IntegerField(default=0)
    fttxr3 = models.IntegerField(default=0)
    fttxr4 = models.IntegerField(default=0)
    fttxr5 = models.IntegerField(default=0)
    ftafa1 = models.IntegerField(default=0)
    ftafa2 = models.IntegerField(default=0)
    ftafa3 = models.IntegerField(default=0)
    ftafa4 = models.IntegerField(default=0)
    ftafa5 = models.IntegerField(default=0)
    # MONEDA
    ftcrcd = models.CharField(max_length=3, null=True, blank=True)
    # Tasa de conversion
    ftcrr = models.IntegerField(default=0)
    # Total
    ftamrt1 = models.IntegerField(default=0)
    # Subtotal
    ftamrt2 = models.IntegerField(default=0)
    # Total
    ftamrt3 = models.IntegerField(default=0)
    ftlo01 = models.CharField(max_length=5, null=True, blank=True)
    fturab = models.IntegerField(default=0)
    fturat = models.IntegerField(default=0)
    # CODIGO PROCESADO  FTURCD (default 0)
    fturcd = models.CharField(max_length=2, null=True, blank=True)
    fturdt = models.IntegerField(default=0)
    fturrf = models.CharField(max_length=15, null=True, blank=True)
    ftuser = models.CharField(max_length=10, null=True, blank=True)
    ftpid = models.CharField(max_length=10, null=True, blank=True)
    ftjobn = models.CharField(max_length=10, null=True, blank=True)
    ftupmj = models.IntegerField(default=0)
    ftupmt = models.IntegerField(default=0)
    ftivd = models.IntegerField(default=0)
    ftan8 = models.IntegerField(default=0)

    class Meta:
        managed = False
        if settings.DEBUG:
            db_table = u'"CRPDTA"."F5903000"'
        else:
            db_table = u'"PRODDTA"."F5903000"'

    def __str__(self):
        return self.FTGENKEY
