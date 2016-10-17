# -*- coding: utf-8 -*-

from tools.datos import FileManager
from tools.datos import Archivo

directorio_entrada = '/Users/Carlos/Downloads/Pendientes_error'
directorio_busqueda = '/Users/Carlos/Files/Trabajo/Nuvoil/Proyectos/Nuve/Sitio/media/monitor/procesadas'

lista_archivos = FileManager.get_Files(directorio_entrada, '.pdf')

for archivo in lista_archivos:

    achivo_buscar = Archivo(
        archivo.basepath,
        archivo.nombre.replace('.pdf', '.xml').replace('.PDF', '.XML')
    )
    archivos_encontrados = FileManager.find_File(
        achivo_buscar, directorio_busqueda)

    if len(archivos_encontrados) > 0:
        print "Archivo {}: {} Encontrados".format(archivo.nombre, len(archivos_encontrados))
        archivos_encontrados[0].copy(directorio_entrada)
        print "Se copio archivo"

    # print "Archivo {}: {} Encontrados".format(archivo.nombre,
    # len(archivos_encontrados))
