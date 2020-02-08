// Stepper
var stepper = new Stepper(document.querySelector('#stepper'), {
  linear: false,
  animation: true
});

// Material Select Initialization
$(document).ready(function() {
$('.mdb-select').materialSelect();
});


// Date and time picker for Risk concern occurence
$('.datetimepicker_occurence').datetimepicker({
  locale: 'en-ca',
  format: 'YYYY-MM-DD HH:mm',
    icons: {
        time: "fa fa-clock-o",
        date: "fa fa-calendar",
        up: "fa fa-chevron-up",
        down: "fa fa-chevron-down",
        previous: 'fa fa-chevron-left',
        next: 'fa fa-chevron-right',
        today: 'fa fa-screenshot',
        clear: 'fa fa-trash',
        close: 'fa fa-remove'
    }
});
