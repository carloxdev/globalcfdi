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

}
Pagina.prototype.init_Alertify = function () {
    alertify.set('notifier', 'position', 'top-right')
    alertify.set('notifier', 'delay', 10)	
}