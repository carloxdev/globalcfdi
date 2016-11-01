
var card_filtros = null
var card_resultados = null
var url_dominio = window.location.protocol + '//' + window.location.host + '/'

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

    this.$estado = $('#id_estado')
    this.$operacion = $('#id_operacion')

    this.$fecha_operacion_inicio = $('#id_fecha_operacion_inicio')
    this.$fecha_operacion_fin = $('#id_fecha_operacion_final')

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

    this.$fecha_operacion_inicio.datepicker(datepicker_init)
    this.$fecha_operacion_fin.datepicker(datepicker_init)

    // Botones
    this.$boton_buscar.on('click', this, this.click_BotonBuscar);
    this.$boton_limpiar.on('click', this, this.click_BotonLimpiar);
}
TargetaFiltros.prototype.click_BotonBuscar = function (e) {

    e.preventDefault()
    card_resultados.buscar()
}
TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

    e.preventDefault()

    e.data.$empresa.val("")
    e.data.$estado.val("")
    e.data.$operacion.val("")
    e.data.$fecha_operacion_inicio.val("")
    e.data.$fecha_operacion_fin.val("")
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

        serverPaging: true,
        pageSize: 10,
        transport: {
            read: {

                url: url_dominio + "api/logs/",
                type: "GET",
                dataType: "json",
            },
            parameterMap: function (data, action) {
                if (action === "read") {

                    return {
                        page: data.page,
                        pageSize: data.pageSize,
                        empresa__clave: card_filtros.$empresa.val(),
                        estado: card_filtros.$estado.val(),
                        operacion: card_filtros.$operacion.val(),
                        fecha_operacion_min: card_filtros.$fecha_operacion_inicio.val(),
                        fecha_operacion_max: card_filtros.$fecha_operacion_fin.val(),
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

    this.kGrid = this.$divGrid.kendoGrid({
        dataSource: this.kFuenteDatos,
        columnMenu: true,
        groupable: false,
        sortable: true,
        resizable: true,
        pageable: true,
        selectable: true,
        editable: false,
        scrollable: true,
        columns: this.kColumns,
    })

}
TargetaResultados.prototype.buscar = function (e) {

    this.kFuenteDatos.page(1)
}
TargetaResultados.prototype.descargar_Log = function (e) {
    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    var url = url_dominio + "media/" + fila.url
    var win = window.open(url, '_blank')
    win.focus()
}

