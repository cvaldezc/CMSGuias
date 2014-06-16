$(document).ready(function() {
	$(".panel-quote,.panel-buy,.table-details").hide();
	$(".btn-proccess").on("click", showConvert);
	$("[name=transfer_buy],[name=traslado_quote]").datepicker({ dateFormat: "yy-mm-dd", showAnim: "slide" });
	$("[name=obser_quote]").focusin(function () {
		this.setAttribute("rows",3);
	}).focusout(function () {
		this.setAttribute("rows",1);
	});
	$(".conquote,.conbuy").on("click", selectConvert);
	$("[name=select]").on("change", changeRadio);
});

// functions
var changeRadio = function (event) {
	event.preventDefault();
	if (this.checked) {
		var value = parseInt(this.value);
		$("input[name=chk]").each(function () {
			this.checked = Boolean(value);
		});
	};
}

var getlistMateriales = function (id_su) {
	if (id_su != "") {
		url = "/json/get/details/supply/".concat(id_su).concat("/");
		$.getJSON(url, function(response) {
			console.info(response);
				if (response.status) {
					var $tb = $(".table-details > tbody");
					$tb.empty();
					var template = "<tr><td>{{ counter }}</td><td><input type='checkbox' name='chk' value='{{ materiales_id }}'></td><td>{{ materiales_id }}</td><td>{{ materiales__matnom }}</td><td>{{ materiales__matmed }}</td><td>{{ materiales__unidades_id }}</td><td>{{ cantidad }}</td></tr>";
					for(var x in response.list){
						response.list[x].counter = (parseInt(x) + 1);
						$tb.append(Mustache.render(template, response.list[x]));
					}
				};
		});
	}else{
		$().toastmessage("showWaringToast","Hay un error al traer la lista de materiales. Código incorrecto");
	};
}
var showConvert = function(event) {
	event.preventDefault();
	$(".conquote,.conbuy").val(this.name);
	$(".consu").html(this.name);
	$(".mquestion").modal("show");
};
var selectConvert = function (event) {
	event.preventDefault();
	// recover list of materials
	$(".table-principal").hide("blind", 600);
	getlistMateriales(this.value);
	if (this.title == "quote") {
		$(".panel-quote").show("slide", 600);
	}else{
		$(".panel-buy").show("slide",600);
	};
	$(".table-details").show("slide",600);
	$(".mquestion").modal("hide");
};