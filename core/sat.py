# -*- coding: utf-8 -*-

# Librerias Terceros:
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from requests import Request, Session
from xml.etree import ElementTree

# Librerias Propias:
from tools.mistakes import ErrorEjecucion
from tools.mistakes import ErrorValidacion
from tools.datos import Visualizador
from tools.datos import Chronos


class SitioLogin(object):
    url = 'https://cfdiau.sat.gob.mx/nidp/app/login' \
        '?id=SATUPCFDiCon&sid=0&option=credential&sid=0'
    user = 'Ecom_User_ID'
    password = 'Ecom_Password'
    submit = 'submit'


class SitioLoginFiel(object):
    url = 'https://cfdiau.sat.gob.mx/nidp/app/login' \
        '?id=SATx509Custom&sid=0&option=credential&sid=0'
    input_certificado = 'certificate'
    input_llave = 'privateKey'
    input_contrasena = 'privateKeyPassword'
    input_rfc = 'userID'
    boton_submit = 'submit'


class SitioCFDI(object):
    url = 'https://portalcfdi.facturaelectronica.sat.gob.mx/{}'


class SitioFacturasRecibidas(object):
    url = 'https://portalcfdi.facturaelectronica.sat.gob.mx/' \
        'ConsultaReceptor.aspx'
    uuid = 'ctl00_MainContent_TxtUUID'
    date = 'ctl00_MainContent_RdoFechas'
    emisor = 'ctl00_MainContent_TxtRfcReceptor'
    date_from = 'ctl00_MainContent_CldFechaInicial2_Calendario_text'
    date_from_name = 'ctl00$MainContent$CldFechaInicial2$Calendario_text'
    date_to = 'ctl00_MainContent_CldFechaFinal2_Calendario_text'
    date_to_name = 'ctl00$MainContent$CldFechaFinal2$Calendario_text'
    year = 'DdlAnio'
    month = 'ctl00_MainContent_CldFecha_DdlMes'
    day = 'ctl00_MainContent_CldFecha_DdlDia'
    start_hour = 'ctl00_MainContent_CldFecha_DdlHora'
    start_minute = 'ctl00_MainContent_CldFecha_DdlMinuto'
    start_second = 'ctl00_MainContent_CldFecha_DdlSegundo'
    end_hour = 'ctl00_MainContent_CldFecha_DdlHoraFin'
    end_minute = 'ctl00_MainContent_CldFecha_DdlMinutoFin'
    end_second = 'ctl00_MainContent_CldFecha_DdlSegundoFin'
    resultados = 'ctl00_MainContent_PnlResultados'
    noresultados = 'ctl00_MainContent_PnlNoResultados'
    submit = 'ctl00_MainContent_BtnBusqueda'
    download = 'BtnDescarga'


class SitioFacturasEmitidas(object):
    url = 'https://portalcfdi.facturaelectronica.sat.gob.mx/' \
        'ConsultaEmisor.aspx'
    uuid = 'ctl00_MainContent_TxtUUID'
    date = 'ctl00_MainContent_RdoFechas'
    receptor = 'ctl00_MainContent_TxtRfcReceptor'
    date_from = 'ctl00_MainContent_CldFechaInicial2_Calendario_text'
    date_from_name = 'ctl00$MainContent$CldFechaInicial2$Calendario_text'
    date_to = 'ctl00_MainContent_CldFechaFinal2_Calendario_text'
    date_to_name = 'ctl00$MainContent$CldFechaFinal2$Calendario_text'
    start_hour = 'ctl00_MainContent_CldFechaInicial2_DdlHora'
    start_minute = 'ctl00_MainContent_CldFechaInicial2_DdlMinuto'
    start_second = 'ctl00_MainContent_CldFechaInicial2_DdlSegundo'
    end_hour = 'ctl00_MainContent_CldFechaFinal2_DdlHora'
    end_minute = 'ctl00_MainContent_CldFechaFinal2_DdlMinuto'
    end_second = 'ctl00_MainContent_CldFechaFinal2_DdlSegundo'
    resultados = 'ctl00_MainContent_PnlResultados'
    noresultados = 'ctl00_MainContent_PnlNoResultados'
    submit = 'ctl00_MainContent_BtnBusqueda'
    download = 'BtnDescarga'


