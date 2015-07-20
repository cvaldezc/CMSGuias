var changeCheck, changeSearch, changeSelect, listTemplate, loadIngress, saveNoteIngress, searchPurchase, showAction, showDeposit, showIngressInventory, validQuantityBlur;

$(document).ready(function() {
  $(".step-second,.step-tree").hide();
  $("input[name=start], input[name=end]").datepicker({
    "showAnim": "slide",
    "dateFormat": "yy-mm-dd"
  });
  $("input[name=search]").on("change", changeSearch);
  $(".btn-search").on("click", searchPurchase);
  $(document).on("click", ".btn-deposit", showDeposit);
  $(document).on("click", ".btn-action", showAction);
  $(".btn-ingress").on("click", showIngressInventory);
  $(document).on("blur", ".materials", validQuantityBlur);
  $(document).on("change", "input[name=mats]", changeCheck);
  $("[name=select]").on("change", changeSelect);
  $(".btn-generate-note").on("click", loadIngress);
  $(".btn-generate").on("click", saveNoteIngress);
  $(".btn-repeat").click(function(event) {
    location.reload();
  });
});

changeSearch = function() {
  if (this.checked) {
    if (this.value === "code") {
      $("input[name=code]").attr("disabled", false);
      $("input[name=start],input[name=end]").attr("disabled", true);
    } else if (this.value === "dates") {
      $("input[name=code]").attr("disabled", true);
      $("input[name=start],input[name=end]").attr("disabled", false);
    }
  }
};

searchPurchase = function() {
  var data;
  data = new Object();
  $("input[name=search]").each(function(index, element) {
    if (element.checked) {
      data.type = element.value;
      if (element.value === "code") {
        data.code = $("input[name=code]").val();
      } else if (element.value === "dates") {
        data.start = $("input[name=start]").val();
        if ($("input[name=end]").val().length === 10) {
          data.end = $("input[name=end]").val();
        }
      }
    }
  });
  if (data.type === "code") {
    if (data.code.length === 10) {
      data.pass = true;
    } else {
      data.pass = false;
      $().toastmessage("showWarningToast", "No se a ingresado el código.");
    }
  } else if (data.type === "dates") {
    if (data.start.length === 10) {
      data.pass = true;
    } else {
      data.pass = false;
      $().toastmessage("showWarningToast", "No se han ingresado la fecha a buscar.");
    }
  }
  if (data.pass) {
    $.getJSON("", data, function(response) {
      if (response.status) {
        console.log(response);
        listTemplate(response.list);
      } else {
        $().toastmessage("showWarningToast", "Se han encontrado errores. " + response.raise);
      }
    });
  }
};

listTemplate = function(list) {
  var $tb, template, x;
  $tb = $("table > tbody");
  $tb.empty();
  if (list.length) {
    template = "<tr> <td>{{ item }}</td> <td>{{ purchase }}</td> <td>{{ reason }}</td> <td>{{ document }}</td> <td>{{ transfer }}</td> <td class=\"text-center\"> <button value=\"{{ purchase }}\" data-ruc=\"{{ x.supplier }}\" class=\"btn btn-link btn-xs text-black btn-deposit\"><span class=\"glyphicon glyphicon-credit-card\"></span></button> </td> <td class=\"text-center\"> <a href=\"/reports/order/purchase/{{ purchase }}/\" target=\"_blank\" class=\"btn btn-xs btn-link text-black\"><span class=\"glyphicon glyphicon-eye-open\"></span></a> </td> <td class=\"text-center\"> <button value=\"{{ purchase }}\" data-ruc=\"{{ x.supplier }}\" class=\"btn btn-link btn-xs text-black btn-action\"><span class=\"glyphicon glyphicon-inbox\"></span></button> </td> </tr>";
    for (x in list) {
      list[x].item = parseInt(x) + 1;
      $tb.append(Mustache.render(template, list[x]));
    }
  }
};

showDeposit = function() {
  var purchase, supplier, url;
  purchase = this.value;
  supplier = this.getAttribute("data-ruc");
  url = "/media/storage/compra/" + purchase + "/" + supplier + ".pdf";
  window.open(url, "Deposit");
};

showAction = function() {
  $(".maction").modal("show").find("button").val(this.value);
};

