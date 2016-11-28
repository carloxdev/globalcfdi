# -*- coding: utf-8 -*-

# Librerias Django:

# Urls
from django.conf.urls import url

# Aplicacion
from django.conf import settings

# Autentificacion
from django.contrib.auth import views as auth_views

# Vistas
from .views import Login
from .views import UsuarioListView
from .views import UsuarioCreateView
from .views import UsuarioEditView

urlpatterns = [


    # ----------------- SEGURIDAD ----------------- #

    url(
        r'^login/$',
        Login.as_view(),
        name='seguridad.login'
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        {'next_page': settings.LOGIN_URL},
        name='seguridad.logout'
    ),


    # ----------------- USUARIO ----------------- #

    url(
        r'^usuarios/$',
        UsuarioListView.as_view(),
        name='seguridad.usuario_lista'
    ),
    url(
        r'^usuarios/nuevo/$',
        UsuarioCreateView.as_view(),
        name='seguridad.usuario_nuevo'
    ),
    url(
        r'^usuarios/editar/(?P<pk>.*)/$',
        UsuarioEditView.as_view(),
        name='seguridad.usuario_editar'
    ),

]
