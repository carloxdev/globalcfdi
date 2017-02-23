# -*- coding: utf-8 -*-

# Django API REST
from rest_framework import filters
import django_filters

# Modelos
from .models import Log
from .models import FacturaProveedor
from .models import FacturaCliente
from .models import ComprobanteEmpleado
from .models import Resumen


def filtra_FechaOperacion_Min(queryset, value):

    if not value:
        return queryset
    else:
        consulta = queryset.filter(fecha_operacion__gte=value)
        return consulta


def filtra_FechaOperacion_Max(queryset, value):

    if not value:
        return queryset
    else:
        consulta = queryset.filter(fecha_operacion__lte=value)
        return consulta


def filtra_created_Min(queryset, value):

    if not value:
        return queryset
    else:
        consulta = queryset.filter(created_date__gte=value)
        return consulta


def filtra_created_Max(queryset, value):

    if not value:
        return queryset
    else:
        consulta = queryset.filter(created_date__lte=value)
        return consulta


class LogFilter(filters.FilterSet):

    fecha_operacion_min = django_filters.CharFilter(
        action=filtra_FechaOperacion_Min)
    fecha_operacion_max = django_filters.CharFilter(
        action=filtra_FechaOperacion_Max)

    created_date_min = django_filters.CharFilter(
        action=filtra_created_Min)
    created_date_max = django_filters.CharFilter(
        action=filtra_created_Max)

    class Meta:
        model = Log
        fields = [
            'empresa__clave',
            'estado',
            'operacion',
            'tipo_comprobante',
            'fecha_operacion_min',
            'fecha_operacion_max',
            'created_date_min',
            'created_date_max',
        ]


def filtra_Fecha_Min(queryset, value):

    valor = "{}T00:00:00".format(value.encode("utf-8"))

    if not value:
        return queryset
    else:
        consulta = queryset.filter(fecha__gte=valor)
        return consulta


def filtra_Fecha_Max(queryset, value):

    valor = "{}T23:59:59".format(value.encode("utf-8"))

    if not value:
        return queryset
    else:
        consulta = queryset.filter(fecha__lte=valor)
        return consulta


def filtra_Resumen_Fecha_Min(queryset, value):

    if not value:
        return queryset
    else:
        consulta = queryset.filter(fecha__gte=value)
        return consulta


def filtra_Resumen_Fecha_Max(queryset, value):

    if not value:
        return queryset
    else:
        consulta = queryset.filter(fecha__lte=value)
        return consulta


def filtra_FechaTimbrado_Min(queryset, value):

    valor = "{}T00:00:00".format(value)

    if not value:
        return queryset
    else:
        consulta = queryset.filter(fecha__gte=valor)
        return consulta


def filtra_FechaTimbrado_Max(queryset, value):

    valor = "{}T23:59:59".format(value)

    if not value:
        return queryset
    else:
        consulta = queryset.filter(fecha__lte=valor)
        return consulta


class FacturaProveedorFilter(filters.FilterSet):

    uuid = django_filters.CharFilter(name="uuid", lookup_expr="contains")

    emisor_rfc = django_filters.CharFilter(
        name="emisor_rfc", lookup_expr="contains")

    emisor_nombre = django_filters.CharFilter(
        name="emisor_nombre", lookup_expr="contains")

    receptor_rfc = django_filters.CharFilter(
        name="receptor_rfc", lookup_expr="contains")
    receptor_nombre = django_filters.CharFilter(
        name="receptor_nombre", lookup_expr="contains")

    fechaTimbrado_min = django_filters.CharFilter(
        action=filtra_FechaTimbrado_Min)
    fechaTimbrado_max = django_filters.CharFilter(
        action=filtra_FechaTimbrado_Max)

    comprobacion = django_filters.CharFilter(
        name="comprobacion", lookup_expr="contains")

    fecha_min = django_filters.CharFilter(action=filtra_Fecha_Min)
    fecha_max = django_filters.CharFilter(action=filtra_Fecha_Max)

    class Meta:
        model = FacturaProveedor
        fields = [
            'empresa__clave',
            'fecha_min',
            'fecha_max',
            'emisor_rfc',
            'emisor_nombre',
            'receptor_rfc',
            'receptor_nombre',
            'uuid',
            'estadoSat',
            'folio',
            'serie',
            'fechaTimbrado_min',
            'fechaTimbrado_max',
            'comprobacion',
            'tiene_pdf',
        ]


