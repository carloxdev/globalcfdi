# -*- coding: utf-8 -*-

# Librerias Python:
import os

# Otros Modelos
from configuracion.models import Empresa

# Librerias de Terceros
from celery import task
from dateutil import parser

# Librerias Propias:
from core.tecnology import Cfdineitor
from core.slaves import Contador


@task(bind=True, max_retries=5)
def obtener_Facturas(self, _empresa_clave, _fecha, _tipo):
    try:
        run_path = os.path.abspath(
            os.path.join(os.getcwd(), os.pardir, 'Sitio')
        )

        fecha = parser.parse(_fecha)

        empresa = Empresa.objects.get(clave=_empresa_clave)

        esclavo = Contador(empresa, run_path)
        esclavo.get_ByDay(_tipo, fecha)

    except Exception as e:
        print "Se volvera intentar en 4 sec."
        self.retry(countdown=4, exc=e)


@task(bind=True, max_retries=5)
def obtener_Facturas_Daily(self):

    try:
        run_path = os.path.abspath(
            os.path.join(os.getcwd(), os.pardir, 'Sitio')
        )
        app = Cfdineitor("PRODUCCION", run_path)
        app.get_AllCompanies_Last3Days()

    except Exception as e:
        self.retry(countdown=4, exc=e)


@task(bind=True, max_retries=5)
def validar_Facturas_Daily(self):

    try:
        run_path = os.path.abspath(
            os.path.join(os.getcwd(), os.pardir, 'Sitio')
        )
        app = Cfdineitor("PRODUCCION", run_path)
        app.valid_AllCompanies_Last2Monts()

    except Exception as e:
        self.retry(countdown=4, exc=e)
