/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// URLS:
var url = window.location
var url_consulta = ""
var url_archivos = ""
var url_validar_factura = ""
var url_marcar_pago = ""
var url_reconocer_factura = ""

if (url.pathname.search("smart") > 0) {
    url_consulta = url.origin + "/smart/api/facturas_cliente/"
    url_archivos = url.origin + "/smart/media/"
    url_validar_factura  = url.origin + "/smart/comprobantes/validar_factura/cliente/"
    url_marcar_pago = url.origin + "/smart/comprobantes/marcar_pago/cliente/"
    url_reconocer_factura = url.origin + "/smart/comprobantes/reconocer_factura/cliente/"
}
else {
    url_consulta = url.origin + "/api/facturas_cliente/"
    url_archivos = url.origin + "/media/"
    url_validar_factura  = url.origin + "/comprobantes/validar_factura/cliente/"
    url_marcar_pago = url.origin + "/comprobantes/marcar_pago/cliente/"
    url_reconocer_factura = url.origin + "/comprobantes/reconocer_factura/cliente/"
}

// OBJS:
var card_filtros = null
var card_resultados = null


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    // Inicializar objetos
    card_filtros = new TargetaFiltros()
    card_resultados = new TargetaResultados()
    pagina = new Pagina()

    // Inicializar Alertify
    pagina.init_Alertify()
})

$(window).resize(function() {

    card_resultados.grid.kGrid.data("kendoGrid").resize()
})


/*-----------------------------------------------*\
            OBJETO: TargetaFiltros
\*-----------------------------------------------*/

function TargetaFiltros() {

    this.$empresa = $('#id_empresa')
    this.$uuid = $('#id_uuid')
    this.$emisor_rfc = $('#id_emisor_rfc')
    this.$serie = $('#id_serie')
    this.$emisor_nombre = $('#id_emisor_nombre')
    this.$folio = $('#id_folio')    
    this.$fecha_inicio = $('#id_fecha_inicio')
    this.$fecha_fin = $('#id_fecha_final')
    this.$fecha_timbrado_inicio = $('#id_fecha_timbrado_inicio')
    this.$fecha_timbrado_fin = $('#id_fecha_timbrado_final')
    this.$estado_sat = $('#id_estadoSat')
    this.$comprobacion = $('#id_comprobacion')

    // Botones
    this.$boton_buscar = $('#id_buscar')
    this.$boton_limpiar = $('#id_limpiar')

    // Iniciamos estilos y funcionalidad
    this.init()
}
TargetaFiltros.prototype.init = function () {

    this.$fecha_inicio.datepicker(datepicker_init)
    this.$fecha_fin.datepicker(datepicker_init)

    this.$fecha_timbrado_inicio.datepicker(datepicker_init)
    this.$fecha_timbrado_fin.datepicker(datepicker_init)  

    // Botones
    this.$boton_buscar.on('click', this, this.click_BotonBuscar)
    this.$boton_limpiar.on('click', this, this.click_BotonLimpiar)
}
TargetaFiltros.prototype.click_BotonBuscar = function (e) {

    e.preventDefault()
    card_resultados.grid.buscar()
}
TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

    e.preventDefault()

    e.data.$empresa.val("")
    e.data.$uuid.val("")
    e.data.$emisor_rfc.val("")
    e.data.$serie.val("")
    e.data.$emisor_nombre.val("")
    e.data.$folio.val("")
    e.data.$fecha_inicio.val("")
    e.data.$fecha_fin.val("")
    e.data.$fecha_timbrado_inicio.val("")
    e.data.$fecha_timbrado_fin.val("")
    e.data.$estado_sat.val("")
    e.data.$comprobacion.val("")
}
TargetaFiltros.prototype.validar_Filtros = function () {
    bandera = false;

    if ((this.$empresa.val() != "") ||
        (this.$uuid.val() != "") ||
        (this.$emisor_rfc.val() != "") ||
        (this.$serie.val() != "") ||
        (this.$emisor_nombre.val() != "") ||
        (this.$folio.val() != "") ||
        (this.$fecha_inicio.val() != "") ||
        (this.$fecha_fin.val() != "") ||
        (this.$fecha_timbrado_inicio.val() != "") ||
        (this.$fecha_timbrado_fin.val() != "") ||
        (this.$estado_sat.val() != "") ||
        (this.$comprobacion.val() != "")) {
        bandera = true
    }

    return bandera;
}


