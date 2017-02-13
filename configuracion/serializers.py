# -*- coding: utf-8 -*-

# Librerias API REST:
from rest_framework import serializers

# Modelos:
from .models import Empresa


class EmpresaSerializer(serializers.HyperlinkedModelSerializer):

    usuario = serializers.SerializerMethodField()

    class Meta:
        model = Empresa
        fields = (
            'pk',
            'clave',
            'razon_social',
            'logo',
            'rfc',
            'ciec',
            'activa',
            'usuario',
            'email',
            'certificado',
            'llave',
            'contrasena',
            'created_date',
            'updated_date',
        )

    def get_usuario(self, obj):

        try:
            return obj.usuario.username
        except:
            return ""
