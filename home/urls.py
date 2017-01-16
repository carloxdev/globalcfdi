# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas Home
from .views import Index
from .views import Servicios
from .views import Contactanos
from .views import QuienesSomos

# from .views import Ejemplo

urlpatterns = [

    url(
        r'^$',
        Index.as_view(),
        name='home.index'
    ),
    url(
        r'^servicios/$',
        Servicios.as_view(),
        name='home.servicios'
    ),
    url(
        r'^contactanos/$',
        Contactanos.as_view(),
        name='home.contactanos'
    ),
    url(
        r'^quienessomos/$',
        QuienesSomos.as_view(),
        name='home.quienes_somos'
    ),
    # url(
    #     r'^ejemplo/$',
    #     Ejemplo.as_view(),
    #     name='home.ejemplo'
    # ),
]
