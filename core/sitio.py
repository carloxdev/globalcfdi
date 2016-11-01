# -*- coding: utf-8 -*-

# Librerias Python:
import os
import sys
import datetime
import json

# Librerias Propias:
from tools.mistakes import ErrorEjecucion


# Conectando con la configuracion del sitio
# import ipdb; ipdb.set_trace() 
if __name__ == 'sitio':
    project_abspath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
else:
    project_abspath = os.getcwd()

print "Programa que ejecuta: {}".format(__name__)
print "Ruta de proyeto: {} \n".format(project_abspath)

sys.path.append(project_abspath)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SmartCFDI.settings")

# Librerias Django
from django.db import connection
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
# from django.conf import settings

# Modelos
from home.models import Ambiente
from configuracion.models import Empresa
from facturas.models import FacturaProveedor
from facturas.models import FacturaCliente
from facturas.models import ComprobanteEmpleado
from facturas.models import Resumen
from facturas.models import Log


class ModeloAmbiente(object):

    @classmethod
    def get(self, _clave):

        try:
            connection.close()
            ambiente = Ambiente.objects.get(clave=_clave)
            return ambiente

        except Exception, error:
            raise ErrorEjecucion(
                "ModeloFacturaProveedor.get(): {0} - {1}".format(
                    type(error).__name__,
                    str(error)
                )
            )


class ModeloEmpresa(object):

    @classmethod
    def get(self, _empresa_clave):

        try:
            connection.close()
            empresa = Empresa.objects.get(clave=_empresa_clave)
            return empresa

        except Exception, error:

            raise ErrorEjecucion(
                "ModeloEmpresa.get_Activas()",
                type(error).__name__,
                str(error)
            )

    @classmethod
    def get_Activas(self):

        try:
            connection.close()
            empresas = Empresa.objects.filter(activa=True)
            return empresas

        except Exception, error:

            raise ErrorEjecucion(
                "ModeloEmpresa.get_Activas()",
                type(error).__name__,
                str(error)
            )


class ModeloFacturaProveedor(object):

    @classmethod
    def add(self, _comprobante):

        try:
            connection.close()
            comprobante = FacturaProveedor(
                serie=_comprobante.serie,
                folio=_comprobante.folio,
                fecha=_comprobante.fecha,
                formaDePago=_comprobante.formaDePago,
                noCertificado=_comprobante.noCertificado,
                subTotal=_comprobante.subTotal,
                tipoCambio=_comprobante.tipoCambio,
                moneda=_comprobante.moneda,
                sello=_comprobante.sello,
                total=_comprobante.total,
                tipoDeComprobante=_comprobante.tipoDeComprobante,
                metodoDePago=_comprobante.metodoDePago,
                lugarExpedicion=_comprobante.lugarExpedicion,
                numCtaPago=_comprobante.numCtaPago,
                condicionesDePago=_comprobante.condicionesDePago,
                emisor_rfc=_comprobante.emisor_rfc,
                emisor_nombre=_comprobante.emisor_nombre,
                emisor_calle=_comprobante.emisor_calle,
                emisor_noExterior=_comprobante.emisor_noExterior,
                emisor_noInterior=_comprobante.emisor_noInterior,
                emisor_colonia=_comprobante.emisor_colonia,
                emisor_localidad=_comprobante.emisor_localidad,
                emisor_municipio=_comprobante.emisor_municipio,
                emisor_estado=_comprobante.emisor_estado,
                emisor_pais=_comprobante.emisor_pais,
                emisor_codigoPostal=_comprobante.emisor_codigoPostal,
                emisor_expedidoEn_calle=_comprobante.emisor_expedidoEn_calle,
                emisor_expedidoEn_noExterior=_comprobante.emisor_expedidoEn_noExterior,
                emisor_expedidoEn_noInterior=_comprobante.emisor_expedidoEn_noInterior,
                emisor_expedidoEn_colonia=_comprobante.emisor_expedidoEn_colonia,
                emisor_expedidoEn_municipio=_comprobante.emisor_expedidoEn_municipio,
                emisor_expedidoEn_estado=_comprobante.emisor_expedidoEn_estado,
                emisor_expedidoEn_pais=_comprobante.emisor_expedidoEn_pais,
                emisor_regimen=_comprobante.emisor_regimen,
                receptor_rfc=_comprobante.receptor_rfc,
                receptor_nombre=_comprobante.receptor_nombre,
                receptor_calle=_comprobante.receptor_calle,
                receptor_noExterior=_comprobante.receptor_noExterior,
                receptor_noInterior=_comprobante.receptor_noInterior,
                receptor_colonia=_comprobante.receptor_colonia,
                receptor_localidad=_comprobante.receptor_localidad,
                receptor_municipio=_comprobante.receptor_municipio,
                receptor_estado=_comprobante.receptor_estado,
                receptor_pais=_comprobante.receptor_pais,
                receptor_codigoPostal=_comprobante.receptor_codigoPostal,
                conceptos=json.dumps(_comprobante.conceptos),
                totalImpuestosTrasladados=_comprobante.totalImpuestosTrasladados,
                totalImpuestosRetenidos=_comprobante.totalImpuestosRetenidos,
                impuestos_trasladados=json.dumps(_comprobante.impuestos_trasladados),
                impuestos_retenidos=json.dumps(_comprobante.impuestos_retenidos),
                uuid=_comprobante.uuid,
                fechaTimbrado=_comprobante.fechaTimbrado,
                noCertificadoSAT=_comprobante.noCertificadoSAT,
                selloSAT=_comprobante.selloSAT,
                url=_comprobante.url,
            )

            empresa = Empresa.objects.get(clave=_comprobante.empresa_clave)
            comprobante.empresa = empresa
            comprobante.save()

            print "Se guardo el comprobante: {}".format(_comprobante.uuid)

        except Exception, error:
            raise ErrorEjecucion(
                'ModeloFacturaProveedor.add()',
                type(error).__name__,
                str(error)
            )

    @classmethod
    def get(self, _uuid):

        try:
            connection.close()
            factura = FacturaProveedor.objects.get(uuid=_uuid)
            return factura

        except Exception, error:
            raise ErrorEjecucion(
                "ModeloFacturaProveedor.get(): {0} - {1}".format(
                    type(error).__name__,
                    str(error)
                )
            )

    @classmethod
    def update(self):
        pass


