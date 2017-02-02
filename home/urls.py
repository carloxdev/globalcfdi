# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas Home
from .views import Index
from .views import Servicios
from .views import Contactanos
from .views import QuienesSomos

# from .views import Ejemplo

app_name = "home"

urlpatterns = [

    url(
        r'^index$',
        Index.as_view(),
        name='index'
    ),
    url(
        r'^servicios/$',
        Servicios.as_view(),
        name='servicios'
    ),
    url(
        r'^contactanos/$',
        Contactanos.as_view(),
        name='contactanos'
    ),
    url(
        r'^quienessomos/$',
        QuienesSomos.as_view(),
        name='quienes_somos'
    ),
    # url(
    #     r'^ejemplo/$',
    #     Ejemplo.as_view(),
    #     name='home.ejemplo'
    # ),
]
