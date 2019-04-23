function formatDate(date) {
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

$("#get-data-button").on("click", function () {
    var from_date = formatDate($("#datetimepicker_from").datetimepicker('viewDate')._d);
    var to_date = formatDate($("#datetimepicker_to").datetimepicker('viewDate')._d);
    window.location.replace("/?start_date=" + from_date + "&end_date=" + to_date);
});

$("#clean-data-button").on("click", function () {
    window.location.replace("/");
});


$("tr").on("click", function () {
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
