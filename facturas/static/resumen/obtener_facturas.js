
var card_filtros = null
var card_resultados = null
var url_dominio = window.location.protocol + '//' + window.location.host + '/'

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    card_filtros = new TargetaFiltros()

    alertify.set('notifier', 'position', 'top-right')
    alertify.set('notifier', 'delay', 10)
});


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

    // this.$fecha_timbrado_inicio.datepicker(datepicker_init)
    // this.$fecha_timbrado_fin.datepicker(datepicker_init)  

    // // Botones
    // this.$boton_buscar.on('click', this, this.click_BotonBuscar);
    // this.$boton_limpiar.on('click', this, this.click_BotonLimpiar);
}
// TargetaFiltros.prototype.click_BotonBuscar = function (e) {

//     e.preventDefault()
//     card_resultados.buscar()
// }
// TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

//     e.preventDefault()

//     e.data.$empresa.val("")
//     e.data.$uuid.val("")
//     e.data.$emisor_rfc.val("")
//     e.data.$serie.val("")
//     e.data.$emisor_nombre.val("")
//     e.data.$folio.val("")
//     e.data.$fecha_inicio.val("")
//     e.data.$fecha_fin.val("")
//     e.data.$fecha_timbrado_inicio.val("")
//     e.data.$fecha_timbrado_fin.val("")
//     e.data.$estado_sat.val("")
//     e.data.$comprobacion.val("")
// }
// TargetaFiltros.prototype.validar_Filtros = function () {
//     bandera = false;

//     if ((this.$empresa.val() != "") ||
//         (this.$uuid.val() != "") ||
//         (this.$emisor_rfc.val() != "") ||
//         (this.$serie.val() != "") ||
//         (this.$emisor_nombre.val() != "") ||
//         (this.$folio.val() != "") ||
//         (this.$fecha_inicio.val() != "") ||
//         (this.$fecha_fin.val() != "") ||
//         (this.$fecha_timbrado_inicio.val() != "") ||
//         (this.$fecha_timbrado_fin.val() != "") ||
//         (this.$estado_sat.val() != "") ||
//         (this.$comprobacion.val() != "")) {
//         bandera = true
//     }

//     return bandera;
// }




