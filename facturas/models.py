# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Otros Modelos:
from configuracion.models import Empresa


MONEDA_PESOS = [
    "NACIONAL",
    "PESOS MEXICANOS",
    "MXP",
    "Pesos",
    "MXN",
    "Peso Mexicano",
    "MN",
    "MONEDA NACIONAL",
    "MEX",
    "M.N.",
    "PMX",
]


class Resumen(models.Model):

    RESUMEN_TIPOS = (
        ('PROVEEDORES', 'FACTURAS DE PROVEEDORES'),
        ('CLIENTES', 'FACTURAS DE CLIENTES'),
        ('EMPLEADOS', 'COMPROBANTES DE EMPLEADOS'),
    )

    fecha = models.DateField()
    tipo = models.CharField(
        max_length=12,
        choices=RESUMEN_TIPOS
    )
    cantidad_guardadas = models.IntegerField(default=0)
    cantidad_validadas = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    empresa = models.ForeignKey(Empresa, null=True)
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = (('empresa', 'fecha', 'tipo'),)

    def __str__(self):
        return "{} - {}".format(self.fecha, self.tipo).encode("utf-8")


class Log(models.Model):

    LOG_ESTADOS = (
        ('EXITO', 'EXITO'),
        ('ERROR', 'ERROR'),
        ('DETALLE', 'DETALLE'),
        ('PROCESANDO', 'PROCESANDO'),
    )

    LOG_OPERACION_TIPO = (
        ('GET', 'OBTENER'),
        ('SAVE', 'GUARDAR'),
        ('VALIDATE', 'VALIDAR'),
    )

    LOG_TIPOS_COMPROBANTE = (
        ('REC', 'RECIBIDOS'),
        ('EMI', 'EMITIDOS'),
    )

    empresa = models.ForeignKey(Empresa, null=True)
    nombre = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    estado = models.CharField(
        max_length=10,
        choices=LOG_ESTADOS,
        null=True
    )
    tipo_comprobante = models.CharField(
        max_length=4,
        choices=LOG_TIPOS_COMPROBANTE,
        null=True
    )
    operacion = models.CharField(
        max_length=8,
        choices=LOG_OPERACION_TIPO,
        null=True
    )
    fecha_operacion = models.DateField()
    descripcion = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('empresa', 'nombre', 'operacion', 'fecha_operacion'),)

    def __str__(self):
        return self.nombre.encode("utf-8")


