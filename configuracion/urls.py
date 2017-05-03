# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import EmpresaListView
from .views import EmpresaCreateView
from .views import EmpresaUpdateView
from .views import EmpresaTestCredentials


# ----------------- Empresas ----------------- #

app_name = "configuracion"

urlpatterns = [
    url(
        r'^empresas/$',
        EmpresaListView.as_view(),
        name='empresa_lista'
    ),
    url(
        r'^empresas/nuevo/$',
        EmpresaCreateView.as_view(),
        name='empresa_nuevo'
    ),
    url(
        r'^empresas/editar/(?P<pk>.*)/$',
        EmpresaUpdateView.as_view(),
        name='empresa_editar'
    ),
    url(
        r'^empresas/test_credentials/(?P<pk>.*)/$',
        EmpresaTestCredentials.as_view(),
        name='empresa_verificacion'
    ),
]
