# -*- coding: utf-8 -*-

# Librerias Python:
import os

# Librerias de Terceros:
from lxml import etree

# Herramientas:
from tools.mistakes import ErrorEjecucion
from tools.mistakes import ErrorValidacion
from tools.datos import Archivo
from tools.datos import Validator

# Librerias Propias:
from sat import WebServiceSAT

# Librerias del Sitio:
from sitio import ModeloFacturaCliente
from sitio import ModeloFacturaProveedor
from sitio import ModeloComprobanteEmpleado


class Comprobante(Archivo):

    def __init__(self, _basepath, _name):

        Archivo.__init__(self, _basepath, _name)

        # Comprobante
        self.serie = ''
        self.folio = ''
        self.fecha = ''
        self.formaDePago = ''
        self.noCertificado = ''
        self.subTotal = '0'
        self.tipoCambio = '1'
        self.moneda = ''
        self.sello = ''
        self.total = '0'
        self.tipoDeComprobante = ''
        self.metodoDePago = ''
        self.lugarExpedicion = ''
        self.numCtaPago = ''
        self.condicionesDePago = ''

        # Emisor
        self.emisor_rfc = ''
        self.emisor_nombre = ''

        # Emisor Direccion
        self.emisor_calle = ''
        self.emisor_noExterior = ''
        self.emisor_noInterior = ''
        self.emisor_colonia = ''
        self.emisor_localidad = ''
        self.emisor_municipio = ''
        self.emisor_estado = ''
        self.emisor_pais = ''
        self.emisor_codigoPostal = ''

        # Emisor Expedido en
        self.emisor_expedidoEn_calle = ''
        self.emisor_expedidoEn_noExterior = ''
        self.emisor_expedidoEn_noInterior = ''
        self.emisor_expedidoEn_colonia = ''
        self.emisor_expedidoEn_municipio = ''
        self.emisor_expedidoEn_estado = ''
        self.emisor_expedidoEn_pais = ''

        # Emisor Regimen
        self.emisor_regimen = ''

        # Receptor
        self.receptor_rfc = ''
        self.receptor_nombre = ''

        # Receptor Direccion
        self.receptor_calle = ''
        self.receptor_noExterior = ''
        self.receptor_noInterior = ''
        self.receptor_colonia = ''
        self.receptor_localidad = ''
        self.receptor_municipio = ''
        self.receptor_estado = ''
        self.receptor_pais = ''
        self.receptor_codigoPostal = ''

        # Conceptos
        self.conceptos = []

        # Impuestos
        self.totalImpuestosTrasladados = '0'
        self.totalImpuestosRetenidos = '0'

        # Impuestos Trasladados
        self.impuestos_trasladados = []

        # Impuestos Retenidos
        self.impuestos_retenidos = []

        # Complementos
        self.uuid = ''
        self.fechaTimbrado = ''
        self.noCertificadoSAT = ''
        self.selloSAT = ''

        # Nomina Datos
        self.registroPatronal = ''
        self.numEmpleado = ''
        self.curp = ''
        self.tipoRegimen = ''
        self.numSeguridadSocial = ''
        self.fechaPago = ''
        self.fechaInicialPago = ''
        self.fechaFinalPago = ''
        self.numDiasPagados = ''
        self.clabe = ''
        self.banco = ''
        self.fechaInicioRelLaboral = ''
        self.antiguedad = ''
        self.puesto = ''
        self.tipoJornada = ''
        self.periodicidadPago = ''
        self.riesgoPuesto = ''
        self.salarioDiarioIntegrado = '0'

        # Nomina Percepciones
        self.percepciones_totalGravado = '0'
        self.percepciones_totalExento = '0'
        self.percepciones = []

        # Nomina Deducciones
        self.deducciones_totalGravado = '0'
        self.deducciones_totalExento = '0'
        self.deducciones = []

        # Horas Extras
        self.horasExtras = []

        # Url, Estado:
        self.empresa_clave = ''
        self.url = ''
        self.resumen_tipo = 'UNKNOWN'

        self.raiz = None
        self.name_spaces = None

        self.init()

    def init(self):

        try:
            recovering_parser = etree.XMLParser(recover=True)

            if os.path.isfile(self.abspath):

                document = etree.parse(self.abspath, parser=recovering_parser)
                self.raiz = document.getroot()

                self.name_spaces = {
                    'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                    'cfdi': 'http://www.sat.gob.mx/cfd/3',
                    'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital',
                    'nomina': 'http://www.sat.gob.mx/nomina'
                }

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.init()',
                type(error).__name__,
                str(error)
            )

    def read_Comprobante_Node(self):

        try:

            self.serie = Validator.convertToChar(
                self.raiz.get('serie')
            )
            self.folio = Validator.convertToChar(
                self.raiz.get('folio')
            )
            self.fecha = Validator.convertToDate(
                self.raiz.get('fecha')
            )
            self.formaDePago = Validator.convertToChar(
                self.raiz.get('formaDePago')
            )
            self.noCertificado = Validator.convertToChar(
                self.raiz.get('noCertificado')
            )
            self.subTotal = Validator.convertToChar(
                self.raiz.get('subTotal')
            )
            self.tipoCambio = Validator.convertToChar(
                self.raiz.get('TipoCambio'), 1
            )
            self.moneda = Validator.convertToChar(
                self.raiz.get('Moneda')
            )
            self.sello = Validator.convertToChar(
                self.raiz.get('sello')
            )
            self.total = Validator.convertToChar(
                self.raiz.get('total')
            )
            self.tipoDeComprobante = Validator.convertToChar(
                self.raiz.get('tipoDeComprobante')
            )
            self.metodoDePago = Validator.convertToChar(
                self.raiz.get('metodoDePago')
            )
            self.lugarExpedicion = Validator.convertToChar(
                self.raiz.get('LugarExpedicion')
            )
            self.numCtaPago = Validator.convertToChar(
                self.raiz.get('NumCtaPago')
            )
            self.condicionesDePago = Validator.convertToChar(
                self.raiz.get("condicionesDePago")
            )

            return True

        except Exception, error:

            raise ErrorEjecucion(
                'Comprobante.read_ComprobanteNode()',
                type(error).__name__,
                str(error)
            )

    def read_Emisor_Node(self):

        try:
            # Obtener nodo
            nodo = self.raiz.find(
                'cfdi:Emisor',
                self.name_spaces
            )

            # Obtener atributos
            self.emisor_rfc = Validator.convertToChar(
                nodo.get('rfc')
            )
            self.emisor_nombre = Validator.convertToChar(
                nodo.get('nombre')
            )

            return True

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_EmisorNode()',
                type(error).__name__,
                str(error)
            )

    def read_Emisor_DomicilioFiscal_Node(self):

        try:

            # obtener nodo
            nodo = self.raiz.find('cfdi:Emisor', self.name_spaces).find(
                'cfdi:DomicilioFiscal',
                self.name_spaces
            )

            # obtener datos
            self.emisor_calle = Validator.convertToChar(
                nodo.get("calle")
            )
            self.emisor_noExterior = Validator.convertToChar(
                nodo.get("noExterior")
            )
            self.emisor_noInterior = Validator.convertToChar(
                nodo.get("noInterior")
            )
            self.emisor_colonia = Validator.convertToChar(
                nodo.get("colonia")
            )
            self.emisor_localidad = Validator.convertToChar(
                nodo.get("localidad")
            )
            self.emisor_municipio = Validator.convertToChar(
                nodo.get("municipio")
            )
            self.emisor_estado = Validator.convertToChar(
                nodo.get("estado")
            )
            self.emisor_pais = Validator.convertToChar(
                nodo.get("pais")
            )
            self.emisor_codigoPostal = Validator.convertToInt(
                nodo.get("codigoPostal")
            )

            return True

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_Emisor_DomicilioFiscal_Node()',
                type(error).__name__,
                str(error)
            )

    def read_Emisor_ExpedidoEn_Node(self):

        try:

            # obtener nodo
            nodo = self.raiz.find('cfdi:Emisor', self.name_spaces).find(
                'cfdi:ExpedidoEn',
                self.name_spaces
            )

            # obtener datos
            self.emisor_expedidoEn_calle = Validator.convertToChar(
                nodo.get("calle")
            )
            self.emisor_expedidoEn_noExterior = Validator.convertToChar(
                nodo.get("noExterior")
            )
            self.emisor_expedidoEn_noInterior = Validator.convertToChar(
                nodo.get("noInterior")
            )
            self.emisor_expedidoEn_colonia = Validator.convertToChar(
                nodo.get("colonia")
            )
            self.emisor_expedidoEn_municipio = Validator.convertToChar(
                nodo.get("municipio")
            )
            self.emisor_expedidoEn_estado = Validator.convertToChar(
                nodo.get("estado")
            )
            self.emisor_expedidoEn_pais = Validator.convertToChar(
                nodo.get("pais")
            )

            return True

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_Emisor_ExpedidoEn_Node()',
                type(error).__name__,
                str(error)
            )

    def read_Emisor_RegimenFiscal_Node(self):

        try:
            nodo = self.raiz.find('cfdi:Emisor', self.name_spaces).find(
                'cfdi:RegimenFiscal',
                self.name_spaces
            )

            self.emisor_regimen = Validator.convertToChar(
                nodo.get("Regimen")
            )

            return True

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_Emisor_RegimenFiscal_Node()',
                type(error).__name__,
                str(error)
            )

    def read_Receptor_Node(self):

        try:

            nodo = self.raiz.find(
                'cfdi:Receptor',
                self.name_spaces
            )

            self.receptor_rfc = Validator.convertToChar(
                nodo.get('rfc')
            )
            self.receptor_nombre = Validator.convertToChar(
                nodo.get('nombre')
            )

            return True

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_Receptor_Node()',
                type(error).__name__,
                str(error)
            )

    def read_Receptor_Domicilio_Node(self):

        try:

            nodo = self.raiz.find('cfdi:Receptor', self.name_spaces).find(
                'cfdi:Domicilio',
                self.name_spaces
            )

            self.receptor_calle = Validator.convertToChar(
                nodo.get("calle")
            )
            self.receptor_noExterior = Validator.convertToChar(
                nodo.get("noExterior")
            )
            self.receptor_noInterior = Validator.convertToChar(
                nodo.get("noInterior")
            )
            self.receptor_colonia = Validator.convertToChar(
                nodo.get("colonia")
            )
            self.receptor_localidad = Validator.convertToChar(
                nodo.get("localidad")
            )
            self.receptor_municipio = Validator.convertToChar(
                nodo.get("municipio")
            )
            self.receptor_estado = Validator.convertToChar(
                nodo.get("estado")
            )
            self.receptor_pais = Validator.convertToChar(
                nodo.get("pais")
            )
            self.receptor_codigoPostal = Validator.convertToInt(
                nodo.get("codigoPostal")
            )

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_Receptor_Domicilio_Node()',
                type(error).__name__,
                str(error)
            )

    def read_Impuestos_Node(self):

        try:

            nodo = self.raiz.find('cfdi:Impuestos', self.name_spaces)

            self.totalImpuestosTrasladados = Validator.convertToChar(
                nodo.get('totalImpuestosTrasladados')
            )
            self.totalImpuestosRetenidos = Validator.convertToChar(
                nodo.get('totalImpuestosRetenidos')
            )

            return True

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_Impuestos_Node()',
                type(error).__name__,
                str(error)
            )

    def read_Impuestos_Traslados(self):

        try:
            nodo = self.raiz.find('cfdi:Impuestos', self.name_spaces)
            nodos = nodo.find('cfdi:Traslados', self.name_spaces)

            for nodo in nodos:

                impuesto = {
                    'impuesto': Validator.convertToChar(nodo.get('impuesto')),
                    'tasa': Validator.convertToChar(nodo.get('tasa')),
                    'importe': Validator.convertToChar(nodo.get('importe'))
                }

                self.impuestos_trasladados.append(impuesto)

            return True

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_Impuestos_Traslados()',
                type(error).__name__,
                str(error)
            )

    def read_Impuestos_Retenciones(self):

        try:
            nodo = self.raiz.find('cfdi:Impuestos', self.name_spaces)
            nodos = nodo.find('cfdi:Retenciones', self.name_spaces)

            for n in nodos:

                impuesto = {
                    'impuesto': Validator.convertToChar(n.get('impuesto')),
                    'importe': Validator.convertToChar(n.get('importe'))
                }

                self.impuestos_retenidos.append(impuesto)

            return True

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_Impuestos_Retenciones()',
                type(error).__name__,
                str(error)
            )

    def read_Conceptos_Node(self):

        try:
            nodos = self.raiz.find('cfdi:Conceptos', self.name_spaces)
            for nodo in nodos:
                item = {
                    'cantidad': Validator.convertToChar(nodo.get('cantidad')),
                    'unidad': Validator.convertToChar(nodo.get('unidad')),
                    'noIdentificacion': Validator.convertToChar(nodo.get('noIdentificacion')),
                    'descripcion': Validator.convertToChar(nodo.get('descripcion')),
                    'valorUnitario': Validator.convertToChar(nodo.get('valorUnitario')),
                    'importe': Validator.convertToChar(nodo.get('importe'))
                }

                self.conceptos.append(item)

            return True

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_Conceptos_Node()',
                type(error).__name__,
                str(error)
            )

    def read_Complemento_Node(self):

        try:

            nodo = self.raiz.find('cfdi:Complemento', self.name_spaces).find(
                'tfd:TimbreFiscalDigital',
                self.name_spaces
            )

            self.uuid = Validator.convertToChar(
                nodo.get('UUID')
            )
            self.fechaTimbrado = Validator.convertToDate(
                nodo.get('FechaTimbrado')
            )
            self.noCertificadoSAT = Validator.convertToChar(
                nodo.get('noCertificadoSAT')
            )
            self.selloSAT = Validator.convertToChar(
                nodo.get('selloSAT')
            )

            return True

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_Complemento_Node()',
                type(error).__name__,
                str(error)
            )

    def read_Nomina_Node(self):

        try:

            nodo = self.raiz.find('cfdi:Complemento', self.name_spaces).find(
                'nomina:Nomina',
                self.name_spaces
            )

            self.registroPatronal = Validator.convertToChar(
                nodo.get('RegistroPatronal')
            )

            self.numEmpleado = Validator.convertToChar(
                nodo.get('NumEmpleado')
            )
            self.curp = Validator.convertToChar(
                nodo.get('CURP')
            )
            self.tipoRegimen = Validator.convertToChar(
                nodo.get('TipoRegimen')
            )
            self.numSeguridadSocial = Validator.convertToChar(
                nodo.get('NumSeguridadSocial')
            )
            self.fechaPago = Validator.convertToDate(
                nodo.get('FechaPago'), hora=False
            )
            self.fechaInicialPago = Validator.convertToDate(
                nodo.get('FechaInicialPago'), hora=False
            )
            self.fechaFinalPago = Validator.convertToDate(
                nodo.get('FechaFinalPago'), hora=False
            )
            self.numDiasPagados = Validator.convertToInt(
                nodo.get('NumDiasPagados')
            )
            self.clabe = Validator.convertToChar(
                nodo.get('CLABE')
            )
            self.banco = Validator.convertToChar(
                nodo.get('Banco')
            )
            self.fechaInicioRelLaboral = Validator.convertToDate(
                nodo.get('FechaInicioRelLaboral'), hora=False
            )
            self.antiguedad = Validator.convertToInt(
                nodo.get('Antiguedad')
            )
            self.puesto = Validator.convertToChar(
                nodo.get('Puesto')
            )
            self.tipoJornada = Validator.convertToChar(
                nodo.get('TipoJornada')
            )
            self.periodicidadPago = Validator.convertToChar(
                nodo.get('PeriodicidadPago')
            )
            self.riesgoPuesto = Validator.convertToChar(
                nodo.get('RiesgoPuesto')
            )
            self.salarioDiarioIntegrado = Validator.convertToFloat(
                nodo.get('SalarioDiarioIntegrado')
            )

            return True

        except Exception, error:

            raise ErrorEjecucion(
                'Comprobante.read_Nomina_Node()',
                type(error).__name__,
                str(error)
            )

    def read_Nomina_Percepciones_Node(self):

        try:
            nodos = self.raiz.find('cfdi:Complemento', self.name_spaces).find(
                'nomina:Nomina',
                self.name_spaces
            ).find('nomina:Percepciones', self.name_spaces)

            self.percepciones_totalGravado = Validator.convertToChar(
                nodos.get('TotalGravado')
            )
            self.percepciones_totalExento = Validator.convertToChar(
                nodos.get('TotalExento')
            )

            for nodo in nodos:
                item = {
                    'TipoPercepcion': Validator.convertToChar(nodo.get('TipoPercepcion')),
                    'Clave': Validator.convertToChar(nodo.get('Clave')),
                    'Concepto': Validator.convertToChar(nodo.get('Concepto')),
                    'ImporteGravado': Validator.convertToChar(nodo.get('ImporteGravado')),
                    'ImporteExento': Validator.convertToChar(nodo.get('ImporteExento')),
                }

                self.percepciones.append(item)

            return True

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_Nomina_Percepciones_Node()',
                type(error).__name__,
                str(error)
            )

    def read_Nomina_Deducciones_Node(self):

        try:
            nodos = self.raiz.find('cfdi:Complemento', self.name_spaces).find(
                'nomina:Nomina',
                self.name_spaces
            ).find('nomina:Deducciones', self.name_spaces)

            self.deducciones_totalGravado = Validator.convertToChar(
                nodos.get('TotalGravado')
            )
            self.deducciones_totalExento = Validator.convertToChar(
                nodos.get('TotalExento')
            )

            for nodo in nodos:
                item = {
                    'TipoDeduccion': Validator.convertToChar(nodo.get('TipoDeduccion')),
                    'Clave': Validator.convertToChar(nodo.get('Clave')),
                    'Concepto': Validator.convertToChar(nodo.get('Concepto')),
                    'ImporteGravado': Validator.convertToChar(nodo.get('ImporteGravado')),
                    'ImporteExento': Validator.convertToChar(nodo.get('ImporteExento')),
                }

                self.deducciones.append(item)

            return True

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_Nomina_Deducciones_Node()',
                type(error).__name__,
                str(error)
            )

    def read_Nomina_HorasExtras(self):

        try:
            nodos = self.raiz.find('cfdi:Complemento', self.name_spaces).find(
                'nomina:Nomina',
                self.name_spaces
            ).find('nomina:HorasExtras', self.name_spaces)

            for nodo in nodos:
                item = {
                    'Dias': Validator.convertToChar(nodo.get('Dias')),
                    'TipoHoras': Validator.convertToChar(nodo.get('TipoHoras')),
                    'ImportePagado': Validator.convertToChar(nodo.get('ImportePagado')),
                }

                self.horasExtras.append(item)

            return True

        except Exception, error:
            raise ErrorEjecucion(
                'Comprobante.read_Nomina_HorasExtras()',
                type(error).__name__,
                str(error)
            )

    def read(self, _tipo):

        # Se obtienen datos del COMPROBANTE
        try:
            self.read_Comprobante_Node()
            print "Obtiendo datos del nodo COMPROBANTE.............OK"

        except Exception, error:
            print "Obtiendo datos del nodo COMPROBANTE.............{}".format(error.mensaje)

        # Se obtienen datos del EMISOR
        try:
            self.read_Emisor_Node()
            print "Obtiendo datos del nodo EMISOR..................OK"

        except Exception, error:
            print "Obtiendo datos del nodo EMISOR..................{}".format(error.mensaje)

        # Se obtienen datos del EMISOR DIRECCION
        try:
            self.read_Emisor_DomicilioFiscal_Node()
            print "Obtiendo datos del nodo EMISOR DIRECCION........OK"

        except Exception, error:
            print "Obtiendo datos del nodo EMISOR DIRECCION........{}".format(error.mensaje)

        # Se obtienen datos del modo EMISOR EXPEDIDO EN
        try:
            self.read_Emisor_ExpedidoEn_Node()
            print "Obtiendo datos del nodo EMISOR EXPEDIDO EN......OK"

        except Exception, error:
            print "Obtiendo datos del nodo EMISOR EXPEDIDO EN......{}".format(error.mensaje)

        # Se obtienen datos del nodo EMISOR REGIMEN
        try:
            self.read_Emisor_RegimenFiscal_Node()
            print "Obtiendo datos del nodo EMISOR REGIMEN..........OK"

        except Exception, error:
            print "Obtiendo datos del nodo EMISOR REGIMEN..........{}".format(error.mensaje)

        # Se obtienen datos del nodo RECEPTOR
        try:
            self.read_Receptor_Node()
            print "Obtiendo datos del nodo RECEPTOR................OK"

        except Exception, error:
            print "Obtiendo datos del nodo RECEPTOR................{}".format(error.mensaje)

        # Se obtienen datos del nodo RECEPTOR DIRECCION
        try:
            self.read_Receptor_Domicilio_Node()
            print "Obtiendo datos del nodo RECEPTOR DIRECCION......OK"

        except Exception, error:
            print "Obtiendo datos del nodo RECEPTOR DIRECCION......{}".format(error.mensaje)

        # Se obtienen datos del nodo IMPUESTOS
        try:
            self.read_Impuestos_Node()
            print "Obtiendo datos del nodo IMPUESTOS...............OK"

        except Exception, error:
            print "Obtiendo datos del nodo IMPUESTOS...............{}".format(error.mensaje)

        # Se obtienen datos del nodo IMPUESTOS TRASLADADOS
        try:
            self.read_Impuestos_Traslados()
            print "Obtiendo datos del nodo IMPUESTOS TRASLADADOS...OK"

        except Exception, error:
            print "Obtiendo datos del nodo IMPUESTOS TRASLADADOS...{}".format(error.mensaje)

        # Se obtienen datos del nodo IMPUESTOS RETENIDOS
        try:
            self.read_Impuestos_Retenciones()
            print "Obtiendo datos del nodo IMPUESTOS RETENIDOS.....OK"

        except Exception, error:

            print "Obtiendo datos del nodo IMPUESTOS RETENIDOS.....{}".format(error.mensaje)

        # Se obtienen datos del nodo CONCEPTOS
        try:
            self.read_Conceptos_Node()
            print "Obtiendo datos del nodo CONCEPTOS...............OK"

        except Exception, error:
            print "Obtiendo datos del nodo CONCEPTOS...............{}".format(error.mensaje)

        # Se obtienen datos del nodo COMPLEMENTO
        try:
            self.read_Complemento_Node()
            print "Obtiendo datos del nodo COMPLEMENTO.............OK"

        except Exception, error:
            print "Obtiendo datos del nodo COMPLEMENTO.............{}".format(error.mensaje)

        # Se obtienen datos del nodo NOMINA
        try:
            self.read_Nomina_Node()
            print "Obtiendo datos del nodo NOMINA..................OK"

        except Exception, error:
            print "Obtiendo datos del nodo NOMINA..................{}".format(error.mensaje)

        # Se obtienen datos del nodo PERCEPCIONES
        try:
            self.read_Nomina_Percepciones_Node()
            print "Obtiendo datos del nodo PERCEPCIONES............OK"

        except Exception, error:
            print "Obtiendo datos del nodo PERCEPCIONES............{}".format(error.mensaje)

        # Se obtienen datos del nodo DEDUCCIONES
        try:
            self.read_Nomina_Deducciones_Node()
            print "Obtiendo datos del nodo DEDUCCIONES.............OK"

        except Exception, error:
            print "Obtiendo datos del nodo DEDUCCIONES.............{}".format(error.mensaje)

        # Se obtienen datos del nodo HORAS EXTRAS
        try:
            self.read_Nomina_HorasExtras()
            print "Obtiendo datos del nodo HORAS EXTRAS............OK"

        except Exception, error:
            print "Obtiendo datos del nodo HORAS EXTRAS............{}".format(error.mensaje)

        if _tipo == "RECIBIDAS":
            self.resumen_tipo = "PROVEEDORES"

        elif _tipo == "EMITIDAS":
            if self.registroPatronal:
                self.resumen_tipo = "EMPLEADOS"
            else:
                self.resumen_tipo = "CLIENTES"
        else:
            self.resumen_tipo = "DESCONOCIDO"

    def __str__(self):
        return """
        UUID: {}
        Emisor: {} ({})
        Receptor: {} ({})
        Fecha: {}
        Fecha Timbrado: {}
        """.format(
            self.uuid,
            self.emisor_nombre,
            self.emisor_rfc,
            self.receptor_nombre,
            self.receptor_rfc,
            self.fecha,
            self.fechaTimbrado
        )

    def validate(self):

        try:
            estadoSAT = WebServiceSAT.get_Estado(
                self.emisor_rfc,
                self.receptor_rfc,
                self.total,
                self.uuid
            )

            print "Estado en SAT: {}".format(estadoSAT)

            if self.resumen_tipo == "PROVEEDORES":
                record = ModeloFacturaProveedor.get(self.uuid)

            elif self.resumen_tipo == "EMPLEADOS":
                record = ModeloComprobanteEmpleado.get(self.uuid)

            elif self.resumen_tipo == "CLIENTES":
                record = ModeloFacturaCliente.get(self.uuid)

            else:
                raise ErrorValidacion(
                    "Comprobante.validate()",
                    "Estado {}: No se establecio un tipo valido".format(self.resumen_tipo)
                )

            print "Estado en BD: {}".format(record.estadoSat)

            if estadoSAT != record.estadoSat:
                record.estadoSat = estadoSAT
                record.save()
                print "Se actualizo estado en la BD"

            else:
                print "No ha cambiado el estado en la BD"

            return 1

        except Exception, error:
            print (error.mensaje)
            return 0

    def save_toBD(self, _empresa_clave, _urlpath):

        self.empresa_clave = _empresa_clave
        self.url = Validator.convertToUrl(
            _urlpath,
            self.nombre
        )

        # import ipdb; ipdb.set_trace()

        try:
            if self.resumen_tipo == "PROVEEDORES":
                ModeloFacturaProveedor.add(self)

            elif self.resumen_tipo == "EMPLEADOS":
                ModeloComprobanteEmpleado.add(self)

            elif self.resumen_tipo == "CLIENTES":
                ModeloFacturaCliente.add(self)

            else:
                raise ErrorValidacion(
                    "Comprobante.save_toBD()",
                    "Estado {}: No se establecio un tipo valido".format(self.resumen_tipo)
                )

            return 1

        except Exception, error:
            print (error.mensaje)
            return 0
