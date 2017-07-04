# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

# Own's Libraries
from configuracion.urls_rest import router_configuracion
from facturas.urls_rest import router_facturas

# Librerias necesarias para publicar Medias en DEBUG
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api-configuracion/', include(router_configuracion.urls)),
    url(r'^api-facturas/', include(router_facturas.urls)),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    url(r'', include('home.urls', namespace="home")),
    url(r'', include('seguridad.urls', namespace="seguridad")),
    url(r'', include('configuracion.urls', namespace="configuracion")),
    url(r'', include('facturas.urls', namespace="facturas")),
    url(r'', include('dashboards.urls', namespace="dashboards")),
]


if settings.DEBUG:

    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
