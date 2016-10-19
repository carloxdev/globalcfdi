# -*- coding: utf-8 -*-

# Liberias django:
from __future__ import unicode_literals
from django.db import models


class Ambiente(models.Model):
    clave = models.CharField(max_length=255, null=True, blank=True)
    account_email = models.CharField(max_length=255, null=True, blank=True)
    password_email = models.CharField(max_length=255, null=True, blank=True)
    smtp_sever = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.clave
