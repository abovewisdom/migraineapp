//prefill date with current date
(function () {
    var date = new Date().toISOString().substring(0, 10),
        field = document.querySelector('#mgstartdate');
    field.value = date;
    console.log(field.value);
})()
//prefill time with current time(not working yet check https://stackoverflow.com/questions/14245339/pre-populating-date-input-field-with-javascript)
(function () {
    var time = new Date().toLocaleTimeString().toISOString().substring(0, 10),
        field = document.querySelector('#mgstarttime');
    field.value = time;
    console.log(field.value);
})()
