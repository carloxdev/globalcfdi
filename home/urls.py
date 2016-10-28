# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas Home
from .views import Index
from .views import Dashboard
from .views import Servicios


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
]
