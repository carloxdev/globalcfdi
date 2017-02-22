# -*- coding: utf-8 -*-

# Librerias Python:
import os

# Librerias de Terceros
from celery import task

# Librerias Propias:
from core.tecnology import Cfdineitor

from core.slaves import Contador


# @task(bind=True, max_retries=5)
# def obtener_Facturas(self, _empresa_clave, _fecha_inicio, _fecha_final):

#     print "Empresa: {}".format(_empresa_clave)
#     print "Fecha Inicio: {}".format(_fecha_inicio)
#     print "Fecha Final: {}".format(_fecha_final)

#     try:
#         fecha_inicio = datetime.strptime(_fecha_inicio, "%Y-%m-%d")
#         fecha_final = datetime.strptime(_fecha_final, "%Y-%m-%d")

#         run_path = os.path.abspath(
#             os.path.join(os.getcwd(), os.pardir, 'Sitio')
#         )
#         app = Cfdineitor("PRODUCCION", run_path)
#         app.get_ByRange(
#             _empresa_clave,
#             fecha_inicio,
#             fecha_final
#         )
#     except Exception as e:
#         print str(e)
#         print "Se volvera intentar en 4 sec."
#         self.retry(countdown=4, exc=e)


# @task(bind=True, max_retries=5)
# def obtener_Facturas(self, _empresa_clave, _fecha_inicio, _fecha_final):
#     try:
#         print "Empresa: {}".format(_empresa_clave)
#         print "Fecha Inicio: {}".format(_fecha_inicio)
#         print "Fecha Final: {}".format(_fecha_final)

#         fecha_inicio = datetime.strptime(_fecha_inicio, "%Y-%m-%d")
#         fecha_final = datetime.strptime(_fecha_final, "%Y-%m-%d")

#         run_path = os.path.abspath(
#             os.path.join(os.getcwd(), os.pardir, 'Sitio')
#         )

#         fechas = Chronos.getDays_FromRange(fecha_inicio, fecha_final)

#         empresa = Empresa.objects.get(clave=_empresa_clave)

#         esclavo = Contador(empresa, run_path)

#         # Descargar Emitidas y Recibidas por cada fecha
#         for fecha in fechas:
#             esclavo.get_ByDay(TIPOS_FACTURA[0], fecha)
#             print "Esperando 15 sec para siguiente descarga"
#             time.sleep(15)
#             esclavo.get_ByDay(TIPOS_FACTURA[1], fecha)
#             print "Esperando 15 sec para siguiente descarga"
#             time.sleep(15)

#     except Exception as e:
#         print str(e)
#         print "Se volvera intentar en 4 sec."
#         self.retry(countdown=4, exc=e)

@task(bind=True, max_retries=5)
def obtener_Facturas(self, _empresa, _fecha, _tipo_factura):
    try:
        run_path = os.path.abspath(
            os.path.join(os.getcwd(), os.pardir, 'Sitio')
        )

        esclavo = Contador(_empresa, run_path)
        esclavo.get_ByDay(_tipo_factura, _fecha)

    except Exception as e:
        print str(e)
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
