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
            'clave',
            'razon_social',
            'logo',
            'rfc',
            'ciec',
            'activa',
            'usuario',
            'email',
            'created_date',
            'updated_date',
        )

    def get_usuario(self, obj):

        try:
            return obj.usuario.username
        except:
            return ""
