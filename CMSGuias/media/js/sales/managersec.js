// Generated by CoffeeScript 1.7.1
(function() {
  var delPlane, keyCode, keyDescription, openAddMaterial, panelPlanes, searchMaterial, uploadPlane, viewFull;

  $(document).ready(function() {
    $(".panel-add,input[name=read],.step-second").hide();
    $("input[name=description]").on("keyup", keyDescription);
    $("input[name=description]").on("keypress", keyUpDescription);
    $("select[name=meter]").on("click", getSummaryMaterials);
    $("input[name=code]").on("keypress", keyCode);
    $(".panel-add-mat, .view-full").hide();
    $(".btn-show-mat").on("click", openAddMaterial);
    $("input[name=plane]").on("change", uploadPlane);
    $(".btn-show-planes").on("click", panelPlanes);
    $("[name=show-full]").on("click", viewFull);
    $("[name=plane-del]").on("click", delPlane);
    $("[name=show-plane]").on("click", function(event) {
      return $("input[name=plane]").click();
    });
  });

  keyDescription = function(event) {
    var key;
    key = window.Event ? event.keyCode : event.which;
    if (key !== 13 && key !== 40 && key !== 38 && key !== 39 && key !== 37) {
      getDescription(this.value.toLowerCase());
    }
    if (key === 40 || key === 38 || key === 39 || key === 37) {
      moveTopBottom(key);
    }
  };

  keyCode = function(event) {
    var key;
    key = window.Event ? event.keyCode : event.which;
    if (key === 13) {
      return searchMaterialCode(this.value);
    }
  };

  searchMaterial = function(event) {
    var code, desc;
    desc = $("input[name=description]").val();
    code = $("input[name=code]").val();
    if (code.length === 15) {
      return searchMaterialCode(code);
    } else {
      return getDescription($.trim(desc).toLowerCase());
    }
  };

  openAddMaterial = function(event) {
    event.preventDefault();
    $(".panel-add-mat").toggle(function() {
      if ($(".btn-show-mat").is(":hidden")) {
        return $(this).find("span").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
      } else {
        return $(".btn-show-mat").find("span").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
      }
    });
  };

  uploadPlane = function(event) {
    var data;
    console.log(this.files[0]);
    if (this.files[0] !== null) {
      data = new FormData();
      data.append("type", "plane");
      data.append("files", this.files[0]);
      data.append("proyecto", $("input[name=pro]").val());
      data.append("subproyecto", $("input[name=sub]").val());
      data.append("sector", $("input[name=sec]").val());
      data.append("csrfmiddlewaretoken", $("[name=csrfmiddlewaretoken]").val());
      $.ajax({
        data: data,
        url: "",
        type: "POST",
        dataType: "json",
        cache: false,
        processData: false,
        contentType: false,
        success: function(response) {
          if (response.status) {
            return location.reload();
          } else {
            return $().toastmessage("showErrorToast", "No se ha cargado un archivo.");
          }
        }
      });
    } else {
      $().toastmessage("showWarningToast", "No se ha cargado un archivo.");
    }
  };

  panelPlanes = function(event) {
    var btn;
    btn = this;
    $(".panel-planes > .panel-body").toggle(function() {
      if ($(".panel-planes > .panel-body").is(":hidden")) {
        return $(btn).find("span").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
      } else {
        return $(btn).find("span").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
      }
    });
  };

  viewFull = function(event) {
    var btn;
    btn = this;
    $(".view-full").toggle(function() {
      if ($(this).is(":hidden")) {
        $(".navbar").show("blind", 600);
      } else {
        $(".navbar").hide("blind", 600);
        $("#planefull").attr("src", btn.value);
      }
    });
  };

  delPlane = function(event) {
    var data;
    data = new Object();
    data.type = "delplane";
    data.files = this.value;
    data.pro = $("input[name=pro]").val();
    data.sub = $("input[name=sub]").val();
    data.sec = $("input[name=sec]").val();
    data.csrfmiddlewaretoken = $("[name=csrfmiddlewaretoken]").val();
    $().toastmessage("showToast", {
      "text": "Desea eliminar el <q>Plano</q>?",
      "type": "confirm",
      "sticky": true,
      buttons: [
        {
          value: 'Si'
        }, {
          value: 'No'
        }
      ],
      success: function(result) {
        if (result === "Si") {
          return $.post("", data, function(response) {
            if (response.status) {
              return location.reload();
            } else {
              return $().toastmessage("showWarningToast", "Error, al eliminar el plano.");
            }
          });
        }
      }
    });
  };

}).call(this);