class ModeloFacturaCliente(object):

    @classmethod
    def add(self, _comprobante):
        try:
            connection.close()
            comprobante = FacturaCliente(
                serie=_comprobante.serie,
                folio=_comprobante.folio,
                fecha=_comprobante.fecha,
                formaDePago=_comprobante.formaDePago,
                noCertificado=_comprobante.noCertificado,
                subTotal=_comprobante.subTotal,
                tipoCambio=_comprobante.tipoCambio,
                moneda=_comprobante.moneda,
                sello=_comprobante.sello,
                total=_comprobante.total,
                tipoDeComprobante=_comprobante.tipoDeComprobante,
                metodoDePago=_comprobante.metodoDePago,
                lugarExpedicion=_comprobante.lugarExpedicion,
                numCtaPago=_comprobante.numCtaPago,
                condicionesDePago=_comprobante.condicionesDePago,
                emisor_rfc=_comprobante.emisor_rfc,
                emisor_nombre=_comprobante.emisor_nombre,
                emisor_calle=_comprobante.emisor_calle,
                emisor_noExterior=_comprobante.emisor_noExterior,
                emisor_noInterior=_comprobante.emisor_noInterior,
                emisor_colonia=_comprobante.emisor_colonia,
                emisor_localidad=_comprobante.emisor_localidad,
                emisor_municipio=_comprobante.emisor_municipio,
                emisor_estado=_comprobante.emisor_estado,
                emisor_pais=_comprobante.emisor_pais,
                emisor_codigoPostal=_comprobante.emisor_codigoPostal,
                emisor_expedidoEn_calle=_comprobante.emisor_expedidoEn_calle,
                emisor_expedidoEn_noExterior=_comprobante.emisor_expedidoEn_noExterior,
                emisor_expedidoEn_noInterior=_comprobante.emisor_expedidoEn_noInterior,
                emisor_expedidoEn_colonia=_comprobante.emisor_expedidoEn_colonia,
                emisor_expedidoEn_municipio=_comprobante.emisor_expedidoEn_municipio,
                emisor_expedidoEn_estado=_comprobante.emisor_expedidoEn_estado,
                emisor_expedidoEn_pais=_comprobante.emisor_expedidoEn_pais,
                emisor_regimen=_comprobante.emisor_regimen,
                receptor_rfc=_comprobante.receptor_rfc,
                receptor_nombre=_comprobante.receptor_nombre,
                receptor_calle=_comprobante.receptor_calle,
                receptor_noExterior=_comprobante.receptor_noExterior,
                receptor_noInterior=_comprobante.receptor_noInterior,
                receptor_colonia=_comprobante.receptor_colonia,
                receptor_localidad=_comprobante.receptor_localidad,
                receptor_municipio=_comprobante.receptor_municipio,
                receptor_estado=_comprobante.receptor_estado,
                receptor_pais=_comprobante.receptor_pais,
                receptor_codigoPostal=_comprobante.receptor_codigoPostal,
                conceptos=json.dumps(_comprobante.conceptos),
                totalImpuestosTrasladados=_comprobante.totalImpuestosTrasladados,
                totalImpuestosRetenidos=_comprobante.totalImpuestosRetenidos,
                impuestos_trasladados=json.dumps(_comprobante.impuestos_trasladados),
                impuestos_retenidos=json.dumps(_comprobante.impuestos_retenidos),
                uuid=_comprobante.uuid,
                fechaTimbrado=_comprobante.fechaTimbrado,
                noCertificadoSAT=_comprobante.noCertificadoSAT,
                selloSAT=_comprobante.selloSAT,
                url=_comprobante.url,
            )
            empresa = Empresa.objects.get(clave=_comprobante.empresa_clave)
            comprobante.empresa = empresa
            comprobante.save()

            print "Se guardo el comprobante: {}".format(_comprobante.uuid)

        except Exception, error:
            raise ErrorEjecucion(
                'ModeloFacturaCliente.add()',
                type(error).__name__,
                str(error)
            )

    @classmethod
    def get(self, _uuid):

        try:
            connection.close()
            factura = FacturaCliente.objects.get(uuid=_uuid)
            return factura

        except Exception, error:
            raise ErrorEjecucion(
                "ModeloFacturaCliente.get(): {0} - {1}".format(
                    type(error).__name__,
                    str(error)
                )
            )

    @classmethod
    def update(self):
        pass


