
var card_filtros = null
var card_resultados = null
var url = window.location
var url_grid = ""

if (url.pathname.search("smart") > 0) {
    url_grid = url.origin + "/smart/api/resumenes/"
}
else {
    url_grid = url.origin + "/api/resumenes/"
}

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    card_filtros = new TargetaFiltros()
    card_resultados = new TargetaResultados()

    alertify.set('notifier', 'position', 'top-right')
    alertify.set('notifier', 'delay', 10)
})


/*-----------------------------------------------*\
            OBJETO: TargetaFiltros
\*-----------------------------------------------*/

function TargetaFiltros() {

    this.$empresa = $('#id_empresa')

    this.$tipo = $("#id_tipo")
    this.$fecha_inicio = $('#id_fecha_inicio')
    this.$fecha_fin = $('#id_fecha_final')

    // Botones
    this.$boton_buscar = $('#id_buscar')
    this.$boton_limpiar = $('#id_limpiar')

    // Iniciamos estilos y funcionalidad
    this.init()
}
TargetaFiltros.prototype.init = function () {

    var datepicker_init = {
        autoSize: true,
        dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
        dayNamesMin: ['Dom', 'Lu', 'Ma', 'Mi', 'Je', 'Vi', 'Sa'],
        firstDay: 1,
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        monthNamesShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
        dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true,
    }

    this.$fecha_inicio.datepicker(datepicker_init)
    this.$fecha_fin.datepicker(datepicker_init)

    // Botones
    this.$boton_buscar.on('click', this, this.click_BotonBuscar)
    this.$boton_limpiar.on('click', this, this.click_BotonLimpiar)
}
TargetaFiltros.prototype.click_BotonBuscar = function (e) {

    e.preventDefault( )
    card_resultados.buscar()
}
TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

    e.preventDefault()

    e.data.$empresa.val("")
    e.data.$tipo.val("")
    e.data.$fecha_inicio.val("")
    e.data.$fecha_fin.val("")

}
TargetaFiltros.prototype.validar_Filtros = function () {
    bandera = false;

    if ((this.$empresa.val() != "") ||
        (this.$fecha_inicio.val() != "") ||
        (this.$fecha_fin.val() != "")) {
        bandera = true
    }

    return bandera;
}



/*-----------------------------------------------*\
            OBJETO: TargetaResultados
\*-----------------------------------------------*/

function TargetaResultados() {

    this.$divGrid = $('#resultados')
    this.kFields = null
    this.kFuenteDatos = null
    this.kRows = null
    this.kColumns = null
    this.kGrid = null
    this.init()
}
TargetaResultados.prototype.init = function () {

    kendo.culture("es-MX")
    
    this.kFields = {
        fecha: { editable: false, type: "string" },
        tipo: { editable: false, type: "string" },
        cantidad_guardadas: { editable: false, type: "string" },
        cantidad_validadas: { editable: false, type: "string" },
        total: { editable: false, type: "number" },
        empresa: { editable: false, type: "string" },
        created_date: { editable: false, type: "date" },
        updated_date: { editable: false, type: "date" },
    }

    this.kFuenteDatos = new kendo.data.DataSource({

        serverPaging: true,
        pageSize: 10,
        transport: {
            read: {

                url: url_grid,
                type: "GET",
                dataType: "json",
            },
            parameterMap: function (data, action) {
                if (action === "read") {

                    return {
                        page: data.page,
                        pageSize: data.pageSize,
                        empresa__clave: card_filtros.$empresa.val(),
                        fecha_min: card_filtros.$fecha_inicio.val(),
                        fecha_max: card_filtros.$fecha_fin.val(),
                        tipo: card_filtros.$tipo.val(),
                    }
                }
            }
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                fields: this.kFields    
            }
        },
        error: function (e) {
			alertify.notify("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    })

    this.kColumns = [
        { field: "empresa", title: "Empresa", width: "140px" },
        { field: "fecha", title: "Fecha", width: "140px" },
        { field: "tipo", title: "Tipo", width: "140px" },
        { field: "cantidad_guardadas", title: "Cantidad Guardada", width: "140px", attributes:{ style:"text-align:center;" }, },
        { field: "cantidad_validadas", title: "Cantidad Validada", width: "140px", attributes:{ style:"text-align:center;" }, },
        { 
            field: "total", 
            title: "total", 
            width: "140px",
            format: '{0:n}',
            attributes:{ style:"text-align:right;" },            
        },
        { field: "created_date", title: "Creacion", width: "100px", format: "{0:dd-MM-yyyy}", attributes:{ style:"text-align:right;" },},   
        { field: "updated_date", title: "Actulizacion", width: "100px", format: "{0:dd-MM-yyyy}", attributes:{ style:"text-align:right;" },},   
    ]

    this.kGrid = this.$divGrid.kendoGrid({
        dataSource: this.kFuenteDatos,
        columnMenu: true,
        groupable: false,
        sortable: true,
        resizable: true,
        selectable: true,
        editable: false,
        scrollable: true,
        columns: this.kColumns,
        mobile: true,
        pageable: true,
    })
}
TargetaResultados.prototype.buscar = function () {

    this.kFuenteDatos.page(1)
}