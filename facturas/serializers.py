# -*- coding: utf-8 -*-

# Librerias API REST:
from rest_framework import serializers

# Modelos:
from .models import FacturaProveedor
from .models import FacturaCliente
from .models import ComprobanteEmpleado
from .models import Log
from .models import Resumen


class FacturaProveedorSerializer(serializers.HyperlinkedModelSerializer):

    empresa = serializers.SerializerMethodField()
    comprobacion = serializers.SerializerMethodField()

    class Meta:
        model = FacturaProveedor
        fields = (
            'serie',
            'folio',
            'fecha',
            'formaDePago',
            'noCertificado',
            'subTotal',
            'tipoCambio',
            'moneda',
            'sello',
            'total',
            'tipoDeComprobante',
            'metodoDePago',
            'lugarExpedicion',
            'numCtaPago',
            'condicionesDePago',
            'emisor_rfc',
            'emisor_nombre',
            'emisor_calle',
            'emisor_noExterior',
            'emisor_noInterior',
            'emisor_colonia',
            'emisor_localidad',
            'emisor_municipio',
            'emisor_estado',
            'emisor_pais',
            'emisor_codigoPostal',
            'emisor_expedidoEn_calle',
            'emisor_expedidoEn_noExterior',
            'emisor_expedidoEn_noInterior',
            'emisor_expedidoEn_colonia',
            'emisor_expedidoEn_municipio',
            'emisor_expedidoEn_estado',
            'emisor_expedidoEn_pais',
            'emisor_regimen',
            'receptor_rfc',
            'receptor_nombre',
            'receptor_calle',
            'receptor_noExterior',
            'receptor_noInterior',
            'receptor_colonia',
            'receptor_localidad',
            'receptor_municipio',
            'receptor_estado',
            'receptor_pais',
            'receptor_codigoPostal',
            'conceptos',
            'totalImpuestosTrasladados',
            'totalImpuestosRetenidos',
            'impuestos_trasladados',
            'impuestos_retenidos',
            'uuid',
            'fechaTimbrado',
            'noCertificadoSAT',
            'selloSAT',
            'empresa',
            'comentarios',
            'comprobacion',
            'url',
            'tiene_pdf',
            'estadoSat',
        )

    def get_empresa(self, obj):

        try:
            return obj.empresa.clave
        except:
            return ""

    def get_comprobacion(self, obj):
        try:
            return obj.get_comprobacion_display()
        except:
            return ""


class FacturaClienteSerializer(serializers.HyperlinkedModelSerializer):

    empresa = serializers.SerializerMethodField()
    comprobacion = serializers.SerializerMethodField()

    class Meta:
        model = FacturaCliente
        fields = (
            'serie',
            'folio',
            'fecha',
            'formaDePago',
            'noCertificado',
            'subTotal',
            'tipoCambio',
            'moneda',
            'sello',
            'total',
            'tipoDeComprobante',
            'metodoDePago',
            'lugarExpedicion',
            'numCtaPago',
            'condicionesDePago',
            'emisor_rfc',
            'emisor_nombre',
            'emisor_calle',
            'emisor_noExterior',
            'emisor_noInterior',
            'emisor_colonia',
            'emisor_localidad',
            'emisor_municipio',
            'emisor_estado',
            'emisor_pais',
            'emisor_codigoPostal',
            'emisor_expedidoEn_calle',
            'emisor_expedidoEn_noExterior',
            'emisor_expedidoEn_noInterior',
            'emisor_expedidoEn_colonia',
            'emisor_expedidoEn_municipio',
            'emisor_expedidoEn_estado',
            'emisor_expedidoEn_pais',
            'emisor_regimen',
            'receptor_rfc',
            'receptor_nombre',
            'receptor_calle',
            'receptor_noExterior',
            'receptor_noInterior',
            'receptor_colonia',
            'receptor_localidad',
            'receptor_municipio',
            'receptor_estado',
            'receptor_pais',
            'receptor_codigoPostal',
            'conceptos',
            'totalImpuestosTrasladados',
            'totalImpuestosRetenidos',
            'impuestos_trasladados',
            'impuestos_retenidos',
            'uuid',
            'fechaTimbrado',
            'noCertificadoSAT',
            'selloSAT',
            'empresa',
            'comentarios',
            'comprobacion',
            'url',
            'tiene_pdf',
            'estadoSat',
        )

    def get_empresa(self, obj):

        try:
            return obj.empresa.clave
        except:
            return ""

    def get_comprobacion(self, obj):
        try:
            return obj.get_comprobacion_display()
        except:
            return ""


