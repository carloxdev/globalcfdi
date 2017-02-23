# -*- coding: utf-8 -*-

# Librerias Propias:
from sat import WebSat

# Herramientas:
from tools.datos import Filtro
from tools.datos import FileManager
from tools.datos import Ruta
from tools.datos import Validator
from tools.datos import ResumenRegistro
from tools.mistakes import ErrorValidacion
from tools.mistakes import ErrorEjecucion
from documentos import Comprobante
from documentos import Log

# Modelos del Sitio:
from sitio import ModeloResumen

TIPOS_FACTURA = ("RECIBIDAS", "EMITIDAS")


class Contador(object):

    def __init__(self, _empresa, _ruta_ejecucion):

        self.empresa = _empresa
        self.ruta_ejecucion = _ruta_ejecucion

    def valid_Credenciales(self):
        # elSat = WebSat("sin_carpeta")
        return None

    def get_ByDay(self, _tipo, _fecha):

        lista_resumen = []
        no_encontradas = 0
        no_descargadas = 0
        no_guardadas = 0
        no_validadas = 0
        total = 0

        ruta = Ruta(
            self.ruta_ejecucion,
            self.empresa.clave,
            _tipo,
            _fecha
        )

        log = Log(
            ruta.logpath,
            ruta.urllogpath,
            "GET",
            _tipo,
            self.empresa,
            _fecha
        )

        try:

            log.begin_capture()
            relativepath = ruta.relativepath
            download_abspath = ruta.abspath

            print "\nCREANDO DIRECTORIOS: "
            FileManager.create_Directory(self.ruta_ejecucion, relativepath)

            print "\nACCESANDO A SAT.COM: "
            elSat = WebSat(download_abspath)
            elSat.open()
            elSat.login_Fiel(
                self.empresa.certificado.path,
                self.empresa.llave.path,
                self.empresa.contrasena,
                self.empresa.rfc
            )

            elFiltro = Filtro(_fecha)

            if _tipo == TIPOS_FACTURA[0]:
                no_encontradas = self.search_ByDay(
                    elSat.search_InvoicesReceived,
                    elFiltro,
                    elSat
                )

            elif _tipo == TIPOS_FACTURA[1]:
                no_encontradas = self.search_ByDay(
                    elSat.search_InvoicesIssued,
                    elFiltro,
                    elSat
                )

            else:
                raise ErrorValidacion(
                    "Contador.get_ByDay()",
                    "No se establecio un tipo valido"
                )

            elSat.disconnect()

            if no_encontradas > 0:

                print "\nELIMINADO ARCHIVOS REPETIDOS: "
                FileManager.delete_DuplicateFiles(download_abspath, ".xml")

                print "\nRECORRIENDO ARCHIVOS DESCARGADOS: "
                lista_archivos = FileManager.get_Files(
                    download_abspath,
                    ".xml"
                )
                no_descargadas = len(lista_archivos)

                if no_descargadas > 0:

                    for archivo in lista_archivos:
                        comprobante = Comprobante(
                            archivo.basepath,
                            archivo.nombre
                        )
                        print "\nLeyendo archivo: {}".format(archivo.nombre)
                        comprobante.read(_tipo)

                        # Guardar en BD:
                        resultado_saveToDB = comprobante.save_toBD(
                            self.empresa.clave,
                            ruta.urlpath
                        )
                        no_guardadas += resultado_saveToDB

                        # Validar comprobante:
                        resultado_validate = comprobante.validate()
                        no_validadas += resultado_validate

                        # Crear objeto de resumen:
                        total = Validator.convertToFloat(
                            comprobante.total
                        ) * Validator.convertToFloat(
                            comprobante.tipoCambio
                        )

                        registroResumen = ResumenRegistro(
                            comprobante.resumen_tipo,
                            resultado_saveToDB,
                            resultado_validate,
                            total
                        )
                        lista_resumen.append(registroResumen)

            # Crear Resumen:
            print "\nRESUMEN: "
            self.set_Resumen(_fecha, _tipo, lista_resumen)

            # Informar Resultado:
            log.resumen_text = """
            Archivos encontrados:.... {}
            Archivos descargados:.... {}
            Archivos guardados:...... {}
            Archivos validados:...... {}
            Total:................... {}
            """.format(
                no_encontradas,
                no_descargadas,
                no_guardadas,
                no_validadas,
                str(total)
            )

            print log.resumen_text

            if no_encontradas == no_descargadas \
                    and no_encontradas == no_validadas:
                log.estado = "EXITO"
            else:
                log.estado = "DETALLES"

            # return log

        except Exception, error:
            log.estado = "ERROR"
            log.resument_text = str(error)

            raise ErrorEjecucion(
                "Contador.get_ByDay()",
                type(error).__name__,
                str(error)
            )

            # return log

        finally:
            if elSat:
                elSat.disconnect()

            log.end_capture()
            # return log

    def search_ByDay(self, _funcion, _elFiltro, _elSat):

        try:

            no_encontradas = 0

            print "\nBUSCANDO FACTURAS POR DIA: "
            lista_links_byDay = _funcion(_elFiltro)
            no_encontradas = len(lista_links_byDay)

            if no_encontradas >= 500:
                print "Se encontraron 500 facturas o mas"
                no_encontradas = self.search_ByHour(
                    _funcion, _elFiltro, _elSat)

            elif no_encontradas > 0:
                print "Descargando facturas del dia:"
                _elSat.download(lista_links_byDay)

            else:
                print "No se encontraron facturas"

            return no_encontradas

        except Exception, error:

            raise ErrorEjecucion(
                'Contador.search_ByHour()',
                type(error).__name__,
                str(error)
            )

    def search_ByHour(self, _funcion, _elFiltro, _elSat):

        try:
            no_encontradas = 0

            print "\nBUSCANDO FACTURAS POR HORA: "
            for hora in list(range(1, 25)):

                # Buscar facturas:
                _elFiltro.set_ForSeach_ByHour(hora)
                lista_links_byHour = _funcion(_elFiltro)

                if len(lista_links_byHour) >= 500:
                    print "Hora {}: Se encontraron 500 facturas o mas".format(
                        hora
                    )
                    no_encontradas += self.search_ByMinute(
                        _funcion,
                        _elFiltro,
                        _elSat
                    )

                elif len(lista_links_byHour) > 0:

                    no_encontradas += len(lista_links_byHour)
                    print 'Hora {0}: {1} Facturas'.format(
                        hora,
                        len(lista_links_byHour)
                    )
                    print 'Descargando:'
                    _elSat.download(lista_links_byHour)

                else:
                    print "Hora {}: No se encontraron facturas".format(hora)

            return no_encontradas

        except Exception, error:
            raise ErrorEjecucion(
                'Contador.search_ByHour()',
                type(error).__name__,
                str(error)
            )

    def search_ByMinute(self, _funcion, _elFiltro, _elSat):

        try:

            no_encontradas = 0

            print "\n BUSCANDO FACTURAS POR MINUTO: "
            for minuto in list(range(1, 61)):

                # Buscar facturas:
                _elFiltro.set_ForSeach_ByMinute(minuto)
                lista_links_byMinute = _funcion(_elFiltro)

                if len(lista_links_byMinute) > 0:
                    no_encontradas += len(lista_links_byMinute)
                    print 'Minuto {0}: {1} Facturas'.format(
                        minuto,
                        len(lista_links_byMinute)
                    )
                    print 'Descargando:'
                    _elSat.download(lista_links_byMinute)

                else:
                    print "Hora {}: No se encontraron facturas".format(minuto)

            return no_encontradas

        except Exception, error:
            raise ErrorEjecucion(
                'Contador.search_ByMinute()',
                type(error).__name__,
                str(error)
            )

    def save_ByDay(self, _tipo, _fecha):

        try:
            ruta = Ruta(
                self.ruta_ejecucion,
                self.empresa.clave,
                _tipo,
                _fecha
            )

            lista_archivos = FileManager.get_Files(
                ruta.abspath,
                ".xml"
            )

            if len(lista_archivos) > 0:

                no_guardadas = 0

                for archivo in lista_archivos:
                    comprobante = Comprobante(
                        archivo.basepath,
                        archivo.nombre
                    )
                    print "\nLeyendo archivo: {}".format(archivo.nombre)
                    comprobante.read()
                    no_guardadas += comprobante.save_toBD(
                        self.empresa_clave,
                        ruta.urlpath
                    )

        except Exception, error:
            print str(error)
            return None, None

    def validate_ByDay(self, _tipo, _fecha):

        try:
            ruta = Ruta(
                self.ruta_ejecucion,
                self.empresa.clave,
                _tipo,
                _fecha
            )

            lista_archivos = FileManager.get_Files(
                ruta.abspath,
                ".xml"
            )

            if len(lista_archivos) > 0:

                for archivo in lista_archivos:
                    comprobante = Comprobante(
                        archivo.basepath,
                        archivo.nombre
                    )
                    print "\nLeyendo archivo: {}".format(archivo.nombre)
                    comprobante.read(_tipo)
                    comprobante.validate()

        except Exception, error:
            print str(error)

    def set_Resumen(self, _fecha, _tipo, _lista_resumen):

        provee_total_guardados = 0
        provee_total_validados = 0
        provee_total_monto = 0.0

        emplea_total_guardados = 0
        emplea_total_validados = 0
        emplea_total_monto = 0.0

        client_total_guardados = 0
        client_total_validados = 0
        client_total_monto = 0.0

        try:

            if len(_lista_resumen):

                for resumen in _lista_resumen:

                    if resumen.tipo == "PROVEEDORES":
                        provee_total_guardados += resumen.no_guardadas
                        provee_total_validados += resumen.no_validadas
                        provee_total_monto += resumen.total

                    elif resumen.tipo == "EMPLEADOS":
                        emplea_total_guardados += resumen.no_guardadas
                        emplea_total_validados += resumen.no_validadas
                        emplea_total_monto += resumen.total

                    elif resumen.tipo == "CLIENTES":
                        client_total_guardados += resumen.no_guardadas
                        client_total_validados += resumen.no_validadas
                        client_total_monto += resumen.total

                    else:
                        raise ErrorValidacion(
                            "Contador.set_Resumen()",
                            """No se establecio un tipo de resumen
                            valido en un registro"""
                        )

            if _tipo == TIPOS_FACTURA[0]:
                self.save_Resumen(
                    _fecha,
                    "PROVEEDORES",
                    provee_total_guardados,
                    provee_total_validados,
                    provee_total_monto
                )

            elif _tipo == TIPOS_FACTURA[1]:

                self.save_Resumen(
                    _fecha,
                    "CLIENTES",
                    client_total_guardados,
                    client_total_validados,
                    client_total_monto
                )

                self.save_Resumen(
                    _fecha,
                    "EMPLEADOS",
                    emplea_total_guardados,
                    emplea_total_validados,
                    emplea_total_monto
                )

            else:
                raise ErrorValidacion(
                    "Contador.set_Resumen()",
                    "No se establecio un tipo valido"
                )

        except Exception, error:
            print str(error)

    def save_Resumen(self, _fecha, _tipo, _guardadas, _validadas, _total):

        try:

            ModeloResumen.add(
                self.empresa,
                _fecha,
                _tipo,
                _guardadas,
                _validadas,
                "{0:.4f}".format(_total)
            )

            print "Resumen de {} creado y guardado".format(_tipo)

        except Exception, error:

            if error.tipo == 'IntegrityError':

                try:
                    resumen = ModeloResumen.get(_fecha, _tipo)

                    es_modificable = False

                    if resumen.cantidad_guardadas < _guardadas:
                        resumen.cantidad_guardadas = _guardadas
                        es_modificable = True

                    if resumen.cantidad_validadas < _validadas:
                        resumen.cantidad_validadas = _validadas
                        es_modificable = True

                    if resumen.total > _total:
                        resumen.total = "{0:.4f}".format(_total)
                        es_modificable = True

                    if es_modificable:
                        resumen.save()
                        print "Se actualizo el Resumen"
                    else:
                        print "No hubo cambios desde " \
                            "la ultima descarga/validacion"

                except Exception, error:
                    print str(error)

            else:
                print str(error)
