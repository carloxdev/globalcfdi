# -*- coding: utf-8 -*-

# Librerias django:
from django import forms

# Modelos de otras APPS:
from configuracion.models import Empresa
from facturas.models import COMPROBACION_ESTADOS
from facturas.models import LOG_ESTADOS
from facturas.models import LOG_OPERACION_TIPO
from facturas.models import RESUMEN_TIPOS

ESTADOSAT_OPCIONES = (
    ('', 'Todos'),
    ('Cancelado', 'Cancelado'),
    ('Sin Validar', 'Sin Validar'),
    ('Vigente', 'Vigente'),
)


class LogFormFiltros(forms.Form):
    empresa = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    fecha_operacion_inicio = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    fecha_operacion_final = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    estado = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    operacion = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    def __init__(self, _usuario, *args, **kwargs):
        super(LogFormFiltros, self).__init__(*args, **kwargs)
        self.fields['empresa'].choices = self.obtener_Empresas(_usuario)
        self.fields['estado'].choices = self.obtener_LogEstados(
            LOG_ESTADOS)
        self.fields['operacion'].choices = self.obtener_LogOperacionTipos(
            LOG_OPERACION_TIPO)

    def obtener_Empresas(self, _usuario):

        empresa = [('', 'Todas'), ]

        registros = Empresa.objects.filter(usuario=_usuario)

        for registro in registros:
            empresa.append(
                (registro.clave, registro.razon_social)
            )

        return empresa

    def obtener_LogEstados(self, _opciones):

        opciones = [('', 'Todos'), ]

        for registro in _opciones:
            opciones.append(
                registro
            )

        return opciones

    def obtener_LogOperacionTipos(self, _opciones):

        opciones = [('', 'Todos'), ]

        for registro in _opciones:
            opciones.append(
                registro
            )

        return opciones


class FacturaProveedorFormFiltros(forms.Form):

    empresa = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    folio = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    serie = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    uuid = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    emisor_rfc = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    emisor_nombre = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    fecha_timbrado_inicio = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    fecha_timbrado_final = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    fecha_inicio = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    fecha_final = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    estadoSat = forms.ChoiceField(
        choices=ESTADOSAT_OPCIONES,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    comprobacion = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    def __init__(self, _usuario, *args, **kwargs):
        super(FacturaProveedorFormFiltros, self).__init__(*args, **kwargs)
        self.fields['empresa'].choices = self.obtener_Empresas(_usuario)
        self.fields['comprobacion'].choices = self.obtener_Comprobaciones(
            COMPROBACION_ESTADOS)

    def obtener_Empresas(self, _usuario):

        empresa = []

        registros = Empresa.objects.filter(usuario=_usuario)

        for registro in registros:
            empresa.append(
                (registro.clave, registro.razon_social)
            )

        return empresa

    def obtener_Comprobaciones(self, _opciones):

        opciones = [('', 'Todas'), ]

        for registro in _opciones:
            opciones.append(
                registro
            )

        return opciones


class ObtenerForm(forms.Form):

    empresa = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    fecha_inicio = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    fecha_final = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('username')
        super(ObtenerForm, self).__init__(*args, **kwargs)
        self.fields['empresa'].choices = self.obtener_Empresas(self.usuario)

    def obtener_Empresas(self, _usuario):

        empresa = [('', 'Todas'), ]

        registros = Empresa.objects.filter(usuario=_usuario)

        for registro in registros:
            empresa.append(
                (registro.clave, registro.razon_social)
            )

        return empresa


class ResumenFormFiltros(forms.Form):

    empresa = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    fecha_inicio = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    fecha_final = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    tipo = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    def __init__(self, _usuario, *args, **kwargs):
        super(ResumenFormFiltros, self).__init__(*args, **kwargs)
        self.fields['empresa'].choices = self.obtener_Empresas(_usuario)
        self.fields['tipo'].choices = self.obtener_ResumenTipos(
            RESUMEN_TIPOS
        )

    def obtener_Empresas(self, _usuario):

        empresa = []

        registros = Empresa.objects.filter(usuario=_usuario)

        for registro in registros:
            empresa.append(
                (registro.clave, registro.razon_social)
            )

        return empresa

    def obtener_ResumenTipos(self, _tipos):

        opciones = [('', 'Todos'), ]

        for tipo in _tipos:
            opciones.append(
                tipo
            )

        return opciones
