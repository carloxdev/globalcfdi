# -*- coding: utf-8 -*-

# Librerias Python:
from datetime import date
from datetime import timedelta

# Librerias Propias:
from sat import WebSat

# Herramientas:
from tools.datos import Filtro
from tools.datos import FileManager
from tools.datos import Ruta
from tools.datos import Validator
from tools.mistakes import ErrorValidacion
from tools.mistakes import ErrorEjecucion
from documentos import Comprobante

# Modelos del Sitio:
from sitio import ModeloResumen


class Contador(object):

    def __init__(self, _empresa, _ruta_ejecucion):

        self.empresa = _empresa
        self.ruta_ejecucion = _ruta_ejecucion

    def get_Invoices_LastThreeDays(self, _tipo):

        ahora = date.today()

        contador = 1
        while contador <= 3:
            fecha = ahora - timedelta(days=contador)
            self.get_Invoices_ByDay(_tipo, fecha)
            contador += 1

    def get_Invoices_ByDay(self, _tipo, _fecha):

        try:
            ruta = Ruta(
                self.ruta_ejecucion,
                self.empresa.clave,
                _tipo,
                _fecha
            )

            relativepath = ruta.relativepath
            download_abspath = ruta.abspath
            print "\nCREANDO DIRECTORIOS: "
            FileManager.create_Directory(self.ruta_ejecucion, relativepath)

            print "\nACCESANDO A SAT.COM: "
            elSat = WebSat(download_abspath)
            elSat.open()
            elSat.login(self.empresa.rfc, self.empresa.ciec)

            elFiltro = Filtro(_fecha)

            if _tipo == "RECIBIDAS":
                no_encontradas = self.search_ByDay(
                    elSat.search_InvoicesReceived,
                    elFiltro,
                    elSat
                )

            elif _tipo == "EMITIDAS":
                no_encontradas = self.search_ByDay(
                    elSat.search_InvoicesIssued,
                    elFiltro,
                    elSat
                )

            else:
                raise ErrorValidacion(
                    "Contador.get_Invoices_ByDay()",
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

                    no_guardadas = 0
                    no_validadas = 0
                    total = 0

                    for archivo in lista_archivos:
                        comprobante = Comprobante(
                            archivo.basepath,
                            archivo.nombre
                        )
                        print "\nLeyendo archivo: {}".format(archivo.nombre)
                        comprobante.read()

                        # if comprobante.registroPatronal:

                        total = Validator.convertToFloat(comprobante.total)

                        no_guardadas += comprobante.save(
                            _tipo, self.empresa.clave, ruta.urlpath)

                        comprobante.validate(_tipo)
                        no_validadas += 1

                print "\nRESUMEN: "
                print "Archivos {} encontrados:.... {}".format(".xml", no_encontradas)
                print "Archivos {} descargados:.... {}".format(".xml", no_descargadas)
                print "Archivos {} guardados:...... {}".format(".xml", no_guardadas)
                print "Archivos {} validados:...... {}".format(".xml", no_validadas)
                print "Total:....................... {}".format(str(total))

            else:
                no_descargadas = 0
                no_guardadas = 0
                no_validadas = 0
                total = 0

            self.set_Resumen(
                self.empresa,
                _fecha,
                _tipo,
                no_encontradas,
                no_descargadas,
                no_guardadas,
                no_validadas,
                total,
            )

        except Exception, error:
            print str(error)

    def search_ByDay(self, _funcion, _elFiltro, _elSat):

        try:
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
                    print "Hora {}: Se encontraron 500 facturas o mas".format(hora)
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

    def save_Invoices_byDay(self, _tipo, _fecha):

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
                    no_guardadas += comprobante.save(
                        _tipo,
                        self.empresa_clave,
                        ruta.urlpath
                    )

        except Exception, error:
            print str(error)
            return None, None

    def validate_Invoices_byDay(self, _tipo, _fecha):

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
                    comprobante.read()
                    comprobante.validate(_tipo)

        except Exception, error:
            print str(error)

    def set_Resumen(self, _empresa, _fecha, _tipo, _encontradas, _descargadas, _guardadas, _validadas, _total):

        try:

            ModeloResumen.add(
                _empresa,
                _fecha,
                _tipo,
                _encontradas,
                _descargadas,
                _guardadas,
                _validadas,
                _total
            )

            print "Resumen creado y guardado"

        except Exception, error:

            if error.tipo == 'IntegrityError':
                print error.mensaje

                try:
                    resumen = ModeloResumen.get(_fecha, _tipo)

                    if resumen.cantidad_encontradas < _encontradas:
                        resumen.cantidad_encontradas = _encontradas

                    if resumen.cantidad_descargadas < _descargadas:
                        resumen.cantidad_descargadas = _descargadas

                    if resumen.cantidad_guardadas < _guardadas:
                        resumen.cantidad_guardadas = _guardadas

                    if resumen.cantidad_validadas < _validadas:
                        resumen.cantidad_validadas = _validadas

                    if resumen.total > _total:
                        resumen.total = _total

                    resumen.save()

                    print "Se actualizo el Resumen"

                except Exception, error:
                    print str(error)
