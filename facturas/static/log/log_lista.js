/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

var dominio = window.location.origin

// URLS:
var url_log_bypage = dominio + "/api-facturas/log_bypage/"
var url_archivos = dominio + "/media/"

// OBJS:
var card_filtros = null
var card_resultados = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    card_filtros = new TargetaFiltros()
    card_resultados = new TargetaResultados()

    // pagina = new Pagina()

    // Inicializar Alertify
    // pagina.init_Alertify()

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
    this.$estado = $('#id_estado')
    this.$operacion = $('#id_operacion')
    this.$tipo_comprobante = $('#id_tipo_comprobante')
    this.$fecha_operacion_inicio = $('#id_fecha_operacion_inicio')
    this.$fecha_operacion_fin = $('#id_fecha_operacion_final')

    // Botones
    this.$boton_buscar = $('#id_buscar')
    this.$boton_limpiar = $('#id_limpiar')

    // Iniciamos estilos y funcionalidad
    this.init()
}
TargetaFiltros.prototype.init = function () {

    this.$fecha_operacion_inicio.datepicker(datepicker_init)
    this.$fecha_operacion_fin.datepicker(datepicker_init)

    // Botones
    this.$boton_buscar.on('click', this, this.click_BotonBuscar);
    this.$boton_limpiar.on('click', this, this.click_BotonLimpiar);

    this.$id.on('shown.bs.collapse', this, this.descolapsar)
    this.$id.on('hidden.bs.collapse', this, this.colapsar)    
}
TargetaFiltros.prototype.click_BotonBuscar = function (e) {

    e.preventDefault()
    card_resultados.grid.buscar()
}
TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

    e.preventDefault()

    e.data.$empresa.val("")
    e.data.$estado.val("")
    e.data.$operacion.val("")
    e.data.$tipo_comprobante.val("")
    e.data.$fecha_operacion_inicio.val("")
    e.data.$fecha_operacion_fin.val("")
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
        estado: this.$estado.val(),
        operacion: this.$operacion.val(),
        fecha_operacion_min: this.$fecha_operacion_inicio.val(),
        fecha_operacion_max: this.$fecha_operacion_fin.val(),
        tipo_comprobante: this.$tipo_comprobante.val(),
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
        dataBound: this.llenar_Grid,
        noRecords: {
            template: "<div class='app-resultados-grid__empy'> No se encontraron registros </div>"
        },                        
    }
}
GridResultados.prototype.get_Campos = function () {

    return {
        empresa: { editable: false, type: "string" },
        nombre: { editable: false, type: "string" },
        estado: { editable: false, type: "string" },
        operacion: { editable: false, type: "string" },
        tipo_comprobante: { editable: false, type: "string" },
        fecha_operacion: { editable: false, type: "string" },
        descripcion: { editable: false, type: "string" },
        url: { editable: false, type: "string" },
        created_date: { editable: false, type: "string" },
        updated_date: { editable: false, type: "string" },
    }
}
GridResultados.prototype.get_Columnas = function (e) {
    
    return [
        { field: "empresa", title: "Empresa", width: "120px" },
        { field: "nombre", title: "Nombre", width: "250px" },
        { field: "estado", title: "Estado", width: "100px" },
        { field: "tipo_comprobante", title: "Tipo", width: "100px" },
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
GridResultados.prototype.get_FuenteDatosConfig = function (e) {

    return {

        serverPaging: true,
        pageSize: 20,
        transport: {
            read: {

                url: url_log_bypage,
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
            alertify.error("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    }
}
GridResultados.prototype.buscar = function () {
    this.kfuente_datos.page(1)
}
GridResultados.prototype.descargar_Log = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    var url = url_archivos + fila.url
    var win = window.open(url, '_blank')
    win.focus()
}
GridResultados.prototype.llenar_Grid = function (e) {

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