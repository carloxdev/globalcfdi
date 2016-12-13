# -*- coding: utf-8 -*-


# Librerias Python:
from datetime import date
from datetime import timedelta


# Librerias Propias:
from slaves import Contador, TIPOS_FACTURA
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

    def get_Invoices_ByRange(self, _empresa_clave, _f_inicio, _f_final):

        # Obtener fechas entre rango dado:
        fechas = Chronos.getDays_FromRange(_f_inicio, _f_final)

        # Obtener datos de empresa:
        empresa = ModeloEmpresa.get(_empresa_clave)

        # Crear esclavo Contador:
        esclavo = Contador(empresa, self.ruta_ejecucion, self.ambiente)

        # Descargar Emitidas y Recibidas por cada fecha
        for fecha in fechas:
            esclavo.get_Invoices_ByDay(TIPOS_FACTURA[0], fecha)
            esclavo.get_Invoices_ByDay(TIPOS_FACTURA[1], fecha)

        # self.informar_Resultados(log, esclavo.empresa, "RECIBIDAS")

    def get_Invoices_Today(self, _empresa_clave):

        # Obtener fecha:
        hoy = date.today()

        # Obtener datos de empresa:
        empresa = ModeloEmpresa.get(_empresa_clave)

        # Crear esclavo Contador:
        esclavo = Contador(empresa, self.ruta_ejecucion, self.ambiente)

        # Descargar facturas:
        esclavo.get_Invoices_ByDay(TIPOS_FACTURA[0], hoy)
        esclavo.get_Invoices_ByDay(TIPOS_FACTURA[1], hoy)

    def get_Invoices_AllCompanies_Today(self):

        # Se obtienen todas las empresas activas:
        lista_empresas = ModeloEmpresa.get_All()

        # Por cada empresa se descagan las facturas de los ultimos 3 dias
        for empresa in lista_empresas:
            self.get_Invoices_Today(empresa.clave)

    def get_Invoices_Last3Days(self, _empresa_clave):

        # Obtenemos rango de fechas
        hoy = date.today()
        anteayer = hoy - timedelta(days=3)

        # Se descargan las facturas en ese rango
        self.get_Invoices_ByRange(_empresa_clave, anteayer, hoy)

    def get_Invoices_AllCompanies_Last3Days(self):

        # Se obtienen todas las empresas activas:
        lista_empresas = ModeloEmpresa.get_All()

        # Por cada empresa se descagan las facturas de los ultimos 3 dias
        for empresa in lista_empresas:
            self.get_Invoices_Last3Days(empresa.clave)

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