class ModeloComprobanteEmpleado(object):

    @classmethod
    def add(self, _comprobante):
        try:
            connection.close()
            comprobante = ComprobanteEmpleado(
                serie=_comprobante.serie,
                folio=_comprobante.folio,
                fecha=_comprobante.fecha,
                formaDePago=_comprobante.formaDePago,
                noCertificado=_comprobante.noCertificado,
                subTotal=_comprobante.subTotal,
                tipoCambio=_comprobante.tipoCambio,
                moneda=_comprobante.moneda,
                sello=_comprobante.sello,
                total=_comprobante.total,
                tipoDeComprobante=_comprobante.tipoDeComprobante,
                metodoDePago=_comprobante.metodoDePago,
                lugarExpedicion=_comprobante.lugarExpedicion,
                numCtaPago=_comprobante.numCtaPago,
                condicionesDePago=_comprobante.condicionesDePago,
                emisor_rfc=_comprobante.emisor_rfc,
                emisor_nombre=_comprobante.emisor_nombre,
                emisor_calle=_comprobante.emisor_calle,
                emisor_noExterior=_comprobante.emisor_noExterior,
                emisor_noInterior=_comprobante.emisor_noInterior,
                emisor_colonia=_comprobante.emisor_colonia,
                emisor_localidad=_comprobante.emisor_localidad,
                emisor_municipio=_comprobante.emisor_municipio,
                emisor_estado=_comprobante.emisor_estado,
                emisor_pais=_comprobante.emisor_pais,
                emisor_codigoPostal=_comprobante.emisor_codigoPostal,
                emisor_expedidoEn_calle=_comprobante.emisor_expedidoEn_calle,
                emisor_expedidoEn_noExterior=_comprobante.emisor_expedidoEn_noExterior,
                emisor_expedidoEn_noInterior=_comprobante.emisor_expedidoEn_noInterior,
                emisor_expedidoEn_colonia=_comprobante.emisor_expedidoEn_colonia,
                emisor_expedidoEn_municipio=_comprobante.emisor_expedidoEn_municipio,
                emisor_expedidoEn_estado=_comprobante.emisor_expedidoEn_estado,
                emisor_expedidoEn_pais=_comprobante.emisor_expedidoEn_pais,
                emisor_regimen=_comprobante.emisor_regimen,
                receptor_rfc=_comprobante.receptor_rfc,
                receptor_nombre=_comprobante.receptor_nombre,
                receptor_calle=_comprobante.receptor_calle,
                receptor_noExterior=_comprobante.receptor_noExterior,
                receptor_noInterior=_comprobante.receptor_noInterior,
                receptor_colonia=_comprobante.receptor_colonia,
                receptor_localidad=_comprobante.receptor_localidad,
                receptor_municipio=_comprobante.receptor_municipio,
                receptor_estado=_comprobante.receptor_estado,
                receptor_pais=_comprobante.receptor_pais,
                receptor_codigoPostal=_comprobante.receptor_codigoPostal,
                conceptos=json.dumps(_comprobante.conceptos),
                totalImpuestosTrasladados=_comprobante.totalImpuestosTrasladados,
                totalImpuestosRetenidos=_comprobante.totalImpuestosRetenidos,
                impuestos_trasladados=json.dumps(_comprobante.impuestos_trasladados),
                impuestos_retenidos=json.dumps(_comprobante.impuestos_retenidos),
                uuid=_comprobante.uuid,
                fechaTimbrado=_comprobante.fechaTimbrado,
                noCertificadoSAT=_comprobante.noCertificadoSAT,
                selloSAT=_comprobante.selloSAT,
                url=_comprobante.url,
                registroPatronal=_comprobante.registroPatronal,
                numEmpleado=_comprobante.numEmpleado,
                curp=_comprobante.curp,
                tipoRegimen=_comprobante.tipoRegimen,
                numSeguridadSocial=_comprobante.numSeguridadSocial,
                fechaPago=_comprobante.fechaPago,
                fechaInicialPago=_comprobante.fechaInicialPago,
                fechaFinalPago=_comprobante.fechaFinalPago,
                numDiasPagados=_comprobante.numDiasPagados,
                clabe=_comprobante.clabe,
                banco=_comprobante.banco,
                fechaInicioRelLaboral=_comprobante.fechaInicioRelLaboral,
                antiguedad=_comprobante.antiguedad,
                puesto=_comprobante.puesto,
                tipoJornada=_comprobante.tipoJornada,
                periodicidadPago=_comprobante.periodicidadPago,
                riesgoPuesto=_comprobante.riesgoPuesto,
                salarioDiarioIntegrado=_comprobante.salarioDiarioIntegrado,
                percepciones_totalGravado=_comprobante.percepciones_totalGravado,
                percepciones_totalExento=_comprobante.percepciones_totalExento,
                percepciones=json.dumps(_comprobante.percepciones),
                deducciones_totalGravado=_comprobante.deducciones_totalGravado,
                deducciones_totalExento=_comprobante.deducciones_totalExento,
                deducciones=json.dumps(_comprobante.deducciones),
                horasExtras=json.dumps(_comprobante.horasExtras),
            )
            empresa = Empresa.objects.get(clave=_comprobante.empresa_clave)
            comprobante.empresa = empresa
            comprobante.save()
            print "Se guardo el comprobante: {}".format(_comprobante.uuid)

        except Exception, error:
            raise ErrorEjecucion(
                'ComprobanteEmpleado.add()',
                type(error).__name__,
                str(error)
            )

    @classmethod
    def get(self, _uuid):

        try:
            connection.close()
            factura = ComprobanteEmpleado.objects.get(uuid=_uuid)
            return factura

        except Exception, error:
            raise ErrorEjecucion(
                "ModeloComprobanteEmpleado.get(): {0} - {1}".format(
                    type(error).__name__,
                    str(error)
                )
            )

    @classmethod
    def update(self):
        pass


