# -*- coding: utf-8 -*-

# Librerias Django:

# Urls
from django.conf.urls import url

# Aplicacion
from django.conf import settings

# Autentificacion
from django.contrib.auth import views as auth_views

# Vistas de Usuario
from .views import UsuarioLogin
from .views import UsuarioListView
from .views import UsuarioCreateView
from .views import UsuarioEditView

urlpatterns = [


    # ----------------- USUARIO ----------------- #

    url(
        r'^login/$',
        UsuarioLogin.as_view(),
        name='home.login'
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        {'next_page': settings.LOGIN_URL},
        name='home.logout'
    ),
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
