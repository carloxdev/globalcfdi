# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError


def validate_cert(_value):
    if (not _value.name.endswith('.cer') and
            not _value.name.endswith('.CER')):

        raise ValidationError("Archivos permitidos: .cer y .CER")


def validate_key(_value):
    if (not _value.name.endswith('.key') and
            not _value.name.endswith('.KEY')):

        raise ValidationError("Archivos permitidos: .key y .KEY")


def validate_size(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Tamaño Máximo de Archivo {}MB".format(str(megabyte_limit)))
