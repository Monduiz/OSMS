// Stepper
var stepper = new Stepper(document.querySelector('#stepper'), {
  linear: false,
  animation: true
});

// Material Select Initialization
$(document).ready(function() {
$('.mdb-select').materialSelect();
});


$("#SelectWork").val('').prop('readonly',true);

// date picker

$('.datetimepicker').datetimepicker({
  locale: 'en-ca',
  format: 'YYYY-MM-DD',
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

// Date and time picker for Hazard occurence
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

// Phone number formatting

new Cleave('#id_supervisor_phone', {
    numericOnly: true,
    blocks: [0, 3, 0, 3, 4],
    delimiters: ["(", ")", " ", "-"]
});
