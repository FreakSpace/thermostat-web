
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

$( "#get-data-button" ).on( "click", function() {
    var from_date = formatDate($("#datetimepicker_from").datetimepicker('viewDate')._d);
    var to_date = formatDate($("#datetimepicker_to").datetimepicker('viewDate')._d);
    window.location.replace("/?start_date="+from_date+"&end_date="+to_date);
});

$( "#clean-data-button" ).on( "click", function() {
    window.location.replace("/");
});
