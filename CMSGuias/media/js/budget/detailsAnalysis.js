// Generated by CoffeeScript 1.8.0
var addMaterials, getListMaterials, getMaterialsAll, getmeasure, getsummary, refreshMaterials, showAddMaterial;

$(document).ready(function() {
  getMaterialsAll();
  $(".materialsadd").hide();
  $("[name=materials], [name=measure]").chosen({
    width: "100%"
  });
  $("[name=materials]").on("change", getmeasure);
  $("[name=measure]").on("change", getsummary);
  $(".bshowaddmat").on("click", showAddMaterial);
  $(".bmrefresh").on("click", refreshMaterials);
  $(".btnaddmat").on("click", addMaterials);
});

getMaterialsAll = function(event) {
  var context;
  context = new Object();
  context.searchName = true;
  context.name = '';
  $.getJSON("/materials/", context, function(response) {
    var $op, template;
    if (response.status) {
      $op = $("[name=materials]");
      $op.empty();
      template = "{{#names}}<option value=\"{{ name }}\">{{ name }}</option>{{/names}}";
      $op.html(Mustache.render(template, response));
      $op.trigger("chosen:updated");
      return getmeasure();
    }
  });
};

getmeasure = function(event) {
  var context;
  context = new Object;
  context.searchMeter = true;
  context.name = $("[name=materials]").val();
  $.getJSON("/materials/", context, function(response) {
    var $se, template;
    if (response.status) {
      $se = $("[name=measure]");
      $se.empty();
      $se.append("<option></option>");
      template = "{{#meter}} <option value=\"{{code}}\">{{measure}}</option> {{/meter}}";
      $se.html(Mustache.render(template, response));
      $se.trigger("chosen:updated");
      return setTimeout(function() {
        return getsummary();
      }, 200);
    }
  });
};

getsummary = function(event) {
  var context;
  context = new Object;
  context.scode = $("[name=measure]").val();
  context.summary = true;
  if (context.scode.length === 15) {
    $.getJSON("/materials/", context, function(response) {
      var $s, template;
      if (response.status) {
        template = "<table class=\"table table-condensed font-11\"> <tbody> <tr> <th>Código</th> <td class=\"matid\">{{ summary.materials }}</td> </tr> <tr> <th>Nombre</th> <td>{{ summary.name }}</td> </tr> <tr> <th>Media</th> <td>{{ summary.measure }}</td> </tr> <tr> <th>Unidad</th> <td>{{ summary.unit }}</td> </tr> </tbody> </table>";
        $s = $("[name=summary]");
        $s.empty();
        $s.html(Mustache.render(template, response));
        $("[name=mprice]").val(response.summary.price);
      }
    });
  } else {
    $().toastmessage("showWarningToast", "El código del material no es valido.");
  }
};

showAddMaterial = function(event) {
  if ($(".materialsadd").is(":visible")) {
    $(this).removeClass("btn-warning").addClass("btn-default");
    $(".materialsadd").hide(800);
  } else {
    $(this).removeClass("btn-default").addClass("btn-warning");
    $(".materialsadd").show(800);
  }
};

addMaterials = function(event) {
  var context;
  context = new Object();
  context.materials = $(".matid").text();
  context.quantity = $("[name=mquantity]").val();
  context.price = $("[name=mprice]").val();
  if (context.materials.length === 15) {
    if (context.quantity !== "") {
      if (context.price !== "") {
        context.csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
        context.addMaterials = true;
        $.post("", context, function(response) {
          if (response.status) {
            getListMaterials();
          } else {
            $().toastmessage("showErrorToast", "Error al guardar los cambios. " + response.raise);
          }
        }, "json");
      } else {
        $().toastmessage("showWarningToast", "Precio invalido.");
      }
    } else {
      $().toastmessage("showWarningToast", "Cantidad invalida.");
    }
  } else {
    $().toastmessage("showWarningToast", "Código de material incorrecto.");
  }
};

getListMaterials = function(event) {
  var context;
  context = new Object;
  context.listMaterials = true;
  $.getJSON("", context, function(response) {
    var $tbl, counter, template;
    if (response.status) {
      $tbl = $(".tmaterials tbody");
      $tbl.empty();
      template = "{{#materials}}<tr><td>{{index}}</td><td>{{code}}</td><td>{{name}}</td><td>{{unit}}</td><td>{{quantity}}</td><td>{{price}}</td><td>{{partial}}</td><td class=\"text-center\"><button class=\"btn btn-default btn-xs\"><span class=\"fa fa-edit\"></span></button></td><td class=\"text-center\"><button class=\"btn btn-default btn-xs\"><span class=\"fa fa-trash\"></span></button></td></tr>{{/materials}}";
      counter = 1;
      response.index = function() {
        return counter++;
      };
      $tbl.html(Mustache.render(template, response));
    } else {
      $().toastmessage("showErrorToast", "Error al Obtener la lista. " + response.raise + ".");
    }
  });
};

refreshMaterials = function(event) {
  getMaterialsAll();
  getListMaterials();
};
