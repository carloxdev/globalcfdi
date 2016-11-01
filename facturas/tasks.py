# -*- coding: utf-8 -*-

# Librerias Python:
import os

# Librerias de Terceros
from celery import task

# Librerias Propias:
from core.tecnology import Cfdineitor


@task
def imprimir_Datos():
    run_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'Sitio'))
    print run_path
    app = Cfdineitor("PRODUCCION", run_path)
    app.get_Invoices_Company("LSV")

    # print "HOla"
