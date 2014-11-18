// Generated by CoffeeScript 1.8.0
var getAllCurrentAccounts, globalMailerData, globalTmpMailer, initializeBodyMailer, mailerLoadsData, sendGlobalMailer, showGCopyMailer, showGPwdMailer, showGlobalEnvelop;

initializeBodyMailer = function(event) {
  tinymce.init({
    selector: "div[name=globalmbody]",
    height: 200,
    theme: "modern",
    menubar: true,
    statusbar: false,
    paste_as_text: true,
    plugins: "link contextmenu",
    font_size_style_values: "10px,12px,13px,14px,16px,18px,20px",
    toolbar: "undo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | fontsizeselect"
  });
};

showGlobalEnvelop = function(event) {
  if (!$("#mailer").length) {
    $("footer").append(globalTmpMailer);
    initializeBodyMailer();
  }
  if ($("#mailer").is(":hidden")) {
    $("#mailer").modal("show");
    mailerLoadsData();
  }
};

getAllCurrentAccounts = function(event) {
  var data;
  data = new Object;
  data.allmails = true;
  data.csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
  $.post("/json/get/emails/", data, function(response) {
    if (response.status) {
      return globalMailerData.fors = response["for"];
    }
  }, "json");
};

globalMailerData = new Object;

mailerLoadsData = function() {
  if (globalMailerData.hasOwnProperty("fors")) {
    $("input[name=globalmfor]").val(globalMailerData.fors.toString().replace(/\,/g, ", "));
  } else {
    $("input[name=globalmfor]").val("");
  }
  if (globalMailerData.hasOwnProperty("cc")) {
    $("input[name=globalmcc]").val(globalMailerData.cc.toString().replace(/\,/g, ", "));
  } else {
    $("input[name=globalmcc]").val("");
  }
  if (globalMailerData.hasOwnProperty("cco")) {
    $("input[name=globalmcco]").val(globalMailerData.cco.toString().replace(/\,/g, ", "));
  } else {
    $("input[name=globalmcco]").val("");
  }
  if (globalMailerData.hasOwnProperty("issue")) {
    $("input[name=globalmissue]").val(globalMailerData.issue.toString());
  } else {
    $("input[name=globalmissue]").val("");
  }
  if (globalMailerData.hasOwnProperty("body")) {
    $("iframe#globalmbody_ifr").contents().find("body").html(globalMailerData.body);
  } else {
    $("iframe#globalmbody_ifr").contents().find("body").html("");
  }
};

globalTmpMailer = "<div class=\"modal fade\" id=\"mailer\"> <div class=\"modal-dialog\"> <div class=\"modal-content\"> <div class=\"modal-body mailer-one\"> <a data-dismiss=\"modal\" class=\"close\">&times;</a> <div class=\"row\"> <div class=\"col-md-12\"> <div class=\"form-group\"> <input type=\"text\" name=\"globalmfor\" class=\"form-control input-sm text-bold\" placeholder=\"Para\" /> <button class=\"btn btn-link close btn-global-copy-mailer\"> <span class=\"fa fa-chevron-down\"></span> </button> </div> </div> <div class=\"col-md-12\"> <div class=\"form-group panel-copy-mailer hide\"> <input type=\"text\" name=\"globalmcc\" class=\"form-control input-sm\" placeholder=\"Cc\" /> <input type=\"text\" name=\"globalmcco\" class=\"form-control input-sm\"  placeholder=\"Cco\"/> </div> </div> <div class=\"col-md-12\"> <div class=\"form-group\"> <input type=\"text\" name=\"globalmissue\" class=\"form-control input-sm text-bold\"  placeholder=\"Asunto\"/ > </div> </div> <div class=\"col-md-12\"> <div id=\"globalmbody\" name=\"globalmbody\"> Escribe algo ... </div> </div> <div class=\"col-md-12\"> <div class=\"row\"> <div class=\"col-md-2\"> <button class=\"btn btn-primary btn-global-send-envelop\"> <span class=\"fa fa-envelope\"></span> ENVIAR </button> </div> <div class=\"col-md-4 col-md-offset-6\"> <div class=\"input-group\"> <div class=\"input-group-btn\"> <button class=\"btn btn-sm btn-default btn-global-show-mailer-password\"> <span class=\"fa fa-chevron-circle-down\"></span> </button> </div> <div class=\"form-group has-primary\"> <input type=\"password\" class=\"form-control input-sm hide\" name=\"globalPwdMailer\"> </div> </div> </div> </div> </div> </div> </div> <div class=\"modal-body mailer-two hide\"> <h2 name=\"mailer-msg\" class=\"text-center\"> <span class=\"glyphicon\"></span> <br /> <span></span> </h2> </div> </div> </div> </div>";

showGPwdMailer = function(event) {
  var $btn, $in;
  $btn = $(this);
  $in = $("input[name=globalPwdMailer]");
  if ($in.is(":visible")) {
    $btn.find("span").removeClass("fa-chevron-circle-right").addClass("fa-chevron-circle-down");
    $in.addClass("hide");
  } else {
    $btn.find("span").removeClass("fa-chevron-circle-down").addClass("fa-chevron-circle-right");
    $in.removeClass("hide");
  }
};

