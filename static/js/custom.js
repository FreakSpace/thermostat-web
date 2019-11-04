function formatDate(date) {
    /*
     * bringing the date and time in the appropriate format
     */
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();
    hours = d.getHours();
    minutes = d.getMinutes();

    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;
    if (hours.length < 2) hours = '0' + hours;
    if (minutes.length < 2) minutes = '0' + minutes;

    return [year, month, day, hours, minutes].join('-');
}


/* Functions to get data by date */
$("#get-data-button").on("click", function () {
    var from_date = formatDate($("#datetimepicker_from").datetimepicker('viewDate')._d);
    var to_date = formatDate($("#datetimepicker_to").datetimepicker('viewDate')._d);
    var to_reduce = $("#to_reduce").prop("checked");
    window.location.replace("/?start_date=" + from_date + "&end_date=" + to_date + "&to_reduce=" + to_reduce);
});

$("#clean-data-button").on("click", function () {
    window.location.replace("/");
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
            $("#detail-data").show("slow");

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
            $("#th-co2").text(data['co2'] + "");
            $("#th-set-co2").text(data['set_co2'] + "");

            $("#th-light").text(function () {
                if (data['light']) {
                    $(this).removeClass("badge-secondary");
                    $(this).addClass("badge-warning");
                    return "Увімкнено";
                }
                else {
                    $(this).removeClass("badge-warning");
                    $(this).addClass("badge-secondary");
                    return "Вимкнено"
                }
            });

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