class FacturaClienteFilter(filters.FilterSet):

    uuid = django_filters.CharFilter(name="uuid", lookup_expr="contains")

    emisor_rfc = django_filters.CharFilter(
        name="emisor_rfc", lookup_expr="contains")

    emisor_nombre = django_filters.CharFilter(
        name="emisor_nombre", lookup_expr="contains")

    receptor_rfc = django_filters.CharFilter(
        name="receptor_rfc", lookup_expr="contains")
    receptor_nombre = django_filters.CharFilter(
        name="receptor_nombre", lookup_expr="contains")

    fechaTimbrado_min = django_filters.CharFilter(
        action=filtra_FechaTimbrado_Min)
    fechaTimbrado_max = django_filters.CharFilter(
        action=filtra_FechaTimbrado_Max)

    comprobacion = django_filters.CharFilter(
        name="comprobacion", lookup_expr="contains")

    fecha_min = django_filters.CharFilter(action=filtra_Fecha_Min)
    fecha_max = django_filters.CharFilter(action=filtra_Fecha_Max)

    class Meta:
        model = FacturaCliente
        fields = [
            'empresa__clave',
            'fecha_min',
            'fecha_max',
            'emisor_rfc',
            'emisor_nombre',
            'receptor_rfc',
            'receptor_nombre',
            'uuid',
            'estadoSat',
            'folio',
            'serie',
            'fechaTimbrado_min',
            'fechaTimbrado_max',
            'comprobacion',
            'tiene_pdf',
        ]


class ComprobanteEmpleadoFilter(filters.FilterSet):

    uuid = django_filters.CharFilter(name="uuid", lookup_expr="contains")

    emisor_rfc = django_filters.CharFilter(
        name="emisor_rfc", lookup_expr="contains")

    emisor_nombre = django_filters.CharFilter(
        name="emisor_nombre", lookup_expr="contains")

    receptor_rfc = django_filters.CharFilter(
        name="receptor_rfc", lookup_expr="contains")
    receptor_nombre = django_filters.CharFilter(
        name="receptor_nombre", lookup_expr="contains")

    fechaTimbrado_min = django_filters.CharFilter(
        action=filtra_FechaTimbrado_Min)
    fechaTimbrado_max = django_filters.CharFilter(
        action=filtra_FechaTimbrado_Max)

    comprobacion = django_filters.CharFilter(
        name="comprobacion", lookup_expr="contains")

    fecha_min = django_filters.CharFilter(action=filtra_Fecha_Min)
    fecha_max = django_filters.CharFilter(action=filtra_Fecha_Max)

    class Meta:
        model = ComprobanteEmpleado
        fields = [
            'empresa__clave',
            'fecha_min',
            'fecha_max',
            'emisor_rfc',
            'emisor_nombre',
            'receptor_rfc',
            'receptor_nombre',
            'uuid',
            'estadoSat',
            'folio',
            'serie',
            'fechaTimbrado_min',
            'fechaTimbrado_max',
            'comprobacion',
            'tiene_pdf',
        ]


class ResumenFilter(filters.FilterSet):

    fecha_min = django_filters.CharFilter(action=filtra_Resumen_Fecha_Min)
    fecha_max = django_filters.CharFilter(action=filtra_Resumen_Fecha_Max)

    class Meta:
        model = Resumen
        fields = [
            'empresa__clave',
            'fecha_min',
            'fecha_max',
            'tipo',
        ]