class ComprobanteEmpleadoSerializer(serializers.HyperlinkedModelSerializer):

    empresa = serializers.SerializerMethodField()
    comprobacion = serializers.SerializerMethodField()

    class Meta:
        model = ComprobanteEmpleado
        fields = (
            'serie',
            'folio',
            'fecha',
            'formaDePago',
            'noCertificado',
            'subTotal',
            'tipoCambio',
            'moneda',
            'sello',
            'total',
            'tipoDeComprobante',
            'metodoDePago',
            'lugarExpedicion',
            'numCtaPago',
            'condicionesDePago',
            'emisor_rfc',
            'emisor_nombre',
            'emisor_calle',
            'emisor_noExterior',
            'emisor_noInterior',
            'emisor_colonia',
            'emisor_localidad',
            'emisor_municipio',
            'emisor_estado',
            'emisor_pais',
            'emisor_codigoPostal',
            'emisor_expedidoEn_calle',
            'emisor_expedidoEn_noExterior',
            'emisor_expedidoEn_noInterior',
            'emisor_expedidoEn_colonia',
            'emisor_expedidoEn_municipio',
            'emisor_expedidoEn_estado',
            'emisor_expedidoEn_pais',
            'emisor_regimen',
            'receptor_rfc',
            'receptor_nombre',
            'receptor_calle',
            'receptor_noExterior',
            'receptor_noInterior',
            'receptor_colonia',
            'receptor_localidad',
            'receptor_municipio',
            'receptor_estado',
            'receptor_pais',
            'receptor_codigoPostal',
            'conceptos',
            'totalImpuestosTrasladados',
            'totalImpuestosRetenidos',
            'impuestos_trasladados',
            'impuestos_retenidos',
            'uuid',
            'fechaTimbrado',
            'noCertificadoSAT',
            'selloSAT',
            'empresa',
            'comentarios',
            'comprobacion',
            'url',
            'tiene_pdf',
            'estadoSat',
            'registroPatronal',
            'numEmpleado',
            'curp',
            'tipoRegimen',
            'numSeguridadSocial',
            'fechaPago',
            'fechaInicialPago',
            'fechaFinalPago',
            'numDiasPagados',
            'clabe',
            'banco',
            'fechaInicioRelLaboral',
            'antiguedad',
            'puesto',
            'tipoJornada',
            'periodicidadPago',
            'riesgoPuesto',
            'salarioDiarioIntegrado',
            'percepciones_totalGravado',
            'percepciones_totalExento',
            'percepciones',
            'deducciones_totalGravado',
            'deducciones_totalExento',
            'deducciones',
            'horasExtras',
        )

    def get_empresa(self, obj):

        try:
            return obj.empresa.clave
        except:
            return ""

    def get_comprobacion(self, obj):
        try:
            return obj.get_comprobacion_display()
        except:
            return ""


class LogSerializer(serializers.HyperlinkedModelSerializer):

    empresa = serializers.SerializerMethodField()
    estado = serializers.SerializerMethodField()
    operacion = serializers.SerializerMethodField()

    class Meta:
        model = Log
        fields = (
            'empresa',
            'nombre',
            'estado',
            'operacion',
            'fecha_operacion',
            'descripcion',
            'url',
            'created_date',
            'updated_date',
        )

    def get_empresa(self, obj):

        try:
            return obj.empresa.clave
        except:
            return ""

    def get_estado(self, obj):
        try:
            return obj.get_estado_display()
        except:
            return ""

    def get_operacion(self, obj):
        try:
            return obj.get_operacion_display()
        except:
            return ""


class ResumenSerializer(serializers.HyperlinkedModelSerializer):

    empresa = serializers.SerializerMethodField()

    class Meta:
        model = Resumen
        fields = (
            'fecha',
            'tipo',
            'cantidad_guardadas',
            'cantidad_validadas',
            'total',
            'empresa',
            'created_date',
            'updated_date',
        )

    def get_empresa(self, obj):

        try:
            return obj.empresa.clave
        except:
            return ""
