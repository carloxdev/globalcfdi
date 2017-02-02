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
var url_export = ""

if (url.pathname.search("smart") > 0) {
    url_consulta = url.origin + "/smart/api/comprobantes_empleado/"
    url_archivos = url.origin + "/smart/media/"
    url_validar_factura  = url.origin + "/smart/comprobantes/validar_factura/empleado/"
    url_marcar_pago = url.origin + "/smart/comprobantes/marcar_pago/empleado/"
    url_reconocer_factura = url.origin + "/smart/comprobantes/reconocer_factura/empleado/"
    url_export = url.origin + "/smart/api/comprobantes_empleado_todos/"
}
else {
    url_consulta = url.origin + "/api/comprobantes_empleado/"
    url_archivos = url.origin + "/media/"
    url_validar_factura  = url.origin + "/comprobantes/validar_factura/empleado/"
    url_marcar_pago = url.origin + "/comprobantes/marcar_pago/empleado/"
    url_reconocer_factura = url.origin + "/comprobantes/reconocer_factura/empleado/"
    url_export = url.origin + "/api/comprobantes_empleado_todos/"
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
    this.$uuid = $('#id_uuid')
    this.$receptor_rfc = $('#id_receptor_rfc')
    this.$serie = $('#id_serie')
    this.$receptor_nombre = $('#id_receptor_nombre')
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

    this.$id.on('shown.bs.collapse', this, this.descolapsar)
    this.$id.on('hidden.bs.collapse', this, this.colapsar)    

    this.show_FilterSelected()
}
TargetaFiltros.prototype.click_BotonBuscar = function (e) {

    e.preventDefault()
    e.data.$id.collapse("hide")
    card_resultados.grid.buscar()
}
TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

    e.preventDefault()

    e.data.$empresa.val("")
    e.data.$uuid.val("")
    e.data.$serie.val("")
    e.data.$receptor_rfc.val("")
    e.data.$receptor_nombre.val("")
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
        (this.$receptor_rfc.val() != "") ||
        (this.$serie.val() != "") ||
        (this.$receptor_nombre.val() != "") ||
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
TargetaFiltros.prototype.get_Filtros = function (_page, _pageSize) {

    return {
        page: _page,
        pageSize: _pageSize,
        empresa__clave: this.$empresa.val(),
        fecha_min: this.$fecha_inicio.val(),
        fecha_max: this.$fecha_fin.val(),
        receptor_rfc: this.$receptor_rfc.val(),
        receptor_nombre: this.$receptor_nombre.val(),
        uuid: this.$uuid.val(),
        estadoSat: this.$estado_sat.val(),
        folio: this.$folio.val(),
        serie: this.$serie.val(),
        fechaTimbrado_min: this.$fecha_timbrado_inicio.val(),
        fechaTimbrado_max: this.$fecha_timbrado_fin.val(),
        comprobacion: this.$comprobacion.val(),
    }
}
TargetaFiltros.prototype.colapsar = function (e) {
    e.data.$btn_collapsed.addClass('glyphicon-chevron-down').removeClass('glyphicon-chevron-up');
}
TargetaFiltros.prototype.descolapsar = function (e) {
    e.data.$btn_collapsed.addClass('glyphicon-chevron-up').removeClass('glyphicon-chevron-down');
}
TargetaFiltros.prototype.show_FilterSelected = function () {

    moment.locale("es")

    var mes_inicio = moment(this.$fecha_inicio.val()).format('MM')
    var anio_inicio = moment(this.$fecha_inicio.val()).format('YYYY')
    var mes_fin = moment(this.$fecha_fin.val()).format('MM')
    var anio_fin = moment(this.$fecha_fin.val()).format('YYYY')

    if (this.$empresa.find(":selected").text() == "Todas") {
        var empresa = "en todas las empresas"    
    }
    else {
        var empresa = "de la empresa " + this.$empresa.find(":selected").text()
    }

    if (mes_inicio == mes_fin) {

        alertify.warning("Comprobantes emitidos en month del year, business"
            .replace("month", moment(this.$fecha_inicio.val()).format('MMMM').toUpperCase())
                .replace("year", moment(this.$fecha_inicio.val()).format('YYYY'))
                    .replace("business", empresa)
        )
    }
    else if (anio_inicio == anio_fin) {

        alertify.warning("Comprobantes emitidos en year business"
                .replace("year", moment(this.$fecha_inicio.val()).format('YYYY'))
                    .replace("business", empresa)
        )
    }

}

