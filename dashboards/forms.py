# -*- coding: utf-8 -*-

# Librerias django:
from django import forms

ANIOS = (
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
)


class DasboardFormFiltros(forms.Form):

    anio = forms.ChoiceField(
        choices=ANIOS,
        widget=forms.Select(
            attrs={'class': 'app-page-select'}
        )
    )
