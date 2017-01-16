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

    def get_Nomina_Resumen(self, _fecha_inicial, _fecha_final):

        facturas = ComprobanteEmpleado.objects.filter(
            empresa=self.empresa,
            fecha__range=[_fecha_inicial, _fecha_final],
            estadoSat="Vigente"
        )

        for factura in facturas:
            self.nomina_cantidad += 1

            if MONEDA_PESOS.count(factura.moneda) > 0:
                self.nomina_total += factura.total
            else:
                self.nomina_total += factura.total * factura.tipoCambio

    def get_Clientes_Resumen(self, _fecha_inicial, _fecha_final):

        facturas = FacturaCliente.objects.filter(
            empresa=self.empresa,
            fecha__range=[_fecha_inicial, _fecha_final],
            estadoSat="Vigente"
        )

        for factura in facturas:
            self.clientes_cantidad += 1

            if MONEDA_PESOS.count(factura.moneda) > 0:
                self.clientes_total += factura.total
            else:
                self.clientes_total += factura.total * factura.tipoCambio

    def get_Proveedores_Resumen(self, _fecha_inicial, _fecha_final):

        facturas = FacturaProveedor.objects.filter(
            empresa=self.empresa,
            fecha__range=[_fecha_inicial, _fecha_final],
            estadoSat="Vigente"
        )

        for factura in facturas:
            self.proveedores_cantidad += 1

            if MONEDA_PESOS.count(factura.moneda) > 0:
                self.proveedores_total += factura.total
            else:
                self.proveedores_total += factura.total * factura.tipoCambio