class WebSat(object):

    def __init__(self, _download_abspath):
        self.navegador = None
        self.download_abspath = _download_abspath

    def close(self):

        if self.navegador:
            self.navegador.quit()
            self.navegador = None

    def disconnect(self):

        if self.navegador:
            try:
                link = self.navegador.find_element_by_partial_link_text(
                    'Cerrar Sesi'
                )
                link.click()
                print "Desconeccion del SAT....OK"

            except Exception, error:

                raise ErrorEjecucion(
                    "WebSAT.disconnect()",
                    type(error).__name__,
                    str(error)
                )

            finally:
                self.navegador.quit()
                self.navegador = None

    def download(self, _links):

        try:
            if len(_links) != 0:

                qtyLinks = len(_links)

                for indice, link in enumerate(_links):

                    print '--- Descargando Factura {0} de {1}'.format(
                        indice + 1,
                        qtyLinks
                    )
                    link_descarga = SitioCFDI.url.format(
                        link.get_attribute('onclick').split("'")[1]
                    )
                    self.navegador.get(link_descarga)

                Chronos.sleep()
                print "Descarga de facturas....OK"
            else:

                self.close()

                raise ErrorValidacion(
                    'Favor de proporcionar links a descargar'
                )

        except Exception, error:

            self.close()

            raise ErrorEjecucion(
                'WebSAT.download()',
                type(error).__name__,
                str(error)
            )

    def login_Fiel(self, _path_cert, _path_key, _password, _rfc):

        try:

            # Ir al sitio login:
            self.navegador.get(SitioLoginFiel.url)

            wait_login = WebDriverWait(self.navegador, 20)
            wait_login.until(
                EC.presence_of_element_located((By.ID, "btnCert"))
            )

            # Especificar Certificado:
            input_cert = self.navegador.find_element_by_name(
                SitioLoginFiel.input_certificado
            )
            input_cert.send_keys(_path_cert)

            # Especificar Llave:
            input_key = self.navegador.find_element_by_name(
                SitioLoginFiel.input_llave
            )
            input_key.send_keys(_path_key)

            # Especificar Contraseña:
            input_pass = self.navegador.find_element_by_name(
                SitioLoginFiel.input_contrasena
            )
            input_pass.send_keys(_password)

            # Especificar RFC:
            input_rfc = self.navegador.find_element_by_name(
                SitioLoginFiel.input_rfc
            )
            script = "document.getElementsByName('{}')[0]." \
                "removeAttribute('readonly');".format(
                    SitioLoginFiel.input_rfc
                )
            self.navegador.execute_script(script)
            input_rfc.send_keys(_rfc)

            # Click en Submit:
            boton_submit = self.navegador.find_element_by_name(
                SitioLoginFiel.boton_submit
            )
            boton_submit.click()

            # Esperamos a que carge la pagina
            wait = WebDriverWait(self.navegador, 20)
            wait.until(EC.title_contains('NetIQ Access'))

            print "Login al sitio SAT Fiel......OK"

        except Exception, error:

            self.close()

            raise ErrorEjecucion(
                "WebSat.login_Fiel()",
                type(error).__name__,
                str(error)
            )

    def login(self, _rfc, _ciec):
        try:
            # Ir a sitio login:
            self.navegador.get(SitioLogin.url)

            # Especificar Usuario
            input_user = self.navegador.find_element_by_name(
                SitioLogin.user
            )
            input_user.send_keys(_rfc)

            # Especificar Contraseña
            input_password = self.navegador.find_element_by_name(
                SitioLogin.password
            )
            input_password.send_keys(_ciec)

            # Click en boton submit y esperamos a que carge
            boton_submit = self.navegador.find_element_by_name(
                SitioLogin.submit
            )
            boton_submit.click()

            # Enviamos datos de conexion y esperamos a que carge la pagina
            wait = WebDriverWait(self.navegador, 10)
            wait.until(EC.title_contains('NetIQ Access'))

            print "Login al sitio SAT......OK"

        except Exception, error:

            self.close()

            raise ErrorEjecucion(
                "WebSat.login()",
                type(error).__name__,
                str(error)
            )

    def open(self):
        try:
            profile = webdriver.FirefoxProfile()

            profile.set_preference('browser.download.folderList', 2)
            profile.set_preference(
                'browser.download.manager.showWhenStarting', False)
            profile.set_preference('browser.helperApps.alwaysAsk.force', False)

            # Evita que se muestre cuadro de dialogo
            profile.set_preference(
                'browser.helperApps.neverAsk.saveToDisk',
                'text/xml, application/octet-stream, application/xml'
            )

            # Habilita Java
            # profile.accept_untrusted_certs(True)
            profile.set_preference("security.enable_java", True)
            profile.set_preference("plugin.state.java", 2)

            # Se establece direcctorio de descarga
            profile.set_preference(
                'browser.download.dir',
                self.download_abspath
            )

            profile.set_preference('toolkit.telemetry.prompted', 2)
            profile.set_preference('toolkit.telemetry.rejected', True)
            profile.set_preference('toolkit.telemetry.enabled', False)
            profile.set_preference(
                'datareporting.healthreport.service.enabled',
                False
            )
            profile.set_preference(
                'datareporting.healthreport.uploadEnabled',
                False
            )
            profile.set_preference(
                'datareporting.healthreport.service.firstRun',
                False
            )
            profile.set_preference(
                'datareporting.healthreport.logging.consoleEnabled',
                False
            )
            profile.set_preference(
                'datareporting.policy.dataSubmissionEnabled',
                False
            )
            profile.set_preference(
                'datareporting.policy.dataSubmissionPolicyResponseType',
                'accepted-info-bar-dismissed'
            )

            # Oculta la flecha de animacion al descargar
            profile.set_preference(
                'browser.download.animateNotifications', False)

            # Se abre el navegador
            self.navegador = webdriver.Firefox(profile)

            self.navegador.set_window_position(0, 0)
            self.navegador.set_window_size(1200, 900)

            print "Abrir navegador.........OK"

        except Exception, error:

            self.close()

            raise ErrorEjecucion(
                "WebSat.open()",
                type(error).__name__,
                str(error)
            )

    def search_InvoicesIssued(self, _filtro):
        try:
            # Redirigiendo a pagina de consulta
            self.navegador.get(SitioFacturasEmitidas.url)
            wait = WebDriverWait(self.navegador, 15)
            wait.until(EC.title_contains('Buscar CFDI'))

            # Configurando filtros
            if _filtro.uuid:

                # Se selecciona la busqueda por FOLIO FISCAL
                input_uuid = self.navegador.find_element_by_id(
                    SitioFacturasEmitidas.uuid
                )
                input_uuid.click()

                # Filtro: FOLIO FISCAL
                input_uuid.send_keys(_filtro.uuid)

            else:

                # Se selecciona la busqueda por FECHA DE EMISION
                opcion = self.navegador.find_element_by_id(
                    SitioFacturasEmitidas.date
                )
                opcion.click()
                wait.until(EC.staleness_of(opcion))

                fechas = Chronos.get_FirstAndLastDay(
                    int(_filtro.year),
                    int(_filtro.month),
                    int(_filtro.day)
                )

                # Filtro: Fecha Inicio
                input_fechaInicio = self.navegador.find_element_by_id(
                    SitioFacturasEmitidas.date_from
                )
                arg = "document.getElementsByName('{}')[0].removeAttribute('disabled');".format(
                    SitioFacturasEmitidas.date_from_name
                )
                self.navegador.execute_script(arg)
                input_fechaInicio.send_keys(fechas[0])

                # Filtro: Fecha Fin
                input_fechaFin = self.navegador.find_element_by_id(
                    SitioFacturasEmitidas.date_to
                )
                arg = "document.getElementsByName('{}')[0].removeAttribute('disabled');".format(
                    SitioFacturasEmitidas.date_to_name
                )
                self.navegador.execute_script(arg)
                input_fechaFin.send_keys(fechas[1])

                # Filtro: Hora Inicial:
                input_horaInicial = "document.getElementById('{}').value='{}';".format(
                    SitioFacturasEmitidas.start_hour,
                    int(_filtro.start_hour)
                )
                self.navegador.execute_script(input_horaInicial)
                input_minutoInicial = "document.getElementById('{}').value='{}';".format(
                    SitioFacturasEmitidas.start_minute,
                    int(_filtro.start_minute)
                )
                self.navegador.execute_script(input_minutoInicial)
                input_segundoInicial = "document.getElementById('{}').value='{}';".format(
                    SitioFacturasEmitidas.start_second,
                    int(_filtro.start_second)
                )
                self.navegador.execute_script(input_segundoInicial)

                # Filtro: Hora Final:
                input_horaFinal = "document.getElementById('{}').value={};".format(
                    SitioFacturasEmitidas.end_hour,
                    _filtro.end_hour)
                self.navegador.execute_script(input_horaFinal)
                input_minutoFinal = "document.getElementById('{}').value={};".format(
                    SitioFacturasEmitidas.end_minute,
                    _filtro.end_minute)
                self.navegador.execute_script(input_minutoFinal)
                input_minutoFinal = "document.getElementById('{}').value={};".format(
                    SitioFacturasEmitidas.end_second,
                    _filtro.end_second)
                self.navegador.execute_script(input_minutoFinal)

            tabla_resultados = self.navegador.find_element_by_id(
                SitioFacturasEmitidas.resultados
            )

            self.navegador.find_element_by_id(
                SitioFacturasEmitidas.submit
            ).click()

            wait.until(EC.staleness_of(tabla_resultados))

            resultados = wait.until(
                Visualizador(
                    (By.ID, SitioFacturasEmitidas.resultados),
                    (By.ID, SitioFacturasEmitidas.noresultados)
                )
            )

            if resultados.get_attribute('id') == SitioFacturasEmitidas.resultados:
                wait.until(EC.element_to_be_clickable(
                    (By.NAME, SitioFacturasEmitidas.download)
                )
                )

                links = self.navegador.find_elements_by_name(
                    SitioFacturasEmitidas.download
                )
                return links

            else:

                # No se encontraron facturas
                return []

        except Exception, error:

            self.close()

            raise ErrorEjecucion(
                'WebSAT.search_InvoicesIssued()',
                type(error).__name__,
                str(error)
            )

    def search_InvoicesReceived(self, _filtro):

        try:
            # Redirigiendo a pagina de consulta
            self.navegador.get(SitioFacturasRecibidas.url)
            wait = WebDriverWait(self.navegador, 15)
            wait.until(EC.title_contains('Buscar CFDI'))

            # Configurando filtros
            if _filtro.uuid:

                # Se selecciona la busqueda por FOLIO FISCAL
                input_uuid = self.navegador.find_element_by_id(
                    SitioFacturasRecibidas.uuid
                )
                input_uuid.click()

                # Filtro: FOLIO FISCAL
                input_uuid.send_keys(_filtro.uuid)

            else:

                # Se selecciona la busqueda por FECHA DE EMISION
                opcion = self.navegador.find_element_by_id(
                    SitioFacturasRecibidas.date
                )
                opcion.click()
                wait.until(EC.staleness_of(opcion))

                # Filtro: Fecha de Emision
                input_fechaEmision = wait.until(
                    EC.element_to_be_clickable(
                        (By.ID, SitioFacturasRecibidas.emisor)
                    )
                )
                input_fechaEmision.send_keys(_filtro.emisor_rfc)

                # Filtro: Anio
                input_anio = "document.getElementById('{}').value={};".format(
                    SitioFacturasRecibidas.year, _filtro.year
                )
                self.navegador.execute_script(input_anio)

                # Filtro: Mes
                input_mes = "document.getElementById('{}').value={};".format(
                    SitioFacturasRecibidas.month, _filtro.month
                )
                self.navegador.execute_script(input_mes)

                # Filtro: Dia
                input_dia = "document.getElementById('{}').value='{}';".format(
                    SitioFacturasRecibidas.day, _filtro.day
                )
                self.navegador.execute_script(input_dia)

                # Filtro: Hora Inicial
                input_horaInicial = "document.getElementById('{}').value='{}';".format(
                    SitioFacturasRecibidas.start_hour,
                    int(_filtro.start_hour)
                )
                self.navegador.execute_script(input_horaInicial)
                input_minutoInicial = "document.getElementById('{}').value='{}';".format(
                    SitioFacturasRecibidas.start_minute,
                    int(_filtro.start_minute)
                )
                self.navegador.execute_script(input_minutoInicial)
                input_segundoInicial = "document.getElementById('{}').value='{}';".format(
                    SitioFacturasRecibidas.start_second,
                    int(_filtro.start_second)
                )
                self.navegador.execute_script(input_segundoInicial)

                # Filtro: Hora Final
                input_horaFinal = "document.getElementById('{}').value='{}';".format(
                    SitioFacturasRecibidas.end_hour,
                    int(_filtro.end_hour)
                )
                self.navegador.execute_script(input_horaFinal)
                input_minutoFinal = "document.getElementById('{}').value='{}';".format(
                    SitioFacturasRecibidas.end_minute,
                    int(_filtro.end_minute)
                )
                self.navegador.execute_script(input_minutoFinal)
                input_segundoFinal = "document.getElementById('{}').value='{}';".format(
                    SitioFacturasRecibidas.end_second,
                    int(_filtro.end_second)
                )
                self.navegador.execute_script(input_segundoFinal)

            tabla_resultados = self.navegador.find_element_by_id(
                SitioFacturasRecibidas.resultados
            )

            self.navegador.find_element_by_id(
                SitioFacturasRecibidas.submit
            ).click()

            wait.until(EC.staleness_of(tabla_resultados))

            resultados = wait.until(
                Visualizador(
                    (By.ID, SitioFacturasRecibidas.resultados),
                    (By.ID, SitioFacturasRecibidas.noresultados)
                )
            )

            if resultados.get_attribute('id') == SitioFacturasRecibidas.resultados:
                wait.until(EC.element_to_be_clickable(
                    (By.NAME, SitioFacturasRecibidas.download)
                )
                )

                links = self.navegador.find_elements_by_name(
                    SitioFacturasRecibidas.download
                )
                return links

            else:

                # No se encontraron facturas
                return []

        except Exception, error:

            self.close()

            raise ErrorEjecucion(
                'WebSAT.search_InvoicesReceived()',
                type(error).__name__,
                str(error)
            )


