
/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// URLS:
var url_test = window.location.origin + "/empresas/test_credentials/"


// OBJS:
var formulario = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    formulario = new TargetaFormulario()

})


/*-----------------------------------------------*\
            OBJETO: Targeta Formulario
\*-----------------------------------------------*/

function TargetaFormulario() {
    this.$boton_test = $('#btn_test')
    this.$empresa_id = $('#empresa_pk')

    this.init()
}
TargetaFormulario.prototype.init = function () {

    this.$boton_test.on("click", this, this.click_BotonTest)
}
TargetaFormulario.prototype.click_BotonTest = function (e) {

    e.preventDefault()



}