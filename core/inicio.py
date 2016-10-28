# -*- coding: utf-8 -*-

# Librerias Python:
import os

# Librerias Propias:
from tecnology import Cfdineitor


if __name__ == '__main__':
    run_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    app = Cfdineitor("PRODUCCION", run_path)
    # app.get_Invoices_AllCompanies()
    app.get_Invoices_Company("LSV")
