# -*- coding: utf-8 -*-

# Librerias Python:
import os

# Modelos
from configuracion.models import Empresa

# Librerias de Terceros
from celery import task

# Librerias propias:
# from core.sat import WebSat


@task(bind=True, max_retries=3)
def test_Credentials(self, _pk):
    pass
    # try:

    #     # Se obtiene variable de ejecucion:
    #     run_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'Sitio'))
    #     print run_path

    #     # Buscar datos de la empresa:
    #     empresa = Empresa.objects.get(pk=_pk)

    #     empresa.verificada = "PRO"
    #     empresa.save()

    #     elSat = WebSat(run_path)
    #     elSat.open()
    #     resultado = elSat.login_Fiel(
    #         empresa.certificado.path,
    #         empresa.llave.path,
    #         empresa.contrasena,
    #         empresa.rfc
    #     )

    #     elSat.close()

    #     if resultado:

    #         # Cambia estado de verificacion
    #         empresa.verificada = "VER"
    #         empresa.save()

    # except Exception as e:
    #     empresa.verificada = "ERR"
    #     empresa.save()
    #     print "Volviendo a intentar en 4 seg."
    #     self.retry(countdown=4, exc=e)
