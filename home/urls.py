# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas Home
from .views import Index
from .views import Dashboard
from .views import Servicios
from .views import Contactanos
from .views import Quienessomos


urlpatterns = [


    # ----------------- Home Site ----------------- #

    url(
        r'^$',
        Index.as_view(),
        name='home.index'
    ),
    url(
        r'^dashboard/$',
        Dashboard.as_view(),
        name='home.dashboard'
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
        Quienessomos.as_view(),
        name='home.quienessomos'
    ),
]
