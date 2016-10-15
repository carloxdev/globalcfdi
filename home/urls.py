# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings

# Vistas Administracion
from .views import Index
from .views import Login
from .views import Dashboard
from .views import Servicios

# Vistas de Usuario
from .views import UsuarioListView
from .views import UsuarioCreateView
from .views import UsuarioEditView

urlpatterns = [


    # ----------------- Admin Site ----------------- #

    url(
        r'^$',
        Index.as_view(),
        name='home.index'
    ),
    url(
        r'^login/$',
        Login.as_view(),
        name='home.login'
    ),
    url(
        r'^dashboard/$',
        Dashboard.as_view(),
        name='home.dashboard'
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        {'next_page': settings.LOGIN_URL},
        name='home.logout'
    ),
    url(
        r'^servicios/$',
        Servicios.as_view(),
        name='home.servicios'
    ),

    # ----------------- USUARIO ----------------- #

    url(
        r'^usuarios/$',
        UsuarioListView.as_view(),
        name='home.usuario_lista'
    ),
    url(
        r'^usuarios/nuevo/$',
        UsuarioCreateView.as_view(),
        name='home.usuario_nuevo'
    ),
    url(
        r'^usuarios/editar/(?P<pk>.*)/$',
        UsuarioEditView.as_view(),
        name='home.usuario_editar'
    ),

]
