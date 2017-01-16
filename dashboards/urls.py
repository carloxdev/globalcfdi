# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas Home
from .views import ResumenAllByYear
from .views import ResumenOneByMonth

urlpatterns = [


    # ----------------- Home Site ----------------- #

    url(
        r'^dashboard/all_by_year/$',
        ResumenAllByYear.as_view(),
        name='dashboard.all_by_year'
    ),
    url(
        r'^dashboard/one_by_month/$',
        ResumenOneByMonth.as_view(),
        name='dashboard.one_by_month'
    ),

]
