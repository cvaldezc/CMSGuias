$(document).ready(function() {
	$(".opad").hide();
	$(document).on('keyup',"input[name=cod],input[name=desc]" , keyUpInput);
	$(".btn-register-all-list").on('click',register_all_list);
	$("button[name=btn-opad]").click(function(event) {
		$(".opad").toggle("blind",600);
	});
});

// functions
var keyUpInput = function (event) {
	event.preventDefault();
	var key = (event.keyCode ? event.keyCode : event.which);
	//if (key == 13) {
		search(this);
	//};
}
var search = function (ctrl) {
	var data = new Object();
	// recover data for search data
	data['periodo'] = $("select[name=periodo]").val(); // get value periodo
	data['almacen'] = $("select[name=almacen]").val(); // get value almacen
	data['omat'] = ctrl.value;
	data['tipo'] = ctrl.name;
	data['stkzero'] = $(".stkzero").is(":checked") ? true : false;
	data['stkmin'] = $(".stkmin").is(":checked") ? $(".smin").val() : '';
	/*
		Code for Postgres function 
		INSERT INTO almacen_inventario(
            materiales_id, almacen_id, precompra, preventa, stkmin, stock, 
            stkpendiente, stkdevuelto, ingreso, compra, flag, periodo)
		SELECT materiales_id,coalesce('AL01',''),coalesce(0,0),coalesce(0,0),coalesce(10,0),coalesce(0,0),
		coalesce(0,0),coalesce(0,0),coalesce(to_char(now(),'YYYY-MM-DD')::date,now()::date), coalesce('',''),
		coalesce(True,True),coalesce(to_char(now(),'YYYY'),'')
		from home_materiale
		limit 5 offset 0
		Code for Python
		from django.db import connection
	  cursor = connection.cursor()
	  cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
	  row = cursor.fetchone()
	  return row

	*/
	console.log(data);
}
var register_all_list = function () {
	var data = new Object();
	data['alid'] = $("select[name=almacen]").val();
	data['quantity'] = parseInt($("input[name=ias]").val());
	data['csrfmiddlewaretoken'] = $("input[name=csrfmiddlewaretoken]").val();
	$.post('',data, function (response) {
		console.info(response);
		if (response.status) {
			location.reload();
		};
	},'json');
}