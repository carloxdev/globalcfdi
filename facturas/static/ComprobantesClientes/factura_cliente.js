
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
});


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

    this.$fecha_timbrado_inicio.datepicker(datepicker_init)
    this.$fecha_timbrado_fin.datepicker(datepicker_init)  

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

    this.$divGrid = $('#resultados')
    this.kFields = null
    this.kFuenteDatos = null
    this.kRows = null
    this.kColumns = null
    this.kGrid = null

    this.$popup_conceptos = $('#id_conceptos')
    this.kWindow_conceptos = null

    this.$popup_trasladados = $('#id_trasladados')
    this.kWindow_trasladados = null

    this.$popup_retenidos = $('#id_retenidos')
    this.kWindow_retenidos = null

    this.init()
}
TargetaResultados.prototype.init = function () {

    kendo.culture("es-MX")
    
    this.kFields = {
        serie: { editable: false, type: "string" },
        folio: { editable: false, type: "string" },
        fecha: { editable: false, type: "string" },
        formaDePago: { editable: false, type: "string" },
        noCertificado: { editable: false, type: "string" },
        subTotal: { type: "number" },
        tipoCambio: { type: "number" },
        moneda: { editable: false, type: "string" },
        sello: { editable: false, type: "string" },
        total: { editable: true, type: "number" },
        tipoDeComprobante: { editable: false, type: "string" },
        metodoDePago: { editable: false, type: "string" },
        lugarExpedicion: { editable: false, type: "string" },
        numCtaPago: { editable: false, type: "string" },
        condicionesDePago: { editable: false, type: "string" },
        emisor_rfc: { editable: false, type: "string" },
        emisor_nombre: { editable: false, type: "string" },
        emisor_calle: { editable: false, type: "string" },
        emisor_noExterior: { editable: false, type: "string" },
        emisor_noInterior: { editable: false, type: "string" },
        emisor_colonia: { editable: false, type: "string" },
        emisor_localidad: { editable: false, type: "string" },
        emisor_municipio: { editable: false, type: "string" },
        emisor_estado: { editable: false, type: "string" },
        emisor_pais: { editable: false, type: "string" },
        emisor_codigoPostal: { editable: false, type: "string" },
        emisor_expedidoEn_calle: { editable: false, type: "string" },
        emisor_expedidoEn_noExterior: { editable: false, type: "string" },
        emisor_expedidoEn_noInterior: { editable: false, type: "string" },
        emisor_expedidoEn_colonia: { editable: false, type: "string" },
        emisor_expedidoEn_municipio: { editable: false, type: "string" },
        emisor_expedidoEn_estado: { editable: false, type: "string" },
        emisor_expedidoEn_pais: { editable: false, type: "string" },
        emisor_regimen: { editable: false, type: "string" },
        receptor_rfc: { editable: false, type: "string" },
        receptor_nombre: { editable: false, type: "string" },
        receptor_calle: { editable: false, type: "string" },
        receptor_noExterior: { editable: false, type: "string" },
        receptor_noInterior: { editable: false, type: "string" },
        receptor_colonia: { editable: false, type: "string" },
        receptor_localidad: { editable: false, type: "string" },
        receptor_municipio: { editable: false, type: "string" },
        receptor_estado: { editable: false, type: "string" },
        receptor_pais: { editable: false, type: "string" },
        receptor_codigoPostal: { editable: false, type: "string" },
        conceptos: { editable: false, type: "string" },
        totalImpuestosTrasladados: { type: "number" },
        totalImpuestosRetenidos: { type: "number" },
        impuestos_trasladados: { editable: false, type: "string" },
        impuestos_retenidos: { editable: false, type: "string" },
        uuid: { editable: false, type: "string" },
        fechaTimbrado: { editable: false, type: "string" },
        noCertificadoSAT: { editable: false, type: "string" },
        selloSAT: { editable: false, type: "string" },
        empresa: { editable: false, type: "string" },
        comentarios: { editable: false, type: "string" },
        comprobacion: { editable: false, type: "string" },
        url: { editable: false, type: "string" },
        tiene_pdf: { editable: false, type: "string" },
        estadoSat: { editable: false, type: "string" },
    }

    this.kFuenteDatos = new kendo.data.DataSource({

        serverPaging: true,
        pageSize: 10,
        transport: {
            read: {

                url: url_dominio + "api/facturas_cliente/",
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
                fields: this.kFields    
            }
        },
        error: function (e) {
            alertify.notify("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    });

    this.kColumns = [
        {
           command: {
               text: "Validar",
               click: this.validar_XML
           },
           title: " ",
           width: "110px"
        },
        {
           command: {
               text: "XML",
               click: this.descargar_XML
           },
           title: " ",
           width: "90px"
        },
        {
           command: {
               text: "PDF",
               // click: this.Click_DescargarArchivoPDF
           },
           title: " ",
           width: "90px"
        },        
        { field: "empresa", title: "Empresa", width: "120px" },
        { field: "uuid", title: "UUID", width: "290px" },
        {   
            field: "fecha", 
            title: "Fecha", 
            width: "120px", 
            template: "#= kendo.toString(kendo.parseDate(fecha, 'yyyy-MM-dd'), 'dd-MMMM-yyyy') #"
        },
        { 
            field: "fechaTimbrado", 
            title: "Fecha Timbrado", 
            width: "150px",
            template: "#= kendo.toString(kendo.parseDate(fechaTimbrado, 'yyyy-MM-dd'), 'dd-MMMM-yyyy') #"
        },
        { field: "serie", title: "Serie", width: "100px" },
        { field: "folio", title: "Folio", width: "120px" },
        { field: "estadoSat", title: "Estado SAT", width: "130px" },
        { field: "comprobacion", title: "Comprobacion", width: "140px" },        
        { field: "emisor_rfc", title: "Emisor RFC", width: "140px" },
        { field: "emisor_nombre", title: "Emisor Nombre", width: "350px" },
        {
           command: {
               text: "ver",
               click: this.ver_Conceptos
           },
           title: "Conceptos",
           width: "90px"
        },        
        { 
            field: "subTotal", 
            title: "Subtotal", 
            width: "150px", 
            format: '{0:c}',
            attributes:{style:"text-align:right;"}            
        },
        { 
            field: "tipoCambio", 
            title: "Tipo Cambio", 
            width: "150px", 
            format: '{0:n6}',
            attributes:{style:"text-align:right;"}
        },
        { field: "moneda", title: "Moneda", width: "120px", },
        { 
            field: "totalImpuestosTrasladados",
            title: "Impuestos Trasladados", 
            width: "180px", 
            format: '{0:c}',
            attributes:{style:"text-align:right;"}
        },
        {
           command: {
               text: "T",
               click: this.ver_Trasladados
           },
           title: "",
           width: "85px"
        },         
        { 
            field: "totalImpuestosRetenidos", 
            title: "Impuestos Retenidos", 
            width: "180px", 
            format: '{0:c}',
            attributes:{style:"text-align:right;"},
        },
        {
           command: {
               text: "R",
               click: this.ver_Retenidos
           },
           title: "",
           width: "85px"
        },         
        { 
            field: "total", 
            title: "Total", 
            width: "150px", 
            format: '{0:c}',
            attributes:{style:"text-align:right;"}
        },
        {  title: "Pago", width: "50px" },       
        
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
        { field: "receptor_rfc", title: "Receptor RFC", width: "200px", hidden: true },
        { field: "receptor_nombre", title: "Receptor Nombre", width: "200px", hidden: true },
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
        // dataBound: this.FillGrid,
        mobile: true
    });

    this.kWindow_conceptos = this.$popup_conceptos.kendoWindow({
        title: "Conceptos",
        modal: true,
        visible: false,
        width: "100%",
        autofocus: true,
        actions: [
            "Maximize",
            "Close"
        ],        
        resizable: true,
    }).data("kendoWindow");    
    this.kWindow_conceptos.element.attr('style', 'padding: 1px');

    this.kWindow_trasladados = this.$popup_trasladados.kendoWindow({
        title: "Impuestos Trasladados",
        modal: true,
        visible: false,
        width: "100%",
        autofocus: true,
        actions: [
            "Maximize",
            "Close"
        ],        
        resizable: true,
    }).data("kendoWindow");    
    this.kWindow_trasladados.element.attr('style', 'padding: 1px');

    this.kWindow_retenidos = this.$popup_retenidos.kendoWindow({
        title: "Impuestos Retenidos",
        modal: true,
        visible: false,
        width: "100%",
        autofocus: true,
        actions: [
            "Maximize",
            "Close"
        ],        
        resizable: true,
    }).data("kendoWindow");    
    this.kWindow_retenidos.element.attr('style', 'padding: 1px');
}
TargetaResultados.prototype.buscar = function (e) {
    this.kFuenteDatos.page(1)
}
TargetaResultados.prototype.descargar_XML = function (e) {
    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    var url = url_dominio + "media/" + fila.url
    var win = window.open(url, '_blank')
    win.focus()
}
TargetaResultados.prototype.validar_XML = function (e) {
    e.preventDefault()
    alertify.notify("Se esta validando")
}
TargetaResultados.prototype.ver_Conceptos = function (e) {
    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))
    
    conceptos = fila.conceptos.replace('[','').replace(']','')

    kGrid_concepto = $('#grid_conceptos').kendoGrid({
        dataSource : {
            schema: {
                model:{
                    fields: {
                        cantidad: { type: "string" },
                        valorUnitario: { type: "string" },
                        noIdentificacion: { type: "string" },
                        descripcion: { type: "string" },
                        unidad: { type: "string" },
                        importe: { type: "string" },
                    }
                }
            },
            // pageSize: 10,
        },
        columns: [
            { 
                field: "cantidad", 
                title: "Cantidad", 
                width: "80px",
                attributes:{style:"text-align:right;"}
            },
            { 
                field: "valorUnitario", 
                title: "Valor Unitario", 
                width: "100px",
                format: '{0:c}',
                attributes:{style:"text-align:right;"}
            },
            { field: "noIdentificacion", title: "#Identificacion", width: "110px" },
            { field: "descripcion", title: "Descripcion", width: "300px" },
            { field: "unidad", title: "Unidad", width: "100px" },
            { 
                field: "importe", 
                title: "Importe", 
                width: "100px",
                format: '{0:c}',
                attributes:{style:"text-align:right;"}
            },
        ],
        groupable: false,
        sortable: true,
        resizable: true,
        selectable: true,
        editable: false,
        scrollable: true,
        mobile: true,
        // pageable: true,
    })

    card_resultados.kWindow_conceptos.center().maximize().open()

    var lista = conceptos.split('},')

    json_lista = []

    $.each(lista ,function (indice, elemento) {
        elemento_formateado = elemento.replace("{","").replace("}","")
        elemento_formateado = "{" + elemento_formateado + "}"
        json_lista.push(JSON.parse(elemento_formateado))
    })
    kGrid_concepto.data('kendoGrid').dataSource.data(json_lista)
}
TargetaResultados.prototype.ver_Trasladados = function (e) {
    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))

    trasladados = fila.impuestos_trasladados.replace('[','').replace(']','')

    kGrid_trasladados = $('#grid_trasladados').kendoGrid({
        dataSource : {
            schema: {
                model:{
                    fields: {
                        tasa: { type: "string" },
                        impuesto: { type: "string" },
                        importe: { type: "string" },
                    }
                }
            },
            // pageSize: 10,
        },
        columns: [
            { 
                field: "tasa", 
                title: "Tasa", 
                width: "80px",
                attributes:{style:"text-align:right;"}
            },
            { field: "impuesto", title: "Impuesto", width: "110px" },
            { 
                field: "importe", 
                title: "Importe", 
                width: "100px",
                format: '{0:c}',
                attributes:{style:"text-align:right;"}
            },
        ],
        groupable: false,
        sortable: true,
        resizable: true,
        selectable: true,
        editable: false,
        scrollable: true,
        mobile: true,
        // pageable: true,
    })

    card_resultados.kWindow_trasladados.center().maximize().open()

    var lista = trasladados.split('},')

    json_lista = []

    $.each(lista ,function (indice, elemento) {
        elemento_formateado = elemento.replace("{","").replace("}","")
        elemento_formateado = "{" + elemento_formateado + "}"
        json_lista.push(JSON.parse(elemento_formateado))
    })
    kGrid_trasladados.data('kendoGrid').dataSource.data(json_lista)
}
TargetaResultados.prototype.ver_Retenidos = function (e) {
    e.preventDefault()
    var fila = this.dataItem($(e.currentTarget).closest('tr'))

    retenidos = fila.impuestos_retenidos.replace('[','').replace(']','')

    kGrid_retenidos = $('#grid_retenidos').kendoGrid({
        dataSource : {
            schema: {
                model:{
                    fields: {
                        tasa: { type: "string" },
                        impuesto: { type: "string" },
                        importe: { type: "string" },
                    }
                }
            },
            // pageSize: 10,
        },
        columns: [
            { 
                field: "tasa", 
                title: "Tasa", 
                width: "80px",
                attributes:{style:"text-align:right;"}
            },
            { field: "impuesto", title: "Impuesto", width: "110px" },
            { 
                field: "importe", 
                title: "Importe", 
                width: "100px",
                format: '{0:c}',
                attributes:{style:"text-align:right;"}
            },
        ],
        groupable: false,
        sortable: true,
        resizable: true,
        selectable: true,
        editable: false,
        scrollable: true,
        mobile: true,
        // pageable: true,
    })

    card_resultados.kWindow_retenidos.center().maximize().open()

    var lista = retenidos.split('},')

    json_lista = []

    $.each(lista ,function (indice, elemento) {
        elemento_formateado = elemento.replace("{","").replace("}","")
        elemento_formateado = "{" + elemento_formateado + "}"
        json_lista.push(JSON.parse(elemento_formateado))
    })
    kGrid_retenidos.data('kendoGrid').dataSource.data(json_lista)
}


