# -*- coding: utf-8 -*-

# Librerias Django
from django.core.urlresolvers import reverse

# Django Atajos
from django.shortcuts import render
from django.shortcuts import redirect

# Django Generic Views
from django.views.generic.base import View


class Index(View):

    def __init__(self):
        self.template_name = 'home/index.html'

    def get(self, request):

        if request.user.is_authenticated():
            return redirect(reverse('dashboards:all_by_year'))

        else:
            return render(request, self.template_name, {})

        return render(request, self.template_name, {})

    def post(self, request):
        return render(request, self.template_name, {})


class Servicios(View):

    def __init__(self):
        self.template_name = 'home/servicios.html'

    def get(self, request):
        return render(request, self.template_name, {})


class Contactanos(View):

    def __init__(self):
        self.template_name = 'home/contactanos.html'

    def get(self, request):
        return render(request, self.template_name, {})


class QuienesSomos(View):

    def __init__(self):
        self.template_name = 'home/quienes_somos.html'

    def get(self, request):
        return render(request, self.template_name, {})