class ModeloResumen(object):

    @classmethod
    def add(self, _empresa, _fecha, _tipo, _guardadas, _validadas, _total):

        try:
            connection.close()
            resumen = Resumen(
                empresa=_empresa,
                fecha=_fecha,
                tipo=_tipo,
                cantidad_guardadas=_guardadas,
                cantidad_validadas=_validadas,
                total=_total
            )

            resumen.save()

        except Exception, error:
            raise ErrorEjecucion(
                'ModeloResumen.add()',
                type(error).__name__,
                str(error)
            )

    @classmethod
    def get(self, _fecha, _tipo):

        try:
            connection.close()
            resumen = Resumen.objects.get(fecha=_fecha, tipo=_tipo)
            return resumen

        except Exception, error:
            raise ErrorEjecucion(
                'ModeloResumen.get()',
                type(error).__name__,
                str(error)
            )


class ModeloLog(object):

    @classmethod
    def add(self, _log):

        try:
            connection.close()
            log = Log(
                nombre=_log.nombre,
                estado=_log.estado,
                operacion=_log.operacion,
                empresa=_log.empresa,
                fecha_operacion=_log.fecha_operacion,
                url=_log.url
            )

            log.save()

            print "Se creo registro de log en BD"

        except Exception, error:
            raise ErrorEjecucion(
                'ModeloLog.add()',
                type(error).__name__,
                str(error)
            )

    @classmethod
    def get(self, _nombre):

        try:
            connection.close()
            log = Log.objects.get(nombre=_nombre)
            return log

        except Exception, error:
            raise ErrorEjecucion(
                'ModeloLog.get()',
                type(error).__name__,
                str(error)
            )
