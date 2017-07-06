# -*- coding: utf-8 -*-

# Librerias django
from django.contrib import admin

# Modelos:
from .models import Resumen
from .models import ComprobanteCliente
from .models import ComprobanteProveedor
from .models import ComprobanteEmpleado
from .models import Log


@admin.register(Resumen)
class AdminResumen(admin.ModelAdmin):

    list_display = (
        'empresa',
        'fecha',
        'tipo',
        'cantidad_guardadas',
        'cantidad_validadas',
        'total',
        'created_date',
        'updated_date',
    )
    search_fields = (
        'created_date',
    )
    list_filter = ('tipo', 'empresa', 'fecha')


@admin.register(ComprobanteCliente)
class AdminComprobanteCliente(admin.ModelAdmin):
    list_display = (
        'uuid',
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
        'fechaTimbrado',
        'noCertificadoSAT',
        'selloSAT',
        'empresa',
        'comentarios',
        'comprobacion',
        'pago',
        'estadoSat',
        'created_date',
        'updated_date',
    )
    list_filter = (
        'empresa',
        'estadoSat',
        'comprobacion',
        'fecha',
        'moneda',
        'receptor_nombre'
    )
    search_fields = (

    )


@admin.register(ComprobanteProveedor)
class AdminComprobanteProveedor(admin.ModelAdmin):
    list_display = (
        'uuid',
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
        'fechaTimbrado',
        'noCertificadoSAT',
        'selloSAT',
        'empresa',
        'comentarios',
        'comprobacion',
        'pago',
        'estadoSat',
        'created_date',
        'updated_date',
    )
    list_filter = (
        'empresa',
        'estadoSat',
        'comprobacion',
        'fecha',
        'moneda',
        'emisor_nombre'
    )


@admin.register(ComprobanteEmpleado)
class AdminComprobanteEmpleado(admin.ModelAdmin):
    list_display = (
        'uuid',
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
        'fechaTimbrado',
        'noCertificadoSAT',
        'selloSAT',
        'empresa',
        'comentarios',
        'comprobacion',
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
        'created_date',
        'updated_date',
    )
    list_filter = (
        'empresa',
        'estadoSat',
        'comprobacion',
        'fecha',
        'moneda',
        'receptor_nombre'
    )


@admin.register(Log)
class AdminLog(admin.ModelAdmin):
    list_display = (
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
    list_filter = (
        'estado',
        'operacion',
        'empresa',
    )
    search_fields = (
        'nombre',
        'fecha_operacion',
        'created_date',
    )
