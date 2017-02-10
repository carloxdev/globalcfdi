# -*- coding: utf-8 -*-

# Librerias Python:
import os
from datetime import datetime

# Librerias de Terceros
from celery import task

# Librerias Propias:
from core.tecnology import Cfdineitor


@task
def obtener_Facturas(_empresa_clave, _fecha_inicio, _fecha_final):

    print "Empresa: {}".format(_empresa_clave)
    print "Fecha Inicio: {}".format(_fecha_inicio)
    print "Fecha Final: {}".format(_fecha_final)

    try:
        fecha_inicio = datetime.strptime(_fecha_inicio, "%Y-%m-%d")
        fecha_final = datetime.strptime(_fecha_final, "%Y-%m-%d")

        run_path = os.path.abspath(
            os.path.join(os.getcwd(), os.pardir, 'Sitio')
        )
        app = Cfdineitor("PRODUCCION", run_path)
        app.get_ByRange(
            _empresa_clave,
            fecha_inicio,
            fecha_final
        )
    except Exception as e:
        print str(e)


@task
def obtener_Facturas_Daily():

    run_path = os.path.abspath(
        os.path.join(os.getcwd(), os.pardir, 'Sitio')
    )
    app = Cfdineitor("PRODUCCION", run_path)
    app.get_AllCompanies_Last3Days()


@task
def validar_Facturas_Daily():

    run_path = os.path.abspath(
        os.path.join(os.getcwd(), os.pardir, 'Sitio')
    )
    app = Cfdineitor("PRODUCCION", run_path)
    app.valid_AllCompanies_Last2Monts()
