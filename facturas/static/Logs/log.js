
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
        empresa: { editable: false, type: "string" },
        nombre: { editable: false, type: "string" },
        estado: { editable: false, type: "string" },
        operacion: { editable: false, type: "string" },
        fecha_operacion: { editable: false, type: "string" },
        descripcion: { editable: false, type: "string" },
        url: { editable: false, type: "string" },
        created_date: { editable: false, type: "string" },
        updated_date: { editable: false, type: "string" },
    }

    this.kFuenteDatos = new kendo.data.DataSource({

        // serverFiltering: true,
        serverPaging: true,
        pageSize: 10,
        transport: {
            read: {

                url: url_dominio + "api/logs/",
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
                fields: this.kFields
            }
        },
        error: function (e) {
			alertify.notify("Status: " + e.status + "; Error message: " + e.errorThrown);
        },
    });

    this.kColumns = [
        { field: "empresa", title: "empresa", width: "200px" },
        { field: "nombre", title: "nombre", width: "200px" },
        { field: "estado", title: "estado", width: "200px" },
        { field: "operacion", title: "operacion", width: "200px" },
        { field: "fecha_operacion", title: "fecha_operacion", width: "200px" },
        { field: "descripcion", title: "descripcion", width: "200px" },
        { field: "url", title: "url", width: "200px" },
        { field: "created_date", title: "created_date", width: "200px" },
        { field: "updated_date", title: "updated_date", width: "200px" },

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
    });

}
TargetaResultados.prototype.Buscar = function (e) {

    this.kFuenteDatos.page(1);
}


