# -*- coding: utf-8 -*-

# Python's Libraries:
import os


def get_FilePath(_instance, _filename):

    upload_dir = os.path.join(
        _instance.empresa.clave,
        _instance.__class__.__name__,
        _instance.fecha.strftime('%Y'),
        _instance.fecha.strftime('%m'),
        _instance.fecha.strftime('%d'),
        _instance.receptor_rfc
    )

    return os.path.join(upload_dir, _filename)
