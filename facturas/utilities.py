# -*- coding: utf-8 -*-

# Python's Libraries:
import os


def get_FilePath(_instance, _filename):

    if _instance.__class__.__name__ == "ComprobanteProveedor":

        upload_dir = os.path.join(
            "comprobantes",
            _instance.empresa.clave,
            _instance.__class__.__name__,
            _instance.fecha.strftime('%Y'),
            _instance.fecha.strftime('%m'),
            _instance.fecha.strftime('%d'),
            _instance.emisor_rfc
        )

    elif _instance.__class__.__name__ == "ComprobanteCliente":

        upload_dir = os.path.join(
            "comprobantes",
            _instance.empresa.clave,
            _instance.__class__.__name__,
            _instance.fecha.strftime('%Y'),
            _instance.fecha.strftime('%m'),
            _instance.fecha.strftime('%d'),
            _instance.receptor_rfc
        )

    else:
        # ComprobanteEmpleado
        upload_dir = os.path.join(
            "comprobantes",
            _instance.empresa.clave,
            _instance.__class__.__name__,
            _instance.fecha.strftime('%Y'),
            _instance.fecha.strftime('%m'),
            _instance.fecha.strftime('%d'),
            _instance.receptor_rfc
        )

    return os.path.join(upload_dir, _filename)
