/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/


// URLS:
var url = window.location
var url_grid = ""

if (url.pathname.search("smart") > 0) {
    url_grid = url.origin +  "/smart/api/logs/"
}
else {

    url_grid = url.origin +  "/api/logs/"
}


// OBJS:
var card_filtros = null
var card_resultados = null

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    card_filtros = new TargetaFiltros()
    card_resultados = new TargetaResultados()
    pagina = new Pagina()

    pagina.init_Alertify()
});


$(window).resize(function() {

    // card_resultados.grid.kgrid.data("kendoGrid").resize()
})


/*-----------------------------------------------*\
            OBJETO: TargetaFiltros
\*-----------------------------------------------*/

function TargetaFiltros() {

    this.$empresa = $('#id_empresa')
    this.$fecha_inicio = $('#id_fecha_inicio')
    this.$fecha_fin = $('#id_fecha_final')

    // Iniciamos estilos y funcionalidad
    this.init()
}
TargetaFiltros.prototype.init = function () {

    this.$fecha_inicio.datepicker(this.get_DateConfig())
    this.$fecha_fin.datepicker(this.get_DateConfig())
}
TargetaFiltros.prototype.get_DateConfig = function () {

    return {
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
}
TargetaFiltros.prototype.get_Filtros = function (_page, _pageSize) {

    return {
        page: _page,
        pageSize: _pageSize,
        empresa__clave: this.$empresa.val(),
        fecha_operacion_min: this.$fecha_operacion_inicio.val(),
        fecha_operacion_max: this.$fecha_operacion_fin.val(),
        created_date_min: this.get_FechaCreacion()

    }    
}
TargetaFiltros.prototype.get_FechaCreacion = function () {

    return "2016-08-12:12:45:00"

}

/*-----------------------------------------------*\
            OBJETO: TargetaResultados
\*-----------------------------------------------*/

function TargetaResultados() {

    this.$bandera = $('#id_bandera')

    this.Load()
}
TargetaResultados.prototype.Load = function () {

    if (this.$bandera.text() == "INICIO_PROCESO") {
        alertify.notify("Esto ya comenzo")
    }
    else {
        alertify.notify("aun no")   
    }
}


/*-----------------------------------------------*\
            OBJETO: GRID
\*-----------------------------------------------*/

function GridPrincipal() {

    this.$id = $("#grid_principal")
    this.kfuente_datos = null
    this.kgrid = null

    this.init()
}
GridPrincipal.prototype.init = function () {

    kendo.culture("es-MX")

    this.kfuente_datos = new kendo.data.DataSource(this.get_FuenteDatosConfig())

    this.kGrid = this.$id.kendoGrid({
        dataSource: this.kfuente_datos,
        columnMenu: false,
        groupable: false,
        sortable: false,
        editable: false,
        resizable: true,
        selectable: true,
        scrollable: false,
        columns: this.get_Columnas(),
        scrollable: true,
        pageable: true,
        noRecords: {
            template: "<div class='grid-empy'> No se encontraron registros </div>"
        },        
    })
}
GridPrincipal.prototype.get_Campos = function (e) {

    return {
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
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [
        { field: "empresa", title: "Empresa", width: "120px" },
        { field: "nombre", title: "Nombre", width: "250px" },
        { field: "estado", title: "Estado", width: "100px" },
        { field: "operacion", title: "Operacion", width: "100px" },
        { 
            field: "fecha_operacion", 
            title: "Fecha Operacion", 
            width: "130px", 
            template: "#= kendo.toString(kendo.parseDate(fecha_operacion, 'yyyy-MM-dd'), 'dd-MMMM-yyyy') #"
        },
        { field: "descripcion", title: "Descripcion", width: "150px" },
        { 
            field: "created_date", 
            title: "Creado el", 
            width: "120px",
            template: "#= kendo.toString(kendo.parseDate(created_date, 'yyyy-MM-dd'), 'dd-MMMM-yyyy') #"
        },
        { 
            field: "updated_date", 
            title: "Actualizado el", 
            width: "120px",
            template: "#= kendo.toString(kendo.parseDate(updated_date, 'yyyy-MM-dd'), 'dd-MMMM-yyyy') #"
        },
        {
           command: {
               text: "Log",
               click: this.descargar_Log
           },
           title: " ",
           width: "90px"
        },
    ]
}
GridPrincipal.prototype.get_FuenteDatosConfig = function (e) {

    return {

        serverPaging: true,
        pageSize: 20,
        transport: {
            read: {

                url: url_consulta,
                type: "GET",
                dataType: "json",
            },
            parameterMap: function (data, action) {
                if (action === "read") {

                    return targeta_filtros.get_Filtros(data.page, data.pageSize)
                }
            }
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                fields: this.kFields
            },
            sort: {
                field: "created_date", dir: "desc"
            }
        },
        error: function (e) {
            alertify.notify("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    }
}

