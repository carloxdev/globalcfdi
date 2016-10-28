# -*- coding: utf-8 -*-

# Librerias API Rest
from rest_framework.pagination import PageNumberPagination


class GenericPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class FacturaProveedorPaginacion(GenericPagination):
    pass


class FacturaClientePaginacion(GenericPagination):
    pass


class ComprobanteEmpleadoPaginacion(GenericPagination):
    pass


class LogPaginacion(GenericPagination):
    pass
