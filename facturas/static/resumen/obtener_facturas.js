/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/


// URLS:
var url = window.location
var url_grid = ""
var url_archivos = ""

if (url.pathname.search("smart") > 0) {
    url_grid = url.origin +  "/smart/api/logs/"
    url_archivos = url.origin + "/smart/media/"
}
else {

    url_grid = url.origin +  "/api/logs/"
    url_archivos = url.origin + "/media/"
}

var fecha_busqueda = ""


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

    moment.locale('es')
});

$(window).resize(function() {

    card_resultados.grid.kgrid.data("kendoGrid").resize()
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
        fecha_operacion_min: this.$fecha_inicio.val(),
        fecha_operacion_max: this.$fecha_fin.val(),
        created_date_min: this.get_FechaCreacion_Min(),
        // created_date_max: this.get_FechaCreacion_Max(),
    }    
}
TargetaFiltros.prototype.get_FechaCreacion_Min = function () {

    if (fecha_busqueda == "") {
        fecha_busqueda = String(moment().format('YYYY-MM-DDTHH:mm:') + "00")
    }

    return fecha_busqueda
    // return "2016-08-12:12:45:00"
}
TargetaFiltros.prototype.get_FechaCreacion_Max = function () {

    var fecha = String(moment().add(3,'m').format('YYYY-MM-DDTHH:mm:ss'))
    return fecha
}

/*-----------------------------------------------*\
            OBJETO: TargetaResultados
\*-----------------------------------------------*/

function TargetaResultados() {

    this.$bandera = $('#id_bandera')

    this.grid = new GridPrincipal()

    this.Load()
}
TargetaResultados.prototype.Load = function () {

    if (this.$bandera.text() == "INICIO_PROCESO") {
        this.grid.kgrid.data("kendoGrid").resize()
        this.grid.buscar()

        setInterval(function () {

            card_resultados.grid.buscar()

        }, 1000)
    }
}


/*-----------------------------------------------*\
            OBJETO: GRID
\*-----------------------------------------------*/

function GridPrincipal() {

    this.$id = $("#resultados")
    this.kfuente_datos = null
    this.kgrid = null

    this.init()
}
GridPrincipal.prototype.init = function () {

    kendo.culture("es-MX")

    this.kfuente_datos = new kendo.data.DataSource(this.get_FuenteDatosConfig())

    this.kgrid = this.$id.kendoGrid(this.get_Config())
}
GridPrincipal.prototype.get_Config = function () {
    return {
        dataSource: this.kfuente_datos,
        columnMenu: false,
        groupable: false,
        sortable: false,
        editable: false,
        resizable: true,
        autoBind: false, 
        selectable: true,
        scrollable: false,
        columns: this.get_Columnas(),
        dataBound: this.llenar_Grid,
        scrollable: true,
        pageable: {
            refresh: true,            
        },
        noRecords: {
            template: "<div class='grid-empy'> No se encontraron registros </div>"
        },        
    }
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

                url: url_grid,
                type: "GET",
                dataType: "json",
            },
            parameterMap: function (data, action) {
                if (action === "read") {

                    return card_filtros.get_Filtros(data.page, data.pageSize)
                }
            }
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                fields: this.get_Campos()
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
GridPrincipal.prototype.buscar = function (e) {
    
    this.kfuente_datos.page(1)   
    this.kgrid.data('kendoGrid').refresh()
}
GridPrincipal.prototype.descargar_Log = function (e) {
    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    var url = url_archivos + fila.url
    var win = window.open(url, '_blank')
    win.focus()
}
GridPrincipal.prototype.llenar_Grid = function (e) {

    e.preventDefault()

    $('td').each( function () {
        if($(this).text()=='EXITO'){ 

            $(this).addClass('cell--exito')
        }
        else if($(this).text()=='DETALLES'){ 
            $(this).addClass('cell--detalle')
        }
        else if($(this).text()=='ERROR'){ 
            $(this).addClass('cell--error')
        }
        else if($(this).text()=='PROCESANDO'){
            $(this).addClass('cell--procesando')
        } 
    })
}
