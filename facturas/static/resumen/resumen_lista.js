/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// URLS:
var url = window.location
var url_consulta = ""
var url_archivos = ""

if (url.pathname.search("smart") > 0) {
    url_consulta = url.origin + "/smart/api/resumenes/"
    url_archivos = url.origin + "/smart/media/"
}
else {
    url_consulta = url.origin + "/api/resumenes/"
    url_archivos = url.origin + "/media/"
}

// OBJS:
var card_filtros = null
var card_resultados = null
var pagina = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    card_filtros = new TargetaFiltros()
    card_resultados = new TargetaResultados()

    pagina = new Pagina()

    // Inicializar Alertify
    pagina.init_Alertify()

    // Asigna eventos a teclas
    $(document).keypress(function (e) {

        // Tecla Enter
        if (e.which == 13) {
            card_filtros.click_BotonBuscar(e)
        }
    })
})


$(window).resize(function() {

    card_resultados.grid.kgrid.data("kendoGrid").resize()
})


/*-----------------------------------------------*\
            OBJETO: TargetaFiltros
\*-----------------------------------------------*/

function TargetaFiltros() {

    this.$id = $('#filtros_id')
    this.$btn_collapsed = $('#btn_collapsed')

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

    this.$fecha_inicio.datepicker(this.get_DateConfig())
    this.$fecha_fin.datepicker(this.get_DateConfig())

    // Botones
    this.$boton_buscar.on('click', this, this.click_BotonBuscar);
    this.$boton_limpiar.on('click', this, this.click_BotonLimpiar);

    this.$id.on('shown.bs.collapse', this, this.descolapsar)
    this.$id.on('hidden.bs.collapse', this, this.colapsar)
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
TargetaFiltros.prototype.click_BotonBuscar = function (e) {

    e.preventDefault()
    card_resultados.grid.buscar()
}
TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

    e.preventDefault()

    e.data.$empresa.val("")
    e.data.$tipo.val("")
    e.data.$fecha_inicio.val("")
    e.data.$fecha_fin.val("")
}
TargetaFiltros.prototype.colapsar = function (e) {
    e.data.$btn_collapsed.addClass('glyphicon-chevron-down').removeClass('glyphicon-chevron-up');
}
TargetaFiltros.prototype.descolapsar = function (e) {
    e.data.$btn_collapsed.addClass('glyphicon-chevron-up').removeClass('glyphicon-chevron-down');
}
TargetaFiltros.prototype.get_Filtros = function (_page, _pageSize) {

    return {
        page: _page,
        pageSize: _pageSize,
        empresa__clave: this.$empresa.val(),
        fecha_min: this.$fecha_inicio.val(),
        fecha_max: this.$fecha_fin.val(),
        tipo: this.$tipo.val(),
    }
}



/*-----------------------------------------------*\
            OBJETO: TargetaResultados
\*-----------------------------------------------*/

function TargetaResultados() {

    // this.toolbar = new ToolBar()

    this.grid = new GridResultados()
}


/*-----------------------------------------------*\
            OBJETO: Grid Resultados
\*-----------------------------------------------*/

function GridResultados() {

    this.$id = $("#resultados")

    this.kfuente_datos = null
    this.kgrid = null
    this.init()
}
GridResultados.prototype.init = function (e) {

    kendo.culture("es-MX")

    this.kfuente_datos = new kendo.data.DataSource(this.get_FuenteDatosConfig())

    this.kgrid = this.$id.kendoGrid(this.get_Config())
}
GridResultados.prototype.get_Config = function () {

    return {
        dataSource: this.kfuente_datos,
        columnMenu: true,
        groupable: false,
        sortable: true,
        resizable: true,
        pageable: true,
        selectable: true,
        editable: false,
        scrollable: true,
        columns: this.get_Columnas(),
        noRecords: {
            template: "<div class='app-resultados-grid__empy'> No se encontraron registros </div>"
        },                        
    }
}
GridResultados.prototype.get_Campos = function () {

    return {
        fecha: { editable: false, type: "string" },
        tipo: { editable: false, type: "string" },
        cantidad_guardadas: { editable: false, type: "string" },
        cantidad_validadas: { editable: false, type: "string" },
        total: { editable: false, type: "number" },
        empresa: { editable: false, type: "string" },
        created_date: { editable: false, type: "date" },
        updated_date: { editable: false, type: "date" },
    }
}
GridResultados.prototype.get_Columnas = function (e) {
    
    return [
        { field: "empresa", title: "Empresa", width: "140px" },
        { field: "fecha", title: "Fecha", width: "140px" },
        { field: "tipo", title: "Tipo", width: "140px" },
        { field: "cantidad_guardadas", title: "Cantidad Guardada", width: "140px", attributes:{ style:"text-align:center;" }, },
        { field: "cantidad_validadas", title: "Cantidad Validada", width: "140px", attributes:{ style:"text-align:center;" }, },
        { 
            field: "total", 
            title: "Total", 
            width: "140px",
            format: '{0:n}',
            attributes:{ style:"text-align:right;" },            
        },
        { field: "created_date", title: "Creacion", width: "100px", format: "{0:dd-MM-yyyy}", attributes:{ style:"text-align:right;" },},   
        { field: "updated_date", title: "Actulizacion", width: "110px", format: "{0:dd-MM-yyyy}", attributes:{ style:"text-align:right;" },},   
    ]
}
GridResultados.prototype.get_FuenteDatosConfig = function (e) {

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
        },
        error: function (e) {
            alertify.error("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    }
}
GridResultados.prototype.buscar = function () {
    this.kfuente_datos.page(1)
}
