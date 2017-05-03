/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// OBJS:
var pagina = null

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/


$(document).ready(function () {

	pagina = new Pagina()

})

/*-----------------------------------------------*\
            OBJETO: PAGINA
\*-----------------------------------------------*/

function Pagina () {

    this.init()
}
Pagina.prototype.init = function () {
    
    this.set_AlertifyConfig()
}
Pagina.prototype.set_AlertifyConfig = function() {

    alertify.set('notifier', 'position', 'top-right')
    alertify.set('notifier', 'delay', 10)   

    alertify.defaults.theme.ok = "btn btn-primary";
    alertify.defaults.theme.cancel = "btn btn-danger";
    alertify.defaults.theme.input = "form-control";

}