
var card_filtros = null;
var card_resultados = null;
var url_dominio = window.location.protocol + '//' + window.location.host + '/'

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    // card_filtros = new TargetaFiltros();
    card_resultados = new TargetaResultados();

    alertify.set('notifier', 'position', 'top-right');
    alertify.set('notifier', 'delay', 10);
});



/*-----------------------------------------------*\
            OBJETO: TargetaResultados
\*-----------------------------------------------*/

function TargetaResultados() {

    this.$divGrid = $('#resultados');
    this.kFields = null;
    this.kFuenteDatos = null;    
    this.kRows = null;
    this.kColumns = null;
    this.kGrid = null;

    this.Init();
}
TargetaResultados.prototype.Init = function () {

    this.kFields = {
        serie: { editable: false, type: "string" },
        folio: { editable: false, type: "string" },
        fecha: { editable: false, type: "string" },
        formaDePago: { editable: false, type: "string" },
        noCertificado: { editable: false, type: "string" },
        subTotal: { editable: false, type: "string" },
        tipoCambio: { editable: false, type: "string" },
        moneda: { editable: false, type: "string" },
        sello: { editable: false, type: "string" },
        total: { editable: false, type: "string" },
        tipoDeComprobante: { editable: false, type: "string" },
        metodoDePago: { editable: false, type: "string" },
        lugarExpedicion: { editable: false, type: "string" },
        numCtaPago: { editable: false, type: "string" },
        condicionesDePago: { editable: false, type: "string" },
        emisor_rfc: { editable: false, type: "string" },
        emisor_nombre: { editable: false, type: "string" },
        emisor_calle: { editable: false, type: "string" },
        emisor_noExterior: { editable: false, type: "string" },
        emisor_noInterior: { editable: false, type: "string" },
        emisor_colonia: { editable: false, type: "string" },
        emisor_localidad: { editable: false, type: "string" },
        emisor_municipio: { editable: false, type: "string" },
        emisor_estado: { editable: false, type: "string" },
        emisor_pais: { editable: false, type: "string" },
        emisor_codigoPostal: { editable: false, type: "string" },
        emisor_expedidoEn_calle: { editable: false, type: "string" },
        emisor_expedidoEn_noExterior: { editable: false, type: "string" },
        emisor_expedidoEn_noInterior: { editable: false, type: "string" },
        emisor_expedidoEn_colonia: { editable: false, type: "string" },
        emisor_expedidoEn_municipio: { editable: false, type: "string" },
        emisor_expedidoEn_estado: { editable: false, type: "string" },
        emisor_expedidoEn_pais: { editable: false, type: "string" },
        emisor_regimen: { editable: false, type: "string" },
        receptor_rfc: { editable: false, type: "string" },
        receptor_nombre: { editable: false, type: "string" },
        receptor_calle: { editable: false, type: "string" },
        receptor_noExterior: { editable: false, type: "string" },
        receptor_noInterior: { editable: false, type: "string" },
        receptor_colonia: { editable: false, type: "string" },
        receptor_localidad: { editable: false, type: "string" },
        receptor_municipio: { editable: false, type: "string" },
        receptor_estado: { editable: false, type: "string" },
        receptor_pais: { editable: false, type: "string" },
        receptor_codigoPostal: { editable: false, type: "string" },
        conceptos: { editable: false, type: "string" },
        totalImpuestosTrasladados: { editable: false, type: "string" },
        totalImpuestosRetenidos: { editable: false, type: "string" },
        impuestos_trasladados: { editable: false, type: "string" },
        impuestos_retenidos: { editable: false, type: "string" },
        uuid: { editable: false, type: "string" },
        fechaTimbrado: { editable: false, type: "string" },
        noCertificadoSAT: { editable: false, type: "string" },
        selloSAT: { editable: false, type: "string" },
        empresa: { editable: false, type: "string" },
        comentarios: { editable: false, type: "string" },
        comprobacion: { editable: false, type: "string" },
        url: { editable: false, type: "string" },
        tiene_pdf: { editable: false, type: "string" },
        estadoSat: { editable: false, type: "string" },
        registroPatronal: { editable: false, type: "string" },
        numEmpleado: { editable: false, type: "string" },
        curp: { editable: false, type: "string" },
        tipoRegimen: { editable: false, type: "string" },
        numSeguridadSocial: { editable: false, type: "string" },
        fechaPago: { editable: false, type: "string" },
        fechaInicialPago: { editable: false, type: "string" },
        fechaFinalPago: { editable: false, type: "string" },
        numDiasPagados: { editable: false, type: "string" },
        clabe: { editable: false, type: "string" },
        banco: { editable: false, type: "string" },
        fechaInicioRelLaboral: { editable: false, type: "string" },
        antiguedad: { editable: false, type: "string" },
        puesto: { editable: false, type: "string" },
        tipoJornada: { editable: false, type: "string" },
        periodicidadPago: { editable: false, type: "string" },
        riesgoPuesto: { editable: false, type: "string" },
        salarioDiarioIntegrado: { editable: false, type: "string" },
        percepciones_totalGravado: { editable: false, type: "string" },
        percepciones_totalExento: { editable: false, type: "string" },
        percepciones: { editable: false, type: "string" },
        deducciones_totalGravado: { editable: false, type: "string" },
        deducciones_totalExento: { editable: false, type: "string" },
        deducciones: { editable: false, type: "string" },
        horasExtras: { editable: false, type: "string" },
    }

    this.kFuenteDatos = new kendo.data.DataSource({

        // serverFiltering: true,
        serverPaging: true,
        pageSize: 10,
        transport: {
            read: {

                url: url_dominio + "api/comprobantes_empleado/",
                type: "GET",
                dataType: "json",
            },
            // parameterMap: function (data, action) {
            //     if (action === "read") {

            //         return {
            //             page: data.page,
            //             pageSize: data.pageSize,
            //             empresa__clave: cardFiltros.$empresa.val(),
            //             min_fecha: cardFiltros.$fechaInicio.val(),
            //             max_fecha: cardFiltros.$fechaFin.val(),
            //             emisor_rfc: cardFiltros.$emisor_rfc.val(),
            //             emisor_nombre: cardFiltros.$emisor_nombre.val(),
            //             uuid: cardFiltros.$uuid.val(),
            //             folio : cardFiltros.$folio.val(),
            //             estado: cardFiltros.$estado.val(),
            //             comprobacion: cardFiltros.$comprobacion.val(),
            //             pdf_save: cardFiltros.$pdf.val()
            //         };
            //     }
            // }
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                id: "uuid",
                fields: this.kfields
            }
        },
        error: function (e) {
			alertify.notify("Status: " + e.status + "; Error message: " + e.errorThrown);
        },
    });

    this.kColumns = [
		{ field: "uuid", title: "uuid", width: "200px" },
		{ field: "estadoSat", title: "estadoSat", width: "200px" },
		{ field: "comprobacion", title: "comprobacion", width: "200px" },		
		{ field: "serie", title: "serie", width: "200px" },
		{ field: "folio", title: "folio", width: "200px" },
		{ field: "fecha", title: "fecha", width: "200px" },
		{ field: "formaDePago", title: "formaDePago", width: "200px" },
		{ field: "subTotal", title: "subTotal", width: "200px" },
		{ field: "tipoCambio", title: "tipoCambio", width: "200px" },
		{ field: "moneda", title: "moneda", width: "200px" },
		{ field: "total", title: "total", width: "200px" },
		{ field: "tipoDeComprobante", title: "tipoDeComprobante", width: "200px" },
		{ field: "metodoDePago", title: "metodoDePago", width: "200px" },
		{ field: "lugarExpedicion", title: "lugarExpedicion", width: "200px" },
		{ field: "numCtaPago", title: "numCtaPago", width: "200px" },
		{ field: "condicionesDePago", title: "condicionesDePago", width: "200px" },
		{ field: "emisor_rfc", title: "emisor_rfc", width: "200px" },
		{ field: "emisor_nombre", title: "emisor_nombre", width: "200px" },
		{ field: "emisor_calle", title: "emisor_calle", width: "200px" },
		{ field: "emisor_noExterior", title: "emisor_noExterior", width: "200px" },
		{ field: "emisor_noInterior", title: "emisor_noInterior", width: "200px" },
		{ field: "emisor_colonia", title: "emisor_colonia", width: "200px" },
		{ field: "emisor_localidad", title: "emisor_localidad", width: "200px" },
		{ field: "emisor_municipio", title: "emisor_municipio", width: "200px" },
		{ field: "emisor_estado", title: "emisor_estado", width: "200px" },
		{ field: "emisor_pais", title: "emisor_pais", width: "200px" },
		{ field: "emisor_codigoPostal", title: "emisor_codigoPostal", width: "200px" },
		{ field: "emisor_expedidoEn_calle", title: "emisor_expedidoEn_calle", width: "200px" },
		{ field: "emisor_expedidoEn_noExterior", title: "emisor_expedidoEn_noExterior", width: "200px" },
		{ field: "emisor_expedidoEn_noInterior", title: "emisor_expedidoEn_noInterior", width: "200px" },
		{ field: "emisor_expedidoEn_colonia", title: "emisor_expedidoEn_colonia", width: "200px" },
		{ field: "emisor_expedidoEn_municipio", title: "emisor_expedidoEn_municipio", width: "200px" },
		{ field: "emisor_expedidoEn_estado", title: "emisor_expedidoEn_estado", width: "200px" },
		{ field: "emisor_expedidoEn_pais", title: "emisor_expedidoEn_pais", width: "200px" },
		{ field: "emisor_regimen", title: "emisor_regimen", width: "200px" },
		{ field: "receptor_rfc", title: "receptor_rfc", width: "200px" },
		{ field: "receptor_nombre", title: "receptor_nombre", width: "200px" },
		{ field: "receptor_calle", title: "receptor_calle", width: "200px" },
		{ field: "receptor_noExterior", title: "receptor_noExterior", width: "200px" },
		{ field: "receptor_noInterior", title: "receptor_noInterior", width: "200px" },
		{ field: "receptor_colonia", title: "receptor_colonia", width: "200px" },
		{ field: "receptor_localidad", title: "receptor_localidad", width: "200px" },
		{ field: "receptor_municipio", title: "receptor_municipio", width: "200px" },
		{ field: "receptor_estado", title: "receptor_estado", width: "200px" },
		{ field: "receptor_pais", title: "receptor_pais", width: "200px" },
		{ field: "receptor_codigoPostal", title: "receptor_codigoPostal", width: "200px" },
		{ field: "totalImpuestosTrasladados", title: "totalImpuestosTrasladados", width: "200px" },
		{ field: "totalImpuestosRetenidos", title: "totalImpuestosRetenidos", width: "200px" },
		{ field: "fechaTimbrado", title: "fechaTimbrado", width: "200px" },
		{ field: "empresa", title: "empresa", width: "200px" },
        { field: "registroPatronal", title: "registroPatronal", width: "200px" },
        { field: "numEmpleado", title: "numEmpleado", width: "200px" },
        { field: "curp", title: "curp", width: "200px" },
        { field: "tipoRegimen", title: "tipoRegimen", width: "200px" },
        { field: "numSeguridadSocial", title: "numSeguridadSocial", width: "200px" },
        { field: "fechaPago", title: "fechaPago", width: "200px" },
        { field: "fechaInicialPago", title: "fechaInicialPago", width: "200px" },
        { field: "fechaFinalPago", title: "fechaFinalPago", width: "200px" },
        { field: "numDiasPagados", title: "numDiasPagados", width: "200px" },
        { field: "clabe", title: "clabe", width: "200px" },
        { field: "banco", title: "banco", width: "200px" },
        { field: "fechaInicioRelLaboral", title: "fechaInicioRelLaboral", width: "200px" },
        { field: "antiguedad", title: "antiguedad", width: "200px" },
        { field: "puesto", title: "puesto", width: "200px" },
        { field: "tipoJornada", title: "tipoJornada", width: "200px" },
        { field: "periodicidadPago", title: "periodicidadPago", width: "200px" },
        { field: "riesgoPuesto", title: "riesgoPuesto", width: "200px" },
        { field: "salarioDiarioIntegrado", title: "salarioDiarioIntegrado", width: "200px" },
        { field: "percepciones_totalGravado", title: "percepciones_totalGravado", width: "200px" },
        { field: "percepciones_totalExento", title: "percepciones_totalExento", width: "200px" },
        { field: "percepciones", title: "percepciones", width: "200px" },
        { field: "deducciones_totalGravado", title: "deducciones_totalGravado", width: "200px" },
        { field: "deducciones_totalExento", title: "deducciones_totalExento", width: "200px" },
        { field: "deducciones", title: "deducciones", width: "200px" },
        { field: "horasExtras", title: "horasExtras", width: "200px" },
        { field: "comentarios", title: "comentarios", width: "200px" },
        { field: "tiene_pdf", title: "tiene_pdf", width: "200px" },
		{ field: "url", title: "url", width: "200px" },
		
           // {
           //     command: {
           //         text: "Archivo XML",
           //         click: this.Click_DescargarArchivoXML
           //     },
           //     title: " ",
           //     width: "160px"
           // },
           // {
           //     command: {
           //         text: "Archivo PDF",
           //         click: this.Click_DescargarArchivoPDF
           //     },
           //     title: " ",
           //     width: "160px"
           // },
           // {
	          //  command: {
	          //      text: "Validar",
	          //      click: this.Click_BotonValidar
	          //  },
	          //  title: " ",
	          //  width: "160px"
           //  },
    ]

    this.kGrid = this.$divGrid.kendoGrid({
        dataSource: this.kFuenteDatos,
        columnMenu: true,
        groupable: false,
        sortable: true,
        pageable: true,
        selectable: true,
        editable: "inline",
        scrollable: true,
        columns: this.kColumns,
        dataBound: this.FillGrid
    });

}
TargetaResultados.prototype.Buscar = function (e) {

    this.kFuenteDatos.page(1);
}


