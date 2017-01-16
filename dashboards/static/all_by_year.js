/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// OBJS
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

	this.$id = $('#formulario')
    this.$anio = $('#id_anio')

	this.init()
}
TargetaFormulario.prototype.init = function () {

    this.$anio.on("change", this, this.change_Anio)
}
TargetaFormulario.prototype.change_Anio = function (e) {

	e.data.$id.submit();	
}