showGCopyMailer = function(event) {
  var $btn, $panel;
  $btn = $(this);
  $panel = $(".panel-copy-mailer");
  if ($panel.is(":visible")) {
    $btn.find("span").removeClass("fa-chevron-up").addClass("fa-chevron-down");
    $panel.addClass("hide");
  } else {
    $btn.find("span").removeClass("fa-chevron-down").addClass("fa-chevron-up");
    $panel.removeClass("hide");
  }
};

sendGlobalMailer = function(event) {
  var data, pass, x, _i, _j, _k, _len, _len1, _len2, _ref, _ref1, _ref2;
  data = new Object;
  if ($.trim($("input[name=globalmfor]").val()) !== "") {
    data.fors = $("input[name=globalmfor]").val().split(",");
  }
  if ($.trim($("input[name=globalmcc]").val()) !== "") {
    data.cc = $("input[name=globalmcc]").val().split(",");
  }
  if ($.trim($("input[name=globalmcco]").val()) !== "") {
    data.cco = $("input[name=globalmcco]").val().split(",");
  }
  if ($.trim($("input[name=globalmissue]").val()) !== "") {
    data.issue = $("input[name=globalmissue]").val();
  }
  data.body = $("iframe#globalmbody_ifr").contents().find("body").html();
  if (!data.hasOwnProperty("fors")) {
    if (data.fors.length) {
      $().toastmessage("showWarningToast", "No se a introducido un destinatario.");
      return false;
    }
  }
  if (!data.hasOwnProperty("issue")) {
    if (data.issue.length) {
      $().toastmessage("showWarningToast", "No se a introducido un destinatario.");
      return false;
    }
  }
  if (!data.hasOwnProperty("body") || data.body === "") {
    $().toastmessage("showWarningToast", "No se a introducido un destinatario.");
    return false;
  }
  _ref = data.fors;
  for (_i = 0, _len = _ref.length; _i < _len; _i++) {
    x = _ref[_i];
    if ($.trim(data.fors[x]) !== "") {
      pass = validateEmail(data.fors[x]);
      if (!pass) {
        $().toastmessage("showWarningToast", "El formato de email no es correcto.");
        return pass;
      }
    }
  }
  if (data.hasOwnProperty("cc")) {
    if (data.cc.length) {
      data.ccb = data.cc.toString();
      _ref1 = data.cc;
      for (_j = 0, _len1 = _ref1.length; _j < _len1; _j++) {
        x = _ref1[_j];
        if ($.trim(data.cc[x]) !== "") {
          pass = validateEmail(data.cc[x]);
          if (!pass) {
            console["return"](pass);
          }
        }
      }
    }
  }
  if (data.hasOwnProperty("cco")) {
    if (data.cco.length) {
      data.ccob = data.cco.toString();
      _ref2 = data.cco;
      for (_k = 0, _len2 = _ref2.length; _k < _len2; _k++) {
        x = _ref2[_k];
        if ($.trim(data.cco[x]) !== "") {
          pass = validateEmail(data.cco[x]);
          if (!pass) {
            return pass;
          }
        }
      }
    }
  }
  data.forsb = data.fors.toString();
  if ($("input[name=globalPwdMailer]").is(":visible")) {
    if ($.trim($("input[name=globalPwdMailer]").val()) !== "") {
      data.email = $("input[name=user-email]").val();
      data.pwdmailer = $("input[name=globalPwdMailer]").val();
    }
  }
  $.ajax({
    url: "http://190.41.246.91:3000",
    type: "GET",
    crossDomain: true,
    data: $.param(data),
    dataType: "jsonp",
    success: function(response) {
      if (response.status) {
        alert(response.msg);
      }
    }
  });
  data.csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
  data.saveEmail = true;
  $.post("/json/emails/", data, function(response) {
    if (response.status) {
      $("div.mailer-one").addClass("hide");
      $("div.mailer-two").removeClass("hide");
      $("[name=mailer-msg]").addClass("text-success");
      $("[name=mailer-msg]").find("span").eq(0).addClass("glyphicon-ok");
      $("[name=mailer-msg]").find("span").eq(1).text("Felicidades, se a enviado el correo.");
      return setTimeout(function() {
        $(".mailer-two").addClass("hide");
        $(".mailer-one").removeClass("hide");
        return $("#mailer").modal("hide");
      }, 1600);
    } else {
      $("div.mailer-two").removeClass("hide");
      $("div.mailer-one").addClass("hide");
      $("[name=mailer-msg]").addClass("text-danger");
      $("[name=mailer-msg]").find("span").eq(0).addClass("glyphicon-remove");
      $("[name=mailer-msg]").find("span").eq(1).text("Error al guardar el email").append("<small>Es posible que el correo se envie mas tarde.</small>");
      return setTimeout(function() {
        $(".mailer-two").addClass("hide");
        $(".mailer-one").removeClass("hide");
        return $("#mailer").modal("hide");
      }, 1600);
    }
  }, "json");
};

$(document).on("click", ".btn-global-show-mailer-password", showGPwdMailer);

$(document).on("click", ".btn-global-copy-mailer", showGCopyMailer);

$(document).on("click", ".btn-global-send-envelop", sendGlobalMailer);
