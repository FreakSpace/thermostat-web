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

function set_filter_by_date(filter) {
    $("#filter_by_date_checkbox").attr("checked", filter)
}

function get_ts_state() {
    var ts_group = document.getElementsByName('ts_group');

    for(i = 0; i < ts_group.length; i++) {
        if(ts_group[i].checked)
            return ts_group[i].value
    }
}

function set_ts_name_state(state="3") {
    if (state === "3")
        state = get_ts_state();

    var state_name = "Всі";

    if (state === "0")
        state_name = "Вимкнуто";
    else if (state === "1")
        state_name = "Увімкнуто";


    document.getElementById("ts_state_text").innerHTML = "<b>"+state_name+"</b>";
}

function get_current_state() {
    var ts_group = document.getElementsByName('current_ts_group');

    for(i = 0; i < ts_group.length; i++) {
        if(ts_group[i].checked)
            return ts_group[i].value
    }
}

function set_current_state_name(state="4") {
    if (state === "4")
        state = get_current_state();
    var state_name = "Всі";

    if (state === "0")
        state_name = "Вимкнуто";
    else if (state === "1")
        state_name = "Нагрів";
    else if (state === "2")
        state_name = "Охолодження";

    document.getElementById("current_state_text").innerHTML = "<b>"+state_name+"</b>";
}

function get_light_state() {
    var light_group = document.getElementsByName('light_group');

    for(i = 0; i < light_group.length; i++) {
        if(light_group[i].checked)
            return light_group[i].value
    }
}

function set_light_name_state(state="5") {
    if (state === "5")
        state = get_light_state();
    var state_name = "Всі";

    if (state === "0")
        state_name = "Вимкнуто";
    else if (state === "1")
        state_name = "UV";
    else if (state === "2")
        state_name = "RGB";
    else if (state === "3")
        state_name = "RGB & UV";


    document.getElementById("light_state_text").innerHTML = "<b>"+state_name+"</b>";
}

function set_ts_checked(state="3") {
    if (state === "0") {
        $("#off_ts_state").attr("checked", true);
    }
    else if (state === "1") {
        $("#on_ts_state").attr("checked", true);
    }
    else if (state === "2") {
        $("#all_ts_state").attr("checked", true);
    }
}

function set_current_checked(state="4") {
    if (state === "0") {
        $("#off_current_state").attr("checked", true);
    }
    else if (state === "1") {
        $("#heat_current_state").attr("checked", true);
    }
    else if (state === "2") {
        $("#cooling_current_state").attr("checked", true);
    }
    else if (state === "3") {
        $("#all_current_state").attr("checked", true);
    }
}

function set_light_checked(state="5") {
    if (state === "0") {
        $("#off_light_state").attr("checked", true);
    }
    else if (state === "1") {
        $("#uv_light_state").attr("checked", true);
    }
    else if (state === "2") {
        $("#rgb_light_state").attr("checked", true);
    }
    else if (state === "3") {
        $("#rgbuv_light_state").attr("checked", true);
    }
    else if (state === "4") {
        $("#all_light_state").attr("checked", true);
    }
}