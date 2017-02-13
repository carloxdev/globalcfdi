# -*- coding: utf-8 -*-

import os


def get_FilePath(_instance, _filename):
    upload_dir = os.path.join(
        'empresas',
        _instance.clave,
        'certificados',
    )

    return os.path.join(upload_dir, _filename)
