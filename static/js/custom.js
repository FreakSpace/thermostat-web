
$("#get-data-button").on("click", function () {
    var from_date = formatDate($("#datetimepicker_from").datetimepicker('viewDate')._d);
    var to_date = formatDate($("#datetimepicker_to").datetimepicker('viewDate')._d);
    var to_reduce = $("#to_reduce").prop("checked");
    window.location.replace("/?start_date=" + from_date + "&end_date=" + to_date + "&to_reduce=" + to_reduce);
});


/* Functions to get data by date in All records */
$("#get-all-data-button").on("click", function () {
    var link = "/all_data/?";

    var filter_by_date = $("#filter_by_date_checkbox")[0].checked;
    link += "filter_by_date=" + filter_by_date;

    if (filter_by_date) {
        var from_date = formatDate($("#datetimepicker_from").datetimepicker('viewDate')._d);
        var to_date = formatDate($("#datetimepicker_to").datetimepicker('viewDate')._d);
        link += "&start_date=" + from_date + "&end_date=" + to_date;
    }


    var ts_state = get_ts_state();
    link += "&ts_state=" + ts_state;

    var current_state = get_current_state();
    link += "&current_state=" + current_state;

    var light_state = get_light_state();
    link += "&light_state=" + light_state;

    window.location.replace(link);
});

$("#ts_state_group").on("click", function () {
    set_ts_name_state();
});

$("#current_state_group").on("click", function () {
    set_current_state_name();
});


$("#light_state_group").on("click", function () {
    set_light_name_state();
});


$("#clean-data-button").on("click", function () {
    window.location.replace("/");
});

$("#clean-all-data-button").on("click", function () {
    window.location.replace("/all_data/");
});


$(function () {
  $('[data-toggle="popover"]').popover()
});


$('#program-modal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
});


$('#activate-program').on('click', function () {
    var _id = $(this)[0].value;
    $.ajax({
        url: "run/?run_id=" + _id,
        dataType: 'json',
        success: function (data) {
            if (data["state"] === "success")
                $("#success-alert").addClass("show");
            else
                $("#not-success-alert").addClass("show");
        }
    });
});


$('#stop-program').on('click', function () {
    var _id = $(this)[0].value;
    $.ajax({
        url: "run/?run_id=" + _id + "&stop=true",
        dataType: 'json',
        success: function (data) {
            $("#stop-program-alert").addClass("show");
        }
    });
});

$("#close-data-block-button").on("click", function () {
    $("#detail-data").hide("fast");
});

$("tr").on("click", function () {
    /*
     * Ajax request for single record data
     */
    var _id = $(this).data("value");
    $.ajax({
        url: "single/?id=" + _id,
        data: _id,
        dataType: 'json',
        success: function (data) {
            $("#detail-data").show("fast");

            $("#th-id").text(data['id']);
            $("#th-date").text(data['date']);
            $("#th-state").text(function () {
                if (data['thermostat_state']) {
                    $(this).addClass("badge-success");
                    $(this).removeClass("badge-secondary");
                    return "Увімкнено";
                }
                else {
                     $(this).removeClass("badge-success");
                    $(this).addClass("badge-secondary");
                    return "Вимкнено"
                }
            });
            $("#th-temp").text(data['temp'] + "°C");
            $("#th-set-t").text(data['set_temp'] + "°C");


            $("#th-light").text(function () {
                if (data['light'] === "Off") {
                    $(this).removeClass("badge-warning");
                    $(this).addClass("badge-secondary");
                    return "Вимкнено"
                }
                else {
                    $(this).removeClass("badge-secondary");
                    $(this).addClass("badge-warning");
                    return data['light'];
                }
            });

            $("#th-uv-intensity").text(data['light_UV']);
            $("#th-r-intensity").text(data['light_R']);
            $("#th-g-intensity").text(data['light_G']);
            $("#th-b-intensity").text(data['light_B']);

            $("#th-color-light").text(function () {
                $(this).css("background-color", 'rgb('+data['light_R']+','+data['light_G']+','+data['light_B']+')')
            });

            $("#th-work").text(function () {
                data = data['current_state'];
                if (data === "1") {
                    $(this).removeClass("badge-primary");
                    $(this).removeClass("badge-secondary");
                    $(this).addClass("badge-danger");
                    $(this).text("Нагрівання");
                }

                else if (data === "2") {
                    $(this).removeClass("badge-danger");
                    $(this).removeClass("badge-secondary");
                    $(this).addClass("badge-primary");
                    $(this).text("Охолодження");
                }

                else {
                    $(this).removeClass("badge-danger");
                    $(this).removeClass("badge-primary");
                    $(this).addClass("badge-secondary");
                    $(this).text("Не працює");
                }
            });
        }
    })
});
