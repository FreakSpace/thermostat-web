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

function get_ts_state() {
    var ts_group = document.getElementsByName('ts_group');

    for(i = 0; i < ts_group.length; i++) {
        if(ts_group[i].checked)
            return ts_group[i].value
        // document.getElementById("ts_state_text").innerHTML = ts_group[i].value;
    }
}

function set_ts_name_state() {
    var state = get_ts_state();
    var state_name = "Всі";

    if (state === "0")
        state_name = "Вимкнуто";
    else if (state === "1")
        state_name = "Нагрів";
    else if (state === "2")
        state_name = "Охолодження";

    document.getElementById("ts_state_text").innerHTML = "<b>"+state_name+"</b>";
}

function get_light_state() {
    var light_group = document.getElementsByName('light_group');

    for(i = 0; i < light_group.length; i++) {
        if(light_group[i].checked)
            return light_group[i].value
    }
}

function set_light_name_state() {
    var state = get_light_state();
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