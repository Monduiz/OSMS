// Stepper
var stepper = new Stepper(document.querySelector('#stepper'), {
  linear: false,
  animation: true
});

var form = document.querySelector('form');
var validFormFeedback = document.querySelector('#test-nl-4 .valid-feedback');
var invalidFormFeedback = document.querySelector('#test-nl-4 .invalid-feedback')

form.addEventListener('submit', function(event) {
  form.classList.remove('was-validated');
  inValidFormFeedback.classList.remove('d-block');
  validFormFeedback.classList.remove('d-block');

  if (!form.checkValidity()) {
    event.preventDefault();
    event.stopPropagation();
    inValidFormFeedback.classList.add('d-block');
  } else {
    validFormFeedback.classList.add('d-block');
  }

  form.classList.add('was-validated');
}, false);

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