/*-----------------------------------------------*\
            OBJETO: TargetaResultados
\*-----------------------------------------------*/

function TargetaResultados() {

    this.grid = new GridResultados()

    // this.$popup_conceptos = $('#id_conceptos')
    // this.kWindow_conceptos = null

    // this.$popup_trasladados = $('#id_trasladados')
    // this.kWindow_trasladados = null

    // this.$popup_retenidos = $('#id_retenidos')
    // this.kWindow_retenidos = null

    this.init()
}
TargetaResultados.prototype.init = function () {

    // this.kWindow_conceptos = this.$popup_conceptos.kendoWindow(kWindow_init).data("kendoWindow")    
    // this.kWindow_conceptos.element.attr('style', 'padding: 1px')

    // this.kWindow_trasladados = this.$popup_trasladados.kendoWindow(kWindow_init).data("kendoWindow")    
    // this.kWindow_trasladados.element.attr('style', 'padding: 1px')

    // this.kWindow_retenidos = this.$popup_retenidos.kendoWindow(kWindow_init).data("kendoWindow")    
    // this.kWindow_retenidos.element.attr('style', 'padding: 1px')
}


/*-----------------------------------------------*\
            OBJETO: Grid Resultados
\*-----------------------------------------------*/

function GridResultados() {

    this.$id = $("#resultados")
    this.kFuenteDatos = null
    this.kGrid = null
    this.init()
}
GridResultados.prototype.init = function (e) {

    kendo.culture("es-MX")

    this.kFuenteDatos = new kendo.data.DataSource(this.get_FuenteDatosConfig())

    this.kGrid = this.$id.kendoGrid({
        dataSource: this.kFuenteDatos,
        columnMenu: true,
        groupable: false,
        sortable: true,
        resizable: true,
        selectable: true,
        editable: true,
        scrollable: true,
        columns: this.get_Columnas(),
        dataBound: this.llenar,
        pageable: true,
    })
}
GridResultados.prototype.get_Columnas = function (e) {
    return [
        { field: "receptor_rfc", title: "Receptor RFC", width: "140px" },
        { field: "receptor_nombre", title: "Receptor Nombre", width: "350px"},                    

        { field: "uuid", title: "UUID", width: "290px" },       
        {   
            field: "fecha", 
            title: "Fecha", 
            width: "120px", 
            template: "#= kendo.toString(kendo.parseDate(fecha, 'yyyy-MM-dd'), 'dd-MM-yyyy') #"
        },
        { 
            field: "fechaTimbrado", 
            title: "Fecha Timbrado", 
            width: "150px",
            template: "#= kendo.toString(kendo.parseDate(fechaTimbrado, 'yyyy-MM-dd'), 'dd-MM-yyyy') #",
            hidden: true
        },
        {
           command: {
               text: "ver",
               click: this.ver_Conceptos
           },
           title: "Conceptos",
           width: "90px",
           hidden: true
        },        
        { 
            field: "subTotal", 
            title: "Subtotal", 
            width: "150px", 
            format: '{0:c}',
            attributes:{style:"text-align:right;"},
            hidden: true            
        },
        { 
            field: "tipoCambio", 
            title: "Tipo Cambio", 
            width: "150px", 
            format: '{0:n6}',
            attributes:{style:"text-align:right;"},
            hidden: true
        },
        { field: "moneda", title: "Moneda", width: "120px", hidden:true },
        {
            title: "Moneda",
            template: "#= (tipoCambio == 1) ? 'MXP' : moneda #",
            width: "70px",

        },        
        { 
            field: "totalImpuestosTrasladados",
            title: "Impuestos Trasladados", 
            width: "180px", 
            format: '{0:c}',
            attributes:{style:"text-align:right;"},
            hidden: true    
        },
        {
           command: {
               text: "T",
               click: this.ver_Trasladados
           },
           title: "",
           width: "85px",
           hidden: true 
        },         
        { 
            field: "totalImpuestosRetenidos", 
            title: "Impuestos Retenidos", 
            width: "180px", 
            format: '{0:c}',
            attributes:{style:"text-align:right;"},
            hidden: true    
        },
        {
           command: {
               text: "R",
               click: this.ver_Retenidos
           },
           title: "",
           width: "85px",
           hidden: true    
        }, 
        { 
            field: "total", 
            title: "Total", 
            width: "130px", 
            format: '{0:c}',
            attributes:{style:"text-align:right;"}
        },
        { field: "serie", title: "Serie", width: "100px" },
        { field: "folio", title: "Folio", width: "120px" },         
        { field: "formaDePago", title: "Forma Pago", width: "200px", hidden: true },
        
        { field: "tipoDeComprobante", title: "Tipo Comprobante", width: "200px", hidden: true },
        { field: "metodoDePago", title: "Metodo Pago", width: "200px", hidden: true },
        { field: "lugarExpedicion", title: "Lugar Expedicion", width: "200px", hidden: true },
        { field: "numCtaPago", title: "Num Cta Pago", width: "200px", hidden: true },
        { field: "condicionesDePago", title: "Condiciones Pago", width: "200px", hidden: true },
        { field: "emisor_calle", title: "Emisor Calle", width: "200px", hidden: true },
        { field: "emisor_noExterior", title: "Emisor no Exterior", width: "200px", hidden: true },
        { field: "emisor_noInterior", title: "Emisor no Interior", width: "200px", hidden: true },
        { field: "emisor_colonia", title: "Emisor Colonia", width: "200px", hidden: true },
        { field: "emisor_localidad", title: "Emisor Localidad", width: "200px", hidden: true },
        { field: "emisor_municipio", title: "Emisor Municipio", width: "200px", hidden: true },
        { field: "emisor_estado", title: "Emisor Estado", width: "200px", hidden: true },
        { field: "emisor_pais", title: "Emisor Pais", width: "200px", hidden: true },
        { field: "emisor_codigoPostal", title: "Emisor CodigoPostal", width: "200px", hidden: true },
        { field: "emisor_expedidoEn_calle", title: "Emisor Expedido En_calle", width: "200px", hidden: true },
        { field: "emisor_expedidoEn_noExterior", title: "Emisor Expedido En_noExterior", width: "200px", hidden: true },
        { field: "emisor_expedidoEn_noInterior", title: "Emisor Expedido En_noInterior", width: "200px", hidden: true },
        { field: "emisor_expedidoEn_colonia", title: "Emisor Expedido En_colonia", width: "200px", hidden: true },
        { field: "emisor_expedidoEn_municipio", title: "Emisor Expedido En_municipio", width: "200px", hidden: true },
        { field: "emisor_expedidoEn_estado", title: "Emisor Expedido En_estado", width: "200px", hidden: true },
        { field: "emisor_expedidoEn_pais", title: "Emisor Expedido En_pais", width: "200px", hidden: true },
        { field: "emisor_regimen", title: "Emisor Regimen", width: "200px", hidden: true },
        { field: "emisor_rfc", title: "Emisor RFC", width: "140px", hidden: true },
        { field: "emisor_nombre", title: "Emisor Nombre", width: "350px", hidden: true  },    
        { field: "receptor_calle", title: "Receptor Calle", width: "200px", hidden: true },
        { field: "receptor_noExterior", title: "Receptor noExterior", width: "200px", hidden: true },
        { field: "receptor_noInterior", title: "Receptor noInterior", width: "200px", hidden: true },
        { field: "receptor_colonia", title: "Receptor Colonia", width: "200px", hidden: true },
        { field: "receptor_localidad", title: "Receptor Localidad", width: "200px", hidden: true },
        { field: "receptor_municipio", title: "Receptor Municipio", width: "200px", hidden: true },
        { field: "receptor_estado", title: "Receptor Estado", width: "200px", hidden: true },
        { field: "receptor_pais", title: "Receptor Pais", width: "200px", hidden: true },
        { field: "receptor_codigoPostal", title: "Receptor CodigoPostal", width: "200px", hidden: true },
        { field: "comentarios", title: "Comentarios", width: "200px", hidden: true },
        { field: "estadoSat", title: "Estado SAT", width: "100px" },
        { 
            field: "comprobacion", 
            title: "Comprobacion", 
            width: "140px",           
            values: [
                { text: "RECONOCIDO",  value : "RECONOCIDO" },
                { text: "NO Reconocido",  value : "NO_RECONOCIDO" },                
            ]
        },
        { 
            field: "pago", 
            title: "Pago", 
            width: "100px",
            values: [
                { text: "PAGADO",  value : "PAGADO" },
                { text: "Pendiente",  value : "PENDIENTE" },
            ]
        },
        {
            command: [
                { text: "Validar", click: this.validar_XML },
                { text: "XML", click: this.descargar_XML },
                { text: "PDF", click: this.descargar_PDF },
            ],
            title: " ",
            width: "230px"
        },              
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

                    return {
                        page: data.page,
                        pageSize: data.pageSize,
                        empresa__clave: card_filtros.$empresa.val(),
                        fecha_min: card_filtros.$fecha_inicio.val(),
                        fecha_max: card_filtros.$fecha_fin.val(),
                        emisor_rfc: card_filtros.$emisor_rfc.val(),
                        emisor_nombre: card_filtros.$emisor_nombre.val(),
                        uuid: card_filtros.$uuid.val(),
                        estadoSat: card_filtros.$estado_sat.val(),
                        folio: card_filtros.$folio.val(),
                        serie: card_filtros.$serie.val(),
                        fechaTimbrado_min: card_filtros.$fecha_timbrado_inicio.val(),
                        fechaTimbrado_max: card_filtros.$fecha_timbrado_fin.val(),
                        comprobacion: card_filtros.$comprobacion.val(),
                    }
                }
            }
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                id: "uuid",    
                fields: kFields_comprobantes
            }
        },
        change: function (e) {

            if (e.action == "itemchange" && e.field == "pago") {

                var uuid = e.items[0].uuid
                var valor = e.items[0].pago
                card_resultados.grid.marcar_Pago(uuid, valor)
            }

            if (e.action == "itemchange" && e.field == "comprobacion") { 

                var uuid = e.items[0].uuid
                var valor = e.items[0].comprobacion
                card_resultados.grid.reconocer_Factura(uuid, valor)
            }
        },
        error: function (e) {
            alertify.notify("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    }
}
GridResultados.prototype.llenar = function (e) {

    e.preventDefault()

    var data = this.dataItems()

    $.each(data, function (indice, elemento) {
        
        if (elemento.tiene_pdf == "false") {
            card_resultados.grid.kGrid.find("[data-uid='" + elemento.uid + "']").find(".k-grid-PDF").attr('disabled', 'disabled')            
        }
        if (elemento.totalImpuestosTrasladados == 0) {
            card_resultados.grid.kGrid.find("[data-uid='" + elemento.uid + "']").find(".k-grid-T").attr('disabled', 'disabled')
        }
        if (elemento.totalImpuestosRetenidos == 0) {
            card_resultados.grid.kGrid.find("[data-uid='" + elemento.uid + "']").find(".k-grid-R").attr('disabled', 'disabled')
        }
    })
}
GridResultados.prototype.buscar = function () {
    this.kFuenteDatos.page(1)
}
GridResultados.prototype.validar_XML = function (e) {
    e.preventDefault()
    
    alertify.notify("Validando......")

    // Obteniedo informacion del registro
    var fila = this.dataItem($(e.currentTarget).closest('tr'))

    $.ajax({
        url: url_validar_factura + fila.uuid + "/",
        data: "",
        dataType: "json",
        type: "GET",
        contentType: "application/json; charset=utf-8",

        success: function (e) {
            alertify.warning(e.mensaje + " " + e.estado)
            card_resultados.grid.kGrid.find("tr[data-uid='" + fila.uid + "'] td:eq(52)").text(e.estado); 
        },
        error: function (e) {

            alertify.error(e.mensaje)
        }

    })
}
GridResultados.prototype.descargar_XML = function (e) {
    e.preventDefault()

    // Obteniedo informacion del registro
    var fila = this.dataItem($(e.currentTarget).closest('tr'))

    var url = url_archivos + fila.url
    var win = window.open(url, '_blank')
    win.focus()
}
GridResultados.prototype.descargar_PDF = function (e) {
    
    e.preventDefault()

    // Obteniedo informacion del registro
    var fila = this.dataItem($(e.currentTarget).closest('tr'))

    var ruta_archivo = fila.ruta_archivo.replace('xml','pdf')

    var url = url_archivos + ruta_archivo;

    var win = window.open(url, '_blank')

    win.focus()
}
GridResultados.prototype.exportar_Datos = function (e) {

    e.preventDefault();

    if (card_filtros.validar_Filtros() == true) {
        var filas_excel = [{
            cell: [
                { value: 'serie' },
                { value: 'folio' },
                { value: 'fecha' },
                { value: 'formaDePago' },
                { value: 'noCertificado' },
                { value: 'subTotal' },
                { value: 'tipoCambio' },
                { value: 'moneda' },
                { value: 'sello' },
                { value: 'total' },
                { value: 'tipoDeComprobante' },
                { value: 'metodoDePago' },
                { value: 'lugarExpedicion' },
                { value: 'numCtaPago' },
                { value: 'condicionesDePago' },
                { value: 'emisor_rfc' },
                { value: 'emisor_nombre' },
                { value: 'emisor_calle' },
                { value: 'emisor_noExterior' },
                { value: 'emisor_noInterior' },
                { value: 'emisor_colonia' },
                { value: 'emisor_localidad' },
                { value: 'emisor_municipio' },
                { value: 'emisor_estado' },
                { value: 'emisor_pais' },
                { value: 'emisor_codigoPostal' },
                { value: 'emisor_expedidoEn_calle' },
                { value: 'emisor_expedidoEn_noExterior' },
                { value: 'emisor_expedidoEn_noInterior' },
                { value: 'emisor_expedidoEn_colonia' },
                { value: 'emisor_expedidoEn_municipio' },
                { value: 'emisor_expedidoEn_estado' },
                { value: 'emisor_expedidoEn_pais' },
                { value: 'emisor_regimen' },
                { value: 'receptor_rfc' },
                { value: 'receptor_nombre' },
                { value: 'receptor_calle' },
                { value: 'receptor_noExterior' },
                { value: 'receptor_noInterior' },
                { value: 'receptor_colonia' },
                { value: 'receptor_localidad' },
                { value: 'receptor_municipio' },
                { value: 'receptor_estado' },
                { value: 'receptor_pais' },
                { value: 'receptor_codigoPostal' },
                { value: 'conceptos' },
                { value: 'totalImpuestosTrasladados' },
                { value: 'totalImpuestosRetenidos' },
                { value: 'impuestos_trasladados' },
                { value: 'impuestos_retenidos' },
                { value: 'uuid' },
                { value: 'fechaTimbrado' },
                { value: 'noCertificadoSAT' },
                { value: 'selloSAT' },
                { value: 'empresa' },
                { value: 'comentarios' },
                { value: 'comprobacion' },
                { value: 'url' },
                { value: 'tiene_pdf' },
                { value: 'estadoSat' },
            ]
        }]
    }
    else {
        alertify.notify("Favor de seleccionar al menos un filtro");
    }      
}
GridResultados.prototype.marcar_Pago = function (_uuid, _valor) {

    $.ajax({

        url: url_marcar_pago + _uuid + "/" + _valor + "/",
        data : "",
        dataType: "json",
        type: "GET",
        contentType: "application/json; charset=utf-8",

        success: function (e) {
            alertify.warning(e.mensaje)
        },
        error: function (e) {
            alertify.error(e.mensaje)
        }
    })    
}
GridResultados.prototype.reconocer_Factura = function (_uuid, _valor) {
    $.ajax({

        url: url_reconocer_factura + _uuid + "/" + _valor + "/",
        data : "",
        dataType: "json",
        type: "GET",
        contentType: "application/json; charset=utf-8",

        success: function (e) {
            alertify.warning(e.mensaje)
        },
        error: function (e) {
            alertify.error(e.mensaje)
        }
    })    
}

/*-----------------------------------------------*\
            OBJETO: Grid Resultados
\*-----------------------------------------------*/

// GridResultados.prototype.ver_Conceptos = function (e) {
//     e.preventDefault()
//     var fila = this.dataItem($(e.currentTarget).closest('tr'))
    
//     conceptos = fila.conceptos.replace('[','').replace(']','')

//     kGrid_concepto = $('#grid_conceptos').kendoGrid({
//         dataSource : {
//             schema: {
//                 model:{
//                     fields: kFields_conceptos
//                 }
//             },
//             // pageSize: 10,
//         },
//         columns: [
//             { 
//                 field: "cantidad", 
//                 title: "Cantidad", 
//                 width: "80px",
//                 attributes:{style:"text-align:right;"}
//             },
//             { 
//                 field: "valorUnitario", 
//                 title: "Valor Unitario", 
//                 width: "100px",
//                 format: '{0:c}',
//                 attributes:{style:"text-align:right;"}
//             },
//             { field: "noIdentificacion", title: "#Identificacion", width: "110px" },
//             { field: "descripcion", title: "Descripcion", width: "300px" },
//             { field: "unidad", title: "Unidad", width: "100px" },
//             { 
//                 field: "importe", 
//                 title: "Importe", 
//                 width: "100px",
//                 format: '{0:c}',
//                 attributes:{style:"text-align:right;"}
//             },
//         ],
//         groupable: false,
//         sortable: true,
//         resizable: true,
//         selectable: true,
//         editable: false,
//         scrollable: true,
//         mobile: true,    })

//     card_resultados.kWindow_conceptos.center().maximize().open()

//     var lista = conceptos.split('},')

//     json_lista = []

//     $.each(lista ,function (indice, elemento) {
//         elemento_formateado = elemento.replace("{","").replace("}","")
//         elemento_formateado = "{" + elemento_formateado + "}"
//         json_lista.push(JSON.parse(elemento_formateado))
//     })
//     kGrid_concepto.data('kendoGrid').dataSource.data(json_lista)
// }
// GridResultados.prototype.ver_Trasladados = function (e) {
//     e.preventDefault()
//     var fila = this.dataItem($(e.currentTarget).closest('tr'))

//     trasladados = fila.impuestos_trasladados.replace('[','').replace(']','')

//     kGrid_trasladados = $('#grid_trasladados').kendoGrid({
//         dataSource : {
//             schema: {
//                 model:{
//                     fields: kFields_impuestos
//                 }
//             },
//             // pageSize: 10,
//         },
//         columns: [
//             { 
//                 field: "tasa", 
//                 title: "Tasa", 
//                 width: "80px",
//                 attributes:{style:"text-align:right;"}
//             },
//             { field: "impuesto", title: "Impuesto", width: "110px" },
//             { 
//                 field: "importe", 
//                 title: "Importe", 
//                 width: "100px",
//                 format: '{0:c}',
//                 attributes:{style:"text-align:right;"}
//             },
//         ],
//         groupable: false,
//         sortable: true,
//         resizable: true,
//         selectable: true,
//         editable: false,
//         scrollable: true,
//         mobile: true,
//         // pageable: true,
//     })

//     card_resultados.kWindow_trasladados.center().maximize().open()

//     var lista = trasladados.split('},')

//     json_lista = []

//     $.each(lista ,function (indice, elemento) {
//         elemento_formateado = elemento.replace("{","").replace("}","")
//         elemento_formateado = "{" + elemento_formateado + "}"
//         json_lista.push(JSON.parse(elemento_formateado))
//     })
//     kGrid_trasladados.data('kendoGrid').dataSource.data(json_lista)
// }
// GridResultados.prototype.ver_Retenidos = function (e) {
//     e.preventDefault()
//     var fila = this.dataItem($(e.currentTarget).closest('tr'))

//     retenidos = fila.impuestos_retenidos.replace('[','').replace(']','')

//     kGrid_retenidos = $('#grid_retenidos').kendoGrid({
//         dataSource : {
//             schema: {
//                 model:{
//                     fields: kFields_impuestos
//                 }
//             },
//             // pageSize: 10,
//         },
//         columns: [
//             { 
//                 field: "tasa", 
//                 title: "Tasa", 
//                 width: "80px",
//                 attributes:{style:"text-align:right;"}
//             },
//             { field: "impuesto", title: "Impuesto", width: "110px" },
//             { 
//                 field: "importe", 
//                 title: "Importe", 
//                 width: "100px",
//                 format: '{0:c}',
//                 attributes:{style:"text-align:right;"}
//             },
//         ],
//         groupable: false,
//         sortable: true,
//         resizable: true,
//         selectable: true,
//         editable: false,
//         scrollable: true,
//         mobile: true,
//         // pageable: true,
//     })

//     card_resultados.kWindow_retenidos.center().maximize().open()

//     var lista = retenidos.split('},')

//     json_lista = []

//     $.each(lista ,function (indice, elemento) {
//         elemento_formateado = elemento.replace("{","").replace("}","")
//         elemento_formateado = "{" + elemento_formateado + "}"
//         json_lista.push(JSON.parse(elemento_formateado))
//     })
//     kGrid_retenidos.data('kendoGrid').dataSource.data(json_lista)
// }