class Factura(models.Model):

    PAGADO_ESTADO = {
        ('PENDIENTE', 'PENDIENTE'),
        ('PAGADO', 'PAGADO'),
    }

    COMPROBACION_ESTADOS = (
        ('RECONOCIDO', 'RECONOCIDO'),
        ('NO_RECONOCIDO', 'NO RECONOCIDO'),
    )

    # Comprobante
    serie = models.CharField(max_length=255, null=True, blank=True)
    folio = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )
    formaDePago = models.CharField(max_length=255, null=True, blank=True)
    noCertificado = models.CharField(max_length=255, null=True, blank=True)
    subTotal = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0)
    tipoCambio = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0)
    moneda = models.CharField(max_length=255, null=True, blank=True)
    sello = models.CharField(max_length=500, null=True, blank=True)
    total = models.DecimalField(max_digits=20, decimal_places=4, default=0.0)
    tipoDeComprobante = models.CharField(max_length=255, null=True, blank=True)
    metodoDePago = models.CharField(max_length=255, null=True, blank=True)
    lugarExpedicion = models.CharField(max_length=255, null=True, blank=True)
    numCtaPago = models.CharField(max_length=255, null=True, blank=True)
    condicionesDePago = models.CharField(
        max_length=2000, null=True, blank=True
    )

    # Emisor
    emisor_rfc = models.CharField(max_length=255, null=True, blank=True)
    emisor_nombre = models.CharField(max_length=255, null=True, blank=True)

    # Emisor Direccion
    emisor_calle = models.CharField(max_length=255, null=True, blank=True)
    emisor_noExterior = models.CharField(max_length=255, null=True, blank=True)
    emisor_noInterior = models.CharField(max_length=255, null=True, blank=True)
    emisor_colonia = models.CharField(max_length=255, null=True, blank=True)
    emisor_localidad = models.CharField(max_length=255, null=True, blank=True)
    emisor_municipio = models.CharField(max_length=255, null=True, blank=True)
    emisor_estado = models.CharField(max_length=255, null=True, blank=True)
    emisor_pais = models.CharField(max_length=255, null=True, blank=True)
    emisor_codigoPostal = models.CharField(
        max_length=255, null=True, blank=True
    )

    # Emisor Expedido En
    emisor_expedidoEn_calle = models.CharField(
        max_length=255, null=True, blank=True
    )
    emisor_expedidoEn_noExterior = models.CharField(
        max_length=255, null=True, blank=True
    )
    emisor_expedidoEn_noInterior = models.CharField(
        max_length=255, null=True, blank=True
    )
    emisor_expedidoEn_colonia = models.CharField(
        max_length=255, null=True, blank=True
    )
    emisor_expedidoEn_municipio = models.CharField(
        max_length=255, null=True, blank=True
    )
    emisor_expedidoEn_estado = models.CharField(
        max_length=255, null=True, blank=True
    )
    emisor_expedidoEn_pais = models.CharField(
        max_length=255, null=True, blank=True
    )

    # Emisor Regimen
    emisor_regimen = models.CharField(max_length=255, null=True, blank=True)

    # Receptor
    receptor_rfc = models.CharField(max_length=255, null=True, blank=True)
    receptor_nombre = models.CharField(max_length=255, null=True, blank=True)

    # Receptor Direccion
    receptor_calle = models.CharField(max_length=255, null=True, blank=True)
    receptor_noExterior = models.CharField(
        max_length=255, null=True, blank=True
    )
    receptor_noInterior = models.CharField(
        max_length=255, null=True, blank=True
    )
    receptor_colonia = models.CharField(max_length=255, null=True, blank=True)
    receptor_localidad = models.CharField(
        max_length=255, null=True, blank=True
    )
    receptor_municipio = models.CharField(
        max_length=255, null=True, blank=True
    )
    receptor_estado = models.CharField(max_length=255, null=True, blank=True)
    receptor_pais = models.CharField(max_length=255, null=True, blank=True)
    receptor_codigoPostal = models.CharField(
        max_length=255, null=True, blank=True
    )

    # Conceptos
    conceptos = models.TextField(null=True, blank=True)

    # Impuestos
    totalImpuestosTrasladados = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0)
    totalImpuestosRetenidos = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0)

    # Impuestos Trasladados
    impuestos_trasladados = models.TextField(null=True, blank=True)

    # Impuestos Retenidos
    impuestos_retenidos = models.TextField(null=True, blank=True)

    # Complementos
    uuid = models.CharField(max_length=255, unique=True)
    fechaTimbrado = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )
    noCertificadoSAT = models.CharField(max_length=255, null=True, blank=True)
    selloSAT = models.CharField(max_length=500, null=True, blank=True)

    # Datos Adicionales
    empresa = models.ForeignKey(Empresa)
    comentarios = models.TextField(null=True, blank=True)
    comprobacion = models.CharField(
        max_length=13,
        choices=COMPROBACION_ESTADOS,
        default="NO_RECONOCIDO",
        null=True
    )
    url = models.CharField(max_length=255, null=True, blank=True)
    tiene_pdf = models.BooleanField(default=False)
    estadoSat = models.CharField(
        max_length=255, null=True, blank=True, default="SIN VALIDAR")

    pago = models.CharField(
        max_length=13,
        choices=PAGADO_ESTADO,
        default="PEDIENTE",
        blank=True,
        null=True
    )
    fecha_validacion = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class FacturaProveedor(Factura):

    def __str__(self):
        return "{} - {}".format(self.uuid, self.emisor_rfc).encode("utf-8")


class FacturaCliente(Factura):

    def __str__(self):
        return "{} - {}".format(self.uuid, self.receptor_rfc).encode("utf-8")


class ComprobanteEmpleado(Factura):

    # Nomina Datos
    registroPatronal = models.CharField(
        max_length=255, null=True, blank=True
    )
    numEmpleado = models.CharField(max_length=255, null=True, blank=True)
    curp = models.CharField(max_length=255, null=True, blank=True)
    tipoRegimen = models.CharField(max_length=255, null=True, blank=True)
    numSeguridadSocial = models.CharField(
        max_length=255, null=True, blank=True
    )
    fechaPago = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )
    fechaInicialPago = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )
    fechaFinalPago = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )
    numDiasPagados = models.IntegerField(default=0)
    clabe = models.CharField(max_length=255, null=True, blank=True)
    banco = models.CharField(max_length=255, null=True, blank=True)
    fechaInicioRelLaboral = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )
    antiguedad = models.CharField(max_length=255, null=True, blank=True)
    puesto = models.CharField(max_length=255, null=True, blank=True)
    tipoJornada = models.CharField(max_length=255, null=True, blank=True)
    periodicidadPago = models.CharField(max_length=255, null=True, blank=True)
    riesgoPuesto = models.CharField(max_length=255, null=True, blank=True)
    salarioDiarioIntegrado = models.CharField(
        max_length=255, null=True, blank=True
    )

    # Nomina Percepciones
    percepciones_totalGravado = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0)
    percepciones_totalExento = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0)
    percepciones = models.TextField(null=True, blank=True)

    # Nomina Deducciones
    deducciones_totalGravado = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0)
    deducciones_totalExento = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0)
    deducciones = models.TextField(null=True, blank=True)

    # Horas Extras
    horasExtras = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.uuid, self.receptor_rfc).encode("utf-8")