/*-----------------------------------------------*\
            OBJETO: TargetaResultados
\*-----------------------------------------------*/

function TargetaResultados() {

    this.toolbar = new ToolBar()

    this.grid = new GridResultados()

    // this.$popup_conceptos = $('#id_conceptos')
    // this.kWindow_conceptos = null

    // this.$popup_trasladados = $('#id_trasladados')
    // this.kWindow_trasladados = null

    // this.$popup_retenidos = $('#id_retenidos')
    // this.kWindow_retenidos = null

    // this.init()
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
        resizable: true,
        selectable: true,
        editable: true,
        scrollable: true,
        columns: this.get_Columnas(),
        dataBound: this.llenar,
        pageable: true,
        noRecords: {
            template: "<div class='app-resultados-grid__empy'> No se encontraron registros </div>"
        },                
    }
}
GridResultados.prototype.get_Columnas = function (e) {
    return [
        { field: "empresa", title: "Empresa", width: "80px"},
        { field: "emisor_rfc", title: "Emisor RFC", width: "140px", hidden: true },
        { field: "emisor_nombre", title: "Emisor Nombre", width: "350px", hidden: true },                
        { field: "receptor_rfc", title: "Empleado RFC", width: "200px" },
        { field: "receptor_nombre", title: "Empleado Nombre", width: "200px" },
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

                    return card_filtros.get_Filtros(data.page, data.pageSize)
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
            alertify.warning("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    }
}
GridResultados.prototype.llenar = function (e) {

    e.preventDefault()

    var data = this.dataItems()

    $.each(data, function (indice, elemento) {
        
        if (elemento.tiene_pdf == "false") {
            card_resultados.grid.kgrid.find("[data-uid='" + elemento.uid + "']").find(".k-grid-PDF").attr('disabled', 'disabled')            
        }
        if (elemento.totalImpuestosTrasladados == 0) {
            card_resultados.grid.kgrid.find("[data-uid='" + elemento.uid + "']").find(".k-grid-T").attr('disabled', 'disabled')
        }
        if (elemento.totalImpuestosRetenidos == 0) {
            card_resultados.grid.kgrid.find("[data-uid='" + elemento.uid + "']").find(".k-grid-R").attr('disabled', 'disabled')
        }
    })
}
GridResultados.prototype.buscar = function () {
    this.kfuente_datos.page(1)
}
GridResultados.prototype.validar_XML = function (e) {
    e.preventDefault()
    
    alertify.warning("Validando......")

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
            card_resultados.grid.kgrid.find("tr[data-uid='" + fila.uid + "'] td:eq(52)").text(e.estado); 
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
            OBJETO: Toolbar
\*-----------------------------------------------*/

function ToolBar() {
    this.boton_exportar = $('#botonExportar')
    this.kfuente_datos = null
    this.krows = null
    this.init()
}
ToolBar.prototype.init = function (e) {

    kendo.culture("es-MX")

    this.kfuente_datos = new kendo.data.DataSource(this.get_FuenteDatosConfig())

    this.boton_exportar.on('click', this, this.click_BotonExportar)
}
ToolBar.prototype.get_FuenteDatosConfig = function (e) {

    return {
        serverFiltering: true,
        transport: {
            read: {
                url: url_export,
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
            model: {
                id: "pk",
                fields: kFields_comprobantes
            }
        },
        error: function (e) {
            alert("Status: " + e.status + "; Error message: " + e.errorThrown);
        },
        serverFiltering: true
    }
}
ToolBar.prototype.init_Celdas = function (e) {

    if (this.krows != null) {
        if (this.krows.length != 1) {
            this.krows.length = 0;
        }
    }

    this.krows = [{
        cells: [
            { value: "UUID" },        
            { value: "ESTADO SAT" },
            { value: "SERIE" },
            { value: "FOLIO" },
            { value: "FECHA" },
            { value: "FORMA DE PAGO" },
            { value: "NO CERTIFICADO" },
            { value: "SUBTOTAL" },
            { value: "TIPO CAMBIO" },
            { value: "MONEDA" },
            { value: "TOTAL" },
            { value: "TIPO DE COMPROBANTE" },
            { value: "METODO DE PAGO" },
            { value: "LUGAR EXPEDICION" },
            { value: "NUM CTA PAGO" },
            { value: "CONDICIONES DE PAGO" },
            { value: "EMISOR RFC" },
            { value: "EMISOR NOMBRE" },
            { value: "EMISOR CALLE" },
            { value: "EMISOR NO EXTERIOR" },
            { value: "EMISOR NO INTERIOR" },
            { value: "EMISOR COLONIA" },
            { value: "EMISOR LOCALIDAD" },
            { value: "EMISOR MUNICIPIO" },
            { value: "EMISOR ESTADO" },
            { value: "EMISOR PAIS" },
            { value: "EMISOR CODIGO POSTAL" },
            { value: "EMISOR EXPEDIDO EN CALLE" },
            { value: "EMISOR EXPEDIDO EN NOEXTERIOR" },
            { value: "EMISOR EXPEDIDO EN NOINTERIOR" },
            { value: "EMISOR EXPEDIDO EN COLONIA" },
            { value: "EMISOR EXPEDIDO EN MUNICIPIO" },
            { value: "EMISOR EXPEDIDO EN ESTADO" },
            { value: "EMISOR EXPEDIDO EN PAIS" },
            { value: "EMISOR REGIMEN" },
            { value: "RECEPTOR RFC" },
            { value: "RECEPTOR NOMBRE" },
            { value: "RECEPTOR CALLE" },
            { value: "RECEPTOR NO EXTERIOR" },
            { value: "RECEPTOR NO INTERIOR" },
            { value: "RECEPTOR COLONIA" },
            { value: "RECEPTOR LOCALIDAD" },
            { value: "RECEPTOR MUNICIPIO" },
            { value: "RECEPTOR ESTADO" },
            { value: "RECEPTOR PAIS" },
            { value: "RECEPTOR CODIGO POSTAL" },
            { value: "CONCEPTOS" },
            { value: "TOTAL IMPUESTOS TRASLADADOS" },
            { value: "TOTAL IMPUESTOS RETENIDOS" },
            { value: "IMPUESTOS TRASLADADOS" },
            { value: "IMPUESTOS RETENIDOS" },
            { value: "FECHA TIMBRADO" },
            { value: "PAGO" },
            { value: "COMPROBACION" },
            { value: "NO CERTIFICADO SAT" },
            { value: "SELLO" },
            { value: "SELLO SAT" },
            { value: "EMPRESA" },
            { value: "COMENTARIOS" },
            { value: "URL" },
        ]
    }];
}
ToolBar.prototype.agregar_Info_A_Celdas = function (data) {

    for (var i = 0; i < data.length; i++) {

        this.krows.push({
            cells: [
                { value: data[i].uuid },
                { value: data[i].estadoSat },
                { value: data[i].serie },
                { value: data[i].folio },
                { value: data[i].fecha },
                { value: data[i].formaDePago },
                { value: data[i].noCertificado },
                { value: data[i].subTotal },
                { value: data[i].tipoCambio },
                { value: data[i].moneda },
                { value: data[i].total },
                { value: data[i].tipoDeComprobante },
                { value: data[i].metodoDePago },
                { value: data[i].lugarExpedicion },
                { value: data[i].numCtaPago },
                { value: data[i].condicionesDePago },
                { value: data[i].emisor_rfc },
                { value: data[i].emisor_nombre },
                { value: data[i].emisor_calle },
                { value: data[i].emisor_noExterior },
                { value: data[i].emisor_noInterior },
                { value: data[i].emisor_colonia },
                { value: data[i].emisor_localidad },
                { value: data[i].emisor_municipio },
                { value: data[i].emisor_estado },
                { value: data[i].emisor_pais },
                { value: data[i].emisor_codigoPostal },
                { value: data[i].emisor_expedidoEn_calle },
                { value: data[i].emisor_expedidoEn_noExterior },
                { value: data[i].emisor_expedidoEn_noInterior },
                { value: data[i].emisor_expedidoEn_colonia },
                { value: data[i].emisor_expedidoEn_municipio },
                { value: data[i].emisor_expedidoEn_estado },
                { value: data[i].emisor_expedidoEn_pais },
                { value: data[i].emisor_regimen },
                { value: data[i].receptor_rfc },
                { value: data[i].receptor_nombre },
                { value: data[i].receptor_calle },
                { value: data[i].receptor_noExterior },
                { value: data[i].receptor_noInterior },
                { value: data[i].receptor_colonia },
                { value: data[i].receptor_localidad },
                { value: data[i].receptor_municipio },
                { value: data[i].receptor_estado },
                { value: data[i].receptor_pais },
                { value: data[i].receptor_codigoPostal },
                { value: data[i].conceptos },
                { value: data[i].totalImpuestosTrasladados },
                { value: data[i].totalImpuestosRetenidos },
                { value: data[i].impuestos_trasladados },
                { value: data[i].impuestos_retenidos },
                { value: data[i].fechaTimbrado },
                { value: data[i].pago },
                { value: data[i].comprobacion },
                { value: data[i].noCertificadoSAT },
                { value: data[i].sello },
                { value: data[i].selloSAT },
                { value: data[i].empresa },
                { value: data[i].comentarios },
                { value: url_archivos + data[i].url },
            ]
        })
    }
}
ToolBar.prototype.get_Hojas = function () {
    return {
        sheets: [{
            columnas: [
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
                { autoWidth: true },
            ],
            title: "registros",
            rows: this.krows
        }]
    }
}
ToolBar.prototype.click_BotonExportar = function (e) {

    e.preventDefault()

    if (card_filtros.validar_Filtros() == true) {

        // Se inicializan los titulos:
        e.data.init_Celdas();

        // show_Spinner()

        // se carga y los datos se agregarn a las filas:
        e.data.kfuente_datos.fetch(function () {

            var datos = this.data();

            e.data.agregar_Info_A_Celdas(datos)

            // Se crea Libro:
            var workbook = new kendo.ooxml.Workbook(e.data.get_Hojas())

            // Se genera archivo de Excel:
            kendo.saveAs({
                dataURI: workbook.toDataURL(),
                fileName: "registros.xlsx",
                // proxyURL: 'frmSaveFile.aspx'
            })
        })
    }
    else {
        alert("Favor de seleccionar al menos un filtro")
    }
}



/*-----------------------------------------------*\
            OBJETO: ??
\*-----------------------------------------------*/

// GridResultados.prototype.ver_Conceptos = function (e) {
//     e.preventDefault()
//     var fila = this.dataItem($(e.currentTarget).closest('tr'))
    
//     conceptos = fila.conceptos.replace('[','').replace(']','')

//     kgrid_concepto = $('#grid_conceptos').kendoGrid({
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
//     kgrid_concepto.data('kendoGrid').dataSource.data(json_lista)
// }
// GridResultados.prototype.ver_Trasladados = function (e) {
//     e.preventDefault()
//     var fila = this.dataItem($(e.currentTarget).closest('tr'))

//     trasladados = fila.impuestos_trasladados.replace('[','').replace(']','')

//     kgrid_trasladados = $('#grid_trasladados').kendoGrid({
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
//     kgrid_trasladados.data('kendoGrid').dataSource.data(json_lista)
// }
// GridResultados.prototype.ver_Retenidos = function (e) {
//     e.preventDefault()
//     var fila = this.dataItem($(e.currentTarget).closest('tr'))

//     retenidos = fila.impuestos_retenidos.replace('[','').replace(']','')

//     kgrid_retenidos = $('#grid_retenidos').kendoGrid({
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
//     kgrid_retenidos.data('kendoGrid').dataSource.data(json_lista)
// }



