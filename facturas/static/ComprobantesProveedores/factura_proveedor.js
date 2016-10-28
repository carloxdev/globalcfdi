
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
    }

    this.kFuenteDatos = new kendo.data.DataSource({

        // serverFiltering: true,
        serverPaging: true,
        pageSize: 10,
        transport: {
            read: {

                url: url_dominio + "api/facturas_proveedor/",
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
        { field: "empresa", title: "empresa", width: "150px" },
        { field: "emisor_rfc", title: "emisor_rfc", width: "200px" },
        { field: "emisor_nombre", title: "emisor_nombre", width: "300px" },    
		{ field: "uuid", title: "uuid", width: "350px" },
        { field: "fecha", title: "fecha", width: "200px" },
        { field: "fechaTimbrado", title: "fechaTimbrado", width: "200px" },		
		{ field: "serie", title: "serie", width: "200px" },
		{ field: "folio", title: "folio", width: "200px" },
		{ field: "estadoSat", title: "estadoSat", width: "200px" },
		{ field: "moneda", title: "moneda", width: "200px" },
        { field: "subTotal", title: "subTotal", width: "200px" },
        { field: "totalImpuestosTrasladados", title: "totalImpuestosTrasladados", width: "200px" },
        { field: "totalImpuestosRetenidos", title: "totalImpuestosRetenidos", width: "200px" },        
        { field: "tipoCambio", title: "tipoCambio", width: "200px" },
		{ field: "total", title: "total", width: "200px" },
		{ field: "tiene_pdf", title: "tiene_pdf", width: "200px" },
		{ field: "url", title: "url", width: "200px" },
        { field: "comprobacion", title: "comprobacion", width: "200px" },
       {
           command: {
               text: "Archivo XML",
               click: this.Click_DescargarArchivoXML
           },
           title: " ",
           width: "160px"
       },
       {
           command: {
               text: "Archivo PDF",
               click: this.Click_DescargarArchivoPDF
           },
           title: " ",
           width: "160px"
       },
       {
           command: {
               text: "Validar",
               click: this.Click_BotonValidar
           },
           title: " ",
           width: "160px"
        },
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
        dataBound: this.FillGrid,
        mobile: true
    });

}
TargetaResultados.prototype.Buscar = function (e) {

    this.kFuenteDatos.page(1);
}


