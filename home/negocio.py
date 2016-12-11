from facturas.models import Resumen


class EmpresaResumen(object):

    def __init__(self, _empresa,):
        self.empresa = _empresa

        self.nomina_cantidad = 0
        self.nomina_total = 0
        self.clientes_cantidad = 0
        self.clientes_total = 0
        self.proveedores_cantidad = 0
        self.proveedores_total = 0

    def get_Nomina_Resumen(self):

        nomina_resumen = Resumen.objects.filter(
            empresa=self.empresa,
            tipo="EMPLEADOS"
        )
        for resumen in nomina_resumen:
            self.nomina_cantidad += resumen.cantidad_guardadas
            self.nomina_total += resumen.total

    def get_Clientes_Resumen(self):

        clientes_resumen = Resumen.objects.filter(
            empresa=self.empresa,
            tipo="CLIENTES"
        )
        for resumen in clientes_resumen:
            self.clientes_cantidad += resumen.cantidad_guardadas
            self.clientes_total += resumen.total

    def get_Proveedores_Resumen(self):

        proveedores_resumen = Resumen.objects.filter(
            empresa=self.empresa,
            tipo="PROVEEDORES"
        )
        for resumen in proveedores_resumen:
            self.proveedores_cantidad += resumen.cantidad_guardadas
            self.proveedores_total += resumen.total