class WebServiceSAT(object):

    @classmethod
    def get_Estado(self, emisor_rfc, receptor_rfc, total, uuid):

        try:

            webservice = 'https://consultaqr.facturaelectronica.sat.gob.mx/' \
                'consultacfdiservice.svc'
            mensajeSoap = """<?xml version="1.0" encoding="UTF-8"?>
                                <soap:Envelope
                                    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
                                    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                                    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                                    <soap:Header/>
                                    <soap:Body>
                                    <Consulta xmlns="http://tempuri.org/">
                                        <expresionImpresa>
                                            ?re={0}&amp;rr={1}&amp;tt={2}&amp;id={3}
                                        </expresionImpresa>
                                    </Consulta>
                                    </soap:Body>
                                </soap:Envelope>"""

            datos = mensajeSoap.format(
                emisor_rfc, receptor_rfc, total, uuid).encode('utf-8')
            cabecera = {
                'SOAPAction': '"http://tempuri.org/'
                'IConsultaCFDIService/Consulta"',
                'Content-length': len(datos),
                'Content-type': 'text/xml; charset="UTF-8"'
            }

            sesion_ = Session()
            request_ = Request('POST', webservice,
                               data=datos, headers=cabecera)

            prepped = request_.prepare()

            response = sesion_.send(prepped, timeout=5)
            tree = ElementTree.fromstring(response.text)
            estado = tree[0][0][0][1].text

            return estado

        except Exception, error:

            raise ErrorEjecucion(
                'WebServiceSAT.get_Estado()',
                type(error).__name__,
                str(error)
            )
