# -*- coding: utf-8 -*-


# Librerias Python:
from datetime import date
from datetime import timedelta

# Librerias Propias:
from slaves import Contador
from tools.comunicacion import Postman
from tools.datos import Chronos

# Librerias del Sitio:
from sitio import ModeloEmpresa
from sitio import ModeloAmbiente


class Cfdineitor(object):

    def __init__(self, _enviroment, _run_path):
        self.ambiente = _enviroment
        self.ruta_ejecucion = _run_path
        self.cartero = None

        self.get_appconfig()

    def get_appconfig(self):

        app_config = ModeloAmbiente.get(self.ambiente)

        self.cartero = Postman(
            app_config.account_email,
            app_config.password_email,
            app_config.smtp_server
        )

    def get_Invoices_Company(self, _empresa_clave):

        empresa = ModeloEmpresa.get(_empresa_clave)
        esclavo = Contador(empresa, self.ruta_ejecucion, self.ambiente)
        lista_meses = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.get_Invoices_ByMonths(esclavo, "RECIBIDAS", lista_meses)
        self.get_Invoices_ByMonths(esclavo, "EMITIDAS", lista_meses)

    def get_Invoices_AllCompanies(self):

        lista_empresas = ModeloEmpresa.get_Activas()

        for empresa in lista_empresas:
            esclavo = Contador(empresa, self.ruta_ejecucion, self.ambiente)
            self.get_Invoices_LastThreeDays(esclavo, "RECIBIDAS")
            self.get_Invoices_LastThreeDays(esclavo, "EMITIDAS")

    def get_Invoices_LastThreeDays(self, _esclavo, _tipo):

        ahora = date.today()

        contador = 1
        while contador <= 3:

            try:
                fecha = ahora - timedelta(days=contador)
                log = _esclavo.get_Invoices_ByDay(_tipo, fecha)
                self.informar_Resultados(log, _esclavo.empresa, _tipo)
                contador += 1
            except Exception, error:
                print str(error)

    def get_Invoices_ByMonths(self, _esclavo, _tipo, _lista_meses):

        ahora = date.today()
        anio = ahora.year

        for mes in _lista_meses:

            dias = Chronos.getDays(mes, anio)
            for dia in dias:
                fecha = date(anio, mes, dia)
                log = _esclavo.get_Invoices_ByDay(_tipo, fecha)
                self.informar_Resultados(log, _esclavo.empresa, _tipo)

    def informar_Resultados(self, _log, _empresa, _tipo):

        if _log:

            if _log.estado == '':
                _log.estado = "Operacion Interrumpida"
                _log.resumen_text = "Lo operacion no termino de forma natural. Favor de comunicarse con el administrador"

            self.cartero.send_GmailMessage_WithAttach(
                _empresa.email,
                "[{}] - [{}] en obtencion de facturas {}".format(
                    _empresa.clave, _log.estado, _tipo),
                _log.resumen_text,
                _log.abspath
            )
        else:
            self.cartero.send_GmailMessage_WithAttach(
                _empresa.email,
                "[{}] - [ERROR] en obtencion de facturas {}".format(
                    _empresa.clave, _tipo),
                "El proceso tuvo algun error en su inicio, que no logro generar LOG. Favor de comunicarse con el administrador",
            )
