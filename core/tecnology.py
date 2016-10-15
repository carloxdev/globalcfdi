# -*- coding: utf-8 -*-


# Librerias Python:
from datetime import date

# Librerias Propias:
from slaves import Contador

# Librerias del Sitio:
from sitio import ModeloEmpresa


class Cfdineitor(object):

    def __init__(self, _enviroment, _run_path):
        self.ambiente = _enviroment
        self.ruta_ejecucion = _run_path

    def get_Invoices_AllCompanies(self):

        lista_empresas = ModeloEmpresa.get_Activas()

        for empresa in lista_empresas:

            esclavo = Contador(empresa, self.ruta_ejecucion)

            esclavo.get_Invoices_LastThreeDays("RECIBIDAS")
            esclavo.get_Invoices_LastThreeDays("EMITIDAS")
