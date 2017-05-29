
/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

var dominio = window.location.origin

// URLS:
var url_empresa_bypage = dominio + "/api-configuracion/empresa_bypage/"
var url_empresa_editar = ""

// OBJS:
var card_filtros = null
var card_resultados = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    // Inicializar URLS:
    url_empresa_editar = dominio.toString() + $('#url_empresa_editar').val()

    // Inicializar Objectos:
    card_resultados = new TargetaResultados()
})

$(window).resize(function() {

    card_resultados.kgrid.data("kendoGrid").resize()
})


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
        editable: true,
        pageable: true,
        selectable: true,
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
        clave: { editable: false, type: "string" },
        razon_social: { editable: false, type: "string" },
        logo: { editable: false, type: "string" },
        rfc: { editable: false, type: "string" },
        ciec: { editable: false, type: "string" },
        activa: { editable: false, type: "string" },
        usuario: { editable: false, type: "string" },
        email: { editable: false, type: "string" },
        created_date: { editable: false, type: "string" },
        updated_date: { editable: false, type: "string" },
    }
}
GridResultados.prototype.get_Columnas = function (e) {
    
    return [
        {
           command: {
               text: "Editar",
               click: this.editar_Registro,
               className: "app-grid-boton-editar",
           },
           title: " ",
           width: "80px"
        },
        { field: "clave", title: "Clave", width: "90px" },
        { field: "razon_social", title: "Razon Social", width: "200px" },
        // { field: "logo", title: "logo", width: "200px" },
        { field: "rfc", title: "RFC", width: "130px" },
        { field: "ciec", title: "CIEC", width: "130px" },
        { 
            field: "activa", 
            title: "Estado", 
            width: "80px",
            template: "#= activa == 'true' ? 'Activa' : 'Inactiva' #"
        },
        { field: "usuario", title: "Usuario", width: "130px" },
        { field: "email", title: "Email", width: "170px" },
        { 
            field: "created_date", 
            title: "Creado el", 
            width: "100px",
            template: "#= kendo.toString(kendo.parseDate(created_date, 'yyyy-MM-dd'), 'dd-MM-yyyy') #",
        },
        { 
            field: "updated_date", 
            title: "Actualizado el", 
            width: "120px",
            template: "#= kendo.toString(kendo.parseDate(updated_date, 'yyyy-MM-dd'), 'dd-MM-yyyy') #",
        },
    ]
}
GridResultados.prototype.get_FuenteDatosConfig = function (e) {

    return {

        serverPaging: true,
        pageSize: 20,
        transport: {
            read: {

                url: url_empresa_bypage,
                type: "GET",
                dataType: "json",
            },
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                id: "uuid",    
                fields: this.get_Campos()    
            }
        },
        error: function (e) {

            if (e.xhr.status==404) {
                alertify.error("No se pudo conectar con el API que surte los datos")
            }
            else if (e.xhr.status==401) {
                alertify.error("No se tienen permisos para conectar con el API que surte los datos")
            }
            else {
                alertify.error("Status: " + e.status + "; Error message: " + e.errorThrown)
            }
        },
    }
}
GridResultados.prototype.buscar = function () {
    this.kfuente_datos.page(1)
}
GridResultados.prototype.editar_Registro = function (e) {

    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    window.location.href = url_empresa_editar.replace('/0/', '/' + fila.pk + '/')
}
GridResultados.prototype.llenar_Grid = function (e) {

    e.preventDefault()

    $('td').each( function () {

        if($(this).text()=='Activa'){ 

            $(this).addClass('cell--activa')
        }
        else if($(this).text()=='Inactiva'){ 
            $(this).addClass('cell--deshabilitada')
        }
    })
}
