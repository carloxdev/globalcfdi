# from facturas.models import Resumen
from facturas.models import FacturaProveedor
from facturas.models import FacturaCliente
from facturas.models import ComprobanteEmpleado
from facturas.models import MONEDA_PESOS


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

        # nomina_resumen = Resumen.objects.filter(
        #     empresa=self.empresa,
        #     tipo="EMPLEADOS"
        # )

        # for resumen in nomina_resumen:
        #     self.nomina_cantidad += resumen.cantidad_guardadas
        #     self.nomina_total += resumen.total

        facturas = ComprobanteEmpleado.objects.filter(
            empresa=self.empresa,
            fecha__range=["2016-01-01", "2016-12-31"],
            estadoSat="Vigente"
        )

        for factura in facturas:
            self.nomina_cantidad += 1

            if MONEDA_PESOS.count(factura.moneda) > 0:
                self.nomina_total += factura.total
            else:
                self.nomina_total += factura.total * factura.tipoCambio

    def get_Clientes_Resumen(self):

        facturas = FacturaCliente.objects.filter(
            empresa=self.empresa,
            fecha__range=["2016-01-01", "2016-12-31"],
            estadoSat="Vigente"
        )

        for factura in facturas:
            self.clientes_cantidad += 1

            if MONEDA_PESOS.count(factura.moneda) > 0:
                self.clientes_total += factura.total
            else:
                self.clientes_total += factura.total * factura.tipoCambio

        # clientes_resumen = Resumen.objects.filter(
        #     empresa=self.empresa,
        #     tipo="CLIENTES"
        # )
        # for resumen in clientes_resumen:
        #     self.clientes_cantidad += resumen.cantidad_guardadas
        #     self.clientes_total += resumen.total

    def get_Proveedores_Resumen(self):

        facturas = FacturaProveedor.objects.filter(
            empresa=self.empresa,
            fecha__range=["2016-01-01", "2016-12-31"],
            estadoSat="Vigente"
        )

        for factura in facturas:
            self.proveedores_cantidad += 1

            if MONEDA_PESOS.count(factura.moneda) > 0:
                self.proveedores_total += factura.total
            else:
                self.proveedores_total += factura.total * factura.tipoCambio

        # proveedores_resumen = Resumen.objects.filter(
        #     empresa=self.empresa,
        #     tipo="PROVEEDORES"
        # )
        # for resumen in proveedores_resumen:
        #     self.proveedores_cantidad += resumen.cantidad_guardadas
        #     self.proveedores_total += resumen.total