showIngressInventory = function(event) {
  var btn;
  btn = this.value;
  $.getJSON("", {
    "purchase": btn
  }, function(response) {
    var $tb, template, x;
    if (response.status) {
      $(".supplier").html(response.head.supplier);
      $(".quote").html(response.head.quote);
      $(".place").html(response.head.place);
      $(".document").html(response.head.document);
      $(".payment").html(response.head.payment);
      $(".currency").html(response.head.currency);
      $(".register").html(response.head.register);
      $(".transfer").html(response.head.transfer);
      $(".contact").html(response.head.contact);
      $(".performed").html(response.head.performed);
      template = "<tr><td><input type=\"checkbox\" name=\"mats\" value=\"{{ materials }}\"></td><td>{{ item }}</td><td>{{ materials }}</td><td>{{ name }}</td><td>{{ measure }}</td><td>{{ brand }}</td><td>{{ model }}</td><td>{{ unit }}</td><td>{{ quantity }}</td><td><input type=\"number\" class=\"form-control input-sm materials\" name=\"{{ materials }}\" value=\"{{ quantity }}\" min=\"1\" max=\"{{ quantity }}\" data-price=\"{{ price }}\" data-brand=\"{{ brand_id }}\" data-model=\"{{ model_id }}\" disabled></td></tr>";
      $tb = $("table.table-ingress > tbody");
      $tb.empty();
      for (x in response.details) {
        response.details[x].item = parseInt(x) + 1;
        $tb.append(Mustache.render(template, response.details[x]));
      }
      $(".purchase").html(btn);
      $("[name=purchase]").val(btn);
      $(".maction").modal("hide");
      $(".step-first").fadeOut(200);
      $(".step-second").fadeIn(600);
    }
  });
};

validQuantityBlur = function(event) {
  var max, min, val;
  min = parseFloat(this.getAttribute("min").replace(",", "."));
  max = parseFloat(this.getAttribute("max").replace(",", "."));
  val = parseFloat(this.value.replace(",", "."));
  if (val < min || val > max) {
    if (val < min) {
      this.value = min;
    } else if (val > max) {
      this.value = max;
    }
  }
};

changeCheck = function(event) {
  var $mat;
  $mat = $("input[name=" + this.value + "]");
  if (this.checked) {
    $mat.attr("disabled", false);
  } else {
    $mat.attr("disabled", true);
  }
};

changeSelect = function(event) {
  var chek;
  if (this.checked) {
    chek = Boolean(parseInt(this.value));
    $("input[name=mats]").each(function(index, element) {
      element.checked = chek;
      $(element).change();
    });
  }
};

loadIngress = function(event) {
  var arr;
  arr = new Array();
  $("input[name=mats]").each(function(index, element) {
    if (element.checked) {
      arr.push({
        "materials": element.value,
        "quantity": $("input[name=" + element.value + "]").val()
      });
    }
  });
  if (arr.length) {
    $(".mingress").modal("toggle");
  } else {
    $().toastmessage("showWarningToast", "Seleccione por lo menos un material para hacer el ingreso a almacén.");
  }
};

saveNoteIngress = function(response) {
  var data, mats, pass;
  data = new Object();
  mats = new Array();
  pass = false;
  $("input[name=mats]").each(function(index, element) {
    var max, quantity, tag;
    if (element.checked) {
      max = $("input[name=" + element.value + "]").attr("max");
      quantity = $("input[name=" + element.value + "]").val();
      tag = parseFloat(quantity) < parseFloat(max) ? "1" : "2";
      mats.push({
        "materials": element.value,
        "quantity": quantity,
        "price": $("input[name=" + element.value + "]").attr("data-price"),
        "tag": tag,
        "brand": $("input[name=" + element.value + "]").attr("data-brand"),
        "model": $("input[name=" + element.value + "]").attr("data-model")
      });
    }
  });
  data.details = JSON.stringify(mats);
  $(".mingress > div > div > div.modal-body > div.row").find("input, select").each(function(index, element) {
    console.info(element);
    if (element.name !== "guide") {
      if ($.trim(element.value !== "")) {
        data[element.name] = $.trim($(element).val());
        pass = true;
      } else {
        $().toastmessage("showWarningToast", "Campo vacio, " + element.name);
        pass = false;
        return pass;
      }
    }
  });
  console.log(pass);
  if (pass) {
    $().toastmessage("showToast", {
      text: "Desea generar una <q>Nota de Ingreso</q> con los materiales seleccionados?",
      sticky: true,
      type: "confirm",
      buttons: [
        {
          value: "Si"
        }, {
          value: "No"
        }
      ],
      success: function(result) {
        if (result === "Si") {
          data.ingress = true;
          data.observation = $("textarea[name=observation]").val();
          data.purchase = $(".purchase").html();
          data.csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
          console.warn(data);
          return $.post("", data, function(response) {
            if (response.status) {
              $(".step-second").fadeOut(200);
              $(".step-tree").fadeIn(600);
              $(".modal").modal("hide");
              $(".note").html(response.ingress);
              return $(".show-note-ingress").attr("href", "/reports/note/ingress/" + response.ingress + "/");
            } else {
              $().toastmessage("showWarningToast", "No se a podido generar la Nota de Ingreso.");
            }
          });
        }
      }
    });
  }
